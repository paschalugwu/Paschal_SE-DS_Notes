import os
import logging
import joblib
import numpy as np
from sklearn.decomposition import NMF
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.utils.validation import check_is_fitted
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer

# Set up logging
logging.basicConfig(level=logging.INFO)

# Custom NMF Recommender Class
class NMFRecommender(BaseEstimator, RegressorMixin):
    def __init__(self, n_components=10, alpha_W=0.1, alpha_H=0.1, init='random', random_state=None):
        self.n_components = n_components
        self.alpha_W = alpha_W
        self.alpha_H = alpha_H
        self.init = init
        self.random_state = random_state

    def fit(self, X, y=None):
        self.nmf_ = NMF(n_components=self.n_components, alpha_W=self.alpha_W, alpha_H=self.alpha_H, init=self.init, random_state=self.random_state)
        self.W_ = self.nmf_.fit_transform(X)
        self.H_ = self.nmf_.components_
        return self

    def predict(self, X):
        check_is_fitted(self, ['W_', 'H_'])
        return np.dot(self.W_, self.H_)

# Custom scoring function for RMSE
def nmf_rmse_scorer(estimator, X, y_true):
    y_pred = estimator.predict(X)
    return mean_squared_error(y_true, y_pred, squared=False)

# Create a custom scorer
nmf_scorer = make_scorer(nmf_rmse_scorer, greater_is_better=False)

def load_or_run_grid_search(X_train_processed, y_train, param_grid, checkpoint_filename='nmf_grid_search_checkpoint.pkl'):
    model = NMFRecommender()
    grid_search = GridSearchCV(model, param_grid, cv=3, scoring=nmf_scorer)

    if os.path.exists(checkpoint_filename):
        logging.info("Loading checkpoint...")
        grid_search = joblib.load(checkpoint_filename)
    else:
        logging.info("Starting new grid search...")
        grid_search.fit(X_train_processed, y_train)
        joblib.dump(grid_search, checkpoint_filename)

    return grid_search

def preprocess_data(X_train, X_val):
    imputer = SimpleImputer(strategy='mean')
    scaler = MinMaxScaler()

    X_train_imputed = imputer.fit_transform(X_train)
    X_train_processed = scaler.fit_transform(X_train_imputed)

    X_val_imputed = imputer.transform(X_val)
    X_val_processed = scaler.transform(X_val_imputed)

    return X_train_processed, X_val_processed

def main():
    # Example data (replace with your actual data)
    np.random.seed(0)
    X_train = np.random.rand(100, 50)
    X_val = np.random.rand(20, 50)
    y_train = X_train.copy()  # Assuming reconstruction task
    y_val = X_val.copy()  # Assuming reconstruction task

    # Preprocessing
    X_train_processed, X_val_processed = preprocess_data(X_train, X_val)

    # Define hyperparameters for grid search
    param_grid = {
        'n_components': [20, 50, 100],
        'alpha_W': [0.1, 0.5, 1.0],
        'alpha_H': [0.1, 0.5, 1.0],
        'init': ['random', 'nndsvd']
    }

    # Perform or resume grid search
    grid_search = load_or_run_grid_search(X_train_processed, y_train, param_grid)

    # Get the best model based on grid search results
    best_model = grid_search.best_estimator_

    # Train the best model on the entire training set
    best_model.fit(X_train_processed, y_train)

    # Save the final model
    final_model_filename = 'nmf_best_model.pkl'
    joblib.dump(best_model, final_model_filename)

    # Optionally, log final training metrics
    logging.info(f"Best Model Parameters: {grid_search.best_params_}")
    y_pred_val = best_model.predict(X_val_processed)  # Changed from transform to predict
    y_pred_val_full = np.dot(y_pred_val, best_model.H_)

    val_rmse = mean_squared_error(y_val, y_pred_val_full, squared=False)
    logging.info(f"Validation RMSE: {val_rmse}")

    print("Model training and hyperparameter tuning completed successfully.")

if __name__ == "__main__":
    main()
