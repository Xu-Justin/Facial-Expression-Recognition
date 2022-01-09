import kaggle

def download_kaggle_dataset(dataset_name, path):
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset_name, force=True, path=path, quiet=False, unzip=True)

if __name__ == '__main__':
    download_kaggle_dataset('msambare/fer2013', 'raw/')