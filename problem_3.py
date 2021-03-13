from collections import deque


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent

    def add_to_dict(self, node_dict):
        node_dict[self.value] = self


def create_tree(value_queue):
    if len(value_queue) <= 0:
        return None, None

    node_dict = {}

    root = Node(value_queue.popleft())

    root.add_to_dict(node_dict)

    current_queue = deque()

    current_queue.append(root)

    while len(current_queue) > 0 and len(value_queue) > 0:

        current_node = current_queue.popleft()

        left = value_queue.popleft()
        if left is not None:
            current_node.left = Node(left, parent=current_node)
            current_node.left.add_to_dict(node_dict)
            current_queue.append(current_node.left)

        right = value_queue.popleft()
        if right is not None:
            current_node.right = Node(right, parent=current_node)
            current_node.right.add_to_dict(node_dict)
            current_queue.append(current_node.right)

    return root, node_dict


def create_t_f_ls(value_list):
    return create_tree(deque(value_list))


def lca(node1, node2):
    parents = set()

    cur_parent = node1
    while cur_parent is not None:
        parents.add(cur_parent)
        cur_parent = cur_parent.parent

    cur_parent = node2
    while cur_parent is not None:
        if cur_parent in parents:
            return cur_parent
        cur_parent = cur_parent.parent

    return None


def main():
    tree_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, ]
    binary_tree, node_dict = create_t_f_ls(tree_list)
    print(lca(node_dict[3], node_dict[7]).value)


if __name__ == "__main__":
    main()
