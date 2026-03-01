# Sol Corp — Locations & Production

## Overview
Each location is a production node with its own market. Transport between locations incurs distance-based penalties: goods are more expensive to import based on logistical distance.

**Distance malus applies both ways:** Selling to Earth and importing from Earth both incur costs.

Current malus (placeholder, TBD exact formula):
- Moon → Earth: ~10% effective price increase
- Mars → Earth: ~20% effective price increase
- Asteroid Belt → Earth: TBD

---

## Production Chain (WIP)

### Production Tier System (3-Tier)

**Tier 1: Raw Materials** (extracted from locations via mines/extractors)
- 5–8 types (ore, minerals, rare earths, ice, metals, etc.) — TBD specifics
- Produced at location-specific extraction facilities
- Inputs: None (drawn from planet/asteroid)
- Outputs: Raw material units

**Tier 2: Intermediates** (refined/processed from raw materials)
- 5+ types (refined metals, alloys, components, processed compounds, etc.) — TBD specifics
- Produced at refineries, component factories, processors
- Inputs: Raw materials
- Outputs: Intermediate products

**Tier 3: Finished Goods** (sold to Earth factions; final layer for economy)
- Military goods (weapons, armor, defense systems)
- Consumer goods (tools, equipment, manufactured products)
- Development goods (construction materials, infrastructure components)
- Research materials (advanced tech inputs, rare components)
- Produced at specialized factories and research labs
- Inputs: Intermediates (and/or raw materials for some recipes)
- Outputs: Finished goods sold to Earth

---

## Locations

### Moon

**Characteristics:**
- Closest to Earth (lowest transport cost)
- High ore concentration
- Limited real estate; mining saturation risk
- Lower extraction costs vs. other locations

**What it produces:**
- TBD raw materials (high-value ore?)

**What it needs:**
- TBD intermediates for factories/refineries

**Capacity/Competition:**
- Multiple factions can build mines at same location (economic competition, not exclusive)
- No hard saturation limit, but player can monopolize via cheap prices
- Space elevator potential (future tech unlock?)

**Strategic role:**
- Early-game foothold; safest investment
- Crowded market; thin margins unless you monopolize

---

### Mars

**Characteristics:**
- Moderate distance to Earth (moderate transport cost)
- Decent resource diversity
- Potential for self-sustaining colony
- Higher extraction costs than Moon, lower than asteroid belt

**What it produces:**
- TBD raw materials (different mix from Moon?)

**What it needs:**
- TBD intermediates for factories/refineries

**Capacity/Competition:**
- Multiple factions can build at same location (economic competition)
- No hard saturation limit
- Less crowded than Moon; opportunity for early expansion

**Strategic role:**
- Mid-game expansion; colony potential
- Foundation for long-term independence from Earth
- Strategic hub for reaching Asteroid Belt

---

### Asteroid Belt

**Characteristics:**
- Far from Earth (high transport cost)
- Rich in rare materials
- No real-estate limit (abundant locations)
- High extraction costs; logistics are complex

**What it produces:**
- TBD raw materials (rare materials, platinum, etc.?)

**What it needs:**
- TBD intermediates for mining operations

**Capacity/Competition:**
- Unlimited expansion (no saturation; many scattered sites)
- Multiple factions can operate independently (low crowding)
- High logistics costs make it less attractive early-game

**Strategic role:**
- Late-game specialization; high-risk, high-reward
- Only profitable if you can manage transport costs
- Source of rare materials commanding premium prices
- Gateway to strategic depth and economic dominance

---

## Market Mechanics per Location

Each location has:
- **Local market:** What's produced here, what's consumed here
- **Import costs:** Bringing goods in (from Earth or other locations) costs extra
- **Export costs:** Shipping goods out costs extra
- **Profit margin:** (Sell price - production cost - import/export costs)

---

## Open Questions

**Locked In:**
- [x] Multiple factions at same location: **Yes (economic competition only)**
- [x] Capacity limits: **No hard saturation; economic forces limit growth**

**TBD:**
- [ ] How do you move goods between locations (Moon → Mars)? Are inter-location transport costs separate from Earth distance costs?
- [ ] Can you store goods at a location, or do they sell/consume immediately?
- [ ] Do locations ever deplete (ore runs out), or are they infinite?
- [ ] How do you establish a location initially? (Build settlement first? Automatic unlock? Research milestone?)
