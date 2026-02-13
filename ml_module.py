import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Загрузка данных из CSV файла.
    """
    return pd.read_csv(file_path)
    
def train_model(X, y):
    """
    Обучение модели линейной регрессии.
    """
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict(model, X):
    """
    Предсказание на новых данных.
    """
    return model.predict(X)

def evaluate_model(y_true, y_pred):
    """
    Оценка модели.
    """
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return mse, r2