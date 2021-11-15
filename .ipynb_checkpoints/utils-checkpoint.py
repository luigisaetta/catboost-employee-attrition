import ocifs
import pandas as pd

#
# read the csv from Object storage and return a pandas df
#
def read_from_object_storage(prefix, file_name):
    # get access to OSS as an fs
    # config={} assume resource_principal auth
    fs = ocifs.OCIFileSystem(config={})
    
    FILE_PATH = prefix + file_name
    
    # reading data from Object Storage
    with fs.open(FILE_PATH, 'rb') as f:
        df = pd.read_csv(f)
    
    return df
