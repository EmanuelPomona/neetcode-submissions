#class Solution:
#    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#        anagrams = {}
 #       for word in strs:
 #           for char in word:
 #               if sorted(word) not in anagrams:
  #                  anagram[sorted(word)] = [word]
  #              else:
  #                  anagram.get(sorted.word).append(word)
  #      return [anagram.values()]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char)-ord('a')] += 1
            signature = tuple(count)
            if signature in anagram:
                anagram[signature].append(word)
            else:
                anagram[signature] = [word]
        return list(anagram.values())









