class MyArrayList:
    # 默认初始容量
    INIT_CAP = 1

    def __init__(self, init_capacity=None):
        self.data = [None] * (init_capacity if init_capacity is not None else self.__class__.INIT_CAP)
        # self.__class__.INIT_CAP 调用的是类属性，如果直接写self.INIT_CAP，
        # 那么会调用def __init__(self, init_capacity=None):中的INIT_CAP变量内容
        # 但是这里确实可以直接写self.INIT_CAP，
        # 因为初始化方法def __init__(self, init_capacity=None):中没有同名变量
        # 这里是为了规范
        self.size = 0

    # 增
    def add_last(self, e):
        cap = len(self.data)
        # 看 data 数组容量够不够
        if self.size == cap:
            self._resize(2 * cap)
        # 在尾部插入元素
        self.data[self.size] = e
        self.size += 1

    def add(self, index, e):
        # 检查索引越界
        self._check_position_index(index)

        cap = len(self.data)
        # 看 data 数组容量够不够
        if self.size == cap:
            self._resize(2 * cap)

        # 搬移数据 data[index..] -> data[index+1..]
        # 给新元素腾出位置
        for i in range(self.size - 1, index - 1, -1):
            self.data[i + 1] = self.data[i]

        # 插入新元素
        self.data[index] = e

        self.size += 1

    def add_first(self, e):
        self.add(0, e)

    # 删
    def remove_last(self):
        if self.size == 0:
            raise NoSuchElementException
        cap = len(self.data)
        # 可以缩容，节约空间
        if self.size == cap // 4:
            self._resize(cap // 2)

        deleted_val = self.data[self.size - 1]
        # 删除最后一个元素
        self.data[self.size - 1] = None
        self.size -= 1

        return deleted_val

    def remove(self, index):
        # 检查索引越界
        self._check_element_index(index)

        cap = len(self.data)
        # 可以缩容，节约空间
        if self.size == cap // 4:
            self._resize(cap // 2)

        deleted_val = self.data[index]

        # 搬移数据 data[index+1..] -> data[index..]
        for i in range(index + 1, self.size):
            self.data[i - 1] = self.data[i]

        self.data[self.size - 1] = None
        self.size -= 1

        return deleted_val

    def remove_first(self):
        return self.remove(0)

    # 查
    def get(self, index):
        # 检查索引越界
        self._check_element_index(index)

        return self.data[index]

    # 改
    def set(self, index, element):
        # 检查索引越界
        self._check_element_index(index)
        # 修改数据
        old_val = self.data[index]
        self.data[index] = element
        return old_val

    # 工具方法
    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    # 将 data 的容量改为 newCap
    def _resize(self, new_cap):
        temp = [None] * new_cap
        for i in range(self.size):
            temp[i] = self.data[i]
        self.data = temp

    def _is_element_index(self, index):
        return 0 <= index < self.size

    def _is_position_index(self, index):
        return 0 <= index <= self.size

    def _check_element_index(self, index):
        if not self._is_element_index(index):
            raise IndexOutOfBoundsException(f"Index: {index}, Size: {self.size}")

    def _check_position_index(self, index):
        if not self._is_position_index(index):
            raise IndexOutOfBoundsException(f"Index: {index}, Size: {self.size}")

    def display(self):
        print(f"size = {self.size}, cap = {len(self.data)}")
        print(self.data)


# Usage example
if __name__ == "__main__":
    arr = MyArrayList(init_capacity=2)

    # 添加 5 个元素
    for i in range(1, 6):
        arr.add_last(i)

    arr.remove(3)
    arr.add(1, 9)
    arr.add_first(100)
    val = arr.remove_last()

    # 100 1 9 2 3
    for i in range(arr.size):
        print(arr.get(i))