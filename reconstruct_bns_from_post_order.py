from math import inf
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reconstruct(post_order, min_=-inf, max_=inf):
    global cur
    if cur < 0:
        return None
    root = None
    cur_value = post_order[cur]
    if cur_value > min_ and cur_value < max_:
        root = Node(cur_value)
        cur -= 1
        if cur >= 0:
            root.right = reconstruct(post_order, cur_value, max_)
            root.left = reconstruct(post_order, min_, cur_value)
    return root

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.val, end = " ")
        
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val, end=" ")
        inOrder(root.right)
        
post_order = [1, 7, 5, 50, 40, 10]
#post_order = [2, 4, 3, 8, 7, 5]
cur = len(post_order) - 1
root = reconstruct(post_order)
postOrder(root)
print()
inOrder(root)

    