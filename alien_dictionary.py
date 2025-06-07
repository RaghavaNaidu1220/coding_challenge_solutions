#!/usr/bin/env python3
"""
alien_dictionary.py:
Determines the order of characters in an alien language based on a sorted list of words.
The solution builds a precedence graph and performs a topological sort.
"""

from collections import defaultdict, deque

def alien_dictionary(words):
    """
    Determines the character order given a sorted list of words from an alien language.
    
    Parameters:
      words: List of words (strings) in lexicographic order.
      
    Returns:
      A string of characters representing the lexicographic order. 
      Returns an empty string if the order cannot be determined.
    """
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}
    
    # Build the graph by comparing adjacent words.
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
        diff_found = False
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                diff_found = True
                break
        # Edge-case: Prefix violation (e.g., "abc" and "ab").
        if not diff_found and len(word1) > len(word2):
            return ""
    
    # Topological sort using BFS.
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    order = []
    while queue:
        char = queue.popleft()
        order.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(order) != len(in_degree):
        return ""
    return "".join(order)


def main():
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print("Alien dictionary order:", alien_dictionary(words))


if __name__ == '__main__':
    main()