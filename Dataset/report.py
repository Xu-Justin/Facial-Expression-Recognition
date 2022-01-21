import os

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
    report('fer2013/train/')
    report('fer2013/val/')
    report('fer2013/test/')
    print()
    
    report('personal/train/')
    report('personal/val/')
    print()
    
    report('mix/train/')
    report('mix/val/')
    print()