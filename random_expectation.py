# %% Imports
import copy

# %% Calculate the expected number of relocations that RANDOM does for given instance

# Recursively calculate relocations
def recursive(instance, location, curr):
    # Finish
    if curr not in location:
        return 0

    # Stack of curr
    curr_stack = location[curr][0]

    # curr is top of stack
    if instance[curr_stack][-1] == curr:
        instance_copy = copy.deepcopy(instance)
        instance_copy[curr_stack].pop()
        location_copy = copy.deepcopy(location)
        location_copy.pop(curr)
        return recursive(instance_copy, location_copy, curr + 1)
    
    # curr is not top of stack
    top = instance[curr_stack][-1]

    ans = 1
    for i in range(len(instance)):
        if i != curr_stack:
            instance_copy = copy.deepcopy(instance)
            instance_copy[curr_stack].pop()
            instance_copy[i].append(top)
            location_copy = copy.deepcopy(location)
            location_copy[top] = (i, len(instance_copy[i]) - 1)
            ans += (1/(len(instance) - 1)) * recursive(instance_copy, location_copy, curr)
    return ans
    

def random(instance):
    # Build reverse mapping 
    location = {}
    for i, lst in enumerate(instance):
        for j, val in enumerate(lst):
            location[val] = (i, j)

    # Call recursive function
    return recursive(instance, location, 1)


# %% Hard example for levelling
instance = [[4, 2], [5, 3, 1, 6], [9, 8, 7]]
print(random(instance))

# %% Jiaqi's example
instance = [[], [2], [3, 1, 4, 5]]
print(random(instance))

# %% Bad example for random?
instance = [[4, 1], [5, 2, 10, 8, 7], [6, 3, 11, 9]]
print(random(instance))

# %% Simple bad example for random
instance = [[4, 1], [5, 2, 7], [6, 3]]
print(random(instance))

# %%
