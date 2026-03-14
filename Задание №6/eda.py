# eda.py
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(df):
    """
    Основной метод для выполнения EDA
    """
    print("\n--- Exploratory Data Analysis ---")
    
    # 1. Базовая статистика
    print("\nБазовая статистика:")
    print(df.describe())
    
    # 2. Анализ распределений
    plot_distributions(df)
    
    # 3. Корреляционный анализ
    plot_correlation_matrix(df)
    
    # 4. Анализ выбросов
    plot_outliers(df)
    
    # 5. Временные паттерны
    plot_time_patterns(df)
    

def plot_distributions(df):
    plt.figure(figsize=(12, 8))
    plt.subplot(221)
    sns.histplot(df['Magnitude'], bins=30, kde=True)
    plt.title('Распределение магнитуд')
    
    plt.subplot(222)
    sns.boxplot(y=df['Magnitude'])
    plt.title('Boxplot магнитуд')
    
    plt.subplot(223)
    sns.histplot(df['Depth'], bins=30, kde=True)
    plt.title('Распределение глубин')
    
    plt.subplot(224)
    sns.boxplot(y=df['Depth'])
    plt.title('Boxplot глубин')
    plt.tight_layout()
    plt.show()

def plot_correlation_matrix(df):
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    if not numeric_df.empty:
        plt.figure(figsize=(10, 8))
        corr = numeric_df.corr()
        
        if not corr.empty:
            sns.heatmap(
                corr, 
                annot=True, 
                cmap='coolwarm', 
                fmt=".2f",
                vmin=-1, 
                vmax=1
            )
            plt.title('Корреляционная матрица')
            plt.show()
        else:
            print("Недостаточно числовых данных для построения корреляционной матрицы")
    else:
        print("В датафрейме нет числовых столбцов для корреляционного анализа")

def plot_outliers(df):
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    sns.scatterplot(x=df.index, y=df['Magnitude'])
    plt.title('Выбросы по магнитуде')
    
    plt.subplot(122)
    sns.scatterplot(x=df.index, y=df['Depth'])
    plt.title('Выбросы по глубине')
    plt.tight_layout()
    plt.show()

def plot_time_patterns(df):
    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df['Magnitude'], alpha=0.5)
    plt.title('Временной ряд магнитуд')
    plt.xlabel('Дата')
    plt.ylabel('Магнитуда')
    plt.show()