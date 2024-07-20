from collections import deque

class Node:
    def __init__(self, bigrams=None, words=None, left=None, right=None):
        self.bigrams = bigrams if bigrams is not None else []
        self.words = words if words is not None else []
        self.left = left
        self.right = right

class DecisionTree:
    def __init__(self):
        self.root = None
        self.node_count = 0  # Initialize node count

    def generate_bigrams(self, words):
        bigrams = set()
        for word in words:
            for i in range(len(word) - 1):
                bigram = word[i:i+2]
                bigrams.add(bigram)
        sorted_bigrams = sorted(bigrams)
        return sorted_bigrams

    def split_words_by_bigrams(self, words, bigrams):
        with_bigrams = [word for word in words if any(bigram in word for bigram in bigrams)]
        return with_bigrams

    def fit(self, words):
        if not words:
            return
        
        bigrams = self.generate_bigrams(words)
        self.root = self._decision_tree_split_iterative(words, bigrams)
        self.node_count = self._count_nodes(self.root)  # Count nodes after fitting

    def _decision_tree_split_iterative(self, words, bigrams):
        if not words or not bigrams:
            return None
        
        root = Node(bigrams=bigrams, words=words)
        queue = deque([(root, words, bigrams)])
        
        while queue:
            node, words, bigrams = queue.popleft()
            
            if len(bigrams) <= 1 or len(words) <= 1:
                node.words = words
                continue
    
            mid_index = len(bigrams) // 2
            left_bigrams = bigrams[:mid_index]
            right_bigrams = bigrams[mid_index:]
    
            with_left_bigrams = self.split_words_by_bigrams(words, left_bigrams)
            with_right_bigrams = self.split_words_by_bigrams(words, right_bigrams)
    
            if with_left_bigrams:
                node.left = Node(bigrams=left_bigrams, words=with_left_bigrams)
                queue.append((node.left, with_left_bigrams, left_bigrams))
            
            if with_right_bigrams:
                node.right = Node(bigrams=right_bigrams, words=with_right_bigrams)
                queue.append((node.right, with_right_bigrams, right_bigrams))
        
        return root

    def traverse_tree_for_bigrams(self, bigrams_to_search):
        if not self.root:
            return []

        remaining_words = self.root.words
        
        for bigram in bigrams_to_search:
            current_node = self.root
            
            while current_node:
                if bigram in current_node.bigrams:
                    remaining_words = self.split_words_by_bigrams(remaining_words, [bigram])
                    if current_node.left and bigram in current_node.left.bigrams:
                        current_node = current_node.left
                    elif current_node.right and bigram in current_node.right.bigrams:
                        current_node = current_node.right
                    else:
                        break
                else:
                    break
        
        return remaining_words[:5]

    def _count_nodes(self, node):
        if not node:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

def my_fit(words):
    tree = DecisionTree()
    tree.fit(words)
    return tree

def my_predict(tree, bigrams_to_search):
    return tree.traverse_tree_for_bigrams(bigrams_to_search)


