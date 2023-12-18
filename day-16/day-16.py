# %% [markdown]
# # AoC 2023, day 16

# %% [markdown]
# ## Part 1

# %%
import itertools
from IPython.display import clear_output
import time
import copy

# %%
filename = "input.txt"

with open(filename) as f:
    grid = [list(x) for x in f.read().splitlines()]


# %%
def trace_light(grid, start, direction):
    M, N = len(grid), len(grid[0])
    x, y = start
    dx, dy = direction
    seen = []
    active = [[x,y,dx,dy]]
    energized = []
    while active:
        active_ = []
        for k, [x, y, dx, dy] in enumerate(active):
            if x < 0 or x >= M or y < 0 or y >= N:
                continue
            if [x, y, dx, dy] in seen:
                continue
            seen.append([x, y, dx, dy])
            if grid[x][y] == ".":
                active_.append([x+dx, y+dy, dx, dy])
            elif grid[x][y] == "\\":
                active_.append([x+dy, y+dx, dy, dx])
                energized.append([x,y])
            elif grid[x][y] == "/":
                active_.append([x-dy, y-dx, -dy, -dx])
                energized.append([x,y])
            elif grid[x][y] == "-" and dx == 0:
                active_.append([x+dx, y+dy, dx, dy]) 
            elif grid[x][y] == "-": 
                active_.append([x, y-1, 0, -1]) 
                active_.append([x, y+1, 0, +1]) 
                energized.append([x,y])
            elif grid[x][y] == "|" and dy == 0:
                active_.append([x+dx, y+dy, dx, dy])
            elif grid[x][y] == "|":
                active_.append([x-1, y, -1, 0]) 
                active_.append([x+1, y, +1, 0])
                energized.append([x,y])
        # Remove out of bounds
        active_ = [x for x in active_ if 0 <= x[0] and x[0] < M and 0 <= x[1] and x[1] < N]
        active = active_

        # Visuals
        # grid_ = copy.deepcopy(grid)
        # for x, y, dx, dy in active:
        #     grid_[x][y] = "#"
        # # print("Active")
        # # print(active)
        # # print("Grid_")
        # print("\n".join("".join(x) for x in grid_))
        # # input("Press any key to continue...")
        # time.sleep(0.2)
        # clear_output(wait=True)
    
    energized = len(set([(x,y) for x, y, _, _ in seen]))

    return energized

energized = trace_light(grid, [0,0], [0,1])

print(f"Part 1: {energized}")

# %% [markdown]
# ## Part 2

# %%
running_max = 0
M = len(grid)
N = len(grid[0])

ids = list(itertools.product(range(M), [0])) # East edge
ids += list(itertools.product(range(M), [N-1])) # West edge
ids += list(itertools.product([0], range(N))) # North edge
ids += list(itertools.product([M-1], range(N))) # South edge

for i, j in ids:
    clear_output(wait=True)
    print(f"Id: {i,j}/{M,N}")
    print(f"Runnig max: {running_max}")
    directions = []
    if j == 0: directions.append([0,1]) # East
    if j == N-1: directions.append([0,-1]) # West
    if i == 0: directions.append([1,0]) # North
    if i == M-1: directions.append([-1,0]) # South
    for di, dj in directions:
        energized = trace_light(grid, [i,j], [di,dj])
        running_max = max(running_max, energized)

print(f"Part 2: {running_max}")
