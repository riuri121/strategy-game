# Sol Corp MVP Documentation Suite

**Complete, production-ready documentation for the Sol Corp economic sandbox game.**

**Status:** Ready for development  
**Version:** Phase 1 MVP  
**Last Updated:** 2026-03-28  

---

## Overview

This documentation package contains everything needed to build, understand, and develop Sol Corp from MVP through Phase 3.

**Key principle:** Clarity over perfection. Every document is written for a developer building the game, with concrete examples and actionable guidance.

---

## Document Guide

### 📋 Start Here: [MVP_PLAN.md](MVP_PLAN.md)

**The main reference.** Read this first.

- What is Sol Corp? (executive summary)
- Why these 3 phases? (philosophy & scope)
- Core systems overview (economy, production, tech, AI)
- Critical decisions needed (game speed, starting capital, etc.)
- Success criteria (what "done" looks like)

**Time to read:** 15–20 minutes  
**When to read:** Before any coding; before design decisions

---

### 🗓️ Phase Roadmap: [PHASE_BREAKDOWN.md](PHASE_BREAKDOWN.md)

**Detailed week-by-week breakdown of all 3 phases.**

- Phase 1 (MVP): Week-by-week milestones, deliverables, task lists
- Phase 2 (Economic Depth): Scope additions, effort estimates
- Phase 3 (Expansion & Scale): New locations, AI types, performance
- Risk timeline: What could block each phase, and how to mitigate

**Time to read:** 10–15 minutes (or reference as you code)  
**When to read:** Before starting Phase 1; review weekly during development

---

### 💻 Technical Details: [TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md)

**System design, data models, and implementation guidance.**

- Architecture overview & design principles
- Complete package structure (all modules, responsibilities)
- Core data models (Resource, Facility, Location, Faction, World, Tech)
- System algorithms (production resolution, market pricing, AI loop, tech research)
- Key algorithms in pseudocode (calculate costs, monthly tick, AI decisions)
- Dependencies & performance targets
- Testing strategy

**Time to read:** 20–30 minutes (reference during coding)  
**When to read:** Week 1, before implementing core models

---

### 📦 Production Chain: [MATERIALS_RECIPES.md](MATERIALS_RECIPES.md)

**Complete resource, facility, and technology reference.**

- All 8 Phase 1 resources (raw, intermediate, finished goods)
- All 6 facility types (extraction, processing, finished goods)
- All recipes (inputs, outputs, costs, operation modes)
- Complete tech tree (6 core technologies, unlocks, progression)
- Production chain diagrams (simple to complex)
- Balance notes & example calculations

**Time to read:** 15–20 minutes (reference constantly)  
**When to read:** Before implementing recipes; during balance tuning

---

### 🤖 AI Behavior: [AI_HEURISTICS.md](AI_HEURISTICS.md)

**AI faction decision-making logic and debugging guide.**

- AI philosophy (deterministic, debuggable, competitive, non-cheating)
- Complete monthly decision loop (pseudocode)
- Heuristic rules: Observe → Assess → Expand → Produce → Trade → Reinvest
- Behavior characteristics (expansion pattern, profitability, competition dynamics)
- Debugging guide (logging, observation, tuning parameters)
- Example game trace (AI behavior over 12 months)
- Difficulty tuning (easy/normal/hard modes)

**Time to read:** 15–20 minutes (reference during AI coding)  
**When to read:** Week 3, before implementing AI agent

---

### ✅ Pre-Development: [DECISIONS_CHECKLIST.md](DECISIONS_CHECKLIST.md)

**Critical decisions Dan must lock before coding starts.**

- 5 quick decisions (game speed, build cost, starting capital, duration, difficulty)
- 5 detailed design decisions (win condition, Earth demand, facility queuing, save/undo, AI types)
- 5 key assumptions to validate during Phase 1 playtest
- Sign-off template (confirm all decisions locked)
- Decision log template (track changes during development)

**Time to read:** 10 minutes (first time); 5 minutes (during development)  
**When to read:** Before starting any code; validate assumptions during Phase 1

---

## How to Use This Documentation

### For Dan (Main Developer)

**Week 0 (Before coding):**
1. Read [MVP_PLAN.md](MVP_PLAN.md) — Understand the vision
2. Review [DECISIONS_CHECKLIST.md](DECISIONS_CHECKLIST.md) — Lock decisions
3. Create materials spreadsheet — Lock all recipes & costs (30 min)
4. Sketch AI pseudocode — Know the heuristic loop (1–2 hrs)

**Week 1–6 (Phase 1 development):**
1. Reference [TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md) — Implement data models
2. Reference [MATERIALS_RECIPES.md](MATERIALS_RECIPES.md) — Implement facilities & recipes
3. Reference [AI_HEURISTICS.md](AI_HEURISTICS.md) — Implement AI faction logic
4. Reference [PHASE_BREAKDOWN.md](PHASE_BREAKDOWN.md) — Track weekly milestones

