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

# %%
filename = "input.txt"

def part_2(filename):
    with open(filename) as f:
        symbols = ''.join(set(re.findall(r"[^0-9\n.]", f.read())))

    with open("input.txt") as f:
        matrix =  np.array([list(x) for x in f.read().splitlines()])
    # include a frame of "." around the matrix
    matrix = np.pad(matrix, 1, 'constant', constant_values=".")

    def get_current_word(matrix, i, j):
        # Get the word (made of digits) that overlaps with the current position
        if not re.findall(f"\d", matrix[i][j]): # If the current position is not a digit
            return ''
        j_start = j
        j_end = j
        while re.findall(r"\d", matrix[i][j_start-1]):
            j_start -= 1
        while re.findall(r"\d", matrix[i][j_end+1]):
            j_end += 1
        current_word = ''.join(matrix[i][j_start:j_end+1])
        current_word = current_word + f"-{i},{j_start}" # Append i,j_start to make the word unique 
        return current_word

    m = matrix.shape[0]
    n = matrix.shape[1]
    cum_sum = 0
    for i in range(1,m-1):
        for j in range(1,n-1):
            if matrix[i][j] == "*":
                adjacent_indices = np.array([[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1,-1], [1,0], [1,1]]) + [i,j]
                adjacent_words = list(set([get_current_word(matrix, x[0], x[1]) for x in adjacent_indices]) - {''})
                if len(adjacent_words) == 2:
                    adjacent_words = [int(x.split("-")[0]) for x in adjacent_words] # Remove the i,j_start part
                    print(f"{i},{j}: {adjacent_words}")
                    cum_sum += np.prod(adjacent_words)

    return cum_sum

print(f"The answer to part 2 is {part_2('input.txt')}")
