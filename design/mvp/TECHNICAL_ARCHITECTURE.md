# Sol Corp Technical Architecture

**System design, data models, package structure, and implementation guidance for Phase 1.**

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Package Structure](#package-structure)
3. [Core Data Models](#core-data-models)
4. [System Design](#system-design)
5. [Key Algorithms](#key-algorithms)
6. [Dependencies & Tools](#dependencies--tools)
7. [Performance Targets](#performance-targets)
8. [Testing Strategy](#testing-strategy)

---

## Architecture Overview

### Design Principles

1. **Separation of Concerns:** Simulation engine (core/) decoupled from UI (ui/)
2. **Testability:** All core logic unit-testable; no hidden state or singletons
3. **Extensibility:** Easy to add new resources, facilities, techs in Phase 2+
4. **Clarity:** Type hints, clear names, minimal magical behavior

### Layered Model

```
┌─────────────────────────────────────────┐
│         UI Layer (cli.py)               │  Player interaction
├─────────────────────────────────────────┤
│       Simulation Layer (world.py)       │  Game logic, monthly tick
├─────────────────────────────────────────┤
│  Core Models (resource, facility, etc.) │  Data, state, production
├─────────────────────────────────────────┤
│      Game Entities (factions, AI)       │  Agents, strategies
└─────────────────────────────────────────┘
```

**Data flow:**
1. Player inputs command (via CLI)
2. Command updates world state (e.g., build facility)
3. Player advances month → simulation tick
4. Tick updates all factions (production, sales, AI decisions)
5. Results displayed via CLI

---

## Package Structure

```
sol_corp/
│
├── core/                           # Core simulation engine
│   ├── __init__.py                 # Package exports
│   ├── resource.py                 # Resource, good types, enums
│   ├── facility.py                 # Facility class, recipes, operation styles
│   ├── location.py                 # Location enum, local markets
│   ├── faction.py                  # Faction base class
│   ├── world.py                    # World state manager, game coordinator
│   └── simulation.py               # Monthly tick, economic resolution
│
├── ai/                             # AI faction logic
│   └── agent.py                    # AI heuristics, decision-making
│
├── earth/                          # Earth faction (demand, events)
│   └── earth_faction.py            # Earth demand model, event system
│
├── ui/                             # User interface
│   ├── __init__.py
│   └── cli.py                      # CLI interface, player commands
│
├── tests/                          # Test suite
│   ├── __init__.py
│   ├── test_resource.py            # Resource, good tests
│   ├── test_facility.py            # Facility, recipe tests
│   ├── test_world.py               # World state tests
│   ├── test_simulation.py          # Economic resolution tests
│   └── test_integration.py         # Full-game simulation tests
│
├── main.py                         # Entry point, game loop
│
├── requirements.txt                # Python dependencies
└── README.md                       # Setup & play instructions
```

### Module Responsibilities

| Module | Responsibility |
|--------|-----------------|
| `resource.py` | Resource/good definitions, enum values, properties (base price, category) |
| `facility.py` | Facility types, recipes, operation styles; production resolution per facility |
| `location.py` | Location enum, local market mechanics |
| `faction.py` | Faction state (capital, facilities), monthly loop stub |
| `world.py` | Global game state, coordinates all systems, provides public API |
| `simulation.py` | Economic math (pricing, costs, profits), monthly tick resolution |
| `agent.py` | AI decision-making heuristics, expansion logic |
| `earth_faction.py` | Earth faction demand, random events, price drivers |
| `cli.py` | Player commands, display, input/output |
| `main.py` | Game loop, CLI main() |

---

## Core Data Models

### 1. Resource & Goods

```python
from enum import Enum
from dataclasses import dataclass

class ResourceType(Enum):
    """Raw materials (extracted from planets)"""
    IRON_ORE = "iron_ore"
    RARE_EARTH = "rare_earth"
    SILICON = "silicon"

class GoodCategory(Enum):
    """Production tier"""
    RAW = "raw"
    INTERMEDIATE = "intermediate"
    FINISHED = "finished"

@dataclass
class Good:
    """Represents a tradable good"""
    name: str                      # e.g., "Iron Ore", "Refined Metal"
    category: GoodCategory         # Tier in production chain
    base_price: float              # Base Earth market price (credits/unit)
    
    # Properties (optional; for game balance)
    density: float = 1.0           # For transport cost calculation
    is_input_flexible: bool = False  # Can accept multiple input types

# Instantiation
goods = {
    'iron_ore': Good('Iron Ore', GoodCategory.RAW, 50),
    'refined_metal': Good('Refined Metal', GoodCategory.INTERMEDIATE, 100),
    'consumer_goods': Good('Consumer Goods', GoodCategory.FINISHED, 150),
    # ... more goods
}
```

### 2. Facility & Recipe

```python
from enum import Enum
from dataclasses import dataclass, field
from typing import Dict

class FacilityType(Enum):
    """Facility types"""
    IRON_MINE = "iron_mine"
    REFINERY = "refinery"
    COMPONENT_FACTORY = "component_factory"
    RESEARCH_LAB = "research_lab"
    # ... more types

class OperationStyle(Enum):
    """Facility operation intensity"""
    BASIC = "basic"              # 1x speed, 1x cost
    SKELETON = "skeleton"         # 1.5x speed, 1.5x cost
    FULLY_MANNED = "fully_manned" # 3x speed, 3x cost

@dataclass
class Recipe:
    """Production recipe: inputs → outputs"""
    name: str                              # e.g., "Smelt Iron"
    inputs: Dict[str, float]               # {good_name: quantity_needed}
    outputs: Dict[str, float]              # {good_name: quantity_produced}
    time_months: int = 1                   # Duration (months)
    cost_credits: float = 0.0              # Facility overhead per cycle
    operation_style_multiplier: Dict[OperationStyle, float] = field(
        default_factory=lambda: {
            OperationStyle.BASIC: 1.0,
            OperationStyle.SKELETON: 1.5,
            OperationStyle.FULLY_MANNED: 3.0,
        }
    )

@dataclass
class Facility:
    """A production facility"""
    id: str                                # Unique identifier
    type: FacilityType                    # Mine, refinery, etc.
    location: str                         # Moon, Mars, Belt (see Location enum)
    owner: str                            # Faction ID
    
    # State
    capital_cost: float = 5000.0          # One-time build cost
    current_recipe: Recipe = None         # Active recipe
    operation_style: OperationStyle = OperationStyle.BASIC
    
    # Inventory at this location
    input_inventory: Dict[str, float] = field(default_factory=dict)
    output_inventory: Dict[str, float] = field(default_factory=dict)
    
    # Methods
    def can_run_recipe(self, recipe: Recipe) -> bool:
        """Check if inputs available"""
        for good, qty in recipe.inputs.items():
            if self.input_inventory.get(good, 0) < qty:
                return False
        return True
    
    def run_production(self, recipe: Recipe) -> Dict[str, float]:
        """Execute production: consume inputs, produce outputs"""
        if not self.can_run_recipe(recipe):
            return {}
        
        # Consume inputs
        for good, qty in recipe.inputs.items():
            self.input_inventory[good] -= qty
        
        # Produce outputs (apply operation style multiplier)
        multiplier = recipe.operation_style_multiplier[self.operation_style]
        results = {}
        for good, qty in recipe.outputs.items():
            amount = qty * multiplier
            self.output_inventory[good] = self.output_inventory.get(good, 0) + amount
            results[good] = amount
        
        return results
```

### 3. Location & Local Market

```python
from enum import Enum
from dataclasses import dataclass, field
from typing import Dict

class Location(Enum):
    """Playable locations"""
    MOON = "moon"
    MARS = "mars"
    ASTEROID_BELT = "asteroid_belt"

@dataclass
class LocalMarket:
    """Market at a specific location"""
    location: Location
    inventory: Dict[str, float] = field(default_factory=dict)  # Goods available
    prices: Dict[str, float] = field(default_factory=dict)     # Local prices
    
    def add_to_inventory(self, good: str, qty: float):
        """Add goods to local market"""
        self.inventory[good] = self.inventory.get(good, 0) + qty
    
    def remove_from_inventory(self, good: str, qty: float) -> bool:
        """Remove goods if available"""
        if self.inventory.get(good, 0) >= qty:
            self.inventory[good] -= qty
            return True
        return False
    
    def calculate_distance_penalty(self) -> float:
        """Distance penalty for transport to Earth"""
        penalties = {
            Location.MOON: 0.10,
            Location.MARS: 0.20,
            Location.ASTEROID_BELT: 0.50,
        }
        return penalties.get(self.location, 0.0)
```

### 4. Faction

```python
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Faction:
    """A faction (player or AI)"""
    id: str                                    # Unique ID
    is_ai: bool = False
    
    # Economics
    capital: float = 50000.0                   # Available credits
    facilities: List[Facility] = field(default_factory=list)
    
    # Tech unlocks
    researched_techs: set = field(default_factory=set)  # Tech IDs
    
    def get_facilities_at_location(self, location: Location) -> List[Facility]:
        """Query facilities at a specific location"""
        return [f for f in self.facilities if f.location == location]
    
    def can_afford_facility(self, cost: float) -> bool:
        """Check if faction has capital for new facility"""
        return self.capital >= cost
    
    def deduct_capital(self, amount: float) -> bool:
        """Pay out capital; return False if insufficient"""
        if self.capital >= amount:
            self.capital -= amount
            return True
        return False
    
    def add_capital(self, amount: float):
        """Earn capital"""
        self.capital += amount
```

### 5. World State Manager

```python
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class World:
    """Global game state"""
    current_year: int = 1
    current_month: int = 1  # 1–12
    
    # All factions
    factions: Dict[str, Faction] = field(default_factory=dict)
    player_id: str = "player"
    
    # Markets
    local_markets: Dict[Location, LocalMarket] = field(default_factory=dict)
    
    # Earth faction (demand driver)
    earth_faction: EarthFaction = None
    
    # Tech state
    global_research_points: float = 0.0
    tech_tree: Dict[str, Technology] = field(default_factory=dict)
    
    def get_player(self) -> Faction:
        """Get player faction"""
        return self.factions.get(self.player_id)
    
    def advance_month(self):
        """Advance time by one month"""
        self.current_month += 1
        if self.current_month > 12:
            self.current_month = 1
            self.current_year += 1
    
    def get_location_market(self, location: Location) -> LocalMarket:
        """Get or create local market"""
        if location not in self.local_markets:
            self.local_markets[location] = LocalMarket(location)
        return self.local_markets[location]
```

### 6. Technology

```python
from dataclasses import dataclass

@dataclass
class Technology:
    """A technology"""
    id: str                        # Unique ID
    name: str                      # Display name
    description: str               # What it does
    research_cost: float = 100.0   # RP required to unlock
    
    # POC (optional)
    has_poc: bool = True
    poc_cost_multiplier: float = 1.5  # Cost to pursue POC (% of base)
    poc_bonus: Dict[str, float] = None  # Bonus stats (e.g., {'+production': 0.1})
    
    # Unlocks
    unlocked_facilities: List[str] = None  # Facility types it unlocks
    unlocked_recipes: List[str] = None     # Recipe names it unlocks
    unlocked_locations: List[Location] = None  # New locations
```

---

## System Design

### 1. Production Resolution (Monthly)

**For each facility:**
```
1. Check if current recipe inputs available
2. If yes:
   a. Consume inputs (remove from local market)
   b. Run production (apply operation style multiplier)
   c. Add outputs to local market (production complete)
3. If no:
   a. Flag facility as blocked (show to player)
   b. Wait for next month
```

### 2. Market Resolution

**Per location, per good:**
```
1. Collect total supply (sum of outputs from all local facilities)
2. Calculate Earth demand for that good (faction demand)
3. Calculate scarcity multiplier: demand / supply (or min 1.0)
4. Calculate Earth price: base_price × scarcity_multiplier × demand_modifier
5. Apply distance penalty: final_price = Earth_price × (1 - distance_penalty)
6. Player sells goods at final_price; profits to player capital
```

### 3. AI Decision Loop (Monthly)

**For each AI faction:**
```
1. ASSESS:
   capital = current_capital
   opportunities = []
   for location in all_locations:
       for facility_type in all_facility_types:
           margin = estimate_profit_margin(facility_type, location)
           if margin > 0:
               opportunities.append((location, facility_type, margin))
   opportunities.sort(by=margin, descending=True)

2. EXPAND (if capital allows):
   best = opportunities[0]
   if capital > facility_cost:
       build_facility(best.location, best.facility_type)

3. PRODUCE:
   for facility in all_facilities:
       if facility.can_run_recipe():
           facility.run_production()
       else if facility.is_blocked():
           switch_operation_style(to=BASIC)  # Reduce costs if stuck

4. TRADE:
   for location in all_locations:
       goods = all_finished_goods_at(location)
       for good in goods:
           price = market_price(good)
           quantity = available_inventory(good)
           revenue = sell(good, quantity, price)
           capital += revenue

5. REINVEST:
   if capital > facility_cost + buffer:
       goto EXPAND  # recursive
```

### 4. Tech Research

```
monthly_increment:
  global_research_points += 10  # Base rate
  for player in all_factions:
      for research_lab in player.facilities:
          global_research_points += 2  # Lab bonus

next_tech_to_unlock = tech_tree.find_next_unresearched()
if global_research_points >= next_tech_to_unlock.cost:
    unlock(next_tech_to_unlock)
    global_research_points -= next_tech_to_unlock.cost
    global_research_points = 0  # Reset pool
```

---

## Key Algorithms

### Algorithm: Calculate Production Cost

```python
def calculate_production_cost(facility: Facility, recipe: Recipe, world: World) -> float:
    """
    Production cost = facility overhead + input acquisition cost
    
    Args:
        facility: The producing facility
        recipe: The recipe being executed
        world: Game world (for current prices)
    
    Returns:
        Total cost in credits
    """
    
    # Facility overhead
    cost = recipe.cost_credits
    
    # Input acquisition cost
    market = world.get_location_market(facility.location)
    for input_good, input_qty in recipe.inputs.items():
        local_price = market.prices.get(input_good, world.earth_faction.base_prices[input_good])
        cost += local_price * input_qty
    
    return cost
```

### Algorithm: Resolve Monthly Tick

```python
def monthly_tick(world: World):
    """Execute one month of game time"""
    
    # Phase 1: Production (all facilities run)
    for faction in world.factions.values():
        for facility in faction.facilities:
            if facility.current_recipe and facility.can_run_recipe(facility.current_recipe):
                facility.run_production(facility.current_recipe)
    
    # Phase 2: Market pricing (calculate prices for all goods)
    for location in world.local_markets.values():
        for good_name in all_goods:
            supply = location.inventory.get(good_name, 0)
            demand = world.earth_faction.get_demand(good_name)
            scarcity = demand / max(supply, 0.1)  # Avoid division by zero
            
            base_price = world.earth_faction.base_prices[good_name]
            earth_price = base_price * scarcity
            location.prices[good_name] = earth_price * (1 - location.calculate_distance_penalty())
    
    # Phase 3: Sales (all factions sell goods to Earth)
    for faction in world.factions.values():
        for location in world.local_markets.values():
            for facility in faction.get_facilities_at_location(location.location):
                for good_name, qty in facility.output_inventory.items():
                    price = location.prices.get(good_name, 0)
                    revenue = price * qty
                    cost = calculate_production_cost(facility, facility.current_recipe, world)
                    profit = revenue - cost
                    
                    faction.add_capital(profit)
                    location.remove_from_inventory(good_name, qty)
    
    # Phase 4: AI decisions (all AI factions decide & act)
    for faction in world.factions.values():
        if faction.is_ai:
            ai_agent = get_ai_agent(faction)
            ai_agent.decide_monthly(world)
    
    # Phase 5: Tech research (advance research pool)
    world.global_research_points += 10
    player = world.get_player()
    for facility in player.facilities:
        if facility.type == FacilityType.RESEARCH_LAB:
            world.global_research_points += 2
    
    # Phase 6: Events (random events might trigger)
    if random.random() < 0.2:  # 20% chance
        world.earth_faction.trigger_random_event()
    
    # Advance calendar
    world.advance_month()
```

---

## Dependencies & Tools

### Required

```
Python 3.8+
```

### Minimal Dependencies (Phase 1)

```
# requirements.txt
attrs>=21.0       # Type-safe data classes (alternative to dataclasses)
# Standard library only:
# - dataclasses (built-in, Python 3.7+)
# - json (built-in)
# - enum (built-in)
# - random (built-in)
# - logging (built-in)
```

### Optional (Phase 2+)

```
arcade>=2.6       # 2D graphics library
pytest>=6.0       # Testing framework
pytest-cov>=2.12  # Coverage reporting
black>=21.0       # Code formatter
mypy>=0.9         # Type checking
```

### Why Minimal Dependencies?

- Phase 1 is core simulation; no need for external libraries
- All core logic uses standard library
- Arcade deferred to Phase 2 (lightweight GUI)
- Easy to add dependencies in Phase 2 without rearchitecting

---

## Performance Targets

### Monthly Tick Performance

**Target:** < 100 ms per tick (monthly resolution)

**Typical load:**
- 3 locations
- 20 facilities (6–7 per location)
- 4 factions
- 15 goods (Phase 1–2)

**Bottleneck likely in:**
1. Price calculation (O(locations × goods))
2. Facility production (O(facilities))
3. AI decision logic (O(AI factions × opportunities))

**Optimization strategy (if needed):**
- Cache market prices (don't recalculate if supply unchanged)
- Batch AI decisions (avoid recomputing same opportunities multiple times)
- Profile first; optimize hotspots only

### Memory Target

**Target:** < 100 MB for 10-year save game

**Typical state:**
- 100+ facilities × (facility struct ~500 bytes) ≈ 50 KB
- Local markets × locations × goods × price history ≈ 10 KB (no history in MVP)
- Faction data ≈ 5 KB per faction
- Tech tree ≈ 5 KB

**No major memory leaks expected** in straightforward Python implementation.

---

## Testing Strategy

### Unit Test Coverage

**Target:** ≥ 80% coverage for core/ and ai/

| Module | Test Focus |
|--------|-----------|
| `resource.py` | Good creation, enum values |
| `facility.py` | Recipe execution, input/output validation, operation style multipliers |
| `location.py` | Local market mechanics, distance penalties |
| `faction.py` | Capital tracking, facility ownership |
| `world.py` | Global state management, faction queries |
| `simulation.py` | Price calculations, profit math, monthly tick |
| `agent.py` | AI heuristics, decision-making logic |

### Integration Tests

| Test | Focus |
|------|-------|
| `test_integration.py::test_full_game_36_months` | Player + 2 AI, 36 turns (3 years), no crashes |
| `test_integration.py::test_recipe_deadlock` | Complex recipes don't deadlock |
| `test_integration.py::test_ai_profitability` | AI factions expand and profit |
| `test_integration.py::test_price_dynamics` | Prices adjust with supply/demand |

### Test Execution

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=sol_corp --cov-report=term-report

# Run specific test
pytest tests/test_simulation.py::test_monthly_tick

# Run with verbose output
pytest -v
```

### Playtest Checklist

- [ ] Can player start game without errors?
- [ ] Can player build facility? See output?
- [ ] Can player switch recipes? See results?
- [ ] Can player save/load game?
- [ ] Does AI expand? Do prices move?
- [ ] Can player reach Year 2+?
- [ ] No negative prices or quantities?

---

## Implementation Notes for Dan

### Week 1 Priority: Get Data Models Right

Don't rush this phase. Spend time on clean data structures:
- Use type hints everywhere
- Use `@dataclass` or `attrs` for clarity
- Define all enums early
- Unit test each model as you build

**Why?** If data models are solid, the rest is straightforward. If they're messy, every feature addition becomes a refactor.

### Week 2–3: Focus on Economic Correctness

The simulation engine is the heart. Test it rigorously:
- Price calculations must be correct
- Profit math must be accurate
- No negative quantities
- No circular logic

**Manual debugging:** Print out detailed tick logs (verbose mode). When something breaks, trace the cash flow:
```
Facility produces 10 units of good X
Good X moves to market
Price calculated as P
10 units × P = revenue R
Revenue - cost = profit Q
Profit added to faction capital
```

### Week 4: Keep CLI Simple

Don't over-engineer the UI. Text commands are fine:
```
> status
Player capital: 45000 credits
Facilities: 3 (1 on Moon, 2 on Mars)
Tech progress: 25/100 RP to Iron Smelting

> map
Moon: 1 iron mine (yours), 1 rare earth processor (China AI)
Mars: 2 refineries (yours), 1 component factory (USA AI)

> next
[Month 5, Year 1]
Production completed. Revenue: 5,000 credits. Profit: 2,500 credits.
```

Keep commands simple. Phase 2 adds graphics.

### Week 5–6: Playtest Ruthlessly

Play your own game. Ask:
- Is Moon profitable? (Should be)
- Can you expand to Mars by Year 2? (Should be)
- Do AI factions compete? (Should be)
- Does any tech feel stuck? (Adjust RP if so)

**Balance log:** Every time you change a number (facility cost, base price, RP generation), write it down:
```
Changed iron ore base price: 50 → 45 (too scarce; Moon unprofitable)
Changed facility cost: 5000 → 4500 (too slow to expand early)
Changed RP generation: 10 → 12 (tech feels gated)
```

This becomes your Phase 2 reference.

---

## Appendix: Example Pseudocode Flow

### Player Builds Facility

```python
# In CLI:
> build moon iron_mine

# World state:
player = world.get_player()
facility_cost = 5000
if player.can_afford_facility(facility_cost):
    player.deduct_capital(facility_cost)
    new_facility = Facility(
        id="moon_mine_3",
        type=FacilityType.IRON_MINE,
        location=Location.MOON,
        owner=player.id,
        current_recipe=recipes['mine_iron']
    )
    player.facilities.append(new_facility)
    print("Built iron mine on Moon. Capital: " + str(player.capital))
else:
    print("Insufficient capital.")
```

### Player Advances Month

```python
# In CLI:
> next

# Simulation:
monthly_tick(world)

# Output:
print("Month 5, Year 1")
print(f"Production: {production_output}")
print(f"Revenue: {revenue}")
print(f"Profit: {profit}")
print(f"New capital: {world.get_player().capital}")
```

---

## Next Steps

1. **Copy this architecture** into your project skeleton
2. **Implement core/ modules** in Week 1 (follow data models above)
3. **Implement simulation.py** in Week 2 (monthly tick)
4. **Test ruthlessly** as you build
5. **Adjust if needed** based on what works for your style

---

**Ready to code? Start with `core/resource.py`. Good luck!** 🚀

