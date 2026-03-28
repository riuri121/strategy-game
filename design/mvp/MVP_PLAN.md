# Sol Corp MVP Development Plan

**Status:** Ready for development  
**Prepared:** 2026-03-28  
**Target Audience:** Dan Bull (solo developer)  
**Scope:** 3-phase MVP to playable economic sandbox

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [MVP Philosophy](#mvp-philosophy)
3. [Phase Overview](#phase-overview)
4. [Core Systems (Phase 1)](#core-systems-phase-1)
5. [Critical Decisions](#critical-decisions)
6. [Technical Architecture](#technical-architecture)
7. [Risk & Mitigation](#risk--mitigation)
8. [Success Criteria](#success-criteria)
9. [Related Documents](#related-documents)

---

## Executive Summary

**Goal:** Build a playable economic sandbox game where players mine resources, manage production chains, compete with AI factions, and reinvest profits.

**Why this matters:**
- Economic feedback loop is core to fun (Mine → Produce → Sell → Reinvest)
- Meaningful scarcity forces real tradeoffs
- Competition with AI creates tension and replayability

**Scope (Phase 1, 4–6 weeks):**
- 3 playable locations (Moon, Mars, Asteroid Belt)
- 8 resources in 3 tiers
- 6 facility types with flexible recipes
- 6 core technologies with progression gates
- 2 AI factions + 4 Earth demand drivers
- Text/CLI interface
- Playable from Year 1 through Year 3+ with visible tech progression

**Success looks like:**
Player builds a mine on the Moon, sells ore, reinvests in a refinery, expands to Mars, competes with AI factions for market share, and reaches Year 3 without economic collapse. **That's Phase 1 done.**

---

## MVP Philosophy

### Strip to Essentials First

Three systems must work for Sol Corp to be fun:

| System | What It Does | Phase 1 Target |
|--------|-------------|----------------|
| **Economic loop** | Mine → Produce → Sell → Reinvest feels rewarding | Build, operate, profit, expand cycles are tight & clear |
| **Scarcity & tradeoffs** | Limited capital, space, resources force choices | Distance penalties, competition, capital constraints matter |
| **Competition** | AI factions compete for same resources | 2 heuristic AI factions drive dynamic prices |

Everything else (diplomacy, complex AI types, military conflict, graphics) is flavor for Phase 2+.

### Speed > Perfection

- Playable code beats perfect design
- Rough edges are OK if the loop is fun
- Iterate based on playtest feel, not theory
- **Ship Phase 1 early; learn fast; iterate Phase 2–3**

---

## Phase Overview

### Phase 1: Core Loop (4–6 weeks)

**Goal:** Playable economic sandbox  
**Deliverables:** Python simulation, CLI interface, save/load, 3-year playthrough

| Aspect | Details |
|--------|---------|
| Locations | 3 (Moon, Mars, Asteroid Belt) |
| Resources | 8 (3 raw, 3 intermediate, 2 finished goods) |
| Facilities | 6 types |
| Technologies | 6 core techs |
| AI Factions | 2 identical heuristic agents |
| Earth | 4 demand drivers (USA, Europe, China, India) |
| Interface | CLI/text-based |
| Approx. Code | 3,000 lines Python |

**Key milestones:**
- Week 1: Data models + production logic
- Week 2: Economic resolution + markets
- Week 3: AI faction loop
- Week 4: CLI UI + player control
- Week 5–6: Testing, balance, polish

### Phase 2: Economic Depth (3–4 weeks)

**Goal:** Expand complexity; deepen tech tree; improve UI  
**Depends on:** Phase 1 playable

- Expand to 15 resources, 12–15 techs
- Facility upgrades over time
- Light military mechanics (blockades, not combat)
- Arcade GUI (lightweight 2D interface)
- Balance pass based on Phase 1 playtest

### Phase 3: Expansion & Scale (4–6 weeks)

**Goal:** More locations, differentiated AI, performance  
**Depends on:** Phase 2 complete

- 6–8 celestial locations (moons, Venus, Mercury)
- 4 AI faction types (specialist miners, tech pioneers, diplomats, logistics)
- Rust performance core (port critical simulation for speed)
- Full 2D GUI with Arcade
- Advanced supply chain mechanics (storage, failures, logistics)

---

## Core Systems (Phase 1)

### 1. Locations & Resources

**3 Playable Locations:**

| Location | Distance | Ore Abundance | Rare Earth | Silicon | Strategic Role |
|----------|----------|---------------|-----------|---------|-----------------|
| **Moon** | 10% penalty | High | Medium | Low | Early foothold; tight margins push efficiency |
| **Mars** | 20% penalty | Medium | High | Medium | Balanced mid-game expansion |
| **Asteroid Belt** | 50% penalty | Low | Very high | Low | Late-game specialization; risky/rewarding |

**Why this progression:** Moon is accessible, forces early-game learning. Mars becomes viable as capital grows. Belt rewards long-term investment but requires significant logistics.

**Distance penalty:** Transport cost reduces sell price. Example: Moon ore sells at 90% of Earth price due to 10% transport malus.

---

### 2. Resources: 3-Tier Production Chain

**Raw Materials (Tier 1):**
- Iron Ore — Abundant, low value, essential base resource
- Rare Earths — Scarce, high value, critical for advanced goods
- Silicon — Abundant, moderate value, electronics base

**Intermediates (Tier 2):**
- Refined Metal (iron ore → metals) — Refined metals for construction
- Electronics Components (silicon → components) — Electronics & tech
- Rare Alloys (rare earth + metal → alloy) — Premium materials

**Finished Goods (Tier 3):**
- Consumer Goods — Sold to all Earth factions (default demand sink)
- Research Materials — Sold for tech acceleration

**Why 8 resources?**
- Testable solo: not overwhelming to balance
- Meaningful chains: 3 production tiers create depth
- Growth path: Expand to 12–15 resources in Phase 2 without rearchitecting

---

### 3. Facilities: 6 Types with Flexible Recipes

| Facility | Input | Output | Time | Cost | Strategic Note |
|----------|-------|--------|------|------|-----------------|
| Iron Mine | (planetary ore) | 10 iron/month | 1 mo | 100 cr | Abundant; low margin; essential |
| Rare Earth Processor | (planetary deposits) | 3 rare earth/month | 1 mo | 200 cr | Scarce; high margin; risky |
| Silicon Quarry | (planetary deposits) | 8 silicon/month | 1 mo | 150 cr | Abundant; moderate margin |
| Metal Refinery | 8 iron | 5 refined metal/month | 1 mo | 150 cr | Core processing; unlocked by tech |
| Component Factory | 6 silicon | 4 components/month | 1 mo | 120 cr | Electronics base; unlocked by tech |
| Research Lab | 2 alloys + 3 components | 5 RP/month | 1 mo | 200 cr | Tech acceleration; unlocked by tech |

**Consumer Goods Factory:** Special facility that accepts any combination of intermediates (flexible recipe) and outputs consumer goods. Reduces deadlock risk.

**Why?** Flexible inputs prevent production chains from locking up. Player has agency in choosing input combinations.

---

### 4. Technology Tree: 6 Core Techs

**Tech progression unlocks recipes and locations:**

| Tech | Cost | Unlocks | Benefit | Typical Unlock |
|------|------|---------|---------|----------------|
| **Iron Smelting** | 100 RP | Metal refinery | Refine iron → metal | Year 1 (Turn 10) |
| **Silicon Processing** | 100 RP | Component factory | Process silicon → components | Year 1 (Turn 10) |
| **Rare Earth Extraction** | 150 RP | Rare earth efficiency | +50% rare earth mine output | Year 1–2 (Turn 15) |
| **Alloy Mastery** | 150 RP | Rare alloy recipe | Combine metal + rare earth → alloy | Year 2 (Turn 15) |
| **Mars Colonization** | 200 RP | Mars location | +distance penalty reduction to 15% | Year 2–3 (Turn 25) |
| **Asteroid Mining** | 200 RP | Belt location | +distance penalty reduction to 40% | Year 3+ (Turn 30) |

**Research mechanics:**
- Global research pool: +10 RP/month (everyone contributes)
- Player research labs: +2 RP/month per lab (player-controlled investment)
- POC system (simplified): Each tech has 1 optional POC per tech
  - Pursuing POC costs 50% extra RP; grants +10% production bonus for that tech
  - Skipping POC gets normal unlock without bonus
- Player choice: Specialize early or diversify slowly?

---

### 5. Factions & Competition

**Player:**
- Identical mechanics to AI
- Player agency via UI (build, operate, sell)
- Starts with 50,000 credits

**AI Factions (2 identical heuristic agents):**
- Each starts with 30,000 credits
- Monthly decision loop: Assess → Expand → Produce → Trade → Reinvest
- Heuristic rules: Expand to underexploited locations, undercut prices, reinvest profits
- Simple, deterministic, debuggable

**Earth Factions (4 demand drivers, non-playable):**
- USA, Europe, China, India
- Constant base demand + monthly random events (boom, crisis, conflict, tech spike)
- Buy consumer goods & research materials at dynamic prices
- Provide market sink; competitive pressure driver

**Why 2 AI factions?**
- 3-way competition (player + 2 AIs) creates tension
- Not overwhelming to simulate solo
- Gives player a sense of pacing: "I'm losing to them, or I'm winning"

---

### 6. Economic System: Markets & Pricing

**Local markets** at each location:
- Supply: What's produced locally (mine output, factory output)
- Demand: What's consumed locally (minimal in MVP; most goods flow to Earth)
- Price: Dynamic based on supply/demand

**Earth market** (central hub):
- Faction demand: Each faction wants specific goods at specific quantities
- Price formula:
  ```
  Earth market price = base_price × demand_multiplier × scarcity_multiplier
  ```
- Distance penalty applied on export:
  ```
  Final sell price = Earth market price × (1 - distance_penalty)
  ```
- Example: Consumer goods base price 100 cr/unit, Moon penalty 10%, Earth demand 2x:
  ```
  Earth price = 100 × 2.0 × 1.0 = 200 cr/unit
  Final Moon sale = 200 × 0.90 = 180 cr/unit net
  ```

**Production cost:**
```
Production cost = (input_costs × input_ratio) + (facility_overhead)
Profit per unit = final_sale_price - production_cost
```

**Key feature:** Prices are alive. Scarcity → high prices → rush production → supply flood → prices drop. Forces player to adapt.

---

### 7. Game Loop: Monthly Resolution

**Each in-game month:**

1. **Player observes** market prices, AI expansion, tech progress
2. **Player acts** via UI: build facilities, switch recipes, operate/pause facilities
3. **Simulation runs:**
   - Mines extract raw materials (limited by location capacity)
   - Factories consume inputs, produce outputs
   - Goods flow to market; prices resolve
4. **Finished goods sell** to Earth factions (automatic at market rates)
5. **Costs deducted:** Facility operation, transport overhead
6. **Profits accumulate** to faction capital
7. **AI factions execute** their monthly loop independently
8. **Tech research advances** (+10 RP/month global + player labs)
9. **Events trigger** (~20% chance monthly: demand shift, tech opportunity, crisis)
10. **Next month begins**

**UI essentials:**
- Map of locations with faction presence & facilities
- Market prices per good per location
- Player balance & facility status
- Tech tree & research progress
- Production queue (simple: queue next facility to build)

---

## Critical Decisions

**These must be locked before coding starts. They affect balance cascades.**

### Decision 1: Game Speed

| Option | Cadence | Feel | Impact |
|--------|---------|------|--------|
| **Weekly** | 52 turns/year | Fast; twitchy | Research slow; lots of turns to play |
| **Monthly** | 12 turns/year | Deliberate; strategic | ⭐ Recommended; matches pacing |
| **Quarterly** | 4 turns/year | Very slow; high-level | Economy feels glacial |

**Recommendation:** **Monthly turns.** Matches strategic play (not real-time), tech unlocks every 1–2 months (good pacing), playthrough of 5 years = 60 turns (reasonable).

---

### Decision 2: Facility Build Cost

| Option | Model | Early Game | Late Game | Complexity |
|--------|-------|-----------|-----------|-----------|
| **Fixed** | All facilities = 5,000 cr | Accessible; easy to plan | No scaling pressure | Simple ✓ |
| **Location-based** | Moon 4k, Mars 6k, Belt 8k | Moon easy, Belt risky | Adds depth | Medium |
| **Facility-based** | Mines 4k, Labs 8k | Encourages specialization | Rewards focus | Medium |

**Recommendation:** **Fixed at 5,000 credits (Phase 1).** Simplest model; easier to balance; Phase 2 can add location scaling if desired.

---

### Decision 3: Starting Capital & Difficulty

| Option | Player | AI | Result |
|--------|--------|-----|--------|
| **Conservative** | 50k | 30k each | Player slight edge; not too hard |
| **Balanced** | 50k | 50k each | Fair fight; hard mode |
| **Easy** | 75k | 30k each | Sandbox; relax & explore |

**Recommendation:** **Player 50k, AI 30k each.** Slight player advantage compensates for human vs. heuristic AI. Difficulty knob for Phase 2 if desired.

---

### Decision 4: Playthrough Duration

| Target | Years | Months | Notes |
|--------|-------|--------|-------|
| **Short** | 3–4 | 36–48 | Moon → Mars only; Belt unreachable |
| **Medium** | 5–7 | 60–84 | Moon → Mars → Belt becomes viable ⭐ Recommended |
| **Long** | 10+ | 120+ | Late-game grind; Phase 2 territory |

**Recommendation:** **5–7 in-game years.** MVP should be playable to Belt unlock (all locations accessible). Longer playthroughs → Phase 2.

---

### Decision 5: Materials & Recipes Lock

**Before coding:** Create a spreadsheet with exact inputs/outputs:
- Facility type → Recipe name → Inputs (with quantities) → Outputs (with quantities) → Cost
- Example: Iron mine → "Mine iron" → 0 inputs → 10 ore output → 100 cr cost

**Why?** Prevents mid-development changes that cascade into balance issues. 30 minutes of spreadsheet work = hours saved debugging.

---

## Technical Architecture

See **TECHNICAL_ARCHITECTURE.md** for full system design, data models, and package structure.

**Quick overview:**

```
sol_corp/
├── core/
│   ├── resource.py       # Resource & good types
│   ├── facility.py       # Facility, recipe, operation styles
│   ├── location.py       # Location, local markets
│   ├── faction.py        # Faction base class
│   ├── world.py          # World state manager
│   └── simulation.py     # Monthly tick, resolution
├── ai/
│   └── agent.py          # AI faction heuristics
├── earth/
│   └── earth_faction.py  # Earth demand & events
├── ui/
│   └── cli.py            # CLI interface
├── tests/
│   └── test_simulation.py
└── main.py               # Entry point
```

**Key dependencies:**
- `attrs` or `dataclasses` (type-safe models)
- `arcade` (Phase 2+; optional for Phase 1)
- Standard library (json, csv, random, logging)

---

## Risk & Mitigation

### High-Risk Items

| Risk | Impact | Likelihood | Mitigation |
|------|--------|-----------|-----------|
| **Recipe deadlocks** (circular dependencies block production) | Game becomes unplayable | Medium | Test early; avoid circular chains; flexible inputs (consumer goods accepts any intermediate) |
| **AI bankrupts** (spends capital unwisely, can't recover) | Game becomes one-sided | Medium | Add AI safety rules (min capital threshold); simplify heuristics |
| **Scope creep** (Phase 1 never ships) | Project stalls | High | Lock scope before Week 1; defer Phase 2+ ruthlessly; use burndown |

### Medium-Risk Items

| Risk | Impact | Likelihood | Mitigation |
|------|--------|-----------|-----------|
| **Tech progression too slow/fast** | Player bored or gates on single tech | Medium | Playtest monthly; tune RP generation early |
| **Python performance lag** (simulation slow by Phase 2) | Game unfun to play | Medium | Profile early; optimize hotspots; port to Rust if needed |
| **Prices tank** (economics broken) | Profit margins vanish; game boring | Low | Price floors; supply sanity checks; avoid race-to-zero |

### Low-Risk Items

| Risk | Impact | Likelihood | Mitigation |
|------|--------|-----------|-----------|
| **UI is clunky** (hard to control game from CLI) | Minor friction | Medium | Keep Phase 1 minimal; invest in GUI Phase 2 |
| **AI is trivial or overpowered** | Game not challenging | Medium | Difficulty knobs (AI capital, resource access, research speed) |

---

## Success Criteria

### Phase 1 is Done When

- [ ] Game runs start to finish without crashes
- [ ] Player can build facilities, watch production, sell goods, reinvest
- [ ] Can play from Year 1 through Year 2–3 with visible tech progression
- [ ] Prices make sense (scarcity → high, abundance → low)
- [ ] AI factions expand, compete, affect market prices
- [ ] Player can win (accumulate wealth) or lose (go broke)
- [ ] At least 2 tech unlocks visible in a playthrough
- [ ] No deadlocks, softlocks, or economic paradoxes
- [ ] Save/load works; game is resumable

### Balance Targets (Phase 1)

- Moon profitability: **10–30% margin** early game
- Tech unlock rate: **One tech every 10–15 turns** (1–2 months)
- Playthrough length: **60–84 turns** (5–7 years)
- AI competitiveness: Player can win if skillful; AI is not trivial

---

## Related Documents

This document is the **main reference**. For details, see:

- **[PHASE_BREAKDOWN.md](PHASE_BREAKDOWN.md)** — Detailed milestones, deliverables, task lists per phase
- **[TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md)** — System design, data models, package structure, dependency choices
- **[MATERIALS_RECIPES.md](MATERIALS_RECIPES.md)** — Production chain (facilities, recipes, tech tree, resource balance)
- **[AI_HEURISTICS.md](AI_HEURISTICS.md)** — Pseudocode for AI faction decision-making
- **[DECISIONS_CHECKLIST.md](DECISIONS_CHECKLIST.md)** — Pre-coding checklist; critical decisions, assumptions, questions for Dan

---

## Recommendations for Dan

### Before You Code

1. **Lock in decisions 1–5** (game speed, build cost, starting capital, duration, recipes)
2. **Create a materials spreadsheet** (30 minutes; prevents mid-dev chaos)
3. **Sketch AI pseudocode** (1–2 hours; know the decision loop)
4. **Setup Git repo** & project skeleton
5. **Read TECHNICAL_ARCHITECTURE.md** to confirm package structure works for you

### During Phase 1

1. **Playtest monthly** — Play your own game; feel if it's fun
2. **Instrument early** — Logging, telemetry; easy to spot broken economics
3. **Defer polish** — Art, sound, animations → Phase 2
4. **Keep a decision log** — Why you changed recipe costs; saves rework
5. **Test risky bits early:** Recipe chains (deadlock test), price mechanics (sanity test), AI loop (behavior test)

### If You Get Stuck

- **Scope too big?** Cut to 6 resources, 2 locations, 1 AI
- **Economics broken?** Simplify recipes (1 input, 1 output); add price floors; nerf AI
- **AI too smart/dumb?** Adjust heuristics or give AI handicap (lower capital, slower tech)
- **Python slow?** Profile first; usually it's UI, not simulation

---

## Next Steps (This Week)

- [ ] Review this plan; confirm scope & key decisions with Dan
- [ ] Lock materials & recipes in spreadsheet
- [ ] Sketch AI pseudocode
- [ ] Setup Git repo with Phase 1 branch
- [ ] Create project skeleton (package structure)
- [ ] Start Week 1 development: core data models + production logic

---

**Status: Ready to ship Phase 1. Let's build something fun.** 🚀

