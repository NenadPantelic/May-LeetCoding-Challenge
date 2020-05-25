#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:05:56 2020

@author: nenad
"""

"""

Problem URL: 
Problem description:
Construct Binary Search Tree from Preorder Traversal
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Time: O(n), space: O(n)
class Solution:
    index = 0
    def bstFromPreorder(self, preorder) -> TreeNode:
        n = len(preorder)
        def reconstructBST(minimum, maximum):
            # all elements from preorder are used
            if Solution.index >= n:
                return 
            root = None
            # take next element from preorder array
            nodeValue = preorder[Solution.index]
            # node belongs to the current subtree
            if minimum < nodeValue < maximum:
                # create new node
                root = TreeNode(nodeValue)
                # go to next index
                Solution.index += 1
                if Solution.index < n: 
                    # reconstruct left and right subtree
                    root.left = reconstructBST(minimum, nodeValue)
                    root.right = reconstructBST(nodeValue, maximum)
            return root
        # initial bounds are - -oo and +oo
        root = reconstructBST(float("-inf"), float("inf"))
        # reset index - for test cases sake
        Solution.index = 0
        return root
                