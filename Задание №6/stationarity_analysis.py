from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt

def analyze_stationarity(series, series_name):
    """Анализ стационарности временного ряда"""
    result = adfuller(series)
    print(f'Статистика ADF ({series_name}):', result[0])
    print(f'p-значение ({series_name}):', result[1])

    # Дифференцирование для стационарности
    series_diff = series.diff().dropna()
    result_diff = adfuller(series_diff)
    print(f'Статистика ADF (дифференцированный, {series_name}):', result_diff[0])
    print(f'p-значение (дифференцированный, {series_name}):', result_diff[1])

    return series_diff

def plot_autocorrelation(series, lags=12, title=''):
    """Построение графика автокорреляции"""
    plt.figure(figsize=(12, 6))
    plot_acf(series, lags=lags, title=title)
    plt.show()