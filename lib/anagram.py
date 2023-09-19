# anagram class
# init with a word 
# def match
# if anagram return matches
# else return none

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, potential_anagrams):
     
        sorted_word = sorted(self.word)

        # matches = []
        # for potential_anagram in potential_anagrams:
        #     if sorted(potential_anagram) == sorted_word:
        #         matches.append(potential_anagram)

        matches = [potential_anagram for potential_anagram in potential_anagrams 
                   if sorted(potential_anagram) == sorted_word ]
        return matches
        
# Anagram(initial_word, check_words):
#     listen = Anagram(initial_word)
#     listen.match([check_words])

# def Anagram(initial_word, check_words):
#     possible_anagrams = []
#     for check_word in check_words:
#         if sorted(check_word) == sorted(initial_word):
#             possible_anagrams.append(check_word)
#         else:
#             return []
        
#         return possible_anagrams

# anagram if composed of same letters
#   [letter for letter in "hello"]
#   sorted([l, i, s, t, e, n]) == sorted([e, n, l, i, s, t, s])