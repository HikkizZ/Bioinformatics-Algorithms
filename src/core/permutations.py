import time
from itertools import permutations as it_perms

def generate_permutations(seq):
    seen = set()
    def backtrack(s, path):
        if not s:
            seen.add(path)
            return
        for i in range(len(s)):
            backtrack(s[:i] + s[i+1:], path + s[i])
    
    start = time.time()
    backtrack(seq, "")
    return time.time() - start, len(seen)

def itertools_permutations(seq):
    start = time.time()
    perms = list(it_perms(seq))
    return time.time() - start, len(perms)
