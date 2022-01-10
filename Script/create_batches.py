from config import train_fer2013, val_fer2013, train_personal, val_personal, test
from config import train_fer2013_batch, val_fer2013_batch, train_personal_batch, val_personal_batch, test_batch
from config import facial_expression_rev

import os, cv2, Preprocess, shutil
import numpy as np

def create_batches(source, target, batch_size):
    dataset = []
    
    expressions = os.listdir(source)
    for expression in expressions:
        print('reading %s from %s'%(expression, source))
        expression_path = os.path.join(source, expression)
        images_name = os.listdir(expression_path)
        for image_name in images_name:
            image_path = os.path.join(expression_path, image_name)
            image = cv2.imread(image_path, 0)
            dataset.append((image, facial_expression_rev[expression]))
    
    np.random.shuffle(dataset)
    number_of_batch = int(np.ceil(len(dataset)/batch_size))
    
    if(os.path.exists(target)):
        shutil.rmtree(target)
    os.makedirs(target)
    
    for i in range(number_of_batch):
        X = []
        y = []
        for j in range(batch_size):
            index = batch_size * i + j
            if(index >= len(dataset)): break
            print('creating image to batches (%d/%d)'%(index, len(dataset)), end='\r')
            
            image, expression_index = dataset[index]
            
            Xs = image.copy()
            ys = expression_index
            
            Xs = Preprocess.preprocess_gray(Xs)
            ys = Preprocess.preprocess_label(ys)
            
            X.append(Xs)
            y.append(ys)
        
        X = np.asarray(X, 'uint8')
        y = np.asarray(y, 'uint8')
        
        batch = np.array([tuple(X), tuple(y)], dtype='object')
        dir_batch = os.path.join(target, 'batch-%d'%i)
        
        np.save(dir_batch, batch)
    
    print('Finished created image to batches from %s to %s (%d)'%(source, target, len(dataset)))
    
if __name__ == '__main__': 
    create_batches( train_fer2013, train_fer2013_batch, 32 )
    create_batches( val_fer2013, val_fer2013_batch, 32 )
    create_batches( train_personal, train_personal_batch, 32 )
    create_batches( val_personal, val_personal_batch, 32 )
    create_batches( test, test_batch, 32 )