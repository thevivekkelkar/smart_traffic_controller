"""
grader.py
---------
Evaluates an agent on all three difficulty levels.
Returns a score between 0.0 and 1.0.
"""

import random
from tasks import get_task


def run_episode(env, agent_fn):
    """
    Run one full episode using agent_fn to pick actions.

    Parameters
    ----------
    env      : TrafficEnvironment instance
    agent_fn : callable(state) -> action (int 0-3)

    Returns
    -------
    total_reward : float
    """
    state = env.reset()
    total_reward = 0
    done = False

    while not done:
        action = agent_fn(state)
        state, reward, done = env.step(action)
        total_reward += reward

    return total_reward


def normalize_score(reward, max_steps=50, max_cars=30, num_lanes=4):
    """
    Convert a raw total reward into a 0–1 score.

    Worst case : every lane full every step → reward = -(max_cars * num_lanes * max_steps)
    Best case  : no cars waiting            → reward = 0
    """
    worst = -(max_cars * num_lanes * max_steps)
    score = (reward - worst) / (0 - worst)        # linear normalisation
    return round(max(0.0, min(1.0, score)), 4)     # clamp to [0, 1]


def grade(agent_fn, episodes_per_task=5, seed=42):
    """
    Evaluate agent_fn on easy, medium, and hard tasks.

    Parameters
    ----------
    agent_fn         : callable(state) -> int
    episodes_per_task: how many episodes to average per difficulty
    seed             : random seed for reproducibility

    Returns
    -------
    dict with per-task scores and overall score (0–1)
    """
    random.seed(seed)

    difficulties  = ["easy", "medium", "hard"]
    task_scores   = {}

    for diff in difficulties:
        env     = get_task(diff)
        rewards = [run_episode(env, agent_fn) for _ in range(episodes_per_task)]
        avg_reward           = sum(rewards) / len(rewards)
        task_scores[diff]    = normalize_score(avg_reward)

    overall = round(sum(task_scores.values()) / len(task_scores), 4)
    task_scores["overall"] = overall
    return task_scores


# ── Run grader directly ──────────────────────────────────────
if __name__ == "__main__":
    def random_agent(state):
        return random.randint(0, 3)

    def greedy_agent(state):
        return state.index(max(state))   # always serve busiest lane

    print("=== Grading: Random Agent ===")
    scores = grade(random_agent)
    for k, v in scores.items():
        print(f"  {k:<8}: {v:.4f}")

    print("\n=== Grading: Greedy Agent ===")
    scores = grade(greedy_agent)
    for k, v in scores.items():
        print(f"  {k:<8}: {v:.4f}")
