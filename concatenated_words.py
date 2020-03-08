'''
 This problem was recently asked by Twitter:

Find all words that are concatenations of a list.

Input:
["tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"]

Output:
['techlead', 'catsdog']

class Solution(object):
  def findAllConcatenatedWordsInADict(self, words):
    # Fill this in.
    
input = ["tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"]

print(Solution().findAllConcatenatedWordsInADict(input))


Note: This question is classified as "hard."
HINT: Start with a brute-force solution.
'''

class ConcatenatedWords(object):
    @staticmethod
    def find_all_concatenated_words_in_a_list(words):
        concatenated_words = []
        for i in range(len(words)):
            for j in range(len(words)):
                if (words[i] + words[j]) in words:
                    concatenated_words.append(words[i] + words[j])
        return concatenated_words

print(ConcatenatedWords.find_all_concatenated_words_in_a_list([
        "tech", "lead", "techlead", "techleadcat",
        "cat", "cats", "dog", "catsdog"]))
