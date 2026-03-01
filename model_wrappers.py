from sklearn.base import BaseEstimator, RegressorMixin
from catboost import CatBoostRegressor
class CatBoostWrapper(BaseEstimator, RegressorMixin):

    def __init__(self, **params):
        self.params = params

    def fit(self, X, y):
        self.model_ = CatBoostRegressor(
            **self.params,
            allow_writing_files=False,
            verbose=0
        )
        self.model_.fit(X, y)
        return self

    def predict(self, X):
        return self.model_.predict(X)

    def get_params(self, deep=True):
        return self.params.copy()

    def set_params(self, **params):
        self.params.update(params)
        return self