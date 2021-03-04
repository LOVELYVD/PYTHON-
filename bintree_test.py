#!/usr/bin/env python3
# *-* coding:utf-8 *-*

import unittest
from bintree import BinTree, BinTreeNode

class TestBinTree(unittest.TestCase):
    def test_create_has_root_none(self):
        tree = BinTree()
        self.assertIsNone(tree.root)

    def test_has_insert_and_search(self):
        tree = BinTree()
        tree.insert(1)
        self.assertIsInstance(tree.search(1), BinTreeNode)
        self.assertIsNone(tree.search(0))

    def test_insert_into_empty_tree(self):
        tree = BinTree()
        tree.insert(1)
        self.assertIsNotNone(tree.root)
        self.assertIsInstance(tree.root, BinTreeNode)
        self.assertEqual(tree.root.value, 1)

    def test_example(self):
        values = [7, 3, 9, 2, 4, 8, 11]
        tree = BinTree()
        for value in values:
            tree.insert(value)
        for value in values:
            node = tree.search(value)
            self.assertIsInstance(node, BinTreeNode)
            self.assertEqual(value, node.value)
        node = tree.search(3)
        self.assertEqual(node.value, 3)
        self.assertEqual(node.left.value, 2)
        self.assertEqual(node.right.value, 4)

class TestBinTreeNode(unittest.TestCase):
    def test_creation(self):
        node = BinTreeNode(5)
        self.assertEqual(node.value, 5)

    def test_has_left_and_right(self):
        node = BinTreeNode(0)
        self.assertIn("left", node.__dict__)
        self.assertIn("right", node.__dict__)

    def test_has_insert_and_search(self):
        node = BinTreeNode(0)
        node.insert(1)
        node.search(1)

if __name__ == "__main__":
    unittest.main()
