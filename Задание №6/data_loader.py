import pandas as pd

def load_and_preprocess_data(file_path):
    """
    Загрузка и предобработка данных
    """
    # Загрузка данных без parse_dates
    df = pd.read_csv(file_path)
    
    # Объединяем колонки 'Date' и 'Time' и преобразуем в datetime
    if 'Date' in df.columns and 'Time' in df.columns:
        df['Date_Time'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
        # Удаляем исходные колонки, если они больше не нужны
        df = df.drop(['Date', 'Time'], axis=1)
    elif 'Date_Time' in df.columns:
        # Если колонка уже существует, просто преобразуем её
        df['Date_Time'] = pd.to_datetime(df['Date_Time'])
    else:
        raise ValueError("В данных отсутствуют колонки 'Date' и 'Time' или 'Date_Time'")
    
    return df