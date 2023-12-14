# %% [markdown]
# # AoC 2023, day 14

# %% [markdown]
# ## Part 1

# %%
import itertools
from IPython.display import clear_output

# %%
with open('input.txt') as f:
    platform = [list(x) for x in f.read().splitlines()]


# %%
def compute_load(platform):
    load = 0
    M, N = len(platform), len(platform[0])
    for i, j in itertools.product(range(M), range(N)):
        if platform[i][j] == 'O':
            load += M-i
    return load


# %%
def tilt_platform_north(platform):
    M, N = len(platform), len(platform[0])
    for k in range(M-1):
        for i, j in itertools.product(range(M-1), range(N)):
            if platform[i][j] == "." and platform[i+1][j] == "O":
                platform[i][j], platform[i+1][j] = "O", "."
    return platform


# %%
ans = compute_load(tilt_platform_north(platform))
print("Answer to part 1:", ans)


# %% [markdown]
# ## Part 2

# %%
def rotate(A, K=1):
    # Rotate matrix A 90 degrees clockwise k times
    for _ in range(K):
        A = list(zip(*A[::-1]))
    return [list(x) for x in A]


# %%
def tilt_platform(platform, direction="north"):
    if direction=="north":   return tilt_platform_north(platform)
    elif direction=="east":  return rotate(tilt_platform_north(rotate(platform,3)),1)
    elif direction=="south": return rotate(tilt_platform_north(rotate(platform,2)),2)
    elif direction=="west":  return rotate(tilt_platform_north(rotate(platform,1)),3)

def perform_cycle(platform):
    for d in ["north", "west", "south",  "east"]:
        platform = tilt_platform(platform, d)
    return platform


# %%
def flatten(platform):
    return "\n".join(["".join(x) for x in platform])

def unflatten(s):
    return [list(x) for x in s.splitlines()]


# %%
# seen = [''.join([''.join(x) for x in platform])]
seen = [flatten(platform)]
K = 1000000000
print("Looking for cycle...")
for k in range(K):
    seen.append(flatten(perform_cycle(unflatten(seen[-1]))))
    if seen[-1] in seen[:-1]:
        print("Cycle found!")
        break

# %%
for k, s in enumerate(seen):
    if s == seen[-1]:
        break

final_id = k + (K-k)%(len(seen)-1-k)
final_platform = unflatten(seen[final_id]) 

print(f"Answer to part 2: {compute_load(final_platform)}")
