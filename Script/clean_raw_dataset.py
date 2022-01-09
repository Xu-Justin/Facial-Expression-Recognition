import os, cv2
from config import dir_resources, root

cascade_name = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier( os.path.join(dir_resources, 'haarcascade', cascade_name) )

def clear(source, target):
    list_expression = os.listdir(source)
    for expression in list_expression:
        print('Cleaning %s'%(os.path.join(source, expression)))
        
        os.makedirs(os.path.join(target, expression))
        list_file_name = os.listdir(os.path.join(source, expression))
        
        images = []
        for i, file_name in enumerate(list_file_name):
            print('Reading %s (%d/%d)'%(os.path.join(source, expression), i+1, len(list_file_name)), end='\r')
            
            image = cv2.imread( os.path.join(source, expression, file_name), 0)
            image = cv2.equalizeHist(image)
            bounding_boxes = face_cascade.detectMultiScale(image)
            for (x,y,w,h) in bounding_boxes:
                sub_image = image[y:y+h, x:x+w]
                images.append(sub_image)
        
        for i, image in enumerate(images):
            print('Saving %s (%d/%d)'%(os.path.join(target, expression), i+1, len(images)), end='\r')
            image = cv2.resize(image, (48,48), interpolation = cv2.INTER_AREA)
            image = cv2.equalizeHist(image)
            cv2.imwrite( os.path.join(target, expression, '%d.jpg'%i), image )
        
        print('Finished cleaned %s to %s'%( os.path.join(source, expression), os.path.join(target, expression) ))
        
if __name__ == '__main__':
    clear( os.path.join(root, 'Dataset/personal_dataset/raw/'), os.path.join(root, 'Dataset/personal_dataset/cleaned/') )