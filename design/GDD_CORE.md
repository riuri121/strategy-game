# Sol Corp — Game Design Document (Core)

## High Concept
A pauseable real-time/turn-based economic sandbox where the player controls a single corporation industrializing the solar system. Inspired by Victoria 3's economic depth, players manage supply chains, factories, mines, and colonies across multiple celestial bodies to generate profit and export goods back to Earth. No hard win condition—players define their own goals (richest player, self-contained colony, Earth conquest, etc.).

---

## Core Pillars

1. **Emergent Economics** — Supply chains, market dynamics, and profit drive gameplay. Earth factions create demand; space factions compete for the same resources.
2. **Long-term Strategy** — Building and managing infrastructure across locations; tech progression unlocks new capabilities.
3. **Meaningful Choices** — Where to build, what to produce, how to compete. No dominant strategy.
4. **Player-Defined Victory** — Goals are sandbox-style (become richest, create self-sustaining colony, militarize and invade Earth, etc.).

---

## Scope (Iterative Expansion)

### Phase 1 (MVP): Inner Solar System
- **Locations:** Earth (market only), Moon, Mars, Asteroid Belt
- **Mechanics:** Basic mining, factories, trade, technology research
- **Factions:** 4 Earth factions (demand drivers), 2+ space factions (competitors, configurable count)
- **Tech system:** Shared research pool with POC mechanics (see TECH_TREE.md)

### Phase 2: Economic Depth
- Advanced technology progression, more complex supply chains, faction diplomacy, military mechanics (blockades, etc.)

### Phase 3: Expansion
- More celestial bodies, deeper AI, emergent warfare, player alliances (if multiplayer considered).

---

## Key Systems (High-Level)

### Economy
- **Resources:** Raw materials → intermediates → finished goods
- **Markets:** Earth market (price-driven demand from factions), intra-system trade
- **Profit:** Margins = (sell price - production cost - transport cost - facility cost)
- **Currency:** Credits. Player starts with capital; reinvestment is key.
- **Early-game bootstrap:** Earth exports cheap construction materials (unlimited supply) to help player build first facilities. Becomes uneconomical mid-game as space production scales.

### Factions

**Earth Factions (3):**

- Compete with each other; generate demand for specific goods
- Set base prices on Earth goods
- Do NOT compete with the player directly (they're the market)
- May have political relationships that affect demand/supply

**Space Factions (2):**

- Compete with the player for mining sites, locations, and resources
- May trade with you, blockade routes, or fight
- Have their own production capabilities (threat/opportunity)

### Locations

**Moon:**

- High ore concentration; closest to Earth (lowest transport costs ~10%)
- Limited real estate; mining saturation risk

**Mars:**

- Moderate resources; potential for self-sustaining colonies
- Moderate distance to Earth (moderate transport costs ~20%)

**Asteroid Belt:**

- Rich in rare materials; no natural limit on expansion
- Distant from Earth (high transport costs; exact formula TBD)
- Logistics are complex

**Earth:**

- Market hub; never buildable (resource sink)
- Demand fluctuates based on faction behavior

**Distance mechanics:** Transport costs apply both ways (import and export). Goods become more expensive to import/export based on location distance.

### Time & Turns
- **Pauseable real-time** preferred (can pause to make decisions, let it run)
- **Alternative:** Turn-based (each turn = 1 month/quarter/year; TBD)

---

## Player Experience Loop

1. **Observe** — Check markets, faction demand, competitor actions
2. **Plan** — Decide where to build, what to produce, how to finance
3. **Act** — Place factories, mines, adjust production queues, trade
4. **Wait** — Watch resources flow, profits accumulate (pause available)
5. **Iterate** — Reinvest, expand, respond to market shifts

---

## Design Questions / Open Decisions

**Locked In:**
- [x] Supply logistics: **Simulated with distance-based cost penalties** (not instant delivery)
- [x] Earth factions: **USA, Europe, China, India** (4 permanent powers)
- [x] Space factions: **MVP identical; configurable count** (future differentiation via starting conditions & abilities)
- [x] Production tiers: **Raw materials → intermediates → finished goods** (3-tier system)
- [x] Facility operation styles: **Basic Automation / Skeleton Crew / Fully Manned** (affects speed & cost)

**TBD:**
- [ ] Faction relationships with space factions: Can you ally, negotiate, or sabotage?
- [ ] Military mechanics: Direct combat, economic sabotage, both, or deferred to Phase 2?
- [ ] Tech tree structure: Linear, branching, or unlock-based progression?
- [ ] UI paradigm: Classic RTS, spreadsheet/tycoon style, or hybrid?
- [ ] Game length: Typical playthrough 10, 50, or 100+ hours?
- [ ] Difficulty/Sandbox modes: Dynamic AI aggression presets, resource scarcity variants?

---

## Notes

- **Inspiration:** Victoria 3 (economy), Offworld Trading Company (theme), Satisfactory (production chains)
- **Target audience:** Strategy/sim fans who enjoy emergent gameplay and long-term planning
- **Platform:** TBD (Web, Desktop, both?)
- **Engine/Tech:** TBD (to explore with Dan)
