# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value   # to store node's value
        self.left = None     # pointer to root of left subtree
        self.right = None    # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Override string method; display in pre-order
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.

        This is intended to be a troubleshooting method to help find any
        inconsistencies in the tree after the add() or remove() operations.
        A return of True from this method doesn't guarantee that your tree
        is the 'correct' result, just that it satisfies bst ordering.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object, current_node=None) -> None:
        """
        TODO: Write your implementation
        """

    #     if self._root == None:
    #         self._root = BSTNode(value)
    #     else:
    #         self._add(value, self._root)
    #
    # def _add(self, value, cur_node):
    #
    #     if value < cur_node.value:
    #         if cur_node.left == None:
    #             cur_node.left = BSTNode(value)
    #             # cur_node.left.parent=cur_node # set parent
    #         else:
    #             self._add(value, cur_node.left)
    #     elif value >= cur_node.value:
    #         if cur_node.right == None:
    #             cur_node.right = BSTNode(value)
    #             # cur_node.right.parent=cur_node # set parent
    #         else:
    #             self._add(value, cur_node.right)


        # parent_node = None

        if self._root is None:
            self._root = BSTNode(value)
            # print(self.is_valid_bst())
            return
        node = self._root
        while node is not None:
            if value < node.value:
                if node.left is None:
                    node.left = BSTNode(value)
                    # print(self.is_valid_bst())
                    return
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = BSTNode(value)
                    # print(self.is_valid_bst())
                    return
                else:
                    node = node.right


    def find(self, value):
        node = self._root
        parent_node = None
        child = None
        while node is not None:

            if node.value == value:
                # print(node, parent_node, child)
                return (True, node, parent_node, child)
            elif value < node.value:
                parent_node = node
                child = "left"
                node = node.left
            else:
                parent_node = node
                child = "right"
                node = node.right
        return False
    def inorder_successor_finder(self, node):

        if node.right:
            if node.right.left:
                return node.right.left
            else:
                return node.right
        else:
            return None

    def remove(self, value):

        findResult = self.find(value)
        node = None

        if findResult:
            node = findResult[1]
        else:
            return False

        # if no parent
        if findResult[2] is None:
            # Getting the successor
            inorder_successor = self.inorder_successor_finder(node)
            #setting the successor as the root
            self._root = inorder_successor
            print("in order succesrot:", inorder_successor)

            return True
        else:
            print("crum a")
            parent_node = findResult[2] # parent node
            whichChild = findResult[3]
            inorder_successor = self.inorder_successor_finder(node)





        # no children of node
        if node.left == None and node.right == None:
            print("crum 1")
            if whichChild == "left":
                parent_node.left = None
                return True
            # if node is parent's right child
            else:
                parent_node.right = None
                return True
            # parent_node.left = None
            # parent_node.right = None
            print(parent_node)

            node=None


            # if node == self._root:
            #     self._root = None
            return True
            # else:
            #     print("Strike!")
            #     node = None
            #     return True
        # if node does not have right child
        elif node.left and not node.right:
            print("crum 2")
            #if node is parent's left child
            if whichChild == "left":
                parent_node.left = node.left
                return True
            # if node is parent's right child
            else:
                parent_node.right = node.left
                return True
        #if node does not have a left child
        elif node.right and not node.left:
            print("crum 3")
            # if node is parent's left child
            if whichChild == "left":
                parent_node.left = node.right
                return True
            # if node is parent's right child
            else:
                parent_node.right = node.right
                return True
        # If node has both children
        else:
            print("crum 4")
            if whichChild == "left":
                # If the successor node is the same deleted node left child
                if inorder_successor == node.left:
                    # setting deleted node's right  child and successor's right
                    inorder_successor.right = node.right
                    parent_node.left = inorder_successor
                    return True
                else:
                    inorder_successor.left = node.left
                    parent_node.left = inorder_successor
                    return True
            else:
                if inorder_successor == node.left:
                    # setting deleted node's right  child and successor's right
                    inorder_successor.right = node.right
                    parent_node.right = inorder_successor
                    return True
                else:
                    inorder_successor.left = node.left
                    parent_node.right = inorder_successor
                    return True



    def remove1(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        pass

    # Consider implementing methods that handle different removal scenarios; #
    # you may find that you're able to use some of them in the AVL.          #
    # Remove these comments.                                                 #
    # Remove these method stubs if you decide not to use them.               #
    # Change these methods in any way you'd like.                            #

    def _remove_no_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        TODO: Write your implementation
        """
        # remove node that has no subtrees (no left or right nodes)
        pass

    def _remove_one_subtree(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        TODO: Write your implementation
        """
        # remove node that has a left or right subtree (only)
        pass

    def _remove_two_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        TODO: Write your implementation
        """
        # remove node that has two subtrees
        # need to find inorder successor and its parent (make a method!)
        pass

    def contains(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        result = self.find(value)
        if result:
            return result[0]
        else:
            return False

    def inorder_traversal(self) -> Queue:
        """
        TODO: Write your implementation
        """
        pass

    def find_min(self) -> object:
        """
        TODO: Write your implementation
        """
        node = self._root
        if node is None:
            return None
        elif node.left is None and node.right is None:
            return node.value
        elif node.left is None and node.right:
            node = node.right
            while node.left is not None:
                node = node.left
            if self._root.value < node.value:
                return self._root.value
            return node.value
        elif node.left:
            while node.left is not None:
                node = node.left
            if self._root.value < node.value:
                return self._root.value
            return node.value

    def find_max(self) -> object:
        """
        TODO: Write your implementation
        """
        node = self._root
        if node is None:
            return None
        elif node.right is None:
            return node.value
        else:
            while node.right is not None:
                node = node.right
            return node.value

    def is_empty(self) -> bool:
        """
        TODO: Write your implementation
        """
        if self._root is None:
            return True
        else:
            return False

    def make_empty(self) -> None:
        """
        TODO: Write your implementation
        """
        self._root = None


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    # print("\nPDF - method add() example 1")
    # print("----------------------------")
    # test_cases = (
    #     (1, 2, 3),
    #     (3, 2, 1),
    #     (1, 3, 2),
    #     (3, 1, 2),
    # )
    # for case in test_cases:
    #     tree = BST(case)
    #     print(tree)
    #
    # print("\nPDF - method add() example 2")
    # print("----------------------------")
    # test_cases = (
    #     (10, 20, 30, 40, 50),
    #     (10, 20, 30, 50, 40),
    #     (30, 20, 10, 5, 1),
    #     (30, 20, 10, 1, 5),
    #     (5, 4, 6, 3, 7, 2, 8),
    #     (range(0, 30, 3)),
    #     (range(0, 31, 3)),
    #     (range(0, 34, 3)),
    #     (range(10, -10, -2)),
    #     ('A', 'B', 'C', 'D', 'E'),
    #     (1, 1, 1, 1),
    # )
    # for case in test_cases:
    #     tree = BST(case)
    #     print('INPUT  :', case)
    #     print('RESULT :', tree)

    # print("\nPDF - method add() example 3")
    # print("----------------------------")
    # for _ in range(100):
    #     case = list(set(random.randrange(1, 20000) for _ in range(900)))
    #     tree = BST()
    #     for value in case:
    #         tree.add(value)
    #     if not tree.is_valid_bst():
    #         raise Exception("PROBLEM WITH ADD OPERATION")
    # print('add() stress test finished')


    # print("----------FIND START------------")
    # inputArray = (5, 4, 6, 3, 7, 2, 8)
    #
    # tree = BST()
    #
    # for item in inputArray:
    #     tree.add(item)
    # print(tree)
    #
    # print(tree.find(1))
    # print(tree.find(2))
    #
    # print(tree.find(0))
    # print(tree.find(99))
    # print(tree.remove(6))
    #
    #
    # print("----------FIND END------------")









    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        # ((1, 2, 3), 1),
        # ((1, 2, 3), 2),
        # ((1, 2, 3), 3),
        # ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        # ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 3")
    print("---------------------------------")
    tree = BST( ["AQ", "SO", "QU", "G", "EF", "B", "C", "B", "B", "B", "B", "B", "B", "C",
     "DP","D", "DP", "E", "EF", "G", "NB", "HD", "G", "G", "G", "IG", "I", "HD", "IG", "L", "J", "K", "K", "OX", "P", "OX", "P", "RH", "R", "QU", "QU", "R", "R", "R", "R", "R", "R", "R", "S", "RH", "S", "TI", "T", "T", "Y", "XD", "TI", "Y", "Z", "Y", "ZL", "ZL"])
    print(tree)
    print("Minimum value is:", tree.find_min())




    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
