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
# # AoC 2023, day 9

# %% [markdown]
# ## Part 1

# %%
import numpy as np


# %%
def part_1(filename="input.txt"):
    input = np.loadtxt(filename, dtype=int)
    predictions = []
    for arr in input:
        last_values = [arr[-1]]
        diffs = np.diff(arr)
        while np.sum(np.abs(diffs)) > 0:
            last_values.append(diffs[-1])
            diffs = np.diff(diffs)
        last_last_values = np.zeros(len(last_values), dtype=int)
        last_last_values[-1] = last_values[-1]
        for i in range(len(last_values)-2, -1, -1):
            last_last_values[i] = last_values[i] + last_last_values[i+1]
        predictions.append(last_last_values[0])
    return sum(predictions)

print(f"The answer to part 1 is {part_1()}")


# %% [markdown]
# ## Part 2

# %%
def part_2(filename="input.txt"):
    input = np.loadtxt(filename, dtype=int)
    predictions = []
    for arr in input:
        first_values = [arr[0]]
        diffs = np.diff(arr)
        while np.sum(np.abs(diffs)) > 0:
            first_values.append(diffs[0])
            diffs = np.diff(diffs)
        last_last_values = np.zeros(len(first_values), dtype=int)
        last_last_values[-1] = first_values[-1]
        for i in range(len(first_values)-2, -1, -1):
            last_last_values[i] = first_values[i] - last_last_values[i+1]
        predictions.append(last_last_values[0])
    return sum(predictions)

print(f"The answer to part 2 is {part_2()}")
