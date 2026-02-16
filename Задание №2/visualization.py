# visualization.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder

class DataVisualizer:
    def __init__(self, data):
        self.original_data = data.copy()  # Сохраняем оригинальные данные
        self.data = self._preprocess_data(data)

    def _preprocess_data(self, data):
        # Кодируем категориальную переменную Sex
        encoder = OneHotEncoder(drop='first', sparse_output=False)
        sex_encoded = encoder.fit_transform(data[['Sex']])

        # Преобразуем в DataFrame
        sex_df = pd.DataFrame(sex_encoded,
                             columns=encoder.get_feature_names_out(['Sex']),
                             index=data.index)

        # Объединяем с исходными данными
        return pd.concat([data.drop('Sex', axis=1), sex_df], axis=1)

    def plot_histogram(self, column):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[column], kde=True)
        plt.title(f'Гистограмма {column}')
        plt.xlabel(column)
        plt.ylabel('Частота')
        plt.show()

    def plot_scatter(self, x_column, y_column, hue=None):
        # Используем оригинальные данные для визуализации с Sex
        plt.figure(figsize=(12, 8))
        sns.scatterplot(
            data=self.original_data,
            x=x_column,
            y=y_column,
            hue='Sex'  # Используем оригинальный столбец Sex
        )
        plt.title(f'Диаграмма рассеяния {y_column} от {x_column}')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.legend()
        plt.show()

def plot_line_chart(self, x_column, y_column):
        plt.figure(figsize=(12, 8))
        
        # Сортируем данные для корректного отображения
        sorted_data = self.data.sort_values(by=[x_column])
        
        plt.plot(
            sorted_data[x_column], 
            sorted_data[y_column], 
            marker='o',
            linestyle='-',
            color='blue',
            alpha=0.7
        )
        
        # Добавляем линию тренда
        z = np.polyfit(sorted_data[x_column], sorted_data[y_column], 1)
        p = np.poly1d(z)
        plt.plot(
            sorted_data[x_column], 
            p(sorted_data[x_column]), 
            "r--", 
            label=f'Тренд: y={z[0]:.2f}x+{z[1]:.2f}'
        )
def plot_line_chart(self, x_column, y_column):
        plt.figure(figsize=(12, 8))
        
        # Сортируем данные
        sorted_data = self.data.sort_values(by=[x_column])
        
        # Строим график
        plt.plot(
            sorted_data[x_column], 
            sorted_data[y_column], 
            marker='o',
            linestyle='-',
            color='blue',
            alpha=0.7
        )
        
        # Добавляем линию тренда
        z = np.polyfit(sorted_data[x_column], sorted_data[y_column], 1)
        p = np.poly1d(z)
        plt.plot(
            sorted_data[x_column], 
            p(sorted_data[x_column]), 
            "r--", 
            label=f'Тренд: y={z[0]:.2f}x+{z[1]:.2f}'
        )

        # Упрощенные подписи
        plt.title('Зависимость веса от количества колец')
        plt.xlabel('Количество колец')
        plt.ylabel('Общий вес (г)')
        
        # Настройка оси X только с числами
        plt.xticks(
            ticks=sorted_data[x_column].unique(),
            rotation=45
        )
        
        # Базовая настройка графика
        plt.grid(True)
        plt.legend()
        plt.show()

    def plot_correlation_matrix(self):
        plt.figure(figsize=(12, 10))
        corr = self.data.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Матрица корреляции')
        plt.show()

    def plot_boxplot(self, column, hue=None):
        # Используем оригинальные данные для визуализации с Sex
        plt.figure(figsize=(10, 6))
        sns.boxplot(
            data=self.original_data,
            x=column,
            hue='Sex'  # Используем оригинальный столбец Sex
        )
        plt.title(f'Боксплот {column}')
        plt.show()
    def plot_correlation_matrix(self):
        plt.figure(figsize=(12, 10))
        corr = self.data.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Матрица корреляции')
        plt.show()

    def plot_boxplot(self, column, hue=None):
        # Используем оригинальные данные для визуализации с Sex
        plt.figure(figsize=(10, 6))
        sns.boxplot(
            data=self.original_data,
            x=column,
            hue='Sex'  # Используем оригинальный столбец Sex
        )
        plt.title(f'Боксплот {column}')
        plt.show()