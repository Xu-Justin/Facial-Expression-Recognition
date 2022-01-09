import os
from google_drive_downloader import GoogleDriveDownloader as gdd

def download_model(model_name, id, unzip=True):
    print('Downloading %s model from %s'%(model_name, id))
    gdd.download_file_from_google_drive(file_id=id, dest_path=os.path.join(root, 'Model', '%s.zip'%model_name), unzip=unzip)
    print('Successfully downloaded %s model from %s'%(model_name, id))

if __name__ == '__main__':
    download_model('v1-cnn', '1Pjk3pRu_0A_4Ip8VohAHgJriWx48w_P-')
    download_model('v2-resnet-50', '1-Wp30ij337nUmkx-8TokPHhKZJXxWuEI')
    