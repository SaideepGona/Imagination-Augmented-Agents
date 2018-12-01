'''
Authors: Kwanho Kim, Saideep Gona, Jinke Liu

This file reads in I2A minipacman training runs across varying rollout lengths and plots them superimposed
'''

import random
import matplotlib.pyplot as plt

Ns = ["1", "5", "10", "20"]
readin_files_loss = ["loss_output_{}_rush.txt".format(x) for x in Ns]
readin_files_reward = ["reward_output_{}_rush.txt".format(x) for x in Ns]

def random_noise_file(filename, n):
    with open(filename, "w") as out:
        rand_nums = [str(random.uniform(0,1)) for x in range(n)]
        out.write("\n".join(rand_nums))


def readin(filename):
    data = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            data.append(float(line.rstrip("\n")))
    return data


for n in Ns:    # Generate examples
    for x in ["loss", "reward"]:
        f_name = "{}_output_{}_rush.txt".format(x,n)
        random_noise_file(f_name, 5)


colors = ["blue","green","orange","red"]

plt.figure(1)   # Loss
for ind in range(len(readin_files_loss)):
    l_data = readin(readin_files_loss[ind])
    plt.plot(range(len(l_data)), l_data, color=colors[ind], label="N="+Ns[ind])
    plt.title("I2A Minipacman Training Loss Over Time for Varying Rollout Lengths")
plt.legend()
plt.savefig('loss_rush_{}_{}_{}_{}.png'.format(*Ns))



plt.figure(2)   # Reward
for ind in range(len(readin_files_reward)):
    r_data = readin(readin_files_reward[ind])
    plt.plot(range(len(r_data)), r_data, color=colors[ind], label="N="+Ns[ind])
    plt.title("I2A Minipacman Training Reward Over Time for Varying Rollout Lengths")
plt.legend()
plt.savefig('reward_rush_{}_{}_{}_{}.png'.format(*Ns))