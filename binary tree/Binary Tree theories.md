## Basics of Binary Tree

- A binary tree has less than or equal to 2 nodes.
- A full binary tree is a binary tree where each node has 0 or 2 nodes.
- A complete binary tree is a type of binary tree where-
  1.  all the nodes in the levels except the last level have 2 nodes each,
  2.  the nodes in the last level are the children of the leftmost nodes of the previous levels (for example, if there are 2 nodes in the level before the last level being numbered as 1 and 2 from the left, then either (a) node 1 can have 1 node at its left (node 2 must be empty in this case), or (b) node 1 can have 2 nodes, and node 2 can have 1 node at left, 2 nodes or no node at all.)
- In a Perfect binary tree, all the nodes before the last level have 2 nodes each and all the leaf nodes are in the same level.
- In a Balanced binary tree, the absolute difference between the heights of the left sub-tree and the right sub-tree of each node is at most 1.
- Pathological (or Degenerate) binary is where each parent node has only 1 child node.
- Binary Search Tree (BST) is a binary tree with the following properties:
  1.  Each of the node values of the left sub-tree will be less than the root node value,
  2.  Each of the node values of the right sub-tree will be greater than the root node value,
  3.  Each of the sub-trees will be a BST as well.
- BST traversal:
  1.  Pre-order traversal: node -> left sub-tree -> right sub-tree
  2.  In-order traversal: left sub-tree -> node -> right sub-tree
  3.  Post-order traversal: left sub-tree -> right sub-tree -> node
  4.  Level-order traversal: Level 0 -> Level 1 -> Level 2 -> ... -> Level n
- A binary heap is a complete binary tree that satisfies the heap property.
  - Heap property:
    1.  The key of every parent node is less than or equal to that of the child node (min heap/min binary heap), or
    2.  The key of every parent node is less than or equal to that of the child node (max heap/max binary heap)

#### Binary Heap operations:

- `Heapify`: A process to re-arrange the nodes of a complete binary tree to maintain the heap property (creating a binary heap from a completer binary tree)
  - Heapify operations are of 2 types:
    1. Heapify up: Bottom to top approach (from leaf node to root node)
    2. Heapify down: Top down approach (root to leaf)
  - Heapify is performed when a new node is inserted, a node is deleted or a tree is re-arranged to form a heap tree.
  - Formula to find the parent of a node: (i+1)//2
  - Formula to find the left child of a node: i\*2+1
  - Formula to find the right child of a node: i\*2+2
