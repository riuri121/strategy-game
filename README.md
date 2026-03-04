# Strategy Game: Sol Corp

A single-player economic sandbox strategy game set in a future where competing corporations mine resources on Earth and across the solar system.

**Stack:** Python (core logic) + Rust (performance-critical systems)

## About the Game

Sol Corp is a Victoria 3-inspired economic simulation where you build production chains, manage supply and demand across Earth and space markets, compete with AI factions, and navigate geopolitical factors. The game emphasizes economic strategy, resource logistics, and long-term planning.

## Project Structure

### `/python` — Core Game Logic & Engine
The main game engine and logic layer, written in Python for rapid iteration and clear architecture.

- **Entry point:** `main.py`
- **Dependencies:** See `requirements.txt`
- **Setup:** Create virtual environment, install dependencies, and run `python main.py`
- See [`python/README.md`](python/README.md) for detailed Python development guide

### `/rust` — Performance-Critical Systems
High-performance components for compute-intensive operations (pathfinding, economic calculations, market simulations).

- **Entry point:** `src/main.rs`
- **Setup:** Build with `cargo build`, run with `cargo run`
- See [`rust/README.md`](rust/README.md) for detailed Rust development guide

### `/design` — Game Design & Documentation
Complete game design documentation, including core mechanics, systems documentation, and design decisions.

- **Core Concept:** [`design/GDD_CORE.md`](design/GDD_CORE.md) — High-level concept, design pillars, and key systems
- **Earth Systems:** [`design/SYSTEMS_EARTH.md`](design/SYSTEMS_EARTH.md) — Market mechanics, factions, demand
- **Space Systems:** [`design/SYSTEMS_SPACE_FACTIONS.md`](design/SYSTEMS_SPACE_FACTIONS.md) — AI corporations, competition
- **Locations:** [`design/SYSTEMS_LOCATIONS.md`](design/SYSTEMS_LOCATIONS.md) — Moon, Mars, asteroid belt economics
- **Production:** [`design/SYSTEMS_PRODUCTION.md`](design/SYSTEMS_PRODUCTION.md) — Facilities, recipes, operation styles
- **Design Log:** [`design/SESSION_LOG.md`](design/SESSION_LOG.md) — Design decisions and current work in progress

See [`design/README.md`](design/README.md) for the complete design guide.

### `/tests` — Test Suites
Automated tests for both Python and Rust components.

- **Python tests:** Run with `pytest`
- **Rust tests:** Run with `cargo test`
- See [`tests/README.md`](tests/README.md) for testing guidelines

## Quick Start

### Python Development

```bash
cd python
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py
```

### Rust Development

```bash
cd rust
cargo build
cargo run
```

## Development Workflow

1. **Design changes:** Update relevant docs in `/design` and reference in PRs
2. **Python changes:** Work in `/python`, ensure tests pass with `pytest`
3. **Rust changes:** Work in `/rust`, ensure tests pass with `cargo test`
4. **Full integration:** Both components must build and pass tests

## Tech Stack

- **Python 3.x** — Game engine, logic, simulation
- **Rust** — High-performance systems, calculations
- **Git** — Version control

## Branches

- **main** — Production-ready releases
- **dev** — Active development
- **feature/*** — Feature branches for specific work
