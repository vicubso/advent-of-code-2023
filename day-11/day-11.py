# %% [markdown]
# # AoC 2023, day 11

# %% [markdown]
# ## Part 1

# %%
import numpy as np
import itertools

# %%
with open ('input.txt') as f:
    universe = [list(x) for x in f.read().splitlines()]

universe = np.array(universe)

# %%
# Find the galaxies
M, N = universe.shape
double_rows = np.array([i for i in range(M) if not "#" in universe[i,:]])
galaxies = []
for i,j in itertools.product(range(M), range(N)):
    if universe[i,j] != ".":
        galaxies.append([i,j])

# %%
# Find columns and rows with no galaxies
double_rows = np.array([i for i in range(M) if not "#" in universe[i,:]])
double_cols = np.array([i for i in range(N) if not "#" in universe[:,i]])

# %% [markdown]
# WLOG $i_0\le i_1$, $j_0\le j_1$
#
# The shortest distance between $(i_0,j_0)$ and $(i_1,j_1)$ is just $$i_0-i_1 + j_0-j_1$$
#
# However, if any element of ```duplicate_rows``` falls within the interval $]i_0,i_1[$, we need to duplicate its contribution to the distance.
#
# Similarly if any element of ```duplicate_cols``` falls within the interval $]j_0,j_1[$.
#
#

# %%
sum_length = 0
K = len(galaxies)
for k0 in range(K):
    for k1 in range(k0+1,K):
        i0,j0 = galaxies[k0]
        i1,j1 = galaxies[k1]
        l = np.abs(i0-i1) + np.abs(j0-j1)
        l += len(np.where((double_rows>min(i0,i1)) & (double_rows<max(i0,i1)))[0])
        l += len(np.where((double_cols>min(j0,j1)) & (double_cols<max(j0,j1)))[0])
        sum_length += l
sum_length

# %% [markdown]
# ## Part 2

# %% [markdown]
# Now instead of duplicating, we add them 999999 times (1 million - 1)

# %%
sum_length = 0
K = len(galaxies)
for k0 in range(K):
    for k1 in range(k0+1,K):
        i0,j0 = galaxies[k0]
        i1,j1 = galaxies[k1]
        l = np.abs(i0-i1) + np.abs(j0-j1)
        l += 999999*len(np.where((double_rows>min(i0,i1)) & (double_rows<max(i0,i1)))[0])
        l += 999999*len(np.where((double_cols>min(j0,j1)) & (double_cols<max(j0,j1)))[0])
        sum_length += l
sum_length
