import os, shutil
import numpy as np
np.random.seed(42)

def split(source, target_train, target_val, train_size):
    list_expression = os.listdir(source)
    for expression in list_expression:
        print('Splitting %s'%(os.path.join(source, expression)))
        print('Original size: %d'%(len(os.listdir( os.path.join(source, expression) ))))
        
        os.makedirs(os.path.join(target_train, expression))
        os.makedirs(os.path.join(target_val, expression))
        
        list_file_name = os.listdir(os.path.join(source, expression))
        np.random.shuffle(list_file_name)
        
        list_train_file_name = list_file_name[:int(len(list_file_name)*train_size)]
        list_val_file_name = list_file_name[int(len(list_file_name)*train_size):]
        
        for i, file_name in enumerate(list_train_file_name):
            print('Copying files (%d/%d)'%(i+1, len(list_train_file_name)), end='\r')
            shutil.copyfile( os.path.join(source, expression, file_name), os.path.join(target_train, expression, file_name) )
        print()
        for i, file_name in enumerate(list_val_file_name):
            print('Copying files (%d/%d)'%(i+1, len(list_val_file_name)), end='\r')
            shutil.copyfile( os.path.join(source, expression, file_name), os.path.join(target_val, expression, file_name) )
        print()
        print('Splited into train   : %d     '%(len(os.listdir( os.path.join(target_train, expression) ))))
        print('Splited into Val     : %d     '%(len(os.listdir( os.path.join(target_val, expression) ))))
    
if __name__ == '__main__':
    os.rename('raw/train/', 'raw/temp/')
    split('raw/temp/', 'raw/train/', 'raw/val/', 0.8)
    shutil.rmtree('raw/temp/')