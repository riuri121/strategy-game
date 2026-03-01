# Sol Corp — Production System

## Overview
Facilities convert inputs into outputs. Each resource type has one facility type. Facilities can be customized via **recipes**, **operation styles**, and **faction bonuses**.

---

## Facility Types

One facility per resource:

**Raw Materials (TBD: 5–8 types):**
- Ore mine
- Mineral extractor
- Rare earth processor
- [TBD]

**Intermediates (TBD: 5+ types):**
- Refinery
- Component factory
- [TBD]

**Finished Goods (4 types):**
- Military goods factory
- Consumer goods factory
- Development goods factory
- Research materials lab

---

## Production Mechanics

### Recipes

**Definition:** Each facility type has multiple recipes. A recipe specifies:
- **Inputs:** What raw/intermediate goods are required
- **Input ratio:** How much of each input per unit time
- **Outputs:** What finished good is produced
- **Output ratio:** How much is produced per unit time
- **Efficiency:** How much input waste occurs

**Tech unlocks recipes:**
- Basic recipe available at game start
- Tech research unlocks more advanced recipes
- Advanced recipes typically use different inputs, less waste, or higher output

**Player choice:**
- Can assign different recipes to different facilities of the same type
- Optimal recipe depends on local input availability and import costs
- A "premium" recipe might require imports; a "local" recipe uses available inputs at lower cost

### Operation Styles (Locked Decision)

Every facility can operate in three modes:

| Mode | Speed | Cost | Uptime | Use Case |
|------|-------|------|--------|----------|
| **Basic Automation** | Slow | Low | High | Low-priority resource chains; leave running unattended |
| **Skeleton Crew** | Medium | Medium | Medium | Balanced approach; moderate output & cost |
| **Fully Manned** | High | High | High | Rush production; high-value goods; critical chains |

**Mechanics:**
- Player can switch operation style per facility at any time
- Each style has different input consumption rates and output rates
- Exact ratios TBD, but proportional: Fully Manned ≈ 3× speed & cost vs. Basic

**Strategic depth:** Choose style based on:
- Local resource availability (if bottlenecked, slow style preserves imports)
- Profit margins (high-value goods → Fully Manned; commodity goods → Basic)
- Cash flow (high upfront cost → Skeleton Crew for balance)

---

## Facility Bonuses

Faction passive abilities apply to facilities:

- **Mining Corp:** +10% extraction (mines only?)
- **Logistics Specialist:** -10% transport costs (all facilities?)
- **Tech Pioneer:** Tech research 15% faster (research labs only?)
- **Diplomat:** Earth factions favor them (affects sale prices?)

**TBD:** Which bonuses apply to which facility types, exact values.

---

## Building & Managing Facilities

**Construction:**
- Player builds facility at a location (costs credits, time, materials?)
- Facility starts with basic recipe and basic automation
- Player can immediately switch recipe (if tech unlocked) or operation style

**Inputs & Outputs:**
- Facility pulls inputs from local market
- If inputs aren't locally available, facility imports (at distance penalty)
- Facility produces output; goes to local market (can be exported)

**Upgrades (TBD):**
- Can facilities be upgraded (faster, more efficient)?
- Does size/efficiency scale, or is it flat?

---

## Open Questions

- [ ] What are specific recipes for each facility type? (inputs, ratios, outputs)
- [ ] What are exact speed/cost ratios for operation styles?
- [ ] How much does building a facility cost? Is it location-dependent?
- [ ] Do facilities have maintenance costs? If so, how much?
- [ ] Can facilities break down or need repair?
- [ ] How do you handle "idle" facilities (if inputs run out)?
- [ ] Can facilities be sold/demolished?
- [ ] Is there a limit to how many facilities you can build?
