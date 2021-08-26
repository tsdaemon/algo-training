class Heap():
    def __init__(self):
        super().__init__()
        self.arr = []

    def top(self) -> int:
        return self.arr[0]

    def insert(self, val: int):
        self.arr.append(val)
        self._bubble_up(self.max_index)

    def delete(self, val: int):
        ind = self.arr.index(val)
        self.arr[ind] = self.arr[self.max_index]
        del self.arr[self.max_index]
        self._push_down(ind)

    def _push_down(self, ind: int):
        while ind < self.max_index:
            child_index = self._get_smallest_child(ind)
            if child_index is None:
                break
            if self.arr[child_index] < self.arr[ind]:
                self._swap(ind, child_index)
                ind = child_index
            else:
                break

    @staticmethod
    def _get_parent_index(ind: int):
        return (ind-1)//2

    @staticmethod
    def _get_child_indices(ind: int):
        return 2*ind+1, 2*ind+2

    @property
    def max_index(self):
        return len(self.arr)-1

    def _get_smallest_child(self, ind: int):
        child_indices = self._get_child_indices(ind)
        smallest_child_ind = child_indices[0]
        if smallest_child_ind > self.max_index:
            return
        smallest_child = self.arr[smallest_child_ind]
        for i in child_indices[1:]:
            if i > self.max_index:
                break
            if smallest_child > self.arr[i]:
                smallest_child = self.arr[i]
                smallest_child_ind = i
        return smallest_child_ind

    def _swap(self, ind1: int, ind2: int):
        temp = self.arr[ind1]
        self.arr[ind1] = self.arr[ind2]
        self.arr[ind2] = temp

    def _bubble_up(self, ind: int):
        while ind > 0:
            curr_ind = ind
            ind = self._get_parent_index(ind)
            if self.arr[ind] > self.arr[curr_ind]:
                self._swap(ind, curr_ind)
            else:
                break
