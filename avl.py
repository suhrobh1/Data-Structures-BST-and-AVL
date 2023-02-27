# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


import random
from queue_and_stack import Queue, Stack
from bst import BSTNode, BST


class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'AVL Node: {}'.format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        super()._str_helper(self._root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self._root:
                        return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        TODO: Write your implementation
        """

        if self._root is None:
            self._root = AVLNode(value)
        else:
            self._add(value, self._root)

    def _add(self, value, node):

        if value < node.value:
            if node.left is None:
                node.left = AVLNode(value)
                node.left.parent = node
                self._inspection(node.left)
                return
            else:
                self._add(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = AVLNode(value)
                node.right.parent = node
                self._inspection(node.right)
                return
            else:
                self._add(value, node.right)
        else:
            print("Value already in tree")

    def _inspection(self, node, trace=[]):
        if node.parent is None:
            return

        trace = [node] + trace

        # hieght of children
        left_height = self._get_height(node.parent.left)
        right_height = self._get_height(node.parent.right)

        if abs(left_height - right_height) > 1:
            trace = [node.parent] + trace
            self._rebalance(trace[0], trace[1], trace[2])
            return

        new_height = 1 + node.height
        if new_height > node.parent.height:
            node.parent.height = new_height

        # continue up the tree
        self._inspection(node.parent, trace)

    def _rebalance(self, node: AVLNode, y, x) -> None:
        """
        TODO: Write your implementation
        """
        if y == node.left and x == y.left:
            self._rotate_right(node)
        elif y == node.left and x == y.right:
            self._rotate_left(y)
            self._rotate_right(node)
        elif y == node.right and x == y.right:
            self._rotate_left(node)
        elif y == node.right and x == y.left:
            self._rotate_right(y)
            self._rotate_left(node)
        else:
            print('_rebalance_node: z,y,x node configuration not recognized!')

        # if self._balance_factor(node) < -1:
        #     if self._balance_factor(node.left) > 0:
        #         node.left = self._rotate_left(node.left)
        #         node.left.parent = node
        #     newSubtreeRoot = self._rotate_right(node)
        #     newSubtreeRoot.parent = node.parent
        #     node.parent.left = newSubtreeRoot
        #     #node.parent.right = newSubtreeRoot
        # elif self._balance_factor(node) > 1:
        #     if self._balance_factor(node.right) < 0:
        #         node.right = self._rotate_right(node.right)
        #         node.right.parent = node
        #     newSubtreeRoot = self._rotate_left(node)
        #     newSubtreeRoot.parent = node.parent
        #     #node.parent.left = newSubtreeRoot
        #     node.parent.right = newSubtreeRoot
        # else:
        #     self._update_height(node)

    def _get_height(self, node: AVLNode) -> int:
        """
        TODO: Write your implementation
        """
        if node == None:
            return 0
        return node.height

    def remove(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        pass

    # Experiment and see if you can use the optional                         #
    # subtree removal methods defined in the BST here in the AVL.            #
    # Call normally using self -> self._remove_no_subtrees(parent, node)     #
    # You need to override the _remove_two_subtrees() method in any case.    #
    # Remove these comments.                                                 #
    # Remove these method stubs if you decide not to use them.               #
    # Change this method in any way you'd like.                              #

    def _remove_two_subtrees(self, remove_parent: AVLNode, remove_node: AVLNode) -> AVLNode:
        """
        TODO: Write your implementation
        """
        pass

    # It's highly recommended to implement                          #
    # the following methods for balancing the AVL Tree.             #
    # Remove these comments.                                        #
    # Remove these method stubs if you decide not to use them.      #
    # Change these methods in any way you'd like.                   #

    def _balance_factor(self, node: AVLNode) -> int:
        """
        TODO: Write your implementation
        """
        balance_factor = node.right.height - node.left.height
        return balance_factor



    def _rotate_left(self, node: AVLNode) -> AVLNode:
        """
        TODO: Write your implementation
        """
        sub_root = node.parent
        y = node.right
        t2 = y.left
        y.left = node
        node.parent = y
        node.right = t2
        if t2 != None: t2.parent = node
        y.parent = sub_root
        if y.parent == None:
            self.root = y
        else:
            if y.parent.left == node:
                y.parent.left = y
            else:
                y.parent.right = y
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        """
        TODO: Write your implementation
        """
        sub_root = node.parent
        y = node.left
        t3 = y.right
        y.right = node
        node.parent = y
        node.left = t3
        if t3 is not None: t3.parent = node
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == node:
                y.parent.left = y
            else:
                y.parent.right = y
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
    def _update_height(self, node: AVLNode) -> None:
        """
        TODO: Write your implementation
        """
        if node.left is not None and node.right is not None:
            if node.left.height > node.right.height:
                node.height = node.left.height + 1
            else:
                node.height = node.right.height + 1
        elif node.left is None and node.right is None:
            node.height = 0
        elif node.left is None:
            node.height = node.right.height + 1
        elif node.right is None:
            node.height = node.left.height + 1

        while node.parent is not None:
            # parents are at least of height one
            parent = node.parent
            left, right = parent.left, parent.right
            if left is not None and right is not None:
                if left.height > right.height:
                    parent.height = left.height + 1
                else:
                    parent.height = right.height + 1
            elif right is None:
                parent.height = left.height + 1
            else:
                parent.height = right.height + 1


        # node.height = max(node.left.height, node.right.height) + 1


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        tree = AVL(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 20, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL()
        for value in case:
            tree.add(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = AVL(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = AVL(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL(case)
        for value in case[::2]:
            tree.remove(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('remove() stress test finished')

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
