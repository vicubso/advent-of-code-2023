# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: aoc-2023
#     language: python
#     name: python3
# ---

# %% [markdown]
# # AoC 2023, day 12

# %% [markdown]
# ## Part 1

# %% [markdown]
# Brute force! :D

# %%
import re
import itertools

# %%
springs = []
numbers = []
with open('input.txt') as f:
    for line in f:
        line = line.strip().split(" ")
        springs.append(line[0])
        numbers.append([int(x) for x in line[1].split(",")])


# %%
sum = 0

for i in range(len(springs)):
    # Replace every ? with either # or .
    unknowns_id = [m.start() for m in re.finditer(r"\?", springs[i])] # Indexes of ?'s
    for x in itertools.product(["#", "."], repeat=len(unknowns_id)):
        v = list(springs[i])
        for j in range(len(x)): v[unknowns_id[j]] = x[j]
        v = "".join(v)
        # If the variation satisfies the grouping, add 1 to the sum
        if [len(x) for x in re.findall(r"#+", v)] == numbers[i]:
            sum += 1
    
print(f"Answer to part 1: {sum}")

# %% [markdown]
# ## Part 2

# %% [markdown]
# Obviously brute force won't cut it here... working in it...
