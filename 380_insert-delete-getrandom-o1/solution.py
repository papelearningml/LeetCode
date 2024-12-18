import random

class RandomizedSet:
    def __init__(self):
        # keeping a hashmap for O(1) lookups, and a list for random access. let's go 
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        # already here? nah fam, return False
        if val in self.val_to_index:
            return False
        # add to the list and track its index. ez clap
        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        # not here? can't remove what's not there 
        if val not in self.val_to_index:
            return False
        # swap it with the last item to keep the list intact 
        last_val = self.values[-1]
        idx = self.val_to_index[val]
        self.values[idx] = last_val
        self.val_to_index[last_val] = idx
        # drop the last item, we done here 
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        # just grab something random from the list 
        return random.choice(self.values)
