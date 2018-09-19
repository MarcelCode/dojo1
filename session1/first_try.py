import numpy as np
import matplotlib.pyplot as plt


def move(start, move_string):
    cur_pos = start
    for element in move_string:
        step, direction, blocks = element.split("_")
        if direction == "n":
            plt.plot([cur_pos[0], cur_pos[0]], [cur_pos[1], cur_pos[1] - int(step) * int(blocks)], 'r-o')
            cur_pos = (cur_pos[0], cur_pos[1] - int(step) * int(blocks))
        elif direction == "e":
            plt.plot([cur_pos[0], cur_pos[0] + int(step) * int(blocks)], [cur_pos[1], cur_pos[1]], 'r-o')
            cur_pos = (cur_pos[0] + int(step) * int(blocks), cur_pos[1])
        elif direction == "s":
            plt.plot([cur_pos[0], cur_pos[0]], [cur_pos[1], cur_pos[1] + int(step) * int(blocks)], 'r-o')
            cur_pos = (cur_pos[0], cur_pos[1] + int(step) * int(blocks))
        elif direction == "w":
            plt.plot([cur_pos[0], cur_pos[0] - int(step) * int(blocks)], [cur_pos[1], cur_pos[1]], 'r-o')
            cur_pos = (cur_pos[0] - int(step) * int(blocks), cur_pos[1])
        elif direction == "ne":
            plt.plot([cur_pos[0], cur_pos[0] + int(step) * int(blocks)],
                     [cur_pos[1], cur_pos[1] - int(step) * int(blocks)], 'r-o')
            cur_pos = (cur_pos[0] + int(step) * int(blocks), cur_pos[1] - int(step) * int(blocks))
        elif direction == "se":
            plt.plot([cur_pos[0], cur_pos[0] + int(step) * int(blocks)],
                     [cur_pos[1], cur_pos[1] + int(step) * int(blocks)], 'r-o')
            cur_pos = (cur_pos[0] + int(step) * int(blocks), cur_pos[1] + int(step) * int(blocks))
        elif direction == "sw":
            plt.plot([cur_pos[0], cur_pos[0] - int(step) * int(blocks)],
                     [cur_pos[1], cur_pos[1] + int(step) * int(blocks)], 'r-o')
            cur_pos = (cur_pos[0] - int(step) * int(blocks), cur_pos[1] + int(step) * int(blocks))
        elif direction == "nw":
            plt.plot([cur_pos[0], cur_pos[0] - int(step) * int(blocks)],
                     [cur_pos[1], cur_pos[1] - int(step) * int(blocks)], 'r-o')
            cur_pos = (cur_pos[0] - int(step) * int(blocks), cur_pos[1] - int(step) * int(blocks))


# create window
window = np.zeros((40, 20))

# goal
window[9, 12] = 3

# Start
window[36, 10] = 2

# blocks
window[13, 10:15] = 1
window[16, :11] = 1
window[16, 14:] = 1
np.savetxt(r"C:\Users\Marcel\PycharmProjects\untitled5\session1\test.txt", window, fmt="%d")

plt.imshow(window, cmap="seismic")
# Robot movement
start = [10, 36]
movement_string = ["6_n_3", "1_e_3", "1_n_3", "1_e_3", "2_n_3", "1_w_3", "1_w_1", "1_ne_3"]
move(start, movement_string)

plt.show()
