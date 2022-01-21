import os, shutil
from google_drive_downloader import GoogleDriveDownloader as gdd

def download_model(model_name, id, unzip=True):
    print('Downloading %s model from %s'%(model_name, id))
    if (os.path.exists('%s/'%model_name)):
       shutil.rmtree('%s/'%model_name)
    gdd.download_file_from_google_drive(file_id=id, dest_path='./%s.zip'%(model_name), unzip=unzip, showsize=True)
    os.remove('./%s.zip'%(model_name))
    print('Successfully downloaded %s model from %s'%(model_name, id))


if __name__ == '__main__':
    download_model('v1-resnet50', '1CdMDOS5n_H5FY-Udv7sThbhECrawznAz')
    download_model('v2.1-vgg16', '1yWuaRTjHa0gaNsWRvGOXqarpG6nVyTz2')
    download_model('v2.2-vgg16', '1aovQielPjWMas7nFsI5NG79ak_3iriUY')