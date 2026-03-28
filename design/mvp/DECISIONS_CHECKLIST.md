# Sol Corp Pre-Development Decisions Checklist

**Critical decisions Dan must make before Phase 1 coding starts. Each decision cascades into balance and design choices.**

---

## Table of Contents

1. [Quick Decisions](#quick-decisions)
2. [Design Decisions (Detailed)](#design-decisions-detailed)
3. [Assumptions to Validate](#assumptions-to-validate)
4. [Sign-Off](#sign-off)

---

## Quick Decisions

### Decision 1: Game Speed ⏰

**What:** How fast does time pass in-game?

**Options:**
```
A) Weekly turns (52 turns/year) — Twitchy, fast-paced
B) Monthly turns (12 turns/year) — Strategic, deliberate ✓ RECOMMENDED
C) Quarterly turns (4 turns/year) — Very slow, high-level
```

**Impact:**
- **Affects:** Tech unlock timing, facility payback time, playthrough length
- **Example:** If weekly, Moon iron mine takes 3 months real time to payback (36 weeks). If monthly, it's 3 months = 13 turns (faster feel).
- **Recommended:** Monthly. Matches strategic gameplay; techs unlock every 1–2 months (good pacing); 5-year playthrough = 60 turns (reasonable).

**Decision:** ☐ **Weekly** ☐ **Monthly** ☐ **Quarterly**

**Locked by Dan?** ☐ Yes ☐ No | **Date decided:** ___________

---

### Decision 2: Facility Build Cost 💰

**What:** How much does it cost to build a facility?

**Options:**
```
A) Fixed cost (all facilities = 5,000 cr) ✓ RECOMMENDED
B) Location-dependent (Moon 4k, Mars 6k, Belt 8k)
C) Facility-dependent (mines 4k, labs 8k)
D) Dynamic (costs rise as player builds more)
```

**Impact:**
- **Affects:** Early-game accessibility, capital requirements, expansion pace
- **Example:** Fixed 5k means player can afford 2nd facility by Month 2. Variable costs = unpredictable delays.
- **Recommended:** Fixed. Simpler to understand, balance, and code. Phase 2 can add location scaling if desired.

**Decision:** ☐ **Fixed (5k)** ☐ **Location-dependent** ☐ **Facility-dependent** ☐ **Dynamic**

**Locked by Dan?** ☐ Yes ☐ No | **Date decided:** ___________

---

### Decision 3: Starting Capital 🏦

**What:** How much capital does each faction start with?

**Options:**
```
A) Player 50k, AI 30k each ✓ RECOMMENDED
B) Player 50k, AI 50k each (fair fight)
C) Player 75k, AI 30k each (easy mode)
D) Player 30k, AI 30k each (hard mode)
```

**Impact:**
- **Affects:** Difficulty, early-game pace, competitiveness
- **Example:** Player 50k → can build 10 facilities before running out. AI 30k → builds 6 (catchable but not dominant).
- **Recommended:** 50k/30k. Slight player advantage (human > heuristic AI) without trivializing the game.

**Decision:** ☐ **50k/30k** ☐ **50k/50k** ☐ **75k/30k** ☐ **30k/30k**

**Locked by Dan?** ☐ Yes ☐ No | **Date decided:** ___________

---

### Decision 4: Playthrough Duration 🎯

**What:** How long should a complete MVP playthrough be?

**Options:**
```
A) Short (3–4 in-game years, 36–48 turns)
B) Medium (5–7 in-game years, 60–84 turns) ✓ RECOMMENDED
C) Long (10+ in-game years, 120+ turns)
```

**Impact:**
- **Affects:** Tech progression timing, location unlock schedule, late-game depth
- **Example:** 5–7 years = Belt becomes viable by year 5; player has time to settle Moon, expand Mars, then reach Belt. All 3 locations feel utilized.
- **Recommended:** 5–7 years. Shows all locations; enough time for economic cycling; not so long it feels grindy.

**Decision:** ☐ **Short (3–4y)** ☐ **Medium (5–7y)** ☐ **Long (10+y)**

**Locked by Dan?** ☐ Yes ☐ No | **Date decided:** ___________

---

### Decision 5: Difficulty Setting (Phase 1) 🎮

**What:** What difficulty does the game ship at?

**Options:**
```
A) Single difficulty (player 50k, AI 30k) ✓ RECOMMENDED FOR MVP
B) Multiple difficulties (Easy, Normal, Hard)
C) Custom difficulty (sliders for capital, AI speed, etc.)
```

**Impact:**
- **Affects:** Scope (single difficulty = simpler; multiple = more work), replayability
- **Recommended:** Single difficulty for Phase 1. Easier to balance one configuration. Phase 2 can add difficulty modes if desired.

**Decision:** ☐ **Single** ☐ **Multiple preset** ☐ **Custom sliders**

**Locked by Dan?** ☐ Yes ☐ No | **Date decided:** ___________

---

## Design Decisions (Detailed)

### Decision 6: Win Condition / Endgame

**What:** Does the game have a goal, or is it a sandbox?

**Options:**

```
A) Pure sandbox (no goal; player defines own objectives)
   - Example: "Get 1M credits" or "Build on all 3 locations"
   - Pros: Open-ended, high replay value
   - Cons: No narrative closure
   ✓ RECOMMENDED FOR MVP

B) Soft targets (suggestions, not enforced)
   - Example: "First to 1M credits wins" (displayed, not mandatory)
   - Pros: Guides new players; still open-ended
   - Cons: Slightly more design work

C) Hard win condition (game ends when achieved)
   - Example: "Reach 1M credits = WIN SCREEN"
   - Pros: Clear goal; satisfying closure
   - Cons: Limits replayability; needs balance tuning
```

**Recommendation:** Pure sandbox. MVP should focus on fun loop, not winning. Phase 2 can add soft targets (e.g., achievements) if desired.

**Decision:** ☐ **Pure sandbox** ☐ **Soft targets** ☐ **Hard win**

**Locked by Dan?** ☐ Yes ☐ No | **Date decided:** ___________

---

### Decision 7: Earth Faction Demand Model

**What:** How do the 4 Earth factions demand goods?

**Options:**

```
A) Simple (fixed base demand + monthly random events) ✓ RECOMMENDED
   - Example: USA always wants 30 consumer goods/month
   - Events: 20% chance of boom (+50% demand) or crisis (-30% demand)
   - Pros: Simple to code; easy to balance
   - Cons: Predictable; less economic depth

B) Economic cycles (demand follows predictable waves)
   - Example: Boom years, recession years on a 4-year cycle
   - Pros: Realistic economic rhythms
   - Cons: More complex; harder to balance

C) Tech-driven (demand responds to tech unlocks)
   - Example: Research materials surge after tech unlocks
   - Pros: Tech feels impactful
   - Cons: Complex dependencies; harder to debug
```

**Recommendation:** Simple for MVP. It's sufficient to create market volatility. Phase 2 can add cycles if desired.

**Decision:** ☐ **Simple** ☐ **Economic cycles** ☐ **Tech-driven**

**Locked by Dan?** ☐ Yes ☐ No | **Date decided:** ___________

---

### Decision 8: Facility Storage / Queuing

**What:** Can player queue facility builds, or one at a time?

**Options:**

```
A) One at a time (can only build one facility per month)
   ✓ RECOMMENDED FOR MVP
   - Pros: Simple; less UI complexity; player micromanages
   - Cons: Can feel restrictive

B) Build queue (queue multiple facilities; they build in sequence)
   - Pros: Less micromanagement; modern feel
   - Cons: More complex UI; requires queue management

C) Parallel building (can build multiple simultaneously; cap on quantity)
   - Pros: Fast-paced; reduces tedium
   - Cons: Significantly more complex; affects balance
```

**Recommendation:** One at a time for MVP. Simpler to code and understand. Phase 2 can add queuing.

**Decision:** ☐ **One at a time** ☐ **Build queue** ☐ **Parallel**

**Locked by Dan?** ☐ Yes ☐ No | **Date decided:** ___________

---

### Decision 9: Save / Load / Undo

**What:** Can player undo decisions, or are they permanent?

**Options:**

```
A) No undo; decisions permanent ✓ RECOMMENDED
   - Pros: Decisions have weight; encourages careful play
   - Cons: Mistakes feel irreversible; frustrating if unbalanced

B) Undo (last N turns can be undone)
   - Pros: Forgiving; fun for experimentation
   - Cons: Reduces tension; feels "safe"

C) Save/load anytime
   - Pros: Player agency; can retry
   - Cons: Removes tension; easy to abuse (quicksave before risky moves)
```

**Recommendation:** No undo; frequent autosave. Game saves monthly; player can reload if it crashes, but can't undo past decisions. Keeps decisions meaningful.

**Decision:** ☐ **No undo** ☐ **Undo last N turns** ☐ **Save/load anytime**

**Locked by Dan?** ☐ Yes ☐ No | **Date decided:** ___________

---

### Decision 10: AI Faction Type Specialization

**What:** Do the 2 AI factions play differently, or identically?

**Options:**

```
A) Identical heuristics (both use same decision-making) ✓ RECOMMENDED FOR MVP
   - Pros: Simpler to code; easier to balance; both competitive
   - Cons: Less personality; less variety

B) Different strategies (one focuses on mining, one on research)
   - Pros: Variety; different playstyles to counter
   - Cons: More complex heuristics; harder to balance independently

C) Different personalities (aggressive vs. conservative)
   - Pros: Flavor; replayability
   - Cons: Adds complexity
```

**Recommendation:** Identical for MVP. Phase 3 adds 4 differentiated AI types. For Phase 1, focus on one solid heuristic that works well.

**Decision:** ☐ **Identical** ☐ **Different strategies** ☐ **Different personalities**

**Locked by Dan?** ☐ Yes ☐ No | **Date decided:** ___________

---

## Assumptions to Validate

### Assumption 1: 3 Locations is Enough for MVP

**Assumption:** Moon + Mars + Belt is sufficient for 5-7 year playthrough without feeling empty.

**How to test:** 
- Play Phase 1 to completion (Year 3+)
- Ask: Do I reach Belt? Does all 3 feel utilized?
- If Belt feels unreachable: Add 4th location (Venus)
- If 3 feel crowded: Cut to 2 for MVP

**Validation date:** End of Phase 1 playtest | **Result:** ☐ Confirmed ☐ Adjust

---

### Assumption 2: 8 Resources is Buildable Solo

**Assumption:** 8 resources (3 raw, 3 intermediate, 2 finished) won't cause scope explosion or complex deadlocks.

**How to test:**
- Implement all 8 resources and recipes
- Run integration test: 2 AI + player for 36 months
- Ask: Any deadlocks? Are all resources valuable?
- If deadlocks: Reduce to 6 resources; defer some to Phase 2
- If imbalanced: Adjust prices/production rates

**Validation date:** End of Week 2 | **Result:** ☐ Confirmed ☐ Adjust

---

### Assumption 3: Heuristic AI is Competitive

**Assumption:** Simple rule-based AI (no ML, no planning) is fun to compete against and creates meaningful challenge.

**How to test:**
- Play 2 games against 2 AI factions
- Ask: Can I win if I play skillfully? Is it too easy/hard?
- If too easy: Increase AI capital, reduce expansion costs
- If too hard: Decrease AI capital, give player tech advantage

**Validation date:** End of Phase 1 | **Result:** ☐ Confirmed ☐ Adjust

---

### Assumption 4: Economic Competition Alone is Fun

**Assumption:** Without military conflict or diplomacy, pure economic competition (prices, markets, expansion) is engaging enough for MVP.

**How to test:**
- Play Phase 1 end-to-end
- Ask: Am I bored without combat? Does competition feel tense?
- If bored: Phase 2 should add military/diplomacy sooner
- If engaged: Validate that economics is the core fun loop

**Validation date:** End of Phase 1 | **Result:** ☐ Confirmed ☐ Adjust**

---

### Assumption 5: Monthly Turns are the Right Cadence

**Assumption:** One in-game month per turn is the right speed (not weekly, not quarterly).

**How to test:**
- Play Phase 1 with monthly turns
- Ask: Does tech unlock feel paced right? Is progression too slow/fast?
- If too slow: Switch to weekly (faster progression)
- If too fast: Switch to quarterly (slower, more deliberate)

**Validation date:** End of Week 1 | **Result:** ☐ Confirmed ☐ Adjust

---

## Sign-Off

### For Dan

**Before you start coding, confirm all decisions above:**

```
☐ Decision 1 (Game Speed): LOCKED
☐ Decision 2 (Build Cost): LOCKED
☐ Decision 3 (Starting Capital): LOCKED
☐ Decision 4 (Playthrough Duration): LOCKED
☐ Decision 5 (Difficulty): LOCKED
☐ Decision 6 (Win Condition): LOCKED
☐ Decision 7 (Earth Demand): LOCKED
☐ Decision 8 (Facility Queuing): LOCKED
☐ Decision 9 (Save/Undo): LOCKED
☐ Decision 10 (AI Specialization): LOCKED

All assumptions marked for validation: ☐ Yes
```

**Sign off:**

Name: _________________________ | **Date:** ___________

---

## Template: Decision Log (During Development)

**Keep this updated as you build. When you change a decision, record why.**

```
Date: YYYY-MM-DD
Decision: [Name]
Original: [What it was]
Changed to: [What it is now]
Why: [Reason; what broke or wasn't working]
Impact: [What else changed as a result]
Notes: [Any side effects or future implications]
```

**Example:**
```
Date: 2026-04-10
Decision: Starting Capital
Original: Player 50k, AI 30k
Changed to: Player 50k, AI 20k
Why: AI was winning too consistently; player couldn't keep up
Impact: Adjusted playthrough difficulty to easy; Phase 2 can re-tune
Notes: If difficulty is still off, add difficulty slider in Phase 2
```

---

## What If Changes Happen?

**If you discover mid-development that a locked decision was wrong:**

1. **Document the discovery:** What went wrong? Why?
2. **Evaluate the fix:** Can you adjust balance instead? Or must you change the decision?
3. **Decide:** Change decision? Or adjust balance?
4. **Record it:** Update decision log; inform Dan of change.
5. **Communicate impact:** What else changes if this decision changes?

**Example:**
```
DISCOVERY: 3 locations feels empty; players reach Belt by Month 6
OPTIONS:
  A) Add 4th location (Venus) — major change
  B) Increase distance penalty for Belt (50% → 70%) — balance tweak
  C) Delay Mars/Belt tech unlock — balance tweak

DECISION: Try option B first (balance tweak); validate with playtest
IMPACT: Belt becomes much riskier; playthrough might need 7–10 years instead of 5–7
NEXT STEP: Playtest; if still feels hollow, add 4th location
```

---

## Next Steps

1. **Print this checklist**
2. **Go through each decision with Dan** (quick 30-min call or email)
3. **Lock all decisions** (check all boxes)
4. **Create materials spreadsheet** (30 minutes; lock down all recipes)
5. **Sketch AI pseudocode** (1–2 hours; know the heuristic loop)
6. **Start coding Week 1** with full confidence in decisions

---

**Ready? Decision checklist complete = green light to code.** 🚀

