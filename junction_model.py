import joblib
import numpy as np
import lightgbm as lgb
from catboost import CatBoostRegressor
import pandas as pd
import os
import pickle

class junctionPredict():
    def __init__(self, dir, name, owner):
        self.name = name
        self.owner = owner
        self.dir = dir
        for f in os.listdir(dir):
            _, ext = os.path.splitext(f)
            if(ext == '.pkl'):
                self.pkl = os.path.join(dir, f)
            else: 
                self.cbm = os.path.join(dir, f)
        
    
    def load(self):
        import sys
        from model_wrappers import CatBoostWrapper
        sys.modules["__main__"].CatBoostWrapper = CatBoostWrapper
        model = joblib.load(self.pkl)
        return model
    
    def update_weights(self, X_new, y_new):
        stack = self.load()
        
        lgb_model = stack.named_estimators_["lgb"]
        xgb_model = stack.named_estimators_["xgb"]
        cat_wrapper = stack.named_estimators_["cat"]
        cat_model = cat_wrapper.model_
        
        lgb_dataset = lgb.Dataset(X_new, label=y_new)

        lgb_model = lgb.train(
            lgb_model.get_params(),
            lgb_dataset,
            num_boost_round=100,
            init_model=lgb_model.booster_
        )
        
        xgb_model.fit(
            X_new,
            y_new,
            xgb_model=xgb_model.get_booster()
        )
        
        fixed_cat = CatBoostRegressor()
        fixed_cat.load_model(self.cbm)
        fixed_cat.fit(
            X_new,
            y_new,
            init_model=fixed_cat,
            verbose=False
        )
        self.cbm = fixed_cat
        cat_wrapper.model_ = fixed_cat
        
        
        base_preds = np.column_stack([
            lgb_model.predict(X_new),
            xgb_model.predict(X_new),
            cat_model.predict(X_new)
        ])
        
        stack.final_estimator_.fit(base_preds, y_new)
        
        stack.named_estimators_["lgb"] = lgb_model
        stack.named_estimators_["xgb"] = xgb_model
        stack.named_estimators_["cat"] = cat_wrapper
        
        self.model = stack
        
    def save(self, save_path=''):
        p = os.path.join(save_path, f"{self.name}-{self.owner}")
        i=1 
        while os.path.exists(p):
            p = os.path.join(save_path, f"{self.name}-{self.owner}-{i}")
            i += 1
        os.makedirs(p)
        pkl_dir = os.path.join(p, f"{self.name}-{self.owner}.pkl")
        cbm_dir = os.path.join(p, f"{self.name}-{self.owner}.cbm")
        self.cbm.save_model(cbm_dir)
        joblib.dump(self.model, pkl_dir)
        return p
    
    def predict(self, X_vals):
        stack = self.load()
        return stack.predict(X_vals)