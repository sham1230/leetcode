class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # intialize dict
        hm = defaultdict(list)

        #loop through list and sort each word based on letter
        for word in strs:
            # sort the string
            sorted_word = "".join(sorted(word))
            # append sorted_word into string
            hm[sorted_word].append(word)

        return list(hm.values())




        
        