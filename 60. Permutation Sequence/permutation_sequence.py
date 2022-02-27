from itertools import permutations


class Solution:
    def get_permutations(self, a):
        return permutations(a)
    
    def getPermutation(self, n: int, k: int) -> str:
        a = [i+1 for i in range(n)]
        perms = self.get_permutations(a)
        i = 1
        res = None
        for perm in perms:
            if i==k:
                res = perm
                break
            i += 1
        res = "".join(map(str, res))
        return res
        
        