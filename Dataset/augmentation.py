import os, shutil, cv2
import numpy as np
from tensorflow import keras

augmentation = keras.Sequential(
    [
        keras.layers.RandomFlip(mode='horizontal'),
        keras.layers.RandomZoom(height_factor=(-0.15,0.15)),
        keras.layers.RandomTranslation(height_factor=(-0.2,0.2), width_factor=(-0.2,0.2)),
        keras.layers.RandomRotation(factor = (0.1))
    ]
)

def augment(source, target, num):
    # os.makedirs(target)
    file_names = os.listdir(source)
    
    batch_size = 512
    num_batch = int(np.ceil(num/batch_size))
    
    for i in range(num_batch):
        n = min( batch_size, num-(i*batch_size) )
        selected_file_names = np.random.choice(file_names, n, replace=True)
        
        images = []
        for file_name in selected_file_names:
            image = cv2.imread( os.path.join(source, file_name) )
            images.append(image)
        images = np.asarray(images, 'uint8')
        images = augmentation(images).numpy()

        for j, image in enumerate(images):
            print('augmenting %s (%d/%d)'%(source, i*batch_size+j+1, num), end='\r')
            cv2.imwrite( os.path.join(target, '%d.jpg'%(i*batch_size+j)), image )
    print()

def augment_inplace(source, num):
    os.makedirs("temp/%s"%source)
    augment("%s"%source, "temp/%s"%source, num)
    shutil.rmtree("%s"%source)
    os.rename("temp/%s"%source,"%s"%source)
    shutil.rmtree("temp/")

def augment_expression(source, num):
    list_expression = os.listdir(source)
    for expression in list_expression:
        augment_inplace(os.path.join(source, expression), num )
        
if __name__ == '__main__':
    augment_expression('fer2013/train/', 4000)
    augment_expression('fer2013/val/', 1000)
    augment_expression('personal/train/', 500)
    augment_expression('personal/val/', 100)