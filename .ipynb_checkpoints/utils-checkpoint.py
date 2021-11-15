import ocifs
import pandas as pd

# per la confusion matrix ed altre metriche uso sklearn
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import roc_auc_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score

SEED = 42

#
# read the csv from Object storage and return a pandas df
#
def read_from_object_storage(prefix, file_name):
    # get access to OSS as an fs
    # config={} assume RESOURCE PRINCIPAL auth
    fs = ocifs.OCIFileSystem(config={})
    
    FILE_PATH = prefix + file_name
    
    # reading data from Object Storage
    with fs.open(FILE_PATH, 'rb') as f:
        df = pd.read_csv(f)
    
    return df

#
# compute the number of distinct values for each column of the df
#
def compute_distinct(data, columns):
    l_count = []
    for col in columns:
        l_count.append(data[col].nunique())
    
    count_dict = {}
    count_dict['col'] = columns
    count_dict['count'] = l_count

    count_df = pd.DataFrame(count_dict)
    
    return count_df

#
# my split in train, test set
#
def my_train_test_split(df, frac):
    # frac: the fraction used for train
    # df: the dataframe
    
    # shuffle before split
    df = df.sample(frac=1., random_state=SEED)

    # FRAC = 0.90
    tot_rec = df.shape[0]
    NUM_TRAIN = int(frac*tot_rec)
    NUM_TEST = tot_rec - NUM_TRAIN

    data_train = df[:NUM_TRAIN]
    data_test = df[NUM_TRAIN:]

    print()
    print('Numero totale di campioni:', tot_rec)
    print('Numero di campioni nel TRAIN SET:', data_train.shape[0])
    print('Numero di campioni nel TEST SET:', data_test.shape[0])
    
    return data_train, data_test

#
# easy plot of the confusion matrix
#
def plot_cm(model, x_test, y_test):
    y_pred_labels = model.predict(x_test)
    cm = confusion_matrix(y_test, y_pred_labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot();

#
# Compute metrics
#
def compute_auc(model, x_test, y_test):
    y_pred = model.predict_proba(x_test)
    y_pred = y_pred[:, 1]
    auc = round(roc_auc_score(y_test, y_pred), 4)
    
    return auc

def compute_prec_rec(model, x_test, y_test):
    y_pred_labels = model.predict(x_test)
    
    rec = round(recall_score(y_test, y_pred_labels), 4)
    prec = round(precision_score(y_test, y_pred_labels), 4)
    
    return prec, rec

def compute_accuracy(model, x_test, y_test):
    y_pred_labels = model.predict(x_test)
    acc = accuracy_score(y_test, y_pred_labels)
    
    return round(acc, 3)