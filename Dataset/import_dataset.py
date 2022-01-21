import os, shutil
import kaggle
import numpy as np
np.random.seed(42)

from google_drive_downloader import GoogleDriveDownloader as gdd

def download_kaggle_dataset(dataset_name, path):
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset_name, force=True, path=path, quiet=False, unzip=True)

def download(id, target, unzip=False):
    gdd.download_file_from_google_drive(file_id=id, dest_path=target, unzip=unzip)
    
def split(source, target_train, target_val, train_size):
    list_expression = os.listdir(source)
    for expression in list_expression:
        print('Splitting %s (%d)'%(os.path.join(source, expression), len(os.listdir(os.path.join(source, expression))) ))
        
        os.makedirs(os.path.join(target_train, expression))
        os.makedirs(os.path.join(target_val, expression))
        
        list_file_name = os.listdir(os.path.join(source, expression))
        np.random.shuffle(list_file_name)
        
        list_train_file_name = list_file_name[:int(len(list_file_name)*train_size)]
        list_val_file_name = list_file_name[int(len(list_file_name)*train_size):]
        
        for i, file_name in enumerate(list_train_file_name):
            print('Copying files to %s (%d/%d)'%(os.path.join(target_train, expression), i+1, len(list_train_file_name)), end='\r')
            shutil.copyfile( os.path.join(source, expression, file_name), os.path.join(target_train, expression, file_name) )
        print()
        for i, file_name in enumerate(list_val_file_name):
            print('Copying files to %s (%d/%d)'%(os.path.join(target_val, expression), i+1, len(list_val_file_name)), end='\r')
            shutil.copyfile( os.path.join(source, expression, file_name), os.path.join(target_val, expression, file_name) )
        print()

def copy(source, target):
    list_expression = os.listdir(source)
    for expression in list_expression:
        os.makedirs(os.path.join(target, expression), exist_ok=True)
        
        list_file_name = os.listdir(os.path.join(source, expression))
        for i, file_name in enumerate(list_file_name):
            print('Copying files to %s (%d/%d)'%(os.path.join(target, expression), i+1, len(list_file_name)), end='\r')
            shutil.copyfile( os.path.join(source, expression, file_name), os.path.join(target, expression, file_name) )
    print()    

def merge(source1, source2, target):
    copy(source1, target)
    copy(source2, target)
        
def remove(path):
    if(os.path.exists(path)):
        shutil.rmtree(path)

def report(path):
    print("%s"%path)
    total = 0
    list_expression = os.listdir(path)
    for expression in list_expression:
        list_file_name = os.listdir(os.path.join(path, expression))
        print("%-20s : %d"%(os.path.join(path, expression), len(list_file_name)))
        total += len(list_file_name)
    print("Total : %d"%total)
    print()    

if __name__ == '__main__':
    remove('fer2013')
    remove('personal')
    
    os.makedirs('raw/')
    download_kaggle_dataset('msambare/fer2013', 'raw/')
    split('raw/train/', 'fer2013/train/', 'fer2013/val/', train_size = 0.8)
    os.rename('raw/test', 'fer2013/test/')
    shutil.rmtree('raw/')
    
    os.makedirs('raw/')
    download('1zJ_b5j-f_VpfLAWh2lapvYudpL-9hNJx', 'raw/personal_dataset.zip', unzip=True)
    split('raw/train/', 'personal/train/', 'personal/val/', train_size = 0.8)
    shutil.rmtree('raw/')
    
    print()
    report('fer2013/train/')
    report('fer2013/val/')
    report('fer2013/test/')
    
    print()
    report('personal/train/')
    report('personal/val/')
    
    print()
    report('mix/train/')
    report('mix/val/')