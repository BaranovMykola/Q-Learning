from game import game
from game import action
from game import object
import numpy as np
import matplotlib.pyplot as plt
import cv2

def main():
    prize = object.object('Prize', 1000, color=(0, 255, 0), end=True)
    empty = object.object('Empty', -1, color=(127, 127, 127))
    zombie = object.object('Zombie', -100, color=(0, 0, 255), end=True)

    up = action.action(name='Up', dy=-1)
    down = action.action(name='Down', dy=1)
    left = action.action(name='Left', dx=-1)
    right = action.action(name='Right', dx=1)

    grid = np.array(
        [
            [ prize, empty ],
            [ zombie, empty]
        ])

    position = [1,1]
    actions = np.array([up, down, left, right])


    gameItem =  game.game(grid=grid, position=position, actions=actions)
    gameItem.draw_and_show()

    reward, done = gameItem.act(up)
    reward, done = gameItem.act(left)

    gameItem.draw_and_show()

if __name__ == '__main__':
    main()

