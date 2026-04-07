import random
from traffic_env import TrafficEnvironment

def greedy_agent(state):
    return state.index(max(state))

def run():
    env = TrafficEnvironment()
    state = env.reset()
    print("Using Greedy Baseline Agent")
    print("[START] task=traffic env=traffic model=baseline")

    step = 0
    rewards = []

    done = False
    while not done:
        action = greedy_agent(state)
        next_state, reward, done = env.step(action)

        step += 1
        rewards.append(reward)

        print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null")

        state = env.state()

    max_cars = 30
    num_lanes = 4
    max_steps = 50

    worst = -(max_cars * num_lanes * max_steps)
    score = (sum(rewards) - worst) / (0 - worst)
    score = max(0.0, min(1.0, score))

    print(f"[END] success=true steps={step} score={score:.2f} rewards={','.join([f'{r:.2f}' for r in rewards])}")

if __name__ == "__main__":
    run()