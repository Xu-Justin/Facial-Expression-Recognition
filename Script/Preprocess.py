import numpy as np
import cv2
from config import input_shape, output_shape

def getInterpolation(cur_dim, target_dim):
    if(cur_dim[0] * cur_dim[1] < target_dim[0] * target_dim[1]): return cv2.INTER_CUBIC
    else: return cv2.INTER_AREA

def preprocess_gray(image_gray):
    image = image_gray.copy()
    image = cv2.cv2.equalizeHist(image)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    interpolation = getInterpolation(image.shape, (input_shape[1], input_shape[0]))       
    image = cv2.resize(image, (input_shape[1], input_shape[0]), interpolation = interpolation)
    return image

def preprocess_label(expression_index):
    label = np.full(output_shape, 0)
    label[expression_index] = 1
    return label