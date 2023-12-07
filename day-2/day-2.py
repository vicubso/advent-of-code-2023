# %% [markdown]
# # AoC 2023, day 2

# %% [markdown]
# ## Part 1

# %%
import numpy as np

# %%
ids = []
games = []
with open("input.txt", "r") as f:
    for line in f:
        id = int(line.split(" ")[1].replace(":", ""))
        ids.append(id)
        game = []
        for s in line.replace(" ","0").split(":")[1].split(";"):
            r = s.find("red")
            g = s.find("green")
            b = s.find("blue")
            subgame = [int(s[r-3:r-1]) if r!=-1 else 0,
                        int(s[g-3:g-1]) if g!=-1 else 0,
                        int(s[b-3:b-1]) if b!=-1 else 0]
            game.append(subgame)
        games.append(game)
ids = np.array(ids, dtype="int")

# %%
N = len(ids)
feasibles = np.ones(N, dtype="int")
for i in range(N):
    game = games[i]
    for subgame in game:
        if subgame[0] > 12 or subgame[1] > 13 or subgame[2] > 14:
            feasibles[i] = 0

print(f"Answer to part 1: {np.dot(feasibles, ids)}")

# %% [markdown]
# ## Part 2

# %%
x = 0
for game in games:
    x += np.prod(np.max(game, axis=0))

print(f"Answer to part 2: {x}")