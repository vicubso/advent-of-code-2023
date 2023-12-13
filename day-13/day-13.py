# %% [markdown]
# # AoC 2023, day 13

# %% [markdown]
# ## Part 1

# %%
import numpy as np
import re
import itertools
from IPython.display import clear_output

# %%
with open("input.txt") as f:
    tables = [np.array([list(y) for y in x.splitlines()], dtype=int) for x in re.sub(r"\.","0",re.sub(r"#","1",f.read())).split("\n\n")]


# %%
def is_horizontal_mirror(table, x):
    # Check whether there is a vertical mirror exactly below row x
    n = table.shape[0]
    if x < 0 or x >= n-1: return False
    k = 0
    while x-k >= 0 and x+k+1 < n:
        if np.any(table[x-k,:] != table[x+k+1,:]): return False
        k += 1
    return True

def is_vertical_mirror(table, x):
    # Check whether there is a horizontal mirror exactly to the right of column x
    return is_horizontal_mirror(table.T, x)


# %%
cum_sum = 0
for table in tables.copy():
    table = np.array(table)
    m, n = table.shape
    for i in range(m):
        if is_horizontal_mirror(table, i): cum_sum += (i+1)*100
    for i in range(n):
        if is_vertical_mirror(table, i): cum_sum += i+1

print(f"Answer to part 1: {cum_sum}")


# %% [markdown]
# ## Part 2

# %%
def find_mirrors(table):
    # Find all mirror in the table (horizontal or vertical)
    m, n = table.shape
    mirrors = []
    for i in range(m):
        if is_horizontal_mirror(table, i):
            mirrors.append((i, "horizontal"))
            continue
    for i in range(n):
        if is_vertical_mirror(table, i):
            mirrors.append((i, "vertical"))
            continue
    return mirrors


# %%
cum_sum = 0
k = 0
for table in tables:
    table = np.array(table)
    m, n = table.shape
    mirrors = find_mirrors(table)
    for i, j in itertools.product(range(m), range(n)):
        table_ = table.copy()
        table_[i,j] = 1 - table_[i,j]
        mirrors_ = find_mirrors(table_)
        new_mirrors = list(set(mirrors_) - set(mirrors))
        if new_mirrors != []:
            mirror = new_mirrors[0][0]
            type = new_mirrors[0][1]
            cum_sum += (mirror+1) * (100 if type == "horizontal" else 1)
            break
    k += 1

print(f"Answer to part 2: {cum_sum}")

