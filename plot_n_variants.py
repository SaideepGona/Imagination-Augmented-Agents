'''
Authors: Kwanho Kim, Saideep Gona, Jinke Liu

This file reads in I2A minipacman training runs across varying rollout lengths and plots them superimposed
'''

import random
import matplotlib.pyplot as plt
import os

Ns = ["a2c", "1", "2", "3", "4", "5"]
pwd = os.getcwd()
readin_files_loss = [pwd+"/data/regular/loss_output_{}_regular.txt".format(x) for x in Ns]
readin_files_reward = [pwd+"/data/regular/reward_output_{}_regular.txt".format(x) for x in Ns]

smoothing = 0.9

def readin(filename):
    data = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            data.append(float(line.rstrip("\n")))
    return data

def smooth(scalars, weight):  # Weight between 0 and 1
    last = scalars[0]  # First value in the plot (first timestep)
    smoothed = list()
    for point in scalars:
        smoothed_val = last * weight + (1 - weight) * point  # Calculate smoothed value
        smoothed.append(smoothed_val)                        # Save it
        last = smoothed_val                                  # Anchor the last smoothed value

    return smoothed

colors = ["purple","blue","red","orange","green", "grey"]

plt.figure(1)   # Loss
for ind in range(len(readin_files_loss)):
    print(ind)
    print(readin_files_loss[ind])
    l_data = readin(readin_files_loss[ind])
    print(l_data)
    a = 0.2
    if ind == 1:
        a = 1
    plt.plot(range(len(l_data)), smooth(l_data,smoothing), color=colors[ind], label="N="+Ns[ind])
plt.title("I2A Minipacman Training Loss Over Time for Varying Rollout Lengths")
plt.xlabel("Number of training iterations (1e2)")
plt.ylabel("Total accumulated reward")
plt.legend()
plt.savefig('loss_regular_{}_{}_{}_{}_{}.png'.format(*Ns))

plt.figure(2)   # Reward
for ind in range(len(readin_files_reward)):
    r_data = readin(readin_files_reward[ind])
    a = 0.2
    if ind == 1:
        a = 1
    plt.plot(range(len(r_data)), smooth(r_data,smoothing), color=colors[ind], label="N="+Ns[ind])
plt.title("I2A Minipacman Training Reward Over Time for Varying Rollout Lengths")
plt.xlabel("Number of training iterations (1e2)")
plt.ylabel("Total accumulated reward")
plt.legend()
plt.savefig('reward_regular_{}_{}_{}_{}_{}.png'.format(*Ns))