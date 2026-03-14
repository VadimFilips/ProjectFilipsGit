import matplotlib.pyplot as plt

def plot_earthquake_frequency(df_monthly):
    """Визуализация частоты землетрясений"""
    plt.figure(figsize=(12, 6))
    plt.plot(df_monthly, label='Количество землетрясений')
    plt.title('Частота землетрясений с 1965 года')
    plt.xlabel('Дата')
    plt.ylabel('Количество событий')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_average_magnitude(df_magnitude):
    """Визуализация средних магнитуд"""
    plt.figure(figsize=(12, 6))
    plt.plot(df_magnitude, label='Средняя магнитуда')
    plt.title('Средние магнитуды землетрясений')
    plt.xlabel('Дата')
    plt.ylabel('Магнитуда')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_seasonality(df_seasonal):
    """Визуализация сезонности"""
    plt.figure(figsize=(10, 5))
    plt.plot(df_seasonal.index, df_seasonal.values, marker='o')
    plt.title('Сезонность землетрясений 1965')
    plt.xlabel('Месяц')
    plt.ylabel('Среднее количество событий')
    plt.xticks(range(1, 13))
    plt.grid(True)
    plt.show()

def plot_spatial_distribution(df):
    """Визуализация пространственного распределения"""
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Longitude'], df['Latitude'], c=df['Magnitude'], cmap='viridis', alpha=0.6)
    plt.title('Географическое распределение землетрясений')
    plt.xlabel('Долгота')
    plt.ylabel('Широта')
    plt.colorbar(label='Магнитуда')
    plt.grid(True)
    plt.show()