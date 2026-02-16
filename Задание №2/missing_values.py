# missing_values.py
import pandas as pd
import numpy as np

def check_missing_values(df):
    """
    Проверка наличия пропущенных значений в датафрейме
    """
    # Общее количество пропущенных значений
    total_missing = df.isnull().sum().sum()

    # Пропущенные значения по столбцам
    missing_by_column = df.isnull().sum()

    # Процент пропущенных значений
    missing_percentage = (df.isnull().sum() / len(df)) * 100

    return {
        'total_missing': total_missing,
        'missing_by_column': missing_by_column,
        'missing_percentage': missing_percentage
    }

def handle_missing_values(df, strategy='mean'):
    """
    Обработка пропущенных значений
    :param strategy: метод обработки ('mean', 'median', 'mode', 'drop')
    """
    if strategy == 'mean':
        return df.fillna(df.mean())
    elif strategy == 'median':
        return df.fillna(df.median())
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    elif strategy == 'drop':
        return df.dropna()
    else:
        raise ValueError("Неподдерживаемая стратегия обработки пропусков")

# Удалена функция визуализации
# def visualize_missing_values(df):
#     ...

def get_missing_summary(df):
    """
    Получение сводной информации о пропущенных значениях
    """
    missing_info = check_missing_values(df)
    summary = pd.DataFrame({
        'missing_count': missing_info['missing_by_column'],
        'missing_percentage': missing_info['missing_percentage']
    })
    return summary