import pandas as pd

def print_dataset_description(df):
    """
    Вывод описания колонок и основных характеристик датасета
    """
    print("=" * 80)
    print("ОПИСАНИЕ КОЛОНОК ДАТАСЕТА (USGS Earthquake Database)")
    print("=" * 80)

    dataset_description = {
        'Date': 'Дата землетрясения в формате MM/DD/YYYY',
        'Time': 'Время землетрясения в формате HH:MM:SS',
        'Latitude': 'Широта эпицентра землетрясения (градусы)',
        'Longitude': 'Долгота эпицентра землетрясения (градусы)',
        'Type': 'Тип сейсмического события (Earthquake, Explosion и т. д.)',
        'Depth': 'Глубина гипоцентра землетрясения (км)',
        'Magnitude': 'Магнитуда землетрясения по шкале Рихтера',
        'Magnitude Type': 'Тип шкалы измерения магнитуды (ML, Mb, Ms, Mw и др.)',
        'ID': 'Уникальный идентификатор события',
        'Source': 'Источник данных о землетрясении',
        'Location Source': 'Источник информации о местоположении',
        'Magnitude Source': 'Источник информации о магнитуде',
        'Status': 'Статус события (Reviewed или Automatic)'
    }

    for col, desc in dataset_description.items():
        print(f"{col:<20}: {desc}")

    print("\n" + "=" * 80)
    print("ОСНОВНЫЕ ХАРАКТЕРИСТИКИ ДАТАСЕТА")
    print("=" * 80)

    # Создаём DataFrame с характеристиками
    stats_table = pd.DataFrame({
        'Характеристика': [
            'Количество записей',
            'Количество колонок',
            'Период данных (начало)',
            'Период данных (конец)',
            'Диапазон магнитуд',
            'Средняя магнитуда',
            'Медиана магнитуд',
            'Стандартное отклонение магнитуд',
            'Глубина (мин)',
            'Глубина (макс)',
            'Глубина (среднее)',
            'Уникальных типов событий',
            'Пропущенных значений (всего)',
            'Процент пропущенных значений'
        ],
        'Значение': [
            f"{df.shape[0]:,}",
            df.shape[1],
            df['Date'].min(),
            df['Date'].max(),
            f"{df['Magnitude'].min():.1f} – {df['Magnitude'].max():.1f}",
            f"{df['Magnitude'].mean():.2f}",
            f"{df['Magnitude'].median():.2f}",
            f"{df['Magnitude'].std():.2f}",
            f"{df['Depth'].min():.1f} км",
            f"{df['Depth'].max():.1f} км",
            f"{df['Depth'].mean():.1f} км",
            df['Type'].nunique(),
            f"{df.isnull().sum().sum():,}",
            f"{(df.isnull().sum().sum() / (df.shape[0] * df.shape[1])) * 100:.2f}%"
        ]
    })

    # Выводим таблицу
    print(stats_table.to_string(index=False))
    print("\n" + "-" * 80)