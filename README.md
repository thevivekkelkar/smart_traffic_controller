# AI Smart Traffic Signal Control System

A beginner-friendly Reinforcement Learning environment that simulates
a 4-way traffic intersection. An agent controls traffic lights to
reduce congestion across all lanes.

---

## Problem Statement

Traffic congestion at intersections wastes time and fuel.  
The goal is to train an AI agent that decides **which lane gets a green
light at each timestep** in order to keep the total number of waiting
cars as low as possible.

---

## Environment Overview

```
          [North]
             |
[West] ── JUNCTION ── [East]
             |
          [South]
```

At every timestep:
- Random cars **arrive** in every lane
- The green lane lets some cars **depart**
- Red lanes **accumulate** cars
- The agent receives a **reward** based on how few cars are waiting

---

## State Space

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| cars_north | int | 0–30 | Cars waiting in the North lane |
| cars_south | int | 0–30 | Cars waiting in the South lane |
| cars_east  | int | 0–30 | Cars waiting in the East lane  |
| cars_west  | int | 0–30 | Cars waiting in the West lane  |

**Example state:** `[10, 5, 3, 8]`

---

## Action Space

| Action | Meaning |
|--------|---------|
| `0` | North lane → green |
| `1` | South lane → green |
| `2` | East lane  → green |
| `3` | West lane  → green |

Only **one lane** is green per timestep. All others are red.

---

## Reward Function

```
reward = -(cars_north + cars_south + cars_east + cars_west)
```

- The reward is always **negative or zero**
- A reward of `0` means no cars are waiting (ideal)
- The agent's goal is to **maximize total reward** (= minimize congestion)

---

## Tasks

| Difficulty | Arrival Rate | Description |
|------------|-------------|-------------|
| Easy       | 1 car/step/lane | Light traffic — manageable |
| Medium     | 2 cars/step/lane | Moderate — some congestion |
| Hard       | 4 cars/step/lane | Heavy — very hard to control |

Only `arrival_rate` changes between tasks. All other settings are identical.

---

## Project Files

```
├── traffic_env.py   # Core RL environment (TrafficEnvironment class)
├── tasks.py         # Easy / Medium / Hard task configs
├── grader.py        # Scoring function → returns 0.0–1.0
├── main.py          # Demo simulation with a random agent
├── openenv.yaml     # OpenEnv-style config
├── Dockerfile       # Container setup
└── README.md        # This file
```

---

## How to Run

### Option 1 — Directly with Python

```bash
# Run simulation (random agent, all difficulties)
python main.py

# Run grader (scores random + greedy agents)
python grader.py
```

### Option 2 — With Docker

```bash
# Build the image
docker build -t traffic-signal .

# Run simulation
docker run traffic-signal

# Run grader
docker run traffic-signal python grader.py
```

---

## Using the Environment in Your Own Code

```python
from traffic_env import TrafficEnvironment

env   = TrafficEnvironment(arrival_rate=2)
state = env.reset()          # [cars_N, cars_S, cars_E, cars_W]

done = False
while not done:
    action = 0               # replace with your agent's decision
    state, reward, done = env.step(action)
    print(state, reward)
```

---

## Scoring

The grader runs your agent on all three difficulties and returns:

| Key | Description |
|-----|-------------|
| `easy`    | Score on easy task  |
| `medium`  | Score on medium task |
| `hard`    | Score on hard task  |
| `overall` | Average of the three |

All scores are between **0.0** (worst) and **1.0** (best).

---

## Notes

- No external libraries needed — uses only Python's `random` module
- No RL algorithm is included — the environment is the submission for Round 1
- Replace `random_agent` in `main.py` with your trained agent in Round 2


## Why this matters
Traffic congestion is a major problem in urban areas.
This environment simulates real-world traffic behavior and allows RL agents to learn optimal signal control policies.

## Baseline Results
- Random agent performs poorly
- Greedy agent improves traffic flow
- Environment is challenging at higher traffic levels