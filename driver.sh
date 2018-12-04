#!/usr/bin/env bash

set -e

rollout_steps="2 4"
mode=regular

script=imagination-augmented_agent.py

for rs in ${rollout_steps}
do

    { time python ${script} ${rs} ; } 2> ${mode}_time_N_${rs}.log
done
