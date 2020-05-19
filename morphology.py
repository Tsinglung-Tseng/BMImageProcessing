import numpy as np


class Image:
    def __init__(self, img):
        self.img = np.array(img)
        self.shape = self.img.shape

    def __getitem__(self, index):
        x, y = index
        if x < 0 or y < 0 or x >= self.shape[0] or y >= self.shape[1]:
            return 0
        else:
            return self.img[x][y]
    
    def __setitem__(self, index, value):
        self.img[index[0]][index[1]] = value        

    def __iter__(self):
        for index, value in np.ndenumerate(self.img):
            yield index, value

    def padding(self, pad_width=1, method="edge"):
        if method == "edge":
            return np.pad(self.img, pad_width=pad_width, mode="edge")
        if isinstance(method, int):
            return np.pad(
                self.img, pad_width=pad_width, mode="constant", constant_values=method
            )
        else:
            raise ValueError(f"""Padding method {mothod} not supported!""")


class MorphKernel:
    def __init__(self, value, center):
        self.value = np.array(value)
        self.center = np.array(center)

    def _relative_index_to_abs_index(self):
        pass

    def _abs_index_to_relative_index(self, abs_index):
        pass

    @property
    def shape(self):
        if len(self.value.shape) == 1:
            return 1, self.value.shape[0]
        if len(self.value.shape) == 2:
            return self.value.shape

    def __getitem__(self, index):
        x, y = np.array(index) + self.center
        if len(self.value.shape)==1:
            pass 
        return self.value[x][y]

    def __iter__(self):
        for index, value in np.ndenumerate(self.value):
            if len(index)==1:
                ind = (np.array(index) - self.center)
                yield tuple([0, ind[1]]), value
            else:
                yield tuple(np.array(index) - self.center), value



class MorphologyBuffer(Image):
    def __init__(self, img: Image, kernel: MorphKernel, op):
        self.buffer = np.zeros(
            np.append(
                img.shape + (np.array(kernel.shape) // 2) * 2, np.prod(kernel.shape)
            )
        )

    def __getitem__(self, index):
        pass 

    def dump_result(self):
        pass


def dilation(img: Image, kernel: MorphKernel):
    # padded_img = img.padding(kernel.shape[0] // 2)
    result = np.zeros(img.shape)

    k_a, k_b = kernel.value.shape

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            buffer = np.zeros((k_a, k_b))
            for a in range(k_a):
                for b in range(k_b):
                    buffer[a][b] = padded_img[x - a + 1][y - b + 1] * kernel.value[a][b]
            kernel_result = np.sum(buffer)
            if kernel_result > 255:
                result[x][y] = 255
            elif kernel_result < 0:
                result[x][y] = 0
            else:
                result[x][y] = kernel_result
    return result
