class TreeNode: 
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def Pre_order(self, root):
    stack = []
    result = []
    if not root:
        return []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def In_order(self, root):
    stack = []
    result = []
    if not root:
        return []
    cur = root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
    return result


def Post_order(self, root):
    stack = []
    result = []
    if not root:
        return []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]
