# Sol Corp — Earth Systems (WIP)

## Overview
Earth is the **market hub** and **economic engine**. It cannot be colonized or mined; it's where goods are sold, demand is generated, and prices are set. Earth factions compete with each other for market share, creating dynamic demand for your goods.

---

## Earth Factions

**Four permanent powers:** USA, Europe, China, India

Each is a **pure demand sink**. They don't produce goods relevant to the game; their economies are self-contained on Earth. They consume raw resources, intermediate products, consumer goods, and military goods at rates determined by their internal political situation.

### Demand Drivers

All factions demand the same **resource categories:**
- Raw materials (ore, minerals, rare earths)
- Intermediate products (refined metals, components)
- Consumer goods (manufactured products)
- Research materials (advanced tech inputs)
- Military goods (weapons, armor, equipment)

**Demand levels shift based on internal events:**
- Economic boom → increased demand across all categories
- Internal conflict/war → spiked military demand
- Political instability → reduced demand (economy contracts)
- Tech breakthroughs → temporary demand spikes for research materials
- Population growth → consumer goods demand increases

**Events are random** but constrained: no faction can be permanently destroyed or eliminated. The system stays dynamic but stable.

---

## Early Game Bootstrap

**Problem:** Player needs initial construction materials to build their first facilities, but space mining doesn't exist yet.

**Solution:** Earth exports fixed-price bootstrap materials (construction supplies, basic metals, equipment) during early game. These materials are cheap and available in unlimited quantity.

**Transition:** As player ramps up space production, Earth materials become uneconomical to import (transport costs + competition from cheaper space-mined goods). By mid-game, Earth exports are irrelevant; all production comes from space.

**Effect:** Forces early growth from Earth market, then naturally transitions to space-based supply chains.

---

## Market Mechanics (Draft)

### Demand System
Each faction generates **demand orders** based on:
- **Production capacity** (they need X tons of rare earths per quarter to maintain factories)
- **Growth rate** (expanding factions need more; declining factions need less)
- **Political dynamics** (if two factions ally, combined demand shifts)
- **Technology level** (higher tech → higher material demands)

**Example:**
- Hegemony needs 50 tons of titanium/quarter for construction
- Nexus needs 20 tons of rare earths/quarter for electronics
- Commonwealth needs 30 tons of basic metals/quarter for equipment
- **Total Earth demand:** ~100 tons/quarter (simplified)

### Price Dynamics

**Base Price = Scarcity Factor × Demand Level × Faction Preference**

- If supply is low relative to demand → prices rise
- If you (the player) are the only supplier → you set the price (monopoly advantage)
- If space factions are also supplying → competitive pricing
- Factions have budget limits; if your price is too high, they buy elsewhere or reduce production

**Example:**
- Rare earths base price: 100 credits/ton
- Nexus is desperate (high growth) → multiplier ×1.5 = 150 credits/ton
- But supply is abundant → multiplier ×0.8 = 120 credits/ton
- **Final price:** ~120 credits/ton (negotiated)

### Trade Mechanics

**Player → Earth (Export):**
- You haul goods to Earth orbit
- You sell at the current market price (or negotiate if you're a large supplier)
- You receive credits (profit)

**Earth → Space (Earth imports materials it can't produce):**
- Factions may buy goods from other factions or space factions if your prices are too high
- Creates competitive pressure
- Scarcity events (supply shocks) create opportunity for high margins

---

## Faction Relationships & Dynamics

### Political Alliances
Factions form alliances that affect:
- **Trade routes** (allied factions trade with each other at discounts)
- **Demand shifts** (allied factions coordinate resource needs)
- **Opportunities for player** (if a faction is isolated, they're desperate buyers)

**Example:** Hegemony and Commonwealth form a trade alliance → they share resources, reducing their individual demand for rare Earth materials → player's prices drop.

### Conflict & Instability
- Factions can enter disputes (economic wars, literal conflicts—TBD scope)
- Disputes disrupt supply chains; create demand spikes for weapons, repairs, replacement goods
- Player can exploit instability or suffer from it

### AI Behavior (Rough Sketch)
Each faction runs a simple economic AI:
1. **Assess:** How much of each material do I need?
2. **Source:** Buy from Earth factions or space suppliers (cheapest option wins)
3. **Produce:** Make goods; generate demand for materials
4. **Trade:** Sell to other factions or invest in growth

---

## Player Interaction with Earth

### Export Flow
1. Player builds factory/mine in space; produces goods
2. Player loads goods onto transport (cost: credits/time/fuel)
3. Transport hauls to Earth orbit
4. Goods are sold to faction(s) at current market price
5. Player receives credits in bank

### Market Information
Player can:
- View each faction's current demand
- View current prices per good
- View price history (trending up/down?)
- View competitor activity (which factions are buying what)
- Receive alerts when demand spikes or crashes

### Strategic Opportunities
- **Monopoly play:** Be the only supplier of a rare good → set high prices
- **Volume play:** Supply common goods cheap, profit on scale
- **Speculation:** Buy low, sell high (if Earth goods can be transported to space?)
- **Shortage exploit:** When a faction is desperate, charge premium
- **Cartel prevention:** Space factions might team up; player needs to stay competitive

---

## Open Questions

- [ ] **Event system:** How are random events triggered? What's their frequency? Severity range?
- [ ] **Price volatility:** How much do prices swing when demand changes? Smooth curves or sharp spikes?
- [ ] **Pricing power:** Is pricing algorithmic (player is price-taker), or can player negotiate?
- [ ] **Faction relationships with player:** Are transactions purely transactional, or can factions favor/embargo you?

---

## Design Notes

- Earth should feel like a living, breathing market—not a flat resource sink
- Factions should feel like competitors to the player (indirectly) and to each other
- Prices should reward planning and punish greed; opportunity for clever play
- Player should be able to influence Earth events (by controlling supply)
