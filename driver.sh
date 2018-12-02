#!/usr/bin/env bash

set -e

rollout_steps="1, 5, 10, 20"

script=imagination-augmented_agent.py

for rs in ${rollout_steps}
do
    python ${script} rs
done
