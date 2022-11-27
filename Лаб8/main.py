import time
from random import randint

# бинарное дерево
class node:
  def __init__(self, value=None):
    self.value = value
    self.left_child = None
    self.right_child = None
    self.height = 1

class binary_search_tree:
    def  __init__ (self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = binary_search_tree(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = binary_search_tree(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals


# AVL дерево
class AVL:
    def height(self, Node):
        if Node is None:
            return 0
        else:
            return Node.height

    def balance(self, Node):
        if Node is None:
            return 0
        else:
            return self.height(Node.left) - self.height(Node.right)

    def MinimumValueNode(self, Node):
        if Node is None or Node.left is None:
            return Node
        else:
            return self.MinimumValueNode(Node.left)

    def rotateR(self, Node):
        a = Node.left
        b = a.right
        a.right = Node
        Node.left = b
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    def rotateL(self, Node):
        a = Node.right
        b = a.left
        a.left = Node
        Node.right = b
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    def insert(self, val, root):
        if root is None:
            return node(val)
        elif val <= root.value:
            root.left = self.insert(val, root.left)
        elif val > root.value:
            root.right = self.insert(val, root.right)
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        if balance > 1 and root.left.value > val:
            return self.rotateR(root)
        if balance < -1 and val > root.right.value:
            return self.rotateL(root)
        if balance > 1 and val > root.left.value:
            root.left = self.rotateL(root.left)
            return self.rotateR(root)
        if balance < -1 and val < root.right.value:
            root.right = self.rotateR(root.right)
            return self.rotateL(root)
        return root

    def preorder(self, root):
        if root is None:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def delete(self, val, Node):
        if Node is None:
            return Node
        elif val < Node.value:
            Node.left = self.delete(val, Node.left)
        elif val > Node.value:
            Node.right = self.delete(val, Node.right)
        else:
            if Node.left is None:
                lt = Node.right
                Node = None
                return lt
            elif Node.right is None:
                lt = Node.left
                Node = None
                return lt
            rgt = self.MinimumValueNode(Node.right)
            Node.value = rgt.value
            Node.right = self.delete(rgt.value, Node.right)
        if Node is None:
            return Node
        Node.height = 1 + max(self.height(Node.left), self.height(Node.right))
        balance = self.balance(Node)
        if balance > 1 and self.balance(Node.left) >= 0:
            return self.rotateR(Node)
        if balance < -1 and self.balance(Node.right) <= 0:
            return self.rotateL(Node)
        if balance > 1 and self.balance(Node.left) < 0:
            Node.left = self.rotateL(Node.left)
            return self.rotateR(Node)
        if balance < -1 and self.balance(Node.right) > 0:
            Node.right = self.rotateR(Node.right)
            return self.rotateL(Node)
        return Node

    def find(self, val, Node):
        if not Node:
            return None
        else:
            return self._find(val, Node)

    def _find(self, val, Node):
        if not Node:
            return None
        elif val < Node.value:
            
            return self._find(val, Node.left_child)
        elif val > Node.value:
            return self._find(val, Node.right_child)
        else:
            return Node

# констранты
MIN = -1000
MAX = 1000
summ_AVL = 0
summ_bin = 0

for test in range(10):
  print("  Тест ", test + 1)
  N = pow(2, (10 + test + 1)) - 1
  valArr = []

  print("  Число элементов: ", N + 1)
  for k in range(10):
    bin_tree = binary_search_tree()

    for i in range(N):
      valArr.append(randint(MIN, MAX))

    # Рандомный в бинарном
    start = time.time()
    for i in range(N):
      bin_tree.insert(valArr[i])
    end = time.time()
    sec_diff_bin = end - start

    summ_bin += sec_diff_bin

    start = end = 0
    start = time.time()
    for search in range(1000):
      bin_tree.exists(randint(MIN, MAX))
    end = time.time()
    treeKeySearch_bin = end - start

    start = end = 0
    start = time.time()
    for search in range(1000):
      bin_tree.delete(valArr[search])
    end = time.time()
    delTime_bin = end - start

    bin_tree = None

    # рандомный в AVL

    avl_tree = AVL()
    rt = None

    start1 = time.time()
    for i in range(N):
      avl_tree.insert(valArr[i], rt)
    end1 = time.time()
    sec_diff_AVL = end1 - start1

    summ_AVL += sec_diff_AVL

    start1 = end1 = 0
    start1 = time.time()
    for search in range(1000):
      avl_tree.find(randint(MIN, MAX), rt)
    end1 = time.time()
    treeKeySearch_AVL = end1 - start1

    start1 = end1 = 0
    start1 = time.time()
    for search in range(1000):
      avl_tree.delete(valArr[search], rt)
    end1 = time.time()
    delTime_AVL = end1 - start1

    avl_tree = None

  print(" Рандомный массив \n")
  print(" Бинарное дерево \n")
  print(" Среднее время вставки:", summ_bin / 10, "\n")
  print(" Поиск по дереву (1 операция):", treeKeySearch_bin / 1000, "\n")
  print(" Время на удаление (1 операция):", delTime_bin / 1000, "\n")

  print(" AVL дерево \n")
  print(" Среднее время вставки:", summ_AVL / 10, "\n")
  print(" Поиск по дереву (1 операция):", treeKeySearch_AVL / 1000, "\n")
  print(" Время на удаление (1 операция):", delTime_AVL / 1000, "\n")

  summ_AVL = 0
  summ_bin = 0

  for i in range(N):
    valArr.append(i + 1)

  for k in range(10):
    # отсортированный в бинарном

    bin_tree = binary_search_tree()

    start = end = 0
    start = time.time()
    for i in range(N):
      bin_tree.insert(valArr[i])
    end = time.time()
    sec_diff_bin = end - start

    summ_bin += sec_diff_bin

    start = end = 0
    start = time.time()
    for search in range(1000):
      bin_tree.exists(randint(0, N))
    end = time.time()
    treeKeySearch_bin = end - start

    start = end = 0
    start = time.time()
    for search in range(1000):
      bin_tree.delete(valArr[search])
    end = time.time()
    delTime_bin = end - start

    bin_tree = None

    # отсортированный в AVL

    avl_tree = AVL()
    rt = None

    start1 = end1 = 0
    start1 = time.time()
    for i in range(N):
      avl_tree.insert(valArr[i], rt)
    end1 = time.time()
    sec_diff_AVL = end1 - start1

    summ_AVL += sec_diff_AVL

    start1 = end1 = 0
    start1 = time.time()
    for search in range(1000):
      avl_tree.find(randint(0, N), rt)
    end1 = time.time()
    treeKeySearch_AVL = end1 - start1

    start1 = end1 = 0
    start1 = time.time()
    for search in range(1000):
      avl_tree.delete(valArr[search], rt)
    end1 = time.time()
    delTime_AVL = end1 - start1

    avl_tree = None

  print(" Отсортированный массив \n")
  print(" Бинарное дерево \n")
  print(" Среднее время вставки:", summ_bin / 10, "\n")
  print(" Поиск по дереву (1 операция):", treeKeySearch_bin / 1000, "\n")
  print(" Время на удаление (1 операция):", delTime_bin / 1000, "\n")

  print(" AVL дерево \n")
  print(" Среднее время вставки:", summ_AVL / 10, "\n")
  print(" Поиск по дереву (1 операция):", treeKeySearch_AVL / 1000, "\n")
  print(" Время на удаление (1 операция):", delTime_AVL / 1000, "\n")

  summ_AVL = 0
  summ_bin = 0

  print("------------------------------------------------")

      
#tree = fill_tree(tree)

#tree.print_tree()

#print("Высота дерева: "+str(tree.height()))
#print(tree.search(70))