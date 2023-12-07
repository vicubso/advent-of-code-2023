# %% [markdown]
# # AoC 2023, day 1

# %% [markdown]
# ## Part 1

# %%
import re
N = 0
with open("input.txt") as f:
  for l in f:
    l = l.replace("\n","")
    a = re.findall("\d",l)
    n = int(a[0]+a[-1])
    N += n
print(N)

# %% [markdown]
# ## Part 2

# %%
import re

dic = { 
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8", 
    "nine": "9"
  }

regex = r"\d"
for key in dic.keys():
  regex += r"|"+key
# regex = r"\d|one|two|three|four|five|six|seven|eight|nine"

def replace(s):
  for key in dic.keys():
    if s==key:
      return dic[key]
  return s

def split(s):
    # Modify the pattern to use lookahead for overlapping matches
    modified_pattern = r'(?=(' + regex + r'))'
    # Find all matches using finditer
    matches = [m.group(1) for m in re.finditer(modified_pattern, s)]
    return matches

N = 0
with open("input.txt") as f:
  for l in f:
    a = split(l)
    a = [replace(x) for x in a]
    n = int(a[0]+a[-1])
    N += n
print(N)
