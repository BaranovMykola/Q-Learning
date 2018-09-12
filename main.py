from game import game
from game import action
from game import object
from ml import qlearning
import numpy as np
import copy
import matplotlib.pyplot as plt
import cv2

up = action.action(name='Up', dy=-1)
down = action.action(name='Down', dy=1)
left = action.action(name='Left', dx=-1)
right = action.action(name='Right', dx=1)
actions = np.array([up, down, left, right])

def create_game():
    prize = object.object('Prize', 1000, color=(0, 255, 0), end=True)
    empty = object.object('Empty', -1000, color=(127, 127, 127))
    zombie = object.object('Zombie', -100, color=(0, 0, 255), end=True)


    grid = np.array(
        [
            [prize, empty],
            [zombie, empty]
        ])

    position = [1, 1]

    gameItem = game.game(grid=grid, position=position, actions=actions)

    return gameItem


def main():
    N_EPISODES = 100
    MAX_EPISODE_STEPS = 100
    MIN_ALPHA = 0.02

    gamma = 1.0
    eps = 0.2
    alphas = np.linspace(1.0, MIN_ALPHA, N_EPISODES)

    qItem = qlearning.Q(actions=actions, eps=eps)

    for i in range(N_EPISODES):
        total_reward = 0
        alpha = alphas[i]
        gameItem = create_game()
        state = gameItem.state()
        qItem.update_eps(alpha)
        for _ in range(MAX_EPISODE_STEPS):
            action = qItem.choose_action(state)
            last_state =  copy.deepcopy(state)
            reward, end = gameItem.act(action)
            total_reward += reward


            last_state_q = qItem.q(last_state, action)
            possible = qItem.q(gameItem.state())
            max_q = np.max( possible - last_state_q )
            updated_value = last_state_q + alpha * ( reward + gamma * max_q)

            action_id = np.where(actions == action)
            qItem.q(last_state)[action_id] = updated_value

            state = gameItem.state()

            if end:
                break

        print('Episode {0} ends. Reward: {1}'.format(i, total_reward))
    pass

if __name__ == '__main__':
    main()

