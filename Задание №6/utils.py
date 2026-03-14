import numpy as np
import matplotlib.pyplot as plt  # <-- ОБЯЗАТЕЛЬНО: добавлен импорт
from sklearn.metrics import mean_squared_error, mean_absolute_error
import pandas as pd  # <-- ДОБАВЛЕН: нужен для работы с датами

def create_dataset(data, look_back=1):
    """
    Создание датасета для прогнозирования временных рядов.
    """
    X, y = [], []
    for i in range(len(data) - look_back):
        X.append(data[i:(i + look_back)])
        y.append(data[i + look_back])
    return np.array(X), np.array(y)

def print_model_metrics(model_name, y_true, y_pred):
    """
    Вывод метрик качества модели.
    """
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)

    print(f"\n--- Метрики модели {model_name} ---")
    print(f"MSE: {mse:.4f}")
    print(f"MAE: {mae:.4f}")

def plot_forecast(test_dates, y_true, y_pred, model_name):
    """
    Визуализация прогноза модели.

    Параметры:
    - test_dates: даты тестовой выборки
    - y_true: истинные значения
    - y_pred: предсказанные значения
    - model_name: название модели
    """
    plt.figure(figsize=(12, 6))
    plt.plot(test_dates, y_true, label='Фактические значения')
    plt.plot(test_dates, y_pred, label=f'Прогноз {model_name}', linestyle='--')

    plt.title(f'Прогноз модели {model_name}')
    plt.xlabel('Год')
    plt.ylabel('Количество землетрясений')
    plt.legend()
    plt.grid(True)

    # Форматирование оси X
    if isinstance(test_dates[0], pd.Timestamp):  # Проверка типа дат
        plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y'))
        plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.YearLocator())
    else:
        # Если даты не в формате Timestamp, используем обычные метки
        plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()