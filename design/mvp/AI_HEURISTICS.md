# Sol Corp AI Heuristics

**AI faction decision-making logic: pseudocode, behavior rules, and debugging guide.**

---

## Table of Contents

1. [AI Philosophy](#ai-philosophy)
2. [Monthly Decision Loop](#monthly-decision-loop)
3. [Heuristic Rules (Pseudocode)](#heuristic-rules-pseudocode)
4. [Behavior Characteristics](#behavior-characteristics)
5. [Debugging & Observation](#debugging--observation)
6. [Tuning Guide](#tuning-guide)

---

## AI Philosophy

### Goals for Phase 1 AI

1. **Deterministic:** No randomness; same state always produces same decision
2. **Debuggable:** Clear, simple logic; easy to trace decisions
3. **Competitive:** Expands, competes on price, reinvests profits
4. **Non-cheating:** Operates under same constraints as player (no hidden bonuses)
5. **Interesting:** Creates tension and makes game feel populated

### Non-Goals

- Complex pathfinding (all locations are accessible; no blocked routes in MVP)
- Sophisticated trading between AI factions (no inter-AI commerce in Phase 1)
- Diplomacy or alliances (Phase 2+)
- Prediction or planning beyond current month (reactive, not proactive)

---

## Monthly Decision Loop

### Overview

Each month, each AI faction executes this loop:

```
1. OBSERVE: Calculate current state (capital, opportunities, competitors)
2. ASSESS: Identify expansion opportunities by location & facility type
3. EXPAND: Build new facility if profitable
4. PRODUCE: Run all existing facilities (auto-manage operation styles)
5. TRADE: Sell goods to Earth market (automatic)
6. REINVEST: Use profits to fund next expansion
```

### Loop Execution Order

```
FOR each AI faction:
    observe_state()
    assess_opportunities()
    expand_if_profitable()
    produce_all_facilities()
    sell_goods_to_market()
    collect_profits()
    reinvest_if_capital_available()
```

**Timing:** AI operates after player each month, so AI sees results of player's actions. This creates interesting dynamics (player can "respond" to AI in next month).

---

## Heuristic Rules (Pseudocode)

### Rule 1: Observe State

```pseudocode
function OBSERVE_STATE(ai_faction):
    ai.current_capital = ai.capital
    ai.facility_count = length(ai.facilities)
    ai.locations_owned = set of locations with ai facilities
    ai.profit_last_month = ai.capital - ai.capital_last_month
    
    // For each location, count competitors
    for each location in [MOON, MARS, BELT]:
        ai.competitor_count[location] = count of other factions with facilities there
        ai.saturation[location] = competitor_count[location]
    
    return {
        capital: ai.current_capital,
        facility_count: ai.facility_count,
        locations_owned: ai.locations_owned,
        profit: ai.profit_last_month,
        saturation: ai.saturation
    }
```

### Rule 2: Assess Opportunities

```pseudocode
function ASSESS_OPPORTUNITIES(ai_faction, world_state):
    opportunities = []
    
    // For each location
    for each location in [MOON, MARS, BELT]:
        // Skip if we don't have tech to access this location
        if location == MARS and "Mars Colonization" not in ai.researched_techs:
            continue
        if location == BELT and "Asteroid Mining" not in ai.researched_techs:
            continue
        
        // For each facility type
        for each facility_type in [IRON_MINE, RARE_EARTH_PROCESSOR, SILICON_QUARRY, REFINERY, COMPONENT_FACTORY]:
            
            // Estimate profit margin for this facility at this location
            estimated_output = facility_output_per_month[facility_type]
            estimated_price = current_market_price[facility_type's_product][location]
            estimated_revenue = estimated_output * estimated_price
            
            // Account for distance penalty
            distance_penalty = location_distance_penalty[location]
            revenue_after_penalty = estimated_revenue * (1 - distance_penalty)
            
            // Estimate costs
            facility_overhead = facility_maintenance_cost[facility_type]
            input_cost = 0
            if facility_type requires inputs:
                input_cost = estimate_input_cost(facility_type, location, world_state)
            
            total_cost = facility_overhead + input_cost
            
            // Calculate profit margin
            profit_margin = revenue_after_penalty - total_cost
            
            // Store opportunity
            if profit_margin > 0:
                opportunities.append({
                    location: location,
                    facility_type: facility_type,
                    estimated_profit: profit_margin,
                    competitors: saturation[location]
                })
    
    // Sort by profit margin (descending)
    opportunities.sort_by(estimated_profit, descending=true)
    
    return opportunities
```

### Rule 3: Expand (Build New Facility)

```pseudocode
function EXPAND(ai_faction, opportunities):
    FACILITY_COST = 5000
    MIN_CAPITAL_BUFFER = 2000  // Safety margin; don't go broke
    
    if opportunities is empty:
        // No expansion opportunities
        return false
    
    best_opportunity = opportunities[0]
    
    // Check if we can afford it
    if ai.capital > FACILITY_COST + MIN_CAPITAL_BUFFER:
        // Build facility
        new_facility = create_facility(
            location = best_opportunity.location,
            facility_type = best_opportunity.facility_type,
            owner = ai.id
        )
        
        // Deduct capital
        ai.capital -= FACILITY_COST
        ai.facilities.append(new_facility)
        
        // Log the decision (for debugging)
        log("AI " + ai.id + " built " + best_opportunity.facility_type + " at " + best_opportunity.location)
        
        return true
    else:
        // Can't afford, even with best opportunity
        return false
```

### Rule 4: Produce (Run All Facilities)

```pseudocode
function PRODUCE(ai_faction):
    for each facility in ai.facilities:
        
        // Choose recipe (for MVP, facilities have only 1 recipe by default)
        recipe = facility.current_recipe
        
        // Check if recipe can run
        if facility.can_run_recipe(recipe):
            
            // Choose operation style based on cash flow
            if ai.capital > 20000:  // Healthy cash
                operation_style = FULLY_MANNED  // Fast production
            else if ai.capital > 10000:  // Moderate cash
                operation_style = SKELETON  // Medium pace
            else:  // Low cash
                operation_style = BASIC  // Slow, cheap
            
            facility.operation_style = operation_style
            facility.run_production(recipe)
            
        else:
            // Inputs not available; reduce costs by downgrading
            facility.operation_style = BASIC
            // Facility doesn't run this month, but costs less to maintain
```

### Rule 5: Trade (Sell Goods)

```pseudocode
function TRADE(ai_faction, world_state):
    total_revenue = 0
    
    for each location in ai.locations_owned:
        for each facility at location:
            
            // Get all output goods produced this month
            for each (good_name, quantity) in facility.output_inventory:
                
                // Get market price for this good at this location
                market_price = world_state.get_market_price(good_name, location)
                
                // Calculate revenue (including distance penalty)
                distance_penalty = location_distance_penalty[location]
                net_price = market_price * (1 - distance_penalty)
                revenue = quantity * net_price
                
                // Calculate cost (facility overhead + input costs)
                cost = facility.production_cost_last_month
                
                // Add profit to faction capital
                profit = revenue - cost
                ai.capital += profit
                total_revenue += revenue
                
                // Clear inventory (goods sold)
                facility.output_inventory[good_name] = 0
    
    return total_revenue
```

### Rule 6: Reinvest (Recursive Expansion)

```pseudocode
function REINVEST(ai_faction, world_state):
    
    // After selling goods, recursively check for expansion
    // If capital is healthy, expand again immediately
    
    while ai.capital > FACILITY_COST + MIN_CAPITAL_BUFFER:
        
        // Reassess opportunities (market prices may have changed)
        new_opportunities = ASSESS_OPPORTUNITIES(ai_faction, world_state)
        
        if new_opportunities is empty:
            // No more opportunities; stop expanding
            break
        
        // Expand to best opportunity
        success = EXPAND(ai_faction, new_opportunities)
        
        if not success:
            // Should not happen; checked capital above
            break
```

---

## Behavior Characteristics

### Expansion Pattern

**Expected behavior:**
- AI starts on Moon with 30,000 credits
- Builds 1–2 iron mines immediately (abundant, safe)
- Builds refinery once Iron Smelting tech available
- Expands to Mars when Mars Colonization tech available
- Specialized strategies emerge (some AIs focus on rare earths, others on volume)

**Realistic timeline:**
```
Month 1: Build iron mine on Moon (capital: 25k)
Month 2–3: Build refinery on Moon (capital: 20k)
Month 4: Build silicon quarry on Moon (capital: 15k)
Month 5–6: Profits accumulate; build second refinery (capital: 10k)
Month 7–8: Profits allow expansion; explore Mars if tech available
Month 10+: Specialization based on profits & tech
```

### Profitability

**Iron mining (Moon):**
- Revenue per month: 500 cr (10 ore × 50 cr base price)
- Cost: 100 cr maintenance
- Profit: 400 cr/month per mine
- Payback: ~13 months to recoup 5,000 cr build cost

**Refinery (if inputs available):**
- Revenue: 500 cr (5 metal × 100 cr, no distance penalty on Moon)
- Cost: 150 cr maintenance + input cost
- Profit: highly variable (depends on input prices)
- Risk: Can operate at loss if inputs are expensive

**AI strategy:** Prefer raw extraction early (low risk, positive profit). Move to processing only when capital is healthy and inputs are cheap.

### Competition Dynamics

**Price suppression:**
- More facilities at a location → more supply → lower prices
- Example: Moon with 3 iron mines (player + 2 AIs) produces 30 ore/month
- If Earth demand is 15 ore/month, supply exceeds demand 2:1
- Prices drop (scarcity multiplier < 1.0)
- All AI profits decline; incentivizes relocation

**Relocation behavior:**
- AI observes low profits on Moon → Assesses Mars/Belt opportunities
- If Mars tech available and margins better, AI begins Mars expansion
- Mars prices initially higher (lower competition) → profits recover
- Eventually Mars also saturates; Belt becomes attractive

**Result:** Dynamic economy with natural cycles (location → boom → saturation → migration)

---

## Debugging & Observation

### Logging Output (Recommended for Phase 1)

Enable verbose logging to watch AI behavior:

```pseudocode
function AI_MONTHLY_LOOP_VERBOSE(ai_faction, world_state):
    
    log("=== " + ai.id + " MONTHLY LOOP (Month " + month + ") ===")
    
    state = OBSERVE_STATE(ai_faction)
    log("State: Capital=" + state.capital + ", Facilities=" + state.facility_count)
    
    opps = ASSESS_OPPORTUNITIES(ai_faction, world_state)
    if opps.length > 0:
        log("Top opportunity: " + opps[0].facility_type + " at " + opps[0].location + ", profit=" + opps[0].estimated_profit)
    
    EXPAND(ai_faction, opps)
    PRODUCE(ai_faction)
    revenue = TRADE(ai_faction, world_state)
    log("Revenue: " + revenue + ", New capital: " + ai.capital)
    
    REINVEST(ai_faction, world_state)
    log("=== END " + ai.id + " ===\n")
```

### Observing Behavior in Play

**Questions to ask while playing:**

1. **Do AI factions expand?** (Should expand to Mars by Month 10+)
   - If no: AI might be bankrupt (check capital), or cost too high
   
2. **Do prices move?** (Should drop over time as supply increases)
   - If static: Check price formula; should vary with supply/demand
   
3. **Do AI compete?** (Should undercut each other's prices)
   - If not: AI might not be selling; check trade logic
   
4. **Does AI go bankrupt?** (Should not in first 24 months)
   - If yes: MIN_CAPITAL_BUFFER too low; increase to 5k
   
5. **Does AI hoard capital?** (Should reinvest; not sit on 100k)
   - If yes: REINVEST loop might be broken; check expansion logic

### Debug Checklist

- [ ] AI expands at least once per 3 months
- [ ] AI facilities are producing (check output inventory)
- [ ] AI is selling goods (check revenue calculation)
- [ ] AI capital grows or stays stable (not declining)
- [ ] AI doesn't build redundant facilities (e.g., 5 iron mines)
- [ ] AI competes on price (prices are lower than player's)
- [ ] AI survives 36 months without bankruptcy

---

## Tuning Guide

### Parameter Tuning (If Behavior is Off)

#### AI Expands Too Fast (Overkill Facilities)

**Symptom:** AI builds 10+ facilities by Month 12; market totally saturated

**Causes:**
- MIN_CAPITAL_BUFFER too low (AI not conservative enough)
- Profit margins overestimated in ASSESS_OPPORTUNITIES

**Fix:**
```pseudocode
// Increase safety buffer
MIN_CAPITAL_BUFFER = 5000  // up from 2000

// Or reduce expansion greed
if ai.capital > FACILITY_COST + MIN_CAPITAL_BUFFER:
    // Only expand if profit margin is good AND capital is very healthy
    if opportunities[0].estimated_profit > 500 and ai.capital > 25000:
        EXPAND(...)
```

#### AI Expands Too Slow (Sits on Capital)

**Symptom:** AI has 50k capital but doesn't expand; feels passive

**Cause:**
- ASSESS_OPPORTUNITIES underestimates profit
- Opportunities list empty (tech gates?)

**Fix:**
```pseudocode
// Lower the threshold for "good opportunity"
if profit_margin > 100:  // down from 0
    opportunities.append(...)

// Or reduce buffer
MIN_CAPITAL_BUFFER = 1000  // down from 5000

// Or force expansion if not expanding
if opportunity.length > 0 and ai.facility_count < 5:
    EXPAND(...)  // expand even if profit is marginal
```

#### AI Goes Bankrupt

**Symptom:** AI capital drops to 0 by Month 18; stops expanding

**Cause:**
- Facilities running at a loss (high input costs, low output prices)
- MIN_CAPITAL_BUFFER not protecting against margin collapse

**Fix:**
```pseudocode
// Increase buffer significantly
MIN_CAPITAL_BUFFER = 10000

// Or add break-even check before expanding
estimated_monthly_profit = estimate_production_profit(facility_type, location)
if estimated_monthly_profit < 50:
    // Too risky; skip this expansion
    continue

// Or reduce operation style aggressiveness (use BASIC instead of FULLY_MANNED)
if ai.capital < 10000:
    operation_style = BASIC  // reduce costs
```

#### AI Doesn't Adapt to Market (Prices Collapse)

**Symptom:** AI keeps building iron mines; prices drop to 10 cr; AI loses money

**Cause:**
- ASSESS_OPPORTUNITIES doesn't recalculate live prices
- AI uses stale price estimates

**Fix:**
```pseudocode
// Recalculate prices each month
for each opportunity:
    current_market_price = world_state.get_current_price(good_type)
    // Don't use cached price from day 1
    
// Or add saturation penalty
if competitor_count[location] > 1:
    estimated_profit *= 0.8  // 20% penalty per extra competitor
```

### Difficulty Tuning

**Easy Mode (Player advantage):**
```
AI starting capital: 20,000 (down from 30k)
AI MIN_CAPITAL_BUFFER: 10,000 (conservative)
AI Operation Style: BASIC always (slow)
Result: AI expands slowly; player can dominate
```

**Normal Mode (Fair fight):**
```
AI starting capital: 30,000
AI MIN_CAPITAL_BUFFER: 5,000
AI Operation Style: Dynamic (BASIC → SKELETON → FULLY_MANNED based on cash)
Result: Competitive; player can win with skill
```

**Hard Mode (AI advantage):**
```
AI starting capital: 50,000 (up from 30k)
AI MIN_CAPITAL_BUFFER: 2,000 (aggressive)
AI Operation Style: FULLY_MANNED always (fast)
AI bonus: +10% efficiency on all facilities
Result: AI dominates; player must be strategic
```

---

## Example Game Trace

### AI Behavior Over 12 Months

```
Month 1 (Start):
  AI capital: 30,000
  OBSERVE: No facilities yet
  ASSESS: Moon has no competitors; iron mine very profitable
  EXPAND: Build iron mine on Moon (capital now 25,000)
  PRODUCE: Mine runs; produces 10 ore
  TRADE: Sell 10 ore at 50 cr = 500 cr; cost 100 cr overhead = 400 cr profit
  REINVEST: Capital now 25,400; build another mine

Month 2:
  AI capital: ~20,000 (spent 5k on second mine)
  OBSERVE: 2 facilities on Moon
  ASSESS: Iron mines profitable; refinery possible but no tech yet
  EXPAND: Build silicon quarry on Moon (capital now 15,000)
  PRODUCE: 2 mines + 1 quarry producing
  TRADE: Total revenue ~1,500 cr; profit ~1,000 cr
  REINVEST: Capital back to ~16,000

Month 5 (Tech: Iron Smelting, Silicon Processing unlocked):
  AI capital: ~25,000 (profits accumulating)
  OBSERVE: 3 facilities; Moon is profitable
  ASSESS: Refinery now viable; component factory unlocked
  EXPAND: Build refinery (capital now 20,000)
  PRODUCE: 4 facilities running
  TRADE: Revenue includes metal sales; profit +1,500 cr
  REINVEST: Capital ~21,500

Month 10:
  AI capital: ~35,000 (steady profit growth)
  OBSERVE: 5 facilities; Moon prices dropping (competition with player)
  ASSESS: Moon margins declining; Mars not accessible yet
  EXPAND: Build second refinery on Moon; Mars expansion blocked by tech gate
  PRODUCE: All facilities running
  TRADE: Revenue still good; competition not killing profit yet
  REINVEST: Capital stable at ~30,000

Month 15 (Tech: Mars Colonization unlocked):
  AI capital: ~45,000
  OBSERVE: Moon crowded (player + 1 AI + 1 other AI = 15 facilities); prices low
  ASSESS: Mars now accessible; margins better there; fewer competitors
  EXPAND: Build iron mine on Mars (capital now 40,000)
  PRODUCE: Facilities on both Moon and Mars
  TRADE: Mars margins higher; overall profit improving
  REINVEST: Capital climbing to 50,000+

Month 24 (End of Phase 1 Simulation):
  AI capital: ~80,000
  OBSERVE: 8–10 facilities split between Moon and Mars
  ASSESS: Belt not yet accessible; expanding Mars aggressively
  EXPAND: Build 2–3 more facilities this month
  PRODUCE: Strong production across locations
  TRADE: Revenue growing; profit margins healthy
  REINVEST: Positioned for Belt exploration if tech available
```

**Result:** AI expands naturally, adapts to tech gates, competes with player, and feels like an opponent. Good Phase 1 outcome.

---

## Next Steps

1. **Implement OBSERVE_STATE** first (simplest; just queries faction state)
2. **Implement ASSESS_OPPORTUNITIES** (core logic; test thoroughly)
3. **Implement EXPAND** (straightforward; just creates facility)
4. **Implement PRODUCE & TRADE** (mostly reuse existing simulation code)
5. **Implement REINVEST** (recursive; test for infinite loops)
6. **Add verbose logging** and watch a few months of play
7. **Tune parameters** based on observed behavior

---

**Ready to code AI? Start with ASSESS_OPPORTUNITIES; it's the heart of the heuristics.** 🤖

