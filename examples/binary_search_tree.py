# Binary Search Tree Implementation in Python
#
# Blog post: https://emre.me/data-structures/binary-search-trees/
# Blog author: Emre Bolat

class Node:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def has_left_child(self):
        return self.leftChild

    def has_right_child(self):
        return self.rightChild

    def is_left_child(self):
        return self.parent and self.parent.leftChild == self

    def is_right_child(self):
        return self.parent and self.parent.rightChild == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.rightChild or self.leftChild)

    def has_any_children(self):
        return self.rightChild or self.leftChild

    def has_both_children(self):
        return self.rightChild and self.leftChild

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def find_successor(self):
        successor = None
        if self.has_right_child():
            successor = self.rightChild.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.rightChild = None
                    successor = self.parent.find_successor()
                    self.parent.rightChild = self
        return successor

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.leftChild
        return current

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.has_left_child():
            self.leftChild.parent = self
        if self.has_right_child():
            self.rightChild.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = Node(key, val)
        self.size = self.size + 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.leftChild)
            else:
                current_node.leftChild = Node(key, val, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.rightChild)
            else:
                current_node.rightChild = Node(key, val, parent=current_node)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.leftChild)
        else:
            return self._get(key, current_node.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, current_node):
        if current_node.is_leaf():  # leaf
            if current_node == current_node.parent.leftChild:
                current_node.parent.leftChild = None
            else:
                current_node.parent.rightChild = None
        elif current_node.has_both_children():  # interior
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.payload = successor.payload

        else:  # this node has one child
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.leftChild.parent = current_node.parent
                    current_node.parent.leftChild = current_node.leftChild
                elif current_node.is_right_child():
                    current_node.leftChild.parent = current_node.parent
                    current_node.parent.rightChild = current_node.leftChild
                else:
                    current_node.replace_node_data(current_node.leftChild.key,
                                                   current_node.leftChild.payload,
                                                   current_node.leftChild.leftChild,
                                                   current_node.leftChild.rightChild)
            else:
                if current_node.is_left_child():
                    current_node.rightChild.parent = current_node.parent
                    current_node.parent.leftChild = current_node.rightChild
                elif current_node.is_right_child():
                    current_node.rightChild.parent = current_node.parent
                    current_node.parent.rightChild = current_node.rightChild
                else:
                    current_node.replace_node_data(current_node.rightChild.key,
                                                   current_node.rightChild.payload,
                                                   current_node.rightChild.leftChild,
                                                   current_node.rightChild.rightChild)