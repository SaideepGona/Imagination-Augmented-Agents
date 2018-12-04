'''
Authors: Kwanho Kim, Saideep Gona, Jinke Liu

This file reads in I2A minipacman training runs across varying rollout lengths and plots them superimposed
'''

import random
import matplotlib.pyplot as plt

Ns = ["1", "2", "3", "4", "5"]
readin_files_loss = ["data/regular/loss_output_{}_regular.txt".format(x) for x in Ns]
readin_files_reward = ["data/regular/reward_output_{}_regular.txt".format(x) for x in Ns]


def readin(filename):
    data = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            data.append(float(line.rstrip("\n")))


colors = ["blue","red","orange","green", "grey"]

plt.figure(1)   # Loss
for ind in range(len(readin_files_loss)):
    l_data = readin(readin_files_loss[ind])
    a = 0.2
    if ind == 1:
        a = 1
    plt.plot(range(len(l_data)), l_data, color=colors[ind], label="N="+Ns[ind], alpha=a)
    plt.title("I2A Minipacman Training Loss Over Time for Varying Rollout Lengths")
plt.legend()
plt.savefig('loss_regular_{}_{}_{}_{}.png'.format(*Ns))

plt.figure(2)   # Reward
for ind in range(len(readin_files_reward)):
    r_data = readin(readin_files_reward[ind])
    a = 0.2
    if ind == 1:
        a = 1
    plt.plot(range(len(r_data)), r_data, color=colors[ind], label="N="+Ns[ind], alpha=a)
    plt.title("I2A Minipacman Training Reward Over Time for Varying Rollout Lengths")
plt.legend()
plt.savefig('reward_regular_{}_{}_{}_{}.png'.format(*Ns))