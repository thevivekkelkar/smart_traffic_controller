"""
tasks.py
--------
Defines Easy, Medium, and Hard task configurations.
Only the arrival_rate changes — everything else stays the same.
"""

from traffic_env import TrafficEnvironment


def get_task(difficulty="medium"):
    """
    Returns a configured TrafficEnvironment for the chosen difficulty.

    Parameters
    ----------
    difficulty : str  "easy" | "medium" | "hard"

    Task Definitions
    ----------------
    Easy   — arrival_rate=1  : light traffic, agent can manage easily
    Medium — arrival_rate=2  : moderate traffic, some congestion possible
    Hard   — arrival_rate=4  : heavy traffic, hard to prevent jams
    """
    configs = {
        "easy": {
            "arrival_rate": 1,
            "green_flow"  : 3,
            "max_cars"    : 30,
            "max_steps"   : 50,
        },
        "medium": {
            "arrival_rate": 2,
            "green_flow"  : 3,
            "max_cars"    : 30,
            "max_steps"   : 50,
        },
        "hard": {
            "arrival_rate": 4,
            "green_flow"  : 3,
            "max_cars"    : 30,
            "max_steps"   : 50,
        },
    }

    if difficulty not in configs:
        raise ValueError(f"Unknown difficulty '{difficulty}'. Choose: easy, medium, hard")

    cfg = configs[difficulty]
    return TrafficEnvironment(**cfg)


# Quick task info printout
TASK_DESCRIPTIONS = {
    "easy"  : "Low traffic  — arrival_rate=1 car/step/lane",
    "medium": "Moderate traffic — arrival_rate=2 cars/step/lane",
    "hard"  : "Heavy traffic — arrival_rate=4 cars/step/lane",
}
