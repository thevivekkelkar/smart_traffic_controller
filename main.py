"""
main.py
-------
Runs a simple simulation of the Traffic Signal environment
using a random agent. Prints step-by-step output and total reward.
"""

import random
from traffic_env import TrafficEnvironment

LANE_NAMES = ["North", "South", "East", "West"]


def random_agent(state):
    """Picks a random lane to turn green."""
    return random.randint(0, 3)

def greedy_agent(state):
    """Always choose the lane with maximum cars."""
    return state.index(max(state))

def run_simulation(difficulty="medium", verbose=True):
    """
    Run one full episode and print results.

    Parameters
    ----------
    difficulty : "easy" | "medium" | "hard"  (controls arrival rate)
    verbose    : print each step if True
    """
    # Map difficulty to arrival rate
    arrival_rates = {"easy": 1, "medium": 2, "hard": 4}
    arrival_rate  = arrival_rates.get(difficulty, 2)

    env   = TrafficEnvironment(arrival_rate=arrival_rate)
    state = env.reset()

    total_reward = 0
    step         = 0

    print(f"\n{'='*52}")
    print(f"  AI Smart Traffic Signal — Simulation ({difficulty.upper()})")
    print(f"{'='*52}")
    print(f"  Lanes : {LANE_NAMES}")
    print(f"  Initial state: {state}\n")

    done = False
    while not done:
        action = greedy_agent(state)
        next_state, reward, done = env.step(action)
        total_reward += reward
        step         += 1

        if verbose:
            green = LANE_NAMES[action]
            print(
                f"  Step {step:>3} | Green: {green:<6} | "
                f"State: {[f'{x:>2}' for x in next_state]} | "
                f"Reward: {reward:>5}"
            )

        state = next_state

    print(f"\n{'─'*52}")
    print(f"  Episode finished after {step} steps.")
    print(f"  Total Reward : {total_reward}")
    print(f"  Avg per step : {total_reward / step:.2f}")
    print(f"{'='*52}\n")

    return total_reward


if __name__ == "__main__":
    random.seed(0)
    print("\nUsing Agent: Greedy\n")
    for level in ["easy", "medium", "hard"]:
        run_simulation(difficulty=level, verbose=True)
