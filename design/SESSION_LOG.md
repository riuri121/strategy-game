# Sol Corp — Design Session Log

## Session 1 — 2026-02-28 19:32–19:40 UTC
**Attendee:** Dan, Sable
**Purpose:** Initial concept planning & GDD kickoff

### Decisions Made
1. **Game Concept:** Corporations industrializing the solar system; single-player sandbox with Victoria 3–inspired economics
2. **Win Conditions:** None hard; player-defined (richest, self-contained colony, Earth conquest, etc.)
3. **Time Model:** Pauseable real-time preferred; turn-based acceptable for simplicity
4. **Scope Model:** Iterative expansion starting with Moon, Mars, asteroid belt
5. **Faction Types:**
   - **Earth factions** (2–4): Compete with each other, not the player; drive market demand
   - **Space factions** (2): Compete with the player for resources/locations; may interact diplomatically or militarily
6. **Player Start:** TBD (capital + foothold vs. nothing)
7. **Economic Model:** TBD (fixed prices vs. dynamic; how does space economy affect Earth market?)

### Open Questions
- [ ] How granular are locations? (Planet-wide regions vs. specific sites vs. abstract nodes?)
- [ ] Can space factions block you from building? Or purely economic competition?
- [ ] Supply logistics: Simulated (travel time) or abstract (instant)?
- [ ] Can you trade with space factions or only compete?
- [ ] Military mechanics: Direct combat, economic warfare, both, or deferred to Phase 2?
- [ ] Tech progression: When does it unlock new locations/mechanics?
- [ ] Difficulty modes: Dynamic AI, resource scarcity, sandbox presets?

### Session 1 Continued — 19:42 UTC

#### Decisions Made (Earth Focus)
1. **Faction Model:** 3–4 Earth factions, each with sector focus (industrial, tech, agriculture, etc.)
2. **Earth Role:** Market hub only; factions generate demand, set prices, create economic dynamics
3. **Trade Flow:** Player exports goods to Earth, receives credits; factions compete for same goods
4. **Price Model:** Scarcity + demand × faction preference; factions can negotiate or shop around
5. **Faction Relationships:** Alliances, conflicts, and trade dynamics affect available demand

#### Earth Decisions (Locked In)
1. **Factions:** USA, Europe, China, India (pure demand sinks; no internal production)
2. **Demand driver:** Random events (economic boom, conflict, instability, tech breakthrough)
3. **Demand categories:** Raw materials, intermediates, consumer goods, research materials, military goods
4. **Bootstrap mechanic:** Early-game fixed-price Earth exports (construction materials); becomes uneconomical mid-game as space production scales
5. **System constraint:** All four factions remain in play forever (none can be destroyed)

#### Space Faction Decisions (Locked In)
1. **MVP:** Space factions are identical AI corporations (like the player)
2. **Number:** Game-start setting (undefined for now)
3. **Competition:** They compete for same locations/resources; no direct trade with player
4. **Future differentiation:** Starting conditions, Earth alignment, passive abilities

#### Production & Locations Decisions (Locked In)
1. **Locations:** Each location is its own market; distance malus applies both ways (import/export)
2. **Demand categories:** War, consumption, development, research (all Earth factions buy all four; events shift ratios)
3. **Facilities:** One facility type per resource
4. **Recipes:** Tech-unlocked; tied to facilities; can vary per facility to optimize locally
5. **Operation styles:** Basic, skeleton, fully manned (affects speed/cost)
6. **Faction bonuses:** Passive abilities (mining, logistics, tech, diplomacy) apply to facilities

#### Tech Stack Decision (Locked In)
1. **Language:** Python (initial) + Rust (performance core, later)
2. **Framework:** Arcade (UI/presentation layer)
3. **Architecture:** Simulation core as separate library; clear API boundaries between simulation and presentation
4. **Development model:** Solo with Sable as AI collaborator
5. **Learning focus:** Systems programming + game architecture

### Next Steps
1. Define **raw materials list** (5–8 types)
2. Define **intermediates list** (TBD count)
3. Define **recipes per facility type** (inputs, ratios, outputs)
4. Sketch **Tech tree** structure
5. Begin **architecture/API design** document (simulation core structure)
6. Sketch initial **project structure** (Python modules, Rust crate layout)

### Notes
- Dan is interested in using sub-agents for this project; testing agent workflow
- This is a living document—expect frequent iteration
- Focus on economic depth and emergent gameplay over graphics/scope
