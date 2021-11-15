# Catboost-Employee-Attrition
This repository contains all the code developed during the preparation of the Demo for a **Employee Attrition** model using **CatBoost**

## Introduction

## Data used
For the demo I have used a dataset provided with OCI Data Science (orcl_attrition.csv)

You can get a copy from here: https://objectstorage.us-ashburn-1.oraclecloud.com/n/bigdatadatasciencelarge/b/hosted-ds-datasets/o/synthetic%2Forcl_attrition.csv

Data are fictional data, in some way related to this dataset from Kaggle: https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset

## Features
* Conda customized environment, published to Object Storage
* easy handling of **categorical features**
* handling of train dataset **imbalance** with **class-weights**
* hyper-parameter optimization with **Optuna** 
* Integration with **GitHub**
* Model saving to DataScience **Models' Catalog**
* Model "one click" deployment
* integration with **MLFlow** for **Experiment tracking**
* access to Object Storage using Resource Principal and **ocifs**
* Overfitting mitigation through **L2 regolarization** (l2_leaf_reg da Optuna)
* loading data from Oracle **ADWH**
* storing scoring in **ADWH**

## Comparison
I have also tested, on the same dataset, **LightGBM**.

See lightgbm2 NoteBook.

It seems from these tests that:
* Catboost is faster
* it is easier to handle data imbalance


