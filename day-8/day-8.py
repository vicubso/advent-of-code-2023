# %% [markdown]
# # AoC 2023, day 8

# %% [markdown]
# ## Part 1

# %%
import re

# Read and process input file
map_dict = {}
with open("input.txt", "r") as file:
    input_lines = file.read().splitlines()
    instructions = input_lines[0]
    for line in input_lines[2:]:
        arr = re.sub(r"[\(\)=,]", "", line).strip().split()
        map_dict[arr[0]] = arr[1:]

# %%
# Part 1: Navigate through the map
position = "AAA"
step = 0
instruction_length = len(instructions)
direction_map = {"L": 0, "R": 1}

while position != "ZZZ":
    position = map_dict[position][direction_map[instructions[step % instruction_length]]]
    step += 1

step

# %% [markdown]
# ## Part 2

# %%
import numpy as np

with open("input.txt") as file:
    lines = file.read().strip().split("\n")
path_directions = lines[0]
node_map = {node: (left, right) for node, left, right in (re.findall(r"[A-Z]{3}", line) for line in lines[2:])}


# %%
def follow_node(start, end):
    counter = 0
    while not start[-1] == end[-1]:
        direction = 0 if path_directions[counter % len(path_directions)] == "L" else 1
        start = node_map[start][direction]
        counter += 1
    return counter


initial = [node for node in node_map if node[-1]=="A"]


np.lcm.reduce([follow_node(node, 'ZZZ') for node in initial])
