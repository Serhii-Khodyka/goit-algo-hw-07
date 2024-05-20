class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max_value(root):
    if root is None:
        return float('-inf')  # якщо корінь не існує, повертаємо негативну нескінченність

    max_value = root.value
    right_max = find_max_value(root.right) # беремо праву гілку для знаходження максимального елемента 
    return max(max_value, right_max)

def find_min_value(root):
    if root is None:
        return float('inf')  # якщо корінь не існує, повертаємо позитивну нескінченність

    min_value = root.value
    left_min = find_min_value(root.left) # беремо ліву гілку для знаходження мінімального елемента
    return min(min_value, left_min)

def find_sum_of_values(root):
    if root is None:
        return 0

    return root.value + find_sum_of_values(root.left) + find_sum_of_values(root.right)


# створюємо дерево
root = TreeNode(20)
root.left = TreeNode(12)
root.right = TreeNode(28)
root.left.left = TreeNode(8)
root.left.right = TreeNode(16)
root.right.left = TreeNode(24)
root.right.right = TreeNode(32)

# знаходимо найбільше значення
max_value = find_max_value(root)
print("Найбільше значення в дереві:", max_value)

# знаходимо найменше значення
min_value = find_min_value(root)
print("Найменше значення в дереві:", min_value)

# знаходимо суму всіх значень
sum_values = find_sum_of_values(root)
print("Сума всіх значень в дереві:", sum_values)