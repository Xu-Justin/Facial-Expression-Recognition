import os, shutil

def copy(source, target, prefix):
    list_expression = os.listdir(source)
    for expression in list_expression:
        os.makedirs(os.path.join(target, expression), exist_ok=True)
        
        list_file_name = os.listdir(os.path.join(source, expression))
        for i, file_name in enumerate(list_file_name):
            print('Copying files to %s (%d/%d)'%(os.path.join(target, expression), i+1, len(list_file_name)), end='\r')
            shutil.copyfile( os.path.join(source, expression, file_name), os.path.join(target, expression, prefix+file_name) )
        print()    

def merge(source1, source2, target):
    copy(source1, target, 's1-')
    copy(source2, target, 's2-')

def remove(path):
    if(os.path.exists(path)):
        shutil.rmtree(path)

if __name__ == '__main__':
    remove('mix')
    merge('fer2013/train/', 'personal/train/', 'mix/train')
    merge('fer2013/val/', 'personal/val/', 'mix/val')