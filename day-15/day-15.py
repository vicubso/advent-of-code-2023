# %% [markdown]
# # AoC 2023, day 15

# %% [markdown]
# ## Part 1

# %%
filename = "input.txt"

with open(filename) as f:
    sequence = f.read().replace("\n", "").split(",")


# %%
def my_hash(s):
    x = 0
    for c in s:
        # Determine the ASCII value of the character
        x += ord(c)
        x *= 17
        x = x % 256
    return x


# %%
cum_sum = 0
for s in sequence:
    cum_sum += my_hash(s)

print(f"Part 1: {cum_sum}")

# %% [markdown]
# ## Part 2

# %%
boxes = [[] for i in range(256)]

for s in sequence:
    assert ("-" in s or "=" in s) and not ("-" in s and "=" in s)
    if "-" in s:
        operation = "-"
        label = s.split("-")[0].strip()
        box_id = my_hash(label)
        box = boxes[box_id]
        ids = [i for i in range(len(box)) if box[i][0] == label]
        if ids: box.pop(ids[0])

    elif "=" in s:
        operation = "="
        label = s.split("=")[0].strip()
        value = int(s.split("=")[1].strip())
        box_id = my_hash(label)
        box = boxes[box_id]
        ids = [i for i in range(len(box)) if box[i][0] == label]
        if ids: box[ids[0]][1] = value
        else: box.append([label, value])

# %%
sum_power = 0
for box_id, box in enumerate(boxes):
    for lense_id, lense in enumerate(box):
        power = (box_id + 1) * (lense_id + 1) * lense[1]
        sum_power += power

print(f"Part 2: {sum_power}")
