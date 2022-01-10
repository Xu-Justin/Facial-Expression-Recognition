import os, shutil
from google_drive_downloader import GoogleDriveDownloader as gdd

def download_model(model_name, id, unzip=True):
    print('Downloading %s model from %s'%(model_name, id))
    gdd.download_file_from_google_drive(file_id=id, dest_path=os.path.join(root, 'Model', '%s.zip'%model_name), unzip=unzip)
    print('Successfully downloaded %s model from %s'%(model_name, id))

if __name__ == '__main__':
    trained_model = [
        {
            'model_name' : 'v1-resnet-50-fer2013',
            'id' : None,
        },
        {
            'model_name' : 'v2-resnet-50-personal',
            'id' : None,
        }
    ]
    
    for model in trained_model:
        download_model(model['model_name'], model['id'])
        shutil.rmtree('%s.zip'%model[model_name])