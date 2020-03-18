import numpy as np


class Image:
    def __init__(self, img):
        self.img = np.array(img)
        self.shape = self.img.shape
    
    def padding(self, pad_width=1, method='edge'):
        if method=='edge':
            return np.pad(self.img, pad_width=pad_width, mode='edge')
        if isinstance(method, int):
            return np.pad(self.img, pad_width=pad_width, mode='constant', constant_values=method)
        else:
            raise ValueError(f"""Padding method {mothod} not supported!""")


class Kernel:
    def __init__(self, axis='x', ktype='sobel', value=None):
        if value is not None:
            self.value = np.array(value)
            pass
        if axis=='x':
            if ktype=='roberts':
                self.value=np.array([
                    [-1, 0],
                    [0, 1]
                ])
            if ktype=='prewitt':
                self.value=np.array([
                    [-1, -1, -1],
                    [0, 0, 0],
                    [1, 1, 1]
                ])
            if ktype=='sobel':
                self.value=np.array([
                    [-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]
                ])
                
        if axis=='y':
            if ktype=='roberts':
                self.value=np.array([
                    [0, -1],
                    [1, 0]
                ])
            if ktype=='prewitt':
                self.value=np.array([
                    [-1, 0, 1],
                    [-1, 0, 1],
                    [-1, 0, 1]
                ])
            if ktype=='sobel':
                self.value=np.array([
                    [-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]
                ])
                
    @property
    def shape(self):
        return self.value.shape
    
    def __getitem__(self, index):
        return self.value[index[0]+1][index[1]+1]

def convolution(img: Image, kernel: Image):
    
    padded_img = img.padding(kernel.shape[0]//2)
    result = np.zeros(img.shape)
    
    k_a, k_b = kernel.value.shape
    
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            buffer = np.zeros((k_a, k_b))
            for a in reversed(range(k_a)):
                for b in reversed(range(k_b)):
                    buffer[a][b] = padded_img[x-a+1][y-b+1]*kernel.value[a][b]
            kernel_result = np.sum(buffer)
            if kernel_result>255:
                result[x][y] = 255
            elif kernel_result<0:
                result[x][y] = 0
            else:
                result[x][y] = kernel_result
    return result
