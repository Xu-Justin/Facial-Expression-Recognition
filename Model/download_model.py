import os
from google_drive_downloader import GoogleDriveDownloader as gdd

def download_model(model_name, id, unzip=True):
    print('Downloading %s model from %s'%(model_name, id))
    gdd.download_file_from_google_drive(file_id=id, dest_path=os.path.join(root, 'Model', '%s.zip'%model_name), unzip=unzip)
    print('Successfully downloaded %s model from %s'%(model_name, id))

if __name__ == '__main__':
    download_model('v1-resnet-50-fer2013', '1cskda0niSBXBo7PpYzYiK8rkz6Ppnf0Y')
    download_model('v2-resnet-50-personal', '10ZzUgz8hWHwO_pzSzYlVnvq0Mrw2dbw_')
    