**Week 7+ (Phase 2 planning):**
1. Review [PHASE_BREAKDOWN.md](PHASE_BREAKDOWN.md) — Phase 2 additions
2. Playtest Phase 1 — Document what worked/what didn't
3. Plan Phase 2 with fresh insights from Phase 1

---

### For Others (Future Team Members, Reviewers)

**To understand the design:**
→ Read [MVP_PLAN.md](MVP_PLAN.md) + [PHASE_BREAKDOWN.md](PHASE_BREAKDOWN.md)

**To understand the economy:**
→ Read [MATERIALS_RECIPES.md](MATERIALS_RECIPES.md) + [TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md)

**To understand the AI:**
→ Read [AI_HEURISTICS.md](AI_HEURISTICS.md)

**To review decisions:**
→ Read [DECISIONS_CHECKLIST.md](DECISIONS_CHECKLIST.md)

**To implement a specific system:**
→ Jump to the relevant section in [TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md)

---

## Documentation Quality Checklist

✅ **Clarity:** Written for someone new to the project  
✅ **Concrete:** Examples, not abstractions  
✅ **Complete:** All essential information included  
✅ **Organized:** Clear sections, easy to navigate  
✅ **Actionable:** Specific tasks, not vague guidance  
✅ **Consistent:** Style and terminology consistent across docs  
✅ **Linked:** Cross-references between related sections  
✅ **Tested:** Recommendations based on Iris's detailed analysis  

---

## Key Numbers (Quick Reference)

### Phase 1 (MVP)

| Metric | Value |
|--------|-------|
| **Duration** | 4–6 weeks |
| **Locations** | 3 (Moon, Mars, Belt) |
| **Resources** | 8 (3 raw, 3 intermediate, 2 finished) |
| **Facilities** | 6 types |
| **Technologies** | 6 core techs |
| **AI Factions** | 2 identical heuristic agents |
| **Earth Factions** | 4 (demand drivers only) |
| **Code** | ~3,000 lines Python |
| **Interface** | CLI/text-based |
| **Playthrough Length** | 5–7 in-game years (60–84 turns) |

### Critical Decisions (Default Recommendations)

| Decision | Recommended |
|----------|-------------|
| **Game Speed** | Monthly turns |
| **Build Cost** | Fixed 5,000 credits |
| **Starting Capital** | Player 50k, AI 30k |
| **Playthrough Duration** | 5–7 in-game years |
| **Facility Queuing** | One at a time |
| **Win Condition** | Pure sandbox (no hard goals) |
| **Save/Undo** | No undo; frequent autosave |
| **AI Specialization** | Identical heuristics (Phase 1) |

---

## Navigating by Role

### I'm a Designer (Understanding the Game)

1. [MVP_PLAN.md](MVP_PLAN.md) — What the game is
2. [MATERIALS_RECIPES.md](MATERIALS_RECIPES.md) — What players do (economy)
3. [AI_HEURISTICS.md](AI_HEURISTICS.md) — Who they compete with
4. [PHASE_BREAKDOWN.md](PHASE_BREAKDOWN.md) — How it grows over time

### I'm a Programmer (Building the Game)

1. [DECISIONS_CHECKLIST.md](DECISIONS_CHECKLIST.md) — Lock decisions first
2. [TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md) — How to code it
3. [MATERIALS_RECIPES.md](MATERIALS_RECIPES.md) — What to implement
4. [AI_HEURISTICS.md](AI_HEURISTICS.md) — AI logic pseudocode
5. [PHASE_BREAKDOWN.md](PHASE_BREAKDOWN.md) — Track progress weekly

### I'm a Reviewer (Checking the Plan)

1. [MVP_PLAN.md](MVP_PLAN.md) — Is the scope right?
2. [DECISIONS_CHECKLIST.md](DECISIONS_CHECKLIST.md) — Are decisions locked?
3. [PHASE_BREAKDOWN.md](PHASE_BREAKDOWN.md) — Is the timeline realistic?
4. [TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md) — Is the design sound?

### I'm Playtesting (Understanding What to Check)

1. [MVP_PLAN.md](MVP_PLAN.md) — Section "Success Criteria"
2. [PHASE_BREAKDOWN.md](PHASE_BREAKDOWN.md) — Phase 1 success metrics
3. [MATERIALS_RECIPES.md](MATERIALS_RECIPES.md) — Balance targets

---

## Common Questions Answered

### "Where do I start?"

→ [MVP_PLAN.md](MVP_PLAN.md), then [DECISIONS_CHECKLIST.md](DECISIONS_CHECKLIST.md)

### "What's the scope of Phase 1?"

