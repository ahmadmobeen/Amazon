class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Inspired by neetcode
        
        if t == '':
            return ''
        
        count_t = {}
        count_sub = {}
        res, resLen = [-1, -1], float('inf')
        l = 0
        
        for i in range(len(t)):
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        
        have, need = 0, len(count_t)

        
        for r in range(len(s)):
            count_sub[s[r]] = count_sub.get(s[r], 0) + 1
            if s[r] in count_t and count_t[s[r]] == count_sub[s[r]]:
                have += 1
            
            while have == need:
                
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]
                # pop from left of window
                count_sub[s[l]] -= 1
                if s[l] in count_t and count_sub[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ''
            
                
                
        
        
        # Didn't work
        
        # Lets try to use the sliding window method to select substrings
        # After selecting a substring, compare the number of occurrences of 
        # each character in the substring to that of the string 't'.
        # The substrings having exactly the same number of character occurences 
        # as of the string 't', are compared for the length and the shortest is selected.
        '''
        def letter_freq(sub):
            mp = {}
            for i in range(len(sub)):
                mp[sub[i]] = mp.get(sub[i], 0) + 1
            return mp
        # Compute the letter frequencies in string 't'
        count_t = letter_freq(t)
        # print(count_t)
        res = ''
        l,r = 0, len(t) - 1
        min_sub = {'':float('inf')}
        
        while l < r:
            count_sub = letter_freq(s[l:r])
            if count_sub == count_t:
                min_sub[s[l:r]] = len(s[l:r])
                l += 1

            else:
                r += 1
            l += 1
        print(min_sub)
        return min(min_sub, key = min_sub.__getitem__)'''
                
