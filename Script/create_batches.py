import kaggle, os, cv2, random
import numpy as np
from config import dir_dataset_raw, dir_dataset_train, dir_dataset_val, dir_dataset_test
from config import facial_expression_rev
import Preprocess

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
    
    random.shuffle(dataset)
    os.makedirs(target)
    number_of_batch = int(np.ceil(len(dataset)/batch_size))
    
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
    create_batches( os.path.join(dir_dataset_raw, 'train/'), dir_dataset_train, 32 )
    create_batches( os.path.join(dir_dataset_raw, 'val/'), dir_dataset_val, 32 )
    create_batches( os.path.join(dir_dataset_raw, 'test/'), dir_dataset_test, 32 )
    