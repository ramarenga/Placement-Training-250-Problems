class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()

        # Find smallest word globally
        min_index = 0
        for i in range(len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[min_index]):
                min_index = i

        root.index = min_index

        # Build Trie with reversed words
        for i, word in enumerate(wordsContainer):
            node = root
            rev_word = word[::-1]

            for ch in rev_word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                # Store best index
                if node.index == -1:
                    node.index = i
                else:
                    curr_word = wordsContainer[node.index]

                    if len(word) < len(curr_word):
                        node.index = i

        ans = []

        # Process queries
        for query in wordsQuery:
            node = root
            rev_query = query[::-1]
            best_index = root.index

            for ch in rev_query:
                if ch not in node.children:
                    break

                node = node.children[ch]
                best_index = node.index

            ans.append(best_index)

        return ans