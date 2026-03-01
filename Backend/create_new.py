import pandas as pd
import datetime as dt
import warnings
import numpy as np
import junction_model as jm
import joblib
from sklearn.metrics import root_mean_squared_error
import os

def clean_data(main_df):
    main_df['Time'] = 0
    main_df['Day'] = 0
    main_df['Month'] = 0
    main_df['Date'] = 0
    warnings.filterwarnings('ignore')
    for index, t in main_df.iterrows():
        date_time =  main_df.iloc[:, 0][index]
        date_time = date_time.split()
        date = date_time[0].split('-')
        time = date_time[1].split(':')
        main_df.loc[index, 'Time']= int(time[0])
        main_df.loc[index, 'Month'] = int(date[1])
        main_df.loc[index, 'Date'] = int(date[2])
        main_df.loc[index, 'Day'] = dt.date(int(date[0]),int(date[1]),int(date[2])).weekday()
    day_df = main_df.iloc[:, 5]
    month_df = main_df.iloc[:, 6]
    hours_df = main_df.iloc[:, 4]
    main_df["dow_sin"] = np.sin(2 * np.pi * (day_df) / 7)
    main_df["dow_cos"] = np.cos(2 * np.pi * (day_df) / 7)
    main_df["is_weekend"] = main_df.iloc[:,5] >= 5
    main_df["is_business_hours"] = hours_df.between(9,17)
    main_df["month_sin"] = np.sin(2*np.pi*month_df/12)
    main_df["month_cos"] = np.cos(2*np.pi*month_df/12)
    main_df["Vehicles"] = main_df["Vehicles"].astype(int)
    return main_df

def create_new_models(df, user):
    MODEL_DIR = os.path.join(os.getcwd(), 'pretrained_models')
    f_models = {
        "v1": os.path.join(MODEL_DIR, "1-model"),
        "v2": os.path.join(MODEL_DIR, "2-model"),
        "v3": os.path.join(MODEL_DIR, "3-model"),
        "v4": os.path.join(MODEL_DIR, "4-model")
    }
    
    df = clean_data(df)
    print('cleaned file')
    models = []
    for j in df.iloc[:, 1].unique():
        print(j)
        temp_df = df[df["Junction"] == j]
        split_index = int(len(temp_df) * 0.9)
        train_df = temp_df.iloc[:split_index]
        test_df  = temp_df.iloc[split_index:]
        X_train = train_df.drop(train_df.columns[[0, 1, 2]], axis=1)
        Y_train = train_df.iloc[:,2]
        X_test = test_df.drop(test_df.columns[[0, 1, 2]], axis=1)
        Y_test = test_df.iloc[:,2]
        save_path = os.path.join(os.getcwd(), "created_models")
        best_mse = 1000000
        best_model = None
        for name, f in f_models.items():
            print(name)
            print(f)
            temp = jm.junctionPredict(f, f"{j}-{name}", user)
            temp.update_weights(X_train, Y_train)
            preds = temp.predict(X_test)
            rmse = root_mean_squared_error(Y_test, preds)
            if rmse < best_mse:
                best_mse = rmse 
                best_model = temp
        print(f"Best MSE: {best_mse}")
        p = best_model.save(save_path)
        print(p)
        models.append(p)
    return models

        
            
