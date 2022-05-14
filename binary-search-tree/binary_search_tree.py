from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self: 'BinarySearchTree'):
        self.root = None
        self.size = 0

    def insert(self: 'BinarySearchTree', root: Node, node: Node):
        if self.root is None:
            self.root = node
            self.size += 1
            return

        if root.data > node.data:
            if root.left is None:
                root.left = node
                self.size += 1
            else:
                self.insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
                self.size += 1
            else:
                self.insert(root.right, node)

    def search(self: 'BinarySearchTree', root: Node, data: Any) -> Node | None:
        if self.root is None:
            return None

        if root.data == data:
            return root

        if root.data > data:
            return self.search(root.left, data)
        else:
            return self.search(root.right, data)

    def delete(self: 'BinarySearchTree', root: Node, data: Any) -> Node | None:
        if self.root is None:
            return None

        if root.data == data:
            return self.delete_node(root)

        if root.data > data:
            return self.delete(root.left, data)
        else:
            return self.delete(root.right, data)

    def delete_node(self: 'BinarySearchTree', node: Node) -> Node | None:
        if node.left is None and node.right is None:
            return None

        if node.left is None:
            return node.right

        if node.right is None:
            return node.left

        min_node = self.get_min(node.right)
        node.data = min_node.data
        node.right = self.delete(node.right, min_node.data)

        return node

    def get_min(self: 'BinarySearchTree', root: Node) -> Node:
        if root.left is None:
            return root

        return self.get_min(root.left)

    def get_max(self: 'BinarySearchTree', root: Node) -> Node:
        if root.right is None:
            return root

        return self.get_max(root.right)

    def get_size(self: 'BinarySearchTree') -> int:
        return self.size

    def get_height(self: 'BinarySearchTree', root: Node) -> int:
        if root is None:
            return -1

        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def print_in_order(self: 'BinarySearchTree', root: Node):
        if root is None:
            return

        self.print_in_order(root.left)
        print(root.data)
        self.print_in_order(root.right)

    def print_pre_order(self: 'BinarySearchTree', root: Node):
        if root is None:
            return

        print(root.data)
        self.print_pre_order(root.left)
        self.print_pre_order(root.right)

    def print_post_order(self: 'BinarySearchTree', root: Node):
        if root is None:
            return

        self.print_post_order(root.left)
        self.print_post_order(root.right)
        print(root.data)

    def print_level_order(self: 'BinarySearchTree', root: Node):
        if root is None:
            return

        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


if __name__ == '__main__':
    tree: BinarySearchTree = BinarySearchTree()
    tree.insert(tree.root, Node(10))
    tree.insert(tree.root, Node(5))
    tree.insert(tree.root, Node(15))
    tree.insert(tree.root, Node(2))
    tree.insert(tree.root, Node(7))
    tree.delete(tree.root, 5)
