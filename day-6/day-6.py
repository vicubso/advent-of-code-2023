# %% [markdown]
# # AoC 2023, day 6

# %% [markdown]
# ## Part 1

# %%
import numpy as np
with open('input.txt') as f:
    lines = f.readlines()
times = np.array(lines[0].split()[1:], dtype=int)
distances = np.array(lines[1].split()[1:], dtype=int)

# %% [markdown]
# The distance cover by the boat if the button is held for $a$ seconds is
# $$ X(a) = (T-a)a = aT-a^2 $$
# where $T$ is the allowed time for the race.

# %%
ways_of_winning = np.zeros(len(times), dtype=int)
for i in range(len(times)):
    T = times[i]
    for a in range(1,T):
        X = (T-a)*a
        if X > distances[i]:
            ways_of_winning[i] += 1

np.prod(ways_of_winning)

# %% [markdown]
# ## Part 2

# %% [markdown]
# To make it more efficient, now we find the zeros of the function $f(a) = X(a) - D = aT - a^2 - D$, where $D$ is the record distance from the race (using e.g., bisection method). We should expect two zeros, say at the values $a_0$ and $a_1$. Then, the number of ways of winning is the number of integers in the interval $[a_0,a_1]$, i.e.,
# $$ \lfloor a_1 \rfloor - \lceil a_0 \rceil + 1. $$
#
# To find these two zeros, we perform the bisection method on the intervals $[0,T/2]$ and $[T/2, T]$.

# %%
T = int(''.join(lines[0].split()[1:]))
D = int(''.join(lines[1].split()[1:]))


# %%
def bisection(f, a, b, tol=1e-4):
    fa = f(a)
    fb = f(b)
    m = (a+b)/2
    fm = f(m)
    if abs(f(m)) < tol:
        return (a+b)/2
    if fa*fm <= 0:
        return bisection(f, a, m, tol)
    return bisection(f, m, b, tol)



# %%
f = lambda a: (T-a)*a - D
a0 = bisection(f, 0, T/2, tol=.1)
a1 = bisection(f, T/2, T, tol=.1)
print(f" a0 = {a0}, f(a0) = {f(a0)}")
print(f" a1 = {a1}, f(a1) = {f(a1)}")

# %%
print(int(np.floor(a1) - np.ceil(a0) + 1))
