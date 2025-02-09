from typing import Optional, List


class DoublyListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


def createDoublyLinkedList(arr: List[int]) -> Optional[DoublyListNode]:
    # Optional是 Python 的 typing 模块中的一个泛型，
    # Optional[X] 等价于 Union[X, None]，
    # 即表示返回的值要么是类型 X（这里是 DoublyListNode），要么是 None
    #Optional[DoublyListNode] 表示返回值要么是 DoublyListNode，要么是 None

    # if arr is None or len(arr) == 0:
    #     return None
    if not arr:
        return None
    # 当arr = 0或 arr = False时，第一条 if 语句不会返回None，因为它只检查None和空容器。
    # 而第二条 if 语句会返回None，因为它将0和 False也视为“假值”。
    head = DoublyListNode(arr[0])
    cur = head

    # for 循环迭代创建双链表
    for val in arr[1:]:
        new_node = DoublyListNode(val)
        cur.next = new_node
        new_node.prev = cur
        cur = cur.next  #为连接下一个节点做准备

    return head


# 创建一条双链表
head = createDoublyLinkedList([1, 2, 3, 4, 5])
tail = None

# 从头节点向后遍历双链表
p = head
while p:
    print(p.val)
    tail = p
    p = p.next

# 从尾节点向前遍历双链表
p = tail
while p:
    print(p.val)
    p = p.prev

# 创建一条双链表
head = createDoublyLinkedList([1, 2, 3, 4, 5])

# 在第 3 个节点后面插入新节点 66
# 找到第 3 个节点
p = head
for _ in range(2):
    p = p.next

# 组装新节点
newNode = DoublyListNode(66)
newNode.next = p.next
newNode.prev = p

# 插入新节点  这里的顺序不能改
p.next.prev = newNode
p.next = newNode

# 现在链表变成了 1 -> 2 -> 3 -> 66 -> 4 -> 5