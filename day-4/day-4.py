# %% [markdown]
# # AoC 2023, day 4

# %% [markdown]
# ## Part 1

# %%
input = []
prize = 0

with open("input.txt", "r") as f:
  for l in f:
    input.append(l)

for l in input:
    winners = set([int(x) for x in l[10:39].split()])
    owned = set([int(x) for x in l[42:-1].split()])
    winning_numbers = winners.intersection(owned)
    N = len(winning_numbers)
    if N>0: prize += 2**(N-1)

prize

# %% [markdown]
# # Part 2

# %%
import numpy as np
id
winners = []
owned = []
matches = []
with open("input.txt", "r") as f:
  k=1
  for l in f:
    k+=1
    winners.append([int(x) for x in l[10:39].split()])
    owned.append([int(x) for x in l[42:-1].split()])

N = len(winners)
count = np.ones(N)

for i in range(N):
  matches.append(len(set(winners[i]).intersection(set(owned[i]))))

for i in range(N):
  j = min(i+matches[i]+1,N)
  count[i+1:j] += count[i]

int(sum(count))
