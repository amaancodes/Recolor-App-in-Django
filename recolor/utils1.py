import numpy as np
import cv2
from PIL import Image


class Transforms1:
    """
    Holds transformation matrices.
    """

    @staticmethod
    def rgb_to_lms():
        """
        Matrix for RGB color-space to LMS color-space transformation.
        """
        return np.array([[17.8824   , 43.5161 , 4.11935],
                         [ 3.45565  , 27.1554 , 3.86714],
                         [ 0.0299566, 0.184309, 1.46709]]).T

    @staticmethod
    def lms_to_rgb() -> np.ndarray:
        """
        Matrix for LMS colorspace to RGB colorspace transformation.
        """
        return np.array([[ 0.0809, -0.1305,  0.1167],
                         [-0.0102,  0.0540, -0.1136],
                         [-0.0004, -0.0041,  0.6935]]).T

    @staticmethod
    def lms_protanopia_sim(degree: float = 1.0) -> np.ndarray:
        """
        Matrix for Simulating Protanopia colorblindness from LMS color-space.
        :param degree: Protanopia degree.
        """
        return np.array([[0, 2.02344, -2.52581],
                         [0, 1      , 0       ],
                         [0, 0      , 1       ]]).T


    @staticmethod
    def correction_matrix() -> np.ndarray:
        """
        Matrix for Correcting Colorblindness (protanomaly) from LMS color-space.
        """
        
        return np.array([[1   , 0  , 0   ],
                         [0.5 , 0.5, 0   ],
                         [0.25, 0  , 0.75]]).T


class Utils1:
    """
    Couple of utils for loading the images.
    """
    @staticmethod
    def load_rgb(image):
        # img_rgb = np.array(Image.open(path)) / 255
        image = image / 255
        return image

    @staticmethod
    def load_lms(image):
        # img_rgb = np.array(Image.open(path)) / 255
        image = image / 255
        img_lms = np.dot(image[:,:,:3], Transforms1.rgb_to_lms())

        return img_lms
