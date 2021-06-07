# Anticancer-drug-synergy-prediction

## Description

Here includes the code and data used for comparing several published machine learning (especially deep learning) models for predicting anti-cancer drug synergy.

## Data

You can download the data we used for comparison from here <a href="https://www.dropbox.com/s/7tr009a4aw3t4xk/data.zip?dl=0" target="_blank">data</a>. Please Download the datasets and put the data folder in the same path as the code folder.

## Steps

Step 1: decompress data files           
> unzip data.zip

Step 2: run different models       
> cd code       
> python main.py deepsynergy_preuer_2018     
note: 'deepsynergy_preuer_2018' is one of the models we implemented. You can run other models by replacing 'deepsynergy_preuer_2018' with other names listed in `code/method_config.py`.  

