#!/bin/bash
#SBATCH --job-name=hello-world
#SBATCH --output=hello-world.out
#SBATCH --error=hello-world.err
#SBATCH --ntasks=1
#SBATCH --time=00:01:00

echo "Hello, World!" > ~/workdir/hello-world.out
echo "This job ran on node: $(hostname)" >> /home/workdir/scripts/hello-world.out
