from itertools import combinations
from unicodedata import mirrored


class Solution:
    def get_sub_strings(self, s: str) -> str:
        yield [s[x:y] for x, y in combinations(range(len(s)+1), r=2)]

    def check_palindrome(self, s: str) -> bool:
        return s==s[::-1]

    def longestPalindromeNormal(self, s: str) -> str:
        l = 0
        palindrome = ""

        if len(s) == 1:
            return s
            
        if self.check_palindrome(s):
            return s
        
        sub = self.get_sub_strings(s)
        for string in next(sub):
            if len(string) > l:
                if self.check_palindrome(string):
                    l = len(string)
                    palindrome = string
        return palindrome
    
    def manacher_longest_palindrome(self, s: str) -> str:
        s_prime = "|"
        for char in s:
            s_prime = s_prime + char+'|' 
        length = len(s_prime)
        palindrome_radii = [0] * length
        center, radius = 0, 0
        palindrome = ""
        max_radii = 0
        max_center = 0

        while center < length:
            # At the start of the loop, Radius is already set to a lower-bound for the longest radius.
            # In the first iteration, Radius is 0, but it can be higher.
            
            # Determine the longest palindrome starting at Center-Radius and going to Center+Radius
            while center-(radius+1) >= 0 and \
                center+(radius+1) < length and \
                s_prime[center-(radius+1)] == s_prime[center+(radius+1)]:
                radius = radius+1
            # Save the radius of the longest palindrome in the array
            palindrome_radii[center] = radius

            if max_radii < radius:
                max_radii = radius
                max_center = center
                
            # Below, Center is incremented.
            # If any precomputed values can be reused, they are.
            # Also, Radius may be set to a value greater than 0
            
            old_center = center
            old_radius = radius
            center += 1
            # Radius' default value will be 0, if we reach the end of the following loop. 
            radius = 0 
            while center <= old_center + old_radius:
                # Because Center lies inside the old palindrome and every character inside
                # a palindrome has a "mirrored" character reflected across its center, we
                # can use the data that was precomputed for the Center's mirrored point. 
                mirrored_center = old_center - (center - old_center)
                max_mirrored_radius = old_center + old_radius - center
                if palindrome_radii[mirrored_center] < max_mirrored_radius:
                    palindrome_radii[center] = palindrome_radii[mirrored_center]
                    center += 1
                
                elif palindrome_radii[mirrored_center] > max_mirrored_radius:
                    palindrome_radii[center] = max_mirrored_radius
                    center += 1
                 
                # PalindromeRadii[MirroredCenter] = MaxMirroredRadius
                else:
                    radius = max_mirrored_radius
                    if max_radii < radius:
                        max_radii = radius
                        max_center = center
                    break  # exit while loop early
                 
                  
        palindrome = ""
        i = max_center-max_radii
        while i < max_center+max_radii+1:
            if s_prime[i] == "|":
                i += 1
                continue
            palindrome += s_prime[i]
            i += 1

        return palindrome 

    def longestPalindrome(self, s: str) -> str:
        res = self.manacher_longest_palindrome(s)
        return res
            



                