→ [PHASE_BREAKDOWN.md](PHASE_BREAKDOWN.md) under "Phase 1: MVP"

### "What's the production chain?"

→ [MATERIALS_RECIPES.md](MATERIALS_RECIPES.md), "Production Chain Diagrams"

### "How do I code the AI?"

→ [AI_HEURISTICS.md](AI_HEURISTICS.md), "Heuristic Rules (Pseudocode)"

### "What are the critical decisions?"

→ [DECISIONS_CHECKLIST.md](DECISIONS_CHECKLIST.md), "Quick Decisions"

### "What should I test?"

→ [PHASE_BREAKDOWN.md](PHASE_BREAKDOWN.md), "Phase 1 Playtest Checklist"

### "How do I balance the game?"

→ [MATERIALS_RECIPES.md](MATERIALS_RECIPES.md), "Balance Notes"

### "What if I need to change a decision?"

→ [DECISIONS_CHECKLIST.md](DECISIONS_CHECKLIST.md), "What If Changes Happen?"

---

## File Statistics

| Document | Lines | Focus |
|----------|-------|-------|
| MVP_PLAN.md | 482 | Vision, philosophy, core systems |
| PHASE_BREAKDOWN.md | 545 | Week-by-week roadmap (all 3 phases) |
| TECHNICAL_ARCHITECTURE.md | 808 | Data models, algorithms, implementation |
| MATERIALS_RECIPES.md | 550 | Resources, facilities, tech tree |
| AI_HEURISTICS.md | 581 | AI decision-making, debugging, tuning |
| DECISIONS_CHECKLIST.md | 444 | Pre-dev decisions, assumptions, sign-off |
| **Total** | **3,410** | **Complete design & implementation guide** |

---

## Change Log

| Date | Document | Change | Reason |
|------|----------|--------|--------|
| 2026-03-28 | All | Initial release | Phase 1 planning complete |

---

## Appendix: Quick Start Script

**For Dan, Week 0:**

```bash
# 1. Review the design
open MVP_PLAN.md
open DECISIONS_CHECKLIST.md

# 2. Lock decisions (fill out checklist)
# 3. Create materials spreadsheet (in Excel/Sheets)
# 4. Sketch AI pseudocode (30 min)
# 5. Setup Git repo
git init sol-corp
cd sol-corp
git branch -b phase-1-mvp

# 6. Create project skeleton
mkdir sol_corp
mkdir sol_corp/{core,ai,earth,ui,tests}
touch sol_corp/__init__.py
# (see TECHNICAL_ARCHITECTURE.md for structure)

# 7. Read technical architecture
open TECHNICAL_ARCHITECTURE.md

# 8. Start Week 1
# Begin implementing core/resource.py
```

---

## Next Steps

1. **For Dan:** Review [MVP_PLAN.md](MVP_PLAN.md) + [DECISIONS_CHECKLIST.md](DECISIONS_CHECKLIST.md)
2. **Lock decisions** (10 min call or email)
3. **Create materials spreadsheet** (30 min; lock recipes)
4. **Sketch AI pseudocode** (1–2 hours)
5. **Setup Git repo** (5 min)
6. **Start Phase 1 Week 1** with full confidence

---

## Document Versions & Branches

This is the **Phase 1 planning version**. Documentation will evolve as Phase 1 develops:

- **Phase 1 (in progress):** Core design, Week 1–6 implementation
- **Phase 2 (future):** Economic depth, expanded scope
- **Phase 3 (future):** Expansion & performance

Each phase will have its own branch of documentation, but core concepts remain stable.

---

## Support & Questions

**For Dan:**
- Questions about design → Check [MVP_PLAN.md](MVP_PLAN.md)
- Questions about implementation → Check [TECHNICAL_ARCHITECTURE.md](TECHNICAL_ARCHITECTURE.md)
- Questions about balance → Check [MATERIALS_RECIPES.md](MATERIALS_RECIPES.md)
- Questions about decisions → Check [DECISIONS_CHECKLIST.md](DECISIONS_CHECKLIST.md)
- Questions about progress → Check [PHASE_BREAKDOWN.md](PHASE_BREAKDOWN.md)

**During development:**
- Document blockers in a "dev_log.md" alongside this documentation
- Reference documents as needed; they're living guides, not carved in stone
- Update [DECISIONS_CHECKLIST.md](DECISIONS_CHECKLIST.md) if decisions change

---

## Credits

**Created by:** Iris (analysis & planning) → Wave (documentation & organization)

**For:** Dan Bull, Sol Corp MVP development

**Philosophy:** Clarity, completeness, and actionable guidance over theoretical purity.

---

**Last compiled:** 2026-03-28  
**Status:** Ready for Phase 1 development  
**Next review:** End of Phase 1 (Week 6)  

🚀 **Let's build something fun.**

