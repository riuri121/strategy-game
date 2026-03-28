# Sol Corp Phase Breakdown

**Detailed milestones, deliverables, and task lists for each development phase.**

---

## Table of Contents

1. [Phase 1: MVP (Core Loop)](#phase-1-mvp-core-loop)
2. [Phase 2: Economic Depth](#phase-2-economic-depth)
3. [Phase 3: Expansion & Scale](#phase-3-expansion--scale)
4. [Risk Timeline](#risk-timeline)

---

## Phase 1: MVP (Core Loop)

### Overview

**Goal:** Playable economic sandbox with tight feedback loop  
**Duration:** 4–6 weeks (solo dev)  
**Success:** Player can play Year 1 → Year 3+ with visible tech progression and meaningful choices

### Phase 1 Scope

| Aspect | Target | Notes |
|--------|--------|-------|
| Locations | 3 (Moon, Mars, Belt) | All accessible by year 3 |
| Resources | 8 (3 raw, 3 intermediate, 2 finished) | Testable; buildable |
| Facilities | 6 types | Mines, factories, lab |
| Technologies | 6 core techs | One unlock every 1–2 months |
| AI Factions | 2 identical heuristic agents | Compete for profit |
| Earth Factions | 4 (USA, Europe, China, India) | Demand drivers only |
| Interface | CLI/text-based | Functional over beautiful |
| Code | ~3,000 lines Python | Includes tests, structure |
| Approx. LOC Distribution | 1500 core simulation + 800 CLI + 700 tests | Rough; may vary |

### Week-by-Week Milestones

#### Week 1: Core Data Models & Production Logic

**Goal:** Build the foundation; data structures are solid and testable.

**Deliverables:**
- `core/resource.py` — Resource types, goods, categories
- `core/facility.py` — Facility class, recipes, operation styles
- `core/location.py` — Location model, local markets
- `core/faction.py` — Faction base class, capital tracking
- Production logic (mine → refine → sell)
- Unit tests for production (input validation, output calculations)

**Tasks:**
```
Day 1–2: Design & implement Resource, Goods classes
  - Resource enum (Iron, Rare Earth, Silicon, etc.)
  - Goods enum (tiers: Raw, Intermediate, Finished)
  - Properties (base price, density, transport cost)

Day 3–4: Facility, Recipe classes
  - Facility type enum (Mine, Refinery, Factory, Lab, etc.)
  - Recipe: inputs (dict of good → qty) → outputs (dict → qty)
  - Operation styles (Basic, Skeleton, FullyManned; speed/cost multipliers)
  - Facility state tracking (current recipe, operation style, input buffer)

Day 5: Location & local market
  - Location enum (Moon, Mars, Belt)
  - Local inventory (supplies available for production)
  - Local market prices (initially, just pass-through to Earth)

Day 6–7: Faction base class
  - Capital tracking (starts with specified amount)
  - Facility roster (what facilities does faction own, where)
  - Production loop stub (will expand Week 2)
  - Unit tests: Can build facility? Can run recipe? Do outputs appear in inventory?
```

**Acceptance criteria:**
- [ ] Can create a resource, good, facility, location
- [ ] Can define a recipe (inputs → outputs)
- [ ] Can run a recipe; inputs consumed, outputs produced
- [ ] No negative inventory; production fails if inputs insufficient
- [ ] Unit tests pass (≥80% core code coverage)

---

#### Week 2: Economic Resolution & Market System

**Goal:** Prices, costs, profits — make economics tangible.

**Deliverables:**
- `core/world.py` — Global game state manager
- `core/simulation.py` — Monthly tick, price resolution
- Earth market pricing system
- Distance penalties applied correctly
- Full economic calculation (cost → profit)

**Tasks:**
```
Day 1–2: Earth faction demand
  - Earth class with base demand (units/month per good)
  - Demand multiplier for events (boom, crisis)
  - Demand allocation per Earth faction (USA 30% consumer, etc.)

Day 3–4: Market pricing
  - Base prices per good (iron 50 cr, consumer goods 150 cr, etc.)
  - Price formula: price = base × demand_multiplier × scarcity_multiplier
  - Distance penalty (Moon 10%, Mars 20%, Belt 50%)
  - Price floors (never negative; never below production cost)

Day 5: Cost calculation
  - Facility operation cost (fixed + variable overhead)
  - Input acquisition cost (pull from local market at local price)
  - Transport cost (embedded in distance penalty)
  - Profit = sell_price - production_cost

Day 6–7: Monthly simulation tick
  - World state manager (holds all factions, locations, facilities)
  - Tick function: resolve production for all facilities → resolve sales → apply profits
  - Logging (verbose output for debugging prices, flows)
  - Unit tests: Profit calculation correct? Prices move with demand?
```

**Acceptance criteria:**
- [ ] Can set Earth faction demand; prices adjust
- [ ] Distance penalties applied correctly
- [ ] Facility costs subtracted from profits
- [ ] Prices never go negative
- [ ] Can run monthly tick without crashes
- [ ] Monthly logging shows where money goes (clear to debug)

---

#### Week 3: AI Faction Loop & Simulation

**Goal:** AI factions behave, compete, make prices move.

**Deliverables:**
- `ai/agent.py` — AI decision-making heuristics
- AI monthly loop (assess → expand → produce → trade → reinvest)
- Deterministic, debuggable AI (no ML, no randomness except for probabilities)
- Integration test: 2 AI + player all simulating together

**Tasks:**
```
Day 1–3: AI decision heuristics
  - Assess: Calculate profit margins, identify expansion opportunities
    if current_capital > 10k and underutilized_location exists:
      expand to that location
  - Expand: Build facility at profitable location (heuristic: mine at untapped region)
    build_cost = 5000
    if available_capital > build_cost:
      build most profitable facility type
  - Produce: Run facilities (auto-switch operation style based on cash flow)
    if cash_flow > 0: use FullyManned
    else: use Basic
  - Trade: Sell goods to Earth (automatic; same as player)
  - Reinvest: Use profits to expand (recursive; loop repeats)

Day 4–5: AI integration
  - AI factions start with initial capital (30k each)
  - AI start on Moon with 1 mine each
  - AI run monthly loop independently
  - AI don't interact directly (no trade between factions; only price competition)

Day 6–7: Testing
  - Simulation test: 2 AI + player all active for 12 turns; no crashes
  - Check: Do AI expand? Do they undercut prices? Do they lose/win?
  - Debug output: Show AI decisions each turn (for visibility)
```

**Acceptance criteria:**
- [ ] AI expands to new locations
- [ ] AI competes on price (drives prices down as supply increases)
- [ ] AI doesn't go bankrupt in first 12 turns
- [ ] Player can see AI actions (easy to debug)
- [ ] Simulation runs 12 turns without errors

---

#### Week 4: CLI UI & Player Control

**Goal:** Player can build, operate, buy, sell via text interface.

**Deliverables:**
- `ui/cli.py` — Command-line interface
- Player commands: view map, view prices, build facility, switch recipe, operate, pause
- Simple menu loop (interactive or command-based)
- Save/load game state (JSON)

**Tasks:**
```
Day 1–2: CLI structure
  - Main menu loop (show game state, prompt for command)
  - Commands:
    - `status` → show player capital, facility list
    - `map` → show locations, facilities per location, factions present
    - `prices` → show current market prices per location
    - `techs` → show research progress, unlocked techs
    - `build <location> <facility_type>` → build facility at location
    - `recipe <facility_id> <recipe_name>` → switch recipe
    - `operate <facility_id> <style>` → set operation style
    - `next` → advance one month (run simulation tick)
    - `save <filename>` → save game state
    - `load <filename>` → load game state
    - `help` → show command list

Day 3–4: Display logic
  - Format tables (prices, facilities, locations, tech progress)
  - Colorize output if terminal supports it (optional; nice to have)
  - Show monthly summary: revenue, expenses, net profit, new techs

Day 5–6: Save/load
  - Serialize world state to JSON (faction capital, facilities, location inventory, tech progress)
  - Load from JSON (deserialize, restore state)
  - Test: Save, quit, load; game continues as expected

Day 7: Polish & integration
  - User feedback loop (does CLI feel responsive?)
  - Error handling (invalid commands, impossible actions)
  - Playtest: Can new user figure out how to play? (adjust help text if needed)
```

**Acceptance criteria:**
- [ ] Can build facility via CLI
- [ ] Can switch recipe and operation style
- [ ] Can see current prices, capital, facilities
- [ ] Can advance month (simulation tick visible)
- [ ] Can save and load game
- [ ] No crashes on invalid input

---

#### Week 5: Testing, Balance & AI Tuning

**Goal:** Game is playable, fun, and ready for larger playtest.

**Deliverables:**
- Comprehensive test suite (production, markets, AI, save/load)
- Balance pass: prices, costs, tech unlock timing
- AI behavior review: Does it win/lose convincingly?

**Tasks:**
```
Day 1–2: Test suite
  - Unit tests: Resource, Facility, Location, Faction, Market
  - Integration test: Full simulation (player + 2 AI, 36 turns)
  - Edge cases: Bankrupt faction, zero inventory, recipe failures
  - Target: ≥80% code coverage

Day 3–4: Balance tuning (playtest-driven)
  - Play 2–3 games from start to Year 2
  - Q: Is Moon profitable early? (target: 10–30% margin)
  - Q: Do prices make sense? (does scarcity drive prices up?)
  - Q: Is expansion paced right? (when does Mars become viable?)
  - Adjust: base prices, facility costs, RP generation
  - Record decisions in a balance log (for Phase 2 reference)

Day 5–6: AI behavior review
  - Watch AI in detail: Does it expand wisely? Does it bankrupt?
  - Adjust heuristics if needed (e.g., increase capital threshold to avoid bankruptcy)
  - Check: Can player beat 2 AI? (should be possible but challenging)
  - Record AI behavior observations

Day 7: End-to-end playtest
  - Play one full game Moon → Mars → Belt (if reachable in time)
  - Record: Any deadlocks? Boring stretches? Over-powered AI?
  - Document findings for Phase 2
```

**Acceptance criteria:**
- [ ] ≥80% test coverage; no failing tests
- [ ] At least 2 full playthroughs without crashes
- [ ] Moon is profitable early game; Mars viable by Year 2; Belt accessible by Year 3+
- [ ] AI expands, competes, and feels like opponent
- [ ] No deadlocks, softlocks, or price paradoxes

---

#### Week 6: Documentation & Polish

**Goal:** Phase 1 is done, documented, and ready for Phase 2 planning.

**Deliverables:**
- Code documentation (docstrings, comments on complex logic)
- README with setup/play instructions
- Design decisions log (what changed, why)
- Phase 1 playtest report (what worked, what to improve)

**Tasks:**
```
Day 1–2: Code documentation
  - Docstrings: All classes, key methods
  - Comments: Complex calculations (price resolution, profit, etc.)
  - Type hints: Ensure all function signatures are annotated
  - README: How to run, how to play, example commands

Day 3–4: Design log
  - Document decisions made during dev (recipe costs, AI heuristics, etc.)
  - Record assumptions that proved true/false
  - Note: "We thought X, but found Y; for Phase 2 consider Z"

Day 5–6: Playtest report
  - Summary: Is Phase 1 fun? Is it playable?
  - Balance observations (which techs felt too slow/fast?)
  - AI observations (too weak? too strong?)
  - Blockers for Phase 2 (e.g., "if GUI is too slow, do Rust early")

Day 7: Final polish
  - Code cleanup (linting, formatting)
  - Git commit (clean history; good messages)
  - Tag: Phase 1 complete
  - Prepare for Phase 2 kickoff
```

**Acceptance criteria:**
- [ ] Code is documented and linted
- [ ] README explains how to play
- [ ] Playtest report is written
- [ ] No uncommitted changes; Phase 1 branch is clean

---

### Phase 1 Success Metrics

**Playable:** 
- Player can start game and play to Year 2+ without crashes

**Fun:**
- Economic loop (mine → sell → reinvest) feels rewarding
- Competition with AI creates tension
- Player has real choices (where to expand, what to build)

**Balanced:**
- Moon is profitable (10–30% margin early)
- Mars becomes viable by Year 2
- Belt is reachable (though difficult) by Year 3+
- Tech progression feels paced (one unlock every 1–2 months)
- AI is competitive but not overpowered

**Technical:**
- ≥80% test coverage
- Codebase is clean, documented, extensible
- Save/load works
- No major performance issues (monthly tick < 100ms)

---

## Phase 2: Economic Depth

### Overview

**Goal:** Deepen complexity; improve UI; expand tech tree  
**Duration:** 3–4 weeks (iterative; builds on Phase 1)  
**Depends on:** Phase 1 playable and balanced

### Phase 2 Scope

| Aspect | Addition | Why |
|--------|----------|-----|
| Resources | 8 → 15 (add 7 new) | More production chains, specialization |
| Facilities | 6 → 10 types | Upgrade facilities, storage, logistics |
| Technologies | 6 → 12–15 techs | Branching paths; specialization options |
| Recipes | Simple → Complex | Multiple input combos; trade-offs |
| Facility Upgrades | New mechanic | Efficiency gains over time; long-term investment |
| Military Goods | New resource class | Adds conflict element (light blockades) |
| Trade Routes | New mechanic | Inter-location trade; blockade targets |
| GUI | Text → Arcade 2D | Lightweight visual interface |
| AI Factions | Still 2; same heuristics | Focus on depth, not new AI types |

### Phase 2 Task List (High Level)

1. **Expand resources & recipes** (1 week)
   - Design 7 new resources (advanced metals, military goods, specialized components)
   - Design complex recipes (multi-input, multi-output)
   - Ensure no deadlocks; test recipe chains

2. **Add facility upgrades** (1 week)
   - Facility can be upgraded (cost, time, benefit)
   - Upgrades improve efficiency (faster production, lower costs)
   - AI considers upgrades in expansion heuristics

3. **Expand tech tree** (1 week)
   - 12–15 techs total (3–4 new branches)
   - Branching paths (specialize in mining vs. manufacturing vs. research)
   - Adjust POC system if complexity demands

4. **Light military mechanics** (1 week)
   - Military goods resource
   - Blockade mechanic: AI can block trade routes (reduces access to distant locations)
   - Combat: Light version (no full combat; just trade disruption)

5. **Arcade GUI** (1–2 weeks)
   - Simple 2D map view (locations, factions, facilities)
   - Price chart (historical prices per good)
   - Facility control panel (build, operate, recipe)
   - Tech tree visualization
   - Resource: ~1500 lines Arcade code

6. **Balance pass** (ongoing)
   - Playtest weekly
   - Tune prices, costs, tech progression based on play
   - Record balance decisions

### Phase 2 Success Criteria

- [ ] 15 resources, 12–15 techs; no deadlocks
- [ ] Facility upgrades work; AI considers upgrades
- [ ] Light blockade mechanic adds tension without overwhelming
- [ ] Arcade GUI is intuitive; faster than CLI
- [ ] Full playthrough (Year 1–5) is feasible and fun
- [ ] ≥80% test coverage (new code)

---

## Phase 3: Expansion & Scale

### Overview

**Goal:** More locations, differentiated AI, performance optimization  
**Duration:** 4–6 weeks (iterative; builds on Phase 2)  
**Depends on:** Phase 2 complete and balanced

### Phase 3 Scope

| Aspect | Addition | Why |
|--------|----------|-----|
| Locations | 3 → 6–8 (add Venus, Mercury, gas giant moons) | More variety, strategic specialization |
| AI Factions | 2 identical → 4 types | Differentiated strategies (miner, tech, diplomat, logistics) |
| Core Engine | Python → Rust (optional) | Performance if Python slow; full Python OK if fast enough |
| GUI | Arcade 2D → Arcade with sprites/animations | More polished, engaging visuals |
| Supply Chain | Basic → Advanced | Storage limits, logistics failures, supply disruptions |

### Phase 3 Task List (High Level)

1. **Add locations** (1 week)
   - 3 new locations (Venus, Mercury, Io, Europa, Titan, etc.)
   - Each with unique resource distribution
   - Adjust distance penalties for new locations
   - Ensure progression (early → mid → late game)

2. **Differentiated AI types** (1–2 weeks)
   - Miner AI: Focuses on raw material extraction, prioritizes volume
   - Tech Pioneer AI: Invests heavily in research, early adopter of new techs
   - Logistics AI: Specializes in trade, moves goods between locations
   - Diplomat AI: Negotiates, forms alliances (Phase 4 feature; stub in Phase 3)
   - Each type has ~100–150 lines of conditional heuristics

3. **Performance optimization** (1 week)
   - Profile Python simulation; identify hotspots
   - If needed, port core simulation to Rust
   - Rust layer: Production resolution, price calculation (~1000–1500 lines)
   - Python wrapper: Calls Rust, manages UI/AI

4. **Advanced supply chain** (1 week)
   - Storage limits (facilities can hold max N units of inventory)
   - Logistics failures (chance of supply disruption; trade route blocked)
   - Supplier competition (factions bid for same resources; highest bidder gets priority)

5. **Enhanced GUI** (1.5–2 weeks)
   - Sprites for locations (planets, asteroids, facilities)
   - Animation (ships carrying goods, mining, construction)
   - Real-time price chart (update live)
   - Faction profiles (AI type, strategy, stats)
   - ~2000–3000 lines Arcade code

6. **Balance & polish** (ongoing)
   - Playtest 2–3 full games
   - Tune for late-game pacing
   - Ensure new locations feel distinct

### Phase 3 Success Criteria

- [ ] 6–8 locations, all playable and distinct
- [ ] 4 differentiated AI types; each behaves uniquely
- [ ] Performance: Monthly tick < 100ms (even with 8 locations)
- [ ] Supply chain mechanics add depth without overwhelming
- [ ] Arcade GUI is polished and responsive
- [ ] ≥80% test coverage
- [ ] Full playthrough Year 1–10+ is feasible

---

## Risk Timeline

### Phase 1 Blockers (Weeks 1–6)

| Week | Risk | Mitigation |
|------|------|-----------|
| 1 | Data models too complex | Simplify; defer advanced features |
| 2 | Market pricing broken (paradox) | Add price floors; test early |
| 3 | AI heuristics don't work (infinite loop, bankruptcy) | Simplify AI rules; add safety checks |
| 4 | CLI UI takes too long | Use simple text-based menu; GUI Phase 2 |
| 5 | Balance way off (Moon unprofitable, etc.) | Adjust base prices; playtest weekly |
| 6 | Scope creep (Phase 1 never ships) | Cut features ruthlessly; defer to Phase 2 |

### Phase 2 Blockers (Weeks 7–10)

| Week | Risk | Mitigation |
|------|------|-----------|
| 7–8 | Complex recipes deadlock | Limit recipe complexity; test chains early |
| 8–9 | Arcade GUI slow or hard to build | Keep GUI minimal; focus on function over graphics |
| 9 | New techs unbalanced (some useless, some overpowered) | Playtest weekly; tune costs/benefits |
| 10 | Blockade mechanic too harsh (game unplayable) | Add escape hatch (alternative routes); make optional |

### Phase 3 Blockers (Weeks 11–17)

| Week | Risk | Mitigation |
|------|------|-----------|
| 11–12 | Python too slow → Rust port needed | Profile early; consider Rust from Phase 2 if needed |
| 13 | Too many locations; game scale explodes | Reduce to 5–6; keep manageable |
| 14 | 4 AI types all broken; different bugs each | Test each AI type in isolation first |
| 15 | Storage limits create artificial scarcity (unplayable) | Tune storage caps; allow some overflow |
| 16 | GUI bloat; hard to navigate | Keep UI simple; prioritize key info |
| 17 | Balance shattered by new locations/AI | Full balance pass; adjust prices, costs, techs |

---

## Timeline Summary

```
Phase 1 (MVP):     Weeks 1–6   (4–6 weeks of dev)
  ↓
Phase 2 (Depth):   Weeks 7–10  (3–4 weeks iterative)
  ↓
Phase 3 (Scale):   Weeks 11–17 (4–6 weeks iterative)
  ↓
Post-Phase 3:      Multiplayer, Advanced AI, Complex Diplomacy, Platform Expansion
```

**Total estimated time:** 11–17 weeks solo dev to full Phase 3.

---

## Notes for Dan

- **Playtest early, playtest often.** Monthly playtests in Phase 1 catch issues before they compound.
- **Balance is iterative, not predictive.** Accept that initial balance will be off; use playtest data to adjust.
- **Scope discipline is critical.** Each phase has a clear goal; defer tempting features.
- **Document decisions.** Why did you change facility costs? Knowing "why" makes Phase 2 easier.
- **Use burndown.** Track planned tasks vs. completed; adjust scope if falling behind.

---

**Next:** For detailed technical specs, see [TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md).

