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
#   kernelspec:
#     display_name: science
#     language: python
#     name: python3
# ---

# %% [markdown]
# Part 1

# %%
import numpy as np
with open("input.txt") as f:
  input = f.readlines()

# %%
seeds = np.array(input[0].split()[1:], dtype="int")

# %%
seed_to_soil_map = np.array([x.split() for x in input[3:40]], dtype="int")
soil_to_fertilizer_map = np.array([x.split() for x in input[42:72]], dtype="int")
fertilizer_to_water_map = np.array([x.split() for x in input[74:113]], dtype="int")
water_to_light_map = np.array([x.split() for x in input[115:140]], dtype="int")
light_to_temperature_map = np.array([x.split() for x in input[142:159]], dtype="int")
temperature_to_humidity_map = np.array([x.split() for x in input[161:192]], dtype="int")
humidity_to_location_map = np.array([x.split() for x in input[194:237]], dtype="int")

maps = [
  seed_to_soil_map,
  soil_to_fertilizer_map,
  fertilizer_to_water_map,
  water_to_light_map,
  light_to_temperature_map,
  temperature_to_humidity_map,
  humidity_to_location_map
]
# Bit harcode-ish, but oh well...

# %%
def source_to_destination_one_map(source, map):
  for i in range(map.shape[0]):
    if source >= map[i,1] and source < map[i,1] + map[i,2]:
      return map[i,0] + source - map[i,1]
  return source

# %%
def source_to_destination_multiple_maps(source, maps):
  for map in maps:
    source = source_to_destination_one_map(source, map)
  return source

# %%
locations = [source_to_destination_multiple_maps(seed,maps) for seed in seeds]
min(locations)

# %% [markdown]
# Part 2

# %%
seed_ranges = seeds.reshape([-1,2])
seed_ranges.sort(0)
seed_ranges

# %%
#min_location = float("inf")
#for seed_range in seed_ranges:
#  for i in range(seed_range[1]):
#    seed = seed_range[0] + i
#    location = source_to_destination_multiple_maps(seed,maps)
#    if location < min_location:
#      min_location = location
#    print(f"searching range {seed_range}, i = {i}")
#    print(f"running minimum = {min_location}")
#    clear_output(wait=True)

#min_location
