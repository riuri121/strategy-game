# Sol Corp Materials & Recipes

**Complete production chain reference: resources, facilities, recipes, and technology tree.**

---

## Table of Contents

1. [Resources Overview](#resources-overview)
2. [Facility Types](#facility-types)
3. [Recipes (Phase 1)](#recipes-phase-1)
4. [Technology Tree](#technology-tree)
5. [Production Chain Diagrams](#production-chain-diagrams)
6. [Balance Notes](#balance-notes)

---

## Resources Overview

### Tier 1: Raw Materials (Extracted from Planets)

| Resource | Location Availability | Base Price | Strategic Role |
|----------|----------------------|------------|-----------------|
| **Iron Ore** | Moon (high), Mars (medium), Belt (low) | 50 cr/unit | Essential; abundant; foundation for metal production |
| **Rare Earths** | Mars (high), Moon (medium), Belt (very high) | 150 cr/unit | Scarce; high-value; bottleneck for advanced goods |
| **Silicon** | Moon (low), Mars (medium), Belt (low) | 75 cr/unit | Electronics base; moderate value |

### Tier 2: Intermediate Goods (Processed from Raw Materials)

| Resource | Input | Base Price | Role |
|----------|-------|-----------|------|
| **Refined Metal** | Iron Ore | 100 cr/unit | Core production material; used in alloys, consumer goods |
| **Electronics Components** | Silicon | 120 cr/unit | Tech base; used in research, consumer goods |
| **Rare Alloys** | Rare Earth + Refined Metal | 180 cr/unit | Premium material; high-value; research accelerator |

### Tier 3: Finished Goods (Sold to Earth)

| Resource | Inputs | Base Price | Market |
|----------|--------|-----------|--------|
| **Consumer Goods** | Any 2+ intermediates (flexible) | 150 cr/unit | Constant demand (USA, Europe, China, India) |
| **Research Materials** | Rare Alloys + Electronics Components | 200 cr/unit | Tech-driven demand (variable by events) |

---

## Facility Types

### Extraction Facilities (Raw Material Sources)

#### 1. Iron Mine

```
Type:         IRON_MINE
Location:     Moon, Mars, Asteroid Belt
Build Cost:   5,000 credits
Maintenance:  100 credits/month overhead
Inputs:       Planetary deposit (free; infinite supply at location)
Output:       Iron Ore (10 units/month in Basic mode)
Operation Modes:
  - Basic:         10 ore/month, 100 cr overhead
  - Skeleton:      15 ore/month, 150 cr overhead
  - Fully Manned:  30 ore/month, 300 cr overhead

Tech Unlocks: None (available from start)
Notes:        
  - Abundant on Moon/Mars; scarce on Belt
  - Low profit margin; competition drives prices down
  - Essential for expansion (needed for refineries)
```

#### 2. Rare Earth Processor

```
Type:         RARE_EARTH_PROCESSOR
Location:     Moon, Mars, Asteroid Belt
Build Cost:   5,000 credits
Maintenance:  200 credits/month overhead
Inputs:       Planetary deposit (free; scarce supply)
Output:       Rare Earths (3 units/month in Basic mode)
Operation Modes:
  - Basic:         3 units/month, 200 cr overhead
  - Skeleton:      4.5 units/month, 300 cr overhead
  - Fully Manned:  9 units/month, 600 cr overhead

Tech Unlocks: "Rare Earth Extraction" (+50% efficiency)
Notes:        
  - High value; limited supply at each location
  - Risk-reward: Expensive to operate, but high margins
  - Belt has richest deposits (worth the distance penalty risk)
```

#### 3. Silicon Quarry

```
Type:         SILICON_QUARRY
Location:     Moon, Mars, Asteroid Belt
Build Cost:   5,000 credits
Maintenance:  150 credits/month overhead
Inputs:       Planetary deposit (free; abundant supply)
Output:       Silicon (8 units/month in Basic mode)
Operation Modes:
  - Basic:         8 units/month, 150 cr overhead
  - Skeleton:      12 units/month, 225 cr overhead
  - Fully Manned:  24 units/month, 450 cr overhead

Tech Unlocks: None (available from start)
Notes:        
  - Abundant; moderate price
  - Electronics foundation
```

---

### Processing Facilities (Tier 1 → Tier 2)

#### 4. Metal Refinery

```
Type:         METAL_REFINERY
Location:     Moon, Mars, Asteroid Belt
Build Cost:   5,000 credits
Maintenance:  150 credits/month overhead
Recipe (default, unlocked by "Iron Smelting" tech):
  Inputs:     8 Iron Ore
  Outputs:    5 Refined Metal
  Cost:       150 cr/cycle
Operation Modes:
  - Basic:         5 metal/month, cost 150
  - Skeleton:      7.5 metal/month, cost 225
  - Fully Manned:  15 metal/month, cost 450

Recipes Available (if tech unlocked):
  - Standard Smelting: 8 iron → 5 metal
  - Efficiency (Phase 2): 6 iron → 5 metal (requires upgrade)

Tech Unlocks: "Iron Smelting" (unlocks this facility)
Notes:        
  - Transform abundant ore into higher-value metal
  - Required for alloy production
  - Requires "Iron Smelting" tech to build
```

#### 5. Component Factory

```
Type:         COMPONENT_FACTORY
Location:     Moon, Mars, Asteroid Belt
Build Cost:   5,000 credits
Maintenance:  120 credits/month overhead
Recipe (default, unlocked by "Silicon Processing" tech):
  Inputs:     6 Silicon
  Outputs:    4 Electronics Components
  Cost:       120 cr/cycle
Operation Modes:
  - Basic:         4 components/month, cost 120
  - Skeleton:      6 components/month, cost 180
  - Fully Manned:  12 components/month, cost 360

Tech Unlocks: "Silicon Processing" (unlocks this facility)
Notes:        
  - Transform silicon into electronics
  - Essential for research materials
  - Requires "Silicon Processing" tech to build
```

---

### Finished Goods Factories

#### 6. Consumer Goods Factory

```
Type:         CONSUMER_GOODS_FACTORY
Location:     Moon, Mars, Asteroid Belt
Build Cost:   5,000 credits
Maintenance:  200 credits/month overhead
Recipe (flexible):
  Inputs:     Any 2+ intermediates (flexible combinations)
  Outputs:    Consumer Goods
  Examples:
    Option A: 5 Refined Metal + 3 Electronics → 8 Consumer Goods
    Option B: 4 Refined Metal + 2 Components + 1 Rare Alloy → 10 Consumer Goods
    Option C: 8 Electronics → 5 Consumer Goods
  Cost:       200 cr/cycle
Operation Modes:
  - Basic:         8 units/month, cost 200
  - Skeleton:      12 units/month, cost 300
  - Fully Manned:  24 units/month, cost 600

Notes:        
  - **Flexible input model** reduces deadlock risk
  - Player chooses input combination based on available resources
  - Constant Earth demand ensures market sink
  - Available from game start (no tech required)
```

#### 7. Research Lab

```
Type:         RESEARCH_LAB
Location:     Moon, Mars, Asteroid Belt
Build Cost:   5,000 credits
Maintenance:  200 credits/month overhead
Recipe (default):
  Inputs:     2 Rare Alloys + 3 Electronics Components
  Outputs:    5 Research Points (RP) + produces Consumer Goods as byproduct
  Cost:       200 cr/cycle
Operation Modes:
  - Basic:         5 RP/month, cost 200
  - Skeleton:      7.5 RP/month, cost 300
  - Fully Manned:  15 RP/month, cost 600

Tech Unlocks: None (available after tech unlocks alloy production)
Notes:        
  - Unique: Produces research points directly (not a market good)
  - Requires both rare alloys and components (valuable combination)
  - Player investment in labs speeds tech progression
  - Each lab grants +2 RP/month bonus
```

---

## Recipes (Phase 1)

### All Available Recipes

| Recipe | Facility | Inputs | Outputs | Cost | Notes |
|--------|----------|--------|---------|------|-------|
| Mine Iron | Iron Mine | (free) | 10 iron/mo | 100 | Base; abundant |
| Mine Rare Earth | Rare Processor | (free) | 3 rare/mo | 200 | Scarce; high value |
| Mine Silicon | Silicon Quarry | (free) | 8 silicon/mo | 150 | Abundant |
| Smelt Metal | Refinery | 8 iron | 5 metal/mo | 150 | Requires Iron Smelting tech |
| Make Components | Component Factory | 6 silicon | 4 components/mo | 120 | Requires Silicon Processing tech |
| Produce Consumer | Consumer Goods | 5 metal + 3 comp* | 8 goods/mo | 200 | Flexible inputs (see note) |
| Process Research | Research Lab | 2 alloys + 3 comp | 5 RP/mo | 200 | Also generates 2 cr profit |

*Consumer Goods Factory accepts multiple input combinations. All of these are valid:
- 5 metal + 3 components
- 8 metal only (lower output)
- 4 components only (lower output)
- 2 alloys + 2 components

---

## Technology Tree

### Phase 1 Core Technologies (6 Total)

#### Tech 1: Iron Smelting

```
Name:             Iron Smelting
Research Cost:    100 RP
Unlock Condition: Researched automatically after 100 RP
POC (Optional):   Costs 50 extra RP; grants +10% metal output

What It Unlocks:
  - Facility: Metal Refinery
  - Recipe: Iron Ore → Refined Metal (8 ore → 5 metal)

Why It Matters:
  - First major tech; unlocks production chains
  - Allows converting abundant iron into valuable metal
  - Foundation for alloy production

Typical Unlock Time: Turn 10 (Month 10, Year 1)

Strategic Notes:
  - Should unlock early (not a gate)
  - POC bonus (+10% metal) is nice but not critical
  - Player can skip POC if capital is tight
```

#### Tech 2: Silicon Processing

```
Name:             Silicon Processing
Research Cost:    100 RP
Unlock Condition: Researched automatically after 100 RP
POC (Optional):   Costs 50 extra RP; grants +10% component output

What It Unlocks:
  - Facility: Component Factory
  - Recipe: Silicon → Electronics Components (6 silicon → 4 components)

Why It Matters:
  - Electronics foundation
  - Required for research materials (high-value finished goods)
  - Parallel to Iron Smelting (both early)

Typical Unlock Time: Turn 10 (Month 10, Year 1)

Strategic Notes:
  - Should unlock alongside Iron Smelting
  - Creates two separate production chains
  - POC bonus helpful for electronics-heavy strategies
```

#### Tech 3: Rare Earth Extraction

```
Name:             Rare Earth Extraction
Research Cost:    150 RP
Unlock Condition: Researched after 150 RP total
POC (Optional):   Costs 75 extra RP; grants +50% rare earth mine output

What It Unlocks:
  - Efficiency: Rare earth mines output +50% (3 → 4.5 units/month in Basic)
  - Makes Belt mining more viable (compensates for distance penalty)

Why It Matters:
  - Bottleneck remover: Rare earths are scarce; this tech helps
  - Belt specialization becomes possible (high rare earth + efficiency = profit)

Typical Unlock Time: Turn 15 (Month 3, Year 2)

Strategic Notes:
  - Medium-tier tech; gates Belt viability
  - POC bonus is very valuable (+50% output is major)
  - Player considering Belt should pursue this POC
```

#### Tech 4: Alloy Mastery

```
Name:             Alloy Mastery
Research Cost:    150 RP
Unlock Condition: Researched after cumulative 300 RP
POC (Optional):   Costs 75 extra RP; grants +10% alloy output

What It Unlocks:
  - Recipe: Rare Earth + Refined Metal → Rare Alloys (1 rare + 1 metal → 1 alloy)
  - Enables research material production (alloys + components → research)

Why It Matters:
  - Unlocks highest-value production chain
  - Research materials drive tech progression (and sell well)

Typical Unlock Time: Turn 15–20 (Month 3–8, Year 2)

Strategic Notes:
  - Gates research lab usefulness
  - Alloys are expensive to make (requires rare earths); should be scarce
  - POC bonus is moderate (not as critical as Rare Earth Extraction)
```

#### Tech 5: Mars Colonization

```
Name:             Mars Colonization
Research Cost:    200 RP
Unlock Condition: Researched after cumulative 500 RP
POC (Optional):   Costs 100 extra RP; grants 5% reduction in Mars distance penalty (20% → 15%)

What It Unlocks:
  - Location: Mars becomes accessible
  - Bonus: Distance penalty reduced from 20% to 15% (POC only)

Why It Matters:
  - Mid-game expansion gate
  - Mars is balanced (not Moon's abundance, not Belt's scarcity)
  - Natural progression after Moon saturation

Typical Unlock Time: Turn 25 (Month 1, Year 3)

Strategic Notes:
  - Should unlock when Moon feels saturated (too many competitors)
  - POC bonus helps but not essential (difference between 20% and 15% is marginal)
  - Incentivizes tech investment (better to unlock early and expand faster)
```

#### Tech 6: Asteroid Mining

```
Name:             Asteroid Mining
Research Cost:    200 RP
Unlock Condition: Researched after cumulative 700 RP
POC (Optional):   Costs 100 extra RP; grants 10% reduction in Belt distance penalty (50% → 40%)

What It Unlocks:
  - Location: Asteroid Belt becomes accessible
  - Bonus: Distance penalty reduced from 50% to 40% (POC only)

Why It Matters:
  - Late-game expansion gate
  - Belt has richest rare earths; high risk/reward (50% distance penalty)
  - Specialized play (rare earth focused) becomes viable

Typical Unlock Time: Turn 30+ (Month 6+, Year 3)

Strategic Notes:
  - Should unlock late enough that Moon/Mars are already developed
  - POC bonus is valuable (10% reduction is 20% improvement in margins)
  - Encourages long-term play (reaching Belt feels like achievement)
```

### Tech Tree Summary (Visual)

```
Turn 10:  Iron Smelting ─┐
                          ├─→ Turn 20: Alloy Mastery
          Silicon Processing ┘

Turn 15:  Rare Earth Extraction ──→ Makes Belt viable

Turn 25:  Mars Colonization ──→ Unlock Mars location

Turn 30+: Asteroid Mining ──→ Unlock Belt location
```

**Research Point Flow:**
```
Global generation: +10 RP/month
Player research labs: +2 RP/month per lab

Typical 3-year progression:
  Year 1 (Months 1–12):     +120 RP global = 2 early techs
  Year 2 (Months 13–24):    +120 RP global + labs = 2–3 mid-tier techs
  Year 3 (Months 25–36):    +120 RP global + labs = 1–2 late-tier techs
```

---

## Production Chain Diagrams

### Simple Chain (Moon Early Game)

```
Iron Ore (Mine)
       ↓ (Smelt Metal)
   Refined Metal
       ↓ (Combine with Components)
   Consumer Goods ──→ Earth (Sell)
```

**Capital requirement:** 2 facilities (mine + refinery) = 10k credits
**Monthly profit:** ~500–1000 credits (tight margin)

### Complex Chain (Mars Mid-Game)

```
Iron Ore         Silicon             Rare Earth
     ↓               ↓                   ↓
Refined Metal   Electronics        (Stock: limited)
        ╲__________╱                   ↓
         Consumer Goods     +          (Stock)
                  ↓              ╱
              (10,000 cr) ←─ Rare Alloys
              
Refined Metal + Electronics + Rare Alloys
              ↓
        Research Materials (sell for 200 cr/unit)
```

**Capital requirement:** 6 facilities (2 mines, refinery, quarry, component factory, lab) = 30k credits
**Monthly profit:** ~5000+ credits (decent margin)

### Optimized Chain (Belt Late-Game)

```
Rare Earth (Belt, +50% efficiency from tech)
        ↓ (abundant supply now)
Rare Alloys (combine with metals)
        ↓
Research Materials (sell for 200+ cr/unit)
        ↓
Profits reinvested into more rare earth mines
        ↓
Specialization: Belt becomes rare earth factory
```

**Capital requirement:** 5–8 facilities, heavy rare earth focus
**Monthly profit:** 10,000+ credits (belt's rich deposits overcome distance penalty)

---

## Balance Notes

### Facility Costs & Profitability

**Build Cost:** All facilities = 5,000 credits (Phase 1 fixed)

**Profitability by Location (Moon):**

```
Iron Mine:
  Production: 10 ore/month
  Cost: 100 cr overhead
  Base Price: 50 cr/ore
  Gross Revenue: 500 cr
  Profit: 400 cr/month (good for early game)
  
Refinery (8 ore → 5 metal):
  Input Cost: 8 × 50 = 400 cr (from Moon iron)
  Production: 5 metal
  Revenue: 5 × 100 = 500 cr
  Cost: 150 cr overhead + 400 input = 550 cr
  Profit: -50 cr/month (LOSS initially)
  
Fix: When competition drives down ore prices (30 cr/ore):
  Input Cost: 8 × 30 = 240 cr
  Revenue: 500 cr
  Profit: 500 - 240 - 150 = 110 cr/month ✓
```

**Key insight:** Early Moon mining is profitable. Processing is profitable only when:
1. You have access to cheap inputs (your own mines), OR
2. Market price is favorable (low competition)

### Tech Timing

**Desired progression:**
- Year 1 (months 1–12): Iron Smelting, Silicon Processing
- Year 2 (months 13–24): Rare Earth Extraction, Alloy Mastery
- Year 3 (months 25–36): Mars Colonization, then Asteroid Mining

**Research point tuning:**
- Current: +10 RP/month global = ~120 RP/year
- Tech costs: 100, 100, 150, 150, 200, 200 (total 900 RP for all 6)
- At +120/year: takes 7.5 years to unlock all (too slow)
- **Actual:** Player labs provide +2 RP/month boost, so total is 10–20 RP/month depending on lab count
- **Target:** All 6 techs by Year 3.5–4 (42–48 months)

**Adjustment if off:**
- If techs too slow: increase global RP to +12/month or reduce tech costs by 10%
- If techs too fast: reduce global RP or increase tech costs

---

## Appendix: Recipe Balance Spreadsheet Template

For Iris's recommendation, before coding starts, populate this:

```
| Facility Type     | Recipe Name | Inputs | Output | Time | Cost | Notes |
|-------------------|-------------|--------|--------|------|------|-------|
| Iron Mine         | Mine Iron   | (free) | 10 ore | 1 mo | 100  | Basic |
| [...]             | [...]       | [...]  | [...] | [...] | [...] | [...] |
```

Once locked, don't change these mid-development. If balance is off, adjust:
- Base prices (Earth market price for goods)
- Operation style multipliers (speed/cost trade-off)
- Tech bonuses (POC benefits)

Not the recipes themselves (too risky for cascade effects).

---

**Next:** See [AI_HEURISTICS.md](AI_HEURISTICS.md) for AI faction behavior.

