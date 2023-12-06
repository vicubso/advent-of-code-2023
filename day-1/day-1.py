# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
# ---

# %% [markdown]
# Part 1

# %%
import re
N = 0
with open("input.txt") as f:
  for l in f:
    a = re.findall("\d",l)
    n = int(a[0]+a[-1])
    N += n
N

# %% [markdown]
# Part 2

# %%
import re

dic = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5",
       "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def replace(s):
  for key in dic.keys():
    if s==key:
      return dic[key]
  return s


# %%
N = 0
with open("input.txt") as f:
  for l in f:
    a = re.findall("\d|one|two|three|four|five|six|seven|eight|nine",l)
    a = [replace(x) for x in a]
    n = int(a[0]+a[-1])
    N += n
N
