# Sol Corp — Space Factions

## Overview
Space factions are AI-controlled corporations, identical to the player. They compete with you for mining sites, locations, and resources across the solar system. They also generate supply that affects Earth market prices.

---

## MVP (Identical Factions)

**Number of factions:** Game-start setting (TBD, not hardcoded)

**Starting state:** All space factions are mechanically identical to the player. They:
- Start with some capital and a foothold location
- Can build mines, factories, colonies
- Compete for the same resources and locations
- Trade with Earth factions
- Pursue profit independently

---

## Future Differentiation (Post-MVP)

Once core systems are solid, add **3 differentiation levers:**

### 1. Starting Conditions
- **Bare settlement:** Minimal starting capital, basic equipment
- **Established mine:** Pre-built mine on Moon or Mars
- **Trade hub:** Partial space elevator or established logistics
- **Research outpost:** Tech advantage (unlock techs faster)

### 2. Earth Alignment
- Each faction has a **preferred Earth buyer** (USA, Europe, China, or India)
- Aligned Earth power buys from them at slight discount/preference
- Creates natural market niches (e.g., one faction supplies China preferentially)

### 3. Passive Abilities
- **Mining Corp:** +10% mineral extraction efficiency
- **Logistics Specialist:** -10% transport costs
- **Tech Pioneer:** Tech research 15% faster
- **Diplomat:** Earth factions favor them slightly (better prices)

---

## Space Faction AI (Rough Sketch)

Each faction runs a simplified economic loop:
1. **Assess:** What locations are available? What resources are profitable?
2. **Compete:** Build where player hasn't; try to monopolize certain locations
3. **Produce:** Mine ore, build factories, manage supply chains
4. **Trade:** Sell to Earth factions; compete on price
5. **Reinvest:** Expand operations with profits

---

## Player Interaction with Space Factions

**Competition:**
- You can't block them from building (locations can host multiple miners)
- You can undercut their prices, steal their market share
- You can compete for the same rare-deposit sites

**No direct trade with space factions** (MVP):
- You compete, don't cooperate
- Future: could add alliances, sabotage, merger mechanics

---

## Open Questions

- [ ] Can multiple factions mine the same location simultaneously, or is it exclusive?
- [ ] Do space factions ever go bankrupt, or are they persistent?
- [ ] Can player interfere with their operations (sabotage, blockade)?
