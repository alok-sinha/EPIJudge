from test_framework import generic_test


# We use stack and previous node pointer to simulate postorder traversal.
def postorder_traversal(tree):
    # TODO - you fill in here.

    stack = [(tree,0)]

    result = []
    while stack:
        node, visited = stack.pop()
        if visited or (not node.left and not node.right):
            result.append(node.data)
        else:
            stack.append((node,1))
            if node.right:
                stack.append((node.right, 0))
            if node.left:
                stack.append((node.left, 0))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "tree_postorder.py", 'tree_postorder.tsv', postorder_traversal))
