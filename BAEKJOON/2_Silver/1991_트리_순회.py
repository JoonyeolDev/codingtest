# https://www.acmicpc.net/problem/1991
# 트리 순회

# 문제
# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.
# 예를 들어 위와 같은 이진 트리가 입력되면,

# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
# 가 된다.

# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

from sys import stdin
input = stdin.readline

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traversal(root, arr):
    if root:
        arr[0] += root.value
        traversal(root.left, arr)
        arr[1] += root.value
        traversal(root.right, arr)
        arr[2] += root.value

tree = {}
root = TreeNode('A')
tree['A'] = root

for _ in range(int(input())):
    node, left, right = input().split()

    if left != '.':
        tree[node].left = TreeNode(left)
        tree[left] = tree[node].left
    if right != '.':
        tree[node].right = TreeNode(right)
        tree[right] = tree[node].right

arr = ['', '', '']
traversal(root, arr)
print('\n'.join(arr))
# 31120KB, 40ms, 751B


# 초기 코드
from sys import stdin
input = stdin.readline

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

tree = {}
n = int(input())

for _ in range(n):
    node, left, right = input().split()
    if node == 'A':
        root = TreeNode(node)
        tree[node] = root
    if left != '.':
        tree[node].left = TreeNode(left)
        tree[left] = tree[node].left
    if right != '.':
        tree[node].right = TreeNode(right)
        tree[right] = tree[node].right

def preorder_traversal(root, arr=None):
    if arr == None:
        arr = []
    if root:
        arr.append(root.value)
        preorder_traversal(root.left, arr)
        preorder_traversal(root.right, arr)
    return arr

def inorder_traversal(root, arr=None):
    if arr == None:
        arr = []
    if root:
        inorder_traversal(root.left, arr)
        arr.append(root.value)
        inorder_traversal(root.right, arr)
    return arr

def postorder_traversal(root, arr=None):
    if arr == None:
        arr = []
    if root:
        postorder_traversal(root.left, arr)
        postorder_traversal(root.right, arr)
        arr.append(root.value)
    return arr

print(''.join(preorder_traversal(root)))
print(''.join(inorder_traversal(root)))
print(''.join(postorder_traversal(root)))
# 31120KB, 40ms, 1331B
