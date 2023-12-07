# %% [markdown]
# # AoC 2023, day 7

# %%
from collections import Counter
import functools
import numpy as np
import itertools


# %% [markdown]
# ## Part 1

# %%
class Part_1:
    def __init__(self, filename):
        self.filename = filename

    def hand_type(self, h):
        counter = Counter(h) # Returns a dictionary where the key is the card and the value is the number of times it appears
        if 5 in counter.values(): # If there are 5 of the same card
            return 7 # Five of a kind
        elif 4 in counter.values(): # If there are 4 of the same card
            return 6 # Four of a kind
        elif 3 in counter.values() and 2 in counter.values(): # If there is a trio and a pair 
            return 5 # Full house
        elif 3 in counter.values() and len(counter.values()) == 3: # If there is a trio and two other different cards
            return 4 # Three of a kind
        elif 2 in counter.values() and len(counter.values()) == 3: # If there are two pairs and one other card
            return 3 # Two pair
        elif 2 in counter.values() and len(counter.values()) == 4: # If there is one pair and three other different cards
            return 2 # One pair
        else: # All cards are different
            return 1 # High card

    def compare_lexicographically(self, h0, h1):
        order = {"2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "T":9, "J":10, "Q":11, "K":12, "A":13}
        for x in range(len(h0)):
            if order[h0[x]] < order[h1[x]]:
                return -1
            elif order[h0[x]] > order[h1[x]]:
                return 1
        return 0 # If both hands are the same

    def compare_hands(self, h0, h1):
        if h0 == h1:
            return 0 # if both hands are the same
        t0 = self.hand_type(h0)
        t1 = self.hand_type(h1)
        if t0 < t1:
            return -1
        elif t0 > t1:
            return 1
        else: # if both hands have the same type, compare lexicographically
            return self.compare_lexicographically(h0, h1)

    def load_input(self):
        with open(self.filename, "r") as f:
            input = f.read().splitlines()
            N = len(input)
            hands = [""]*N
            bids = np.zeros(N, dtype="int")
            for n in range(N):
                line = input[n].split()
                hands[n] = line[0]
                bids[n] = int(line[1])
        return hands, bids, N

    def sort(self):
        # Sort hands according to custom comparator self.compare_hands(h0, h1)
        hands, bids, N = self.load_input()
        key = functools.cmp_to_key(lambda i, j: self.compare_hands(hands[i], hands[j]))
        sorted_indices = sorted(list(range(N)), key=key)
        sorted_hands = [hands[i] for i in sorted_indices]
        sorted_bids = [bids[i] for i in sorted_indices]
        return sorted_hands, sorted_bids, N

    def solve(self): 
        sorted_hands, sorted_bids, N = self.sort()
        return np.dot(sorted_bids, np.arange(1, N+1))


# %%
part_1 = Part_1("input.txt")
print(f"Answer to part 1: {part_1.solve()}")


# %% [markdown]
# ## Part 2

# %% [markdown]
# For this part, we just need to do a couple of modifications:
#
# ```card_type()``` should consider J as every possible card, and choose the possibility that gives the highest type
#
# ```compare_lexicographically(h0, h1)``` needs to include the modified dictionary where J takes the lowest value
#

# %%
class Part_2(Part_1):
    def __init__(self, filename):
        super().__init__(filename)
        self.hand_type_no_jokers = super().hand_type

    def substitute_jacks(self, h):
        # If a hand contains jacks, replace them with every possible card, and return a list of hands
        # E.g., "J9J3A" -> ["2923A", "3923A", ... , "A9A3A"]
        jacks = [i for i, x in enumerate(h) if x == "J"]
        n_jacks = len(jacks)
        # generate all possible combinations of cards to replace the jacks
        replacements = ["".join(x) for x in itertools.product("23456789TQKA", repeat=n_jacks)]
        hands = [h]*len(replacements)
        for i in range(len(replacements)):
            for j in range(n_jacks):
                hands[i] = hands[i][:jacks[j]] + replacements[i][j] + hands[i][jacks[j]+1:]
        return hands
    
    # Override compare_lexicographically method
    def compare_lexicographically(self, h0, h1):
        order = {"J":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "Q":11, "K":12, "A":13}
        for x in range(len(h0)):
            if order[h0[x]] < order[h1[x]]:
                return -1
            elif order[h0[x]] > order[h1[x]]:
                return 1
        return 0 # If both hands are the same

    # Override hand_type method
    def hand_type(self, h):
        dic = {1:"High card", 2:"One pair", 3:"Two pair", 4:"Three of a kind", 5:"Full house", 6:"Four of a kind", 7:"Five of a kind"}
        if "J" in h: # If there are jacks, replace them with every possible card
            hands = self.substitute_jacks(h)
            # value = max([self.hand_type_no_jokers(x) for x in hands])
            super_hand_type = super().hand_type
            value = max([super_hand_type(x) for x in hands])
        else: # Otherwise, value the hand as usual
            # value = self.hand_type_no_jokers(h)
            value = super().hand_type(h)
        print (f"{h}: {dic[value]}")
        return value


# %%
part_2 = Part_2("input.txt") 
print(f"Answer to part 2: {part_2.solve()}")
