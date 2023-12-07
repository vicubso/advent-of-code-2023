# %% [markdown]
# # AoC 2023, day 3

# %% [markdown]
# ## Part 1

# %%
import re
import numpy as np


# %%
def part_1(filename):
    # Find all symbols that are not numbers, newlines or dots. Ignore repetitions
    with open(filename) as f:
        symbols = ''.join(set(re.findall(r"[^0-9\n.]", f.read())))

    # Read the input as a matrix, an replace all symbols with "*"
    with open("input.txt") as f:
        matrix =  np.array([list(x) for x in re.sub(r"[{}]+".format(re.escape(symbols)), "*", f.read()).splitlines()])
    # include a frame of "." around the matrix
    matrix = np.pad(matrix, 1, 'constant', constant_values=".")

    # Find the positions of all "*" symbols
    locations = np.argwhere(matrix == "*")

    # Create a matrix with ones at the 8 positions around each "*", zeros elsewhere
    ones_zeros = np.zeros_like(matrix, dtype=int)
    for loc in locations:
        row, col = loc
        ones_zeros[row-1:row+2, col-1:col+2] = 1

    # Find all the numbers in matrix that overlap with at least one 1 in ones_zeros
    cum_sum = 0
    m = matrix.shape[0]
    n = matrix.shape[1]
    for i in range(m):
        row = matrix[i]
        j = 0
        while j < n:
            current_idx = np.array([], dtype=int)
            while row[j] != "*" and row[j] != "." and i < n:
                current_idx = np.append(current_idx, j)
                j += 1
            current_word = ''.join(row[current_idx])
            if 1 in ones_zeros[i][current_idx]:
                cum_sum += int(current_word)
            j += 1
    
    return cum_sum


# %%
print(f"The answer to part 1 is {part_1('input.txt')}")

# %% [markdown]
# ## Part 2
