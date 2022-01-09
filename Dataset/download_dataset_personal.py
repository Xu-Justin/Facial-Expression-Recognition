import os
from google_drive_downloader import GoogleDriveDownloader as gdd

def download(id, target, unzip=False):
    print('Downloading %s to %s'%(id, target))
    gdd.download_file_from_google_drive(file_id=id, dest_path=target, unzip=unzip)
    print('Successfully downloaded %s to %s'%(id, target))
    
if __name__ == '__main__':
    os.makedirs('raw/', exist_ok=True)
    download('1zJ_b5j-f_VpfLAWh2lapvYudpL-9hNJx', 'raw/personal_dataset.zip', unzip=True)
    os.remove('raw/personal_dataset.zip')