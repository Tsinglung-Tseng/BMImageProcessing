import matplotlib.pyplot as plt
import numpy as np
import sys
from config import SHOW
from PIL import Image


class Otsu:
    def __init__(self, img):
        self.img = img
        self.gray_levels = np.arange(256)
        self.shape = self.img.shape
        self.N = np.prod(self.shape)
        self.flatten_img = np.reshape(np.array(self.img), np.prod(self.shape))
        self.hist = np.array(
            [len(self.flatten_img[self.flatten_img == i]) for i in self.gray_levels]
        )
        self.P = self.hist / self.N
        self.total_mean = np.sum(self.gray_levels * self.P)
        self.total_variance = np.sum(
            np.square(self.gray_levels - self.total_mean) * self.P
        )
        self.class_frequency = [
            (np.sum(self.P[:T]), np.sum(self.P[T:])) for T in self.gray_levels
        ]

    def plot_hist(self, T=None):
        plt.figure()
        plt.plot(self.gray_levels, self.hist, label="hist")
        if T is None:
            plt.axvline(self.threshold(), color="k", ls="--")
        else:
            plt.axvline(T, color="k", ls="--")
        plt.title("Histogram")
        plt.xlabel("Gray Level")
        plt.ylabel("Count")
        plt.legend()
        plt.savefig(SHOW.HIST)

    def plot_criterion_function(self):
        plt.plot(
            self.gray_levels,
            [self.criterion_function(T) for T in self.gray_levels],
            label="entropy",
        )
        plt.title("Criterion Function")
        plt.xlabel("Gray Level")
        plt.ylabel("Entropy")
        plt.legend()

    def show_origin_image(self):
        plt.figure()
        plt.imshow(self.img, cmap="gray")
        plt.title("Origin Image")
        plt.savefig(SHOW.ORIGIN)

    def show_binary_image(self, T=None):
        plt.figure()
        if T is None:
            T = self.threshold()
        bin_image = np.zeros(self.shape)
        bin_image[self.img > T] = 1
        plt.imshow(bin_image, cmap="gray")
        plt.title(f"Binary Image (threshold={T})")
        plt.savefig(SHOW.BINARY)

    def class_mean(self, T):
        freq_back, freq_front = self.class_frequency[T]
        return (
            np.sum(self.gray_levels[:T] * self.P[:T] / freq_back),
            np.sum(self.gray_levels[T:] * self.P[T:] / freq_front),
        )

    def between_class_variance(self, T):
        w_0, w_1 = self.class_frequency[T]
        u_0, u_1 = self.class_mean(T)
        return w_0 * w_1 * np.square(u_1 - u_0)

    def criterion_function(self, T):
        return self.between_class_variance(T) / self.total_variance

    def threshold(self):
        return np.argmax([self.criterion_function(T) for T in self.gray_levels])

    def __call__(self, manual_T=None):
        if manual_T is None:
            self.plot_hist()
            self.show_origin_image()
            self.show_binary_image()
        else:
            self.plot_hist(manual_T)
            self.show_origin_image()
            self.show_binary_image(manual_T)


class Entropy:
    def __init__(self, img):
        self.img = img
        self.gray_levels = np.arange(256)
        self.shape = self.img.shape
        self.flatten_img = np.reshape(np.array(self.img), np.prod(self.shape))
        self.hist = np.array(
            [len(self.flatten_img[self.flatten_img == i]) for i in self.gray_levels]
        )

    def plot_hist(self):
        plt.figure()
        plt.plot(self.gray_levels, self.hist, label="hist")
        plt.axvline(self.threshold(), color="k", ls="--")
        plt.title("Histogram")
        plt.xlabel("Gray Level")
        plt.ylabel("Count")
        plt.legend()
        plt.savefig(SHOW.HIST)

    def plot_threshuld_to_entropy(self):
        plt.plot(self.gray_levels, [self.H(i) for i in range(256)], label="entropy")
        plt.title("Entropy-Threshold")
        plt.xlabel("Gray Level")
        plt.ylabel("Entropy")
        plt.legend()

    def show_origin_image(self):
        plt.figure()
        plt.imshow(self.img, cmap="gray")
        plt.title("Origin Image")
        plt.savefig(SHOW.ORIGIN)

    def show_binary_image(self, T=None):
        plt.figure()
        if T is None:
            T = self.threshold()
        bin_image = np.zeros(self.shape)
        bin_image[self.img > T] = 1
        plt.imshow(bin_image, cmap="gray")
        plt.title(f"Binary Image (threshold={T})")
        plt.savefig(SHOW.BINARY)

    def H(self, T):
        hist_b, hist_w = self.hist[:T], self.hist[T:]
        N_b = np.sum(hist_b)
        N_w = np.sum(hist_w)

        p_i_b = hist_b / N_b
        p_i_w = hist_w / N_w

        H_b = -np.sum(p_i_b * np.log(p_i_b))
        H_w = -np.sum(p_i_w * np.log(p_i_w))
        return H_b + H_w

    def threshold(self):
        return np.argmax([self.H(i) for i in range(256)])

    def __call__(self):
        self.plot_hist()
        self.show_origin_image()
        self.show_binary_image()
