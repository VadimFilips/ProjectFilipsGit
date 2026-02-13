import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self, data):
        self.data = data
    
    def plot_histogram(self, column):
        """
        Построение гистограммы для числового признака
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[column], kde=True)
        plt.title(f'Гистограмма {column}')
        plt.xlabel(column)
        plt.ylabel('Частота')
        plt.show()
    
    def plot_line_chart(self, x_column, y_column):
        """
        Построение линейного графика
        """
        plt.figure(figsize=(12, 8))
        plt.plot(self.data[x_column], self.data[y_column], marker='o')
        plt.title(f'Линейный график {y_column} от {x_column}')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid(True)
        plt.show()
    
    def plot_scatter(self, x_column, y_column, hue=None):
        """
        Построение диаграммы рассеяния
        """
        plt.figure(figsize=(12, 8))
        sns.scatterplot(data=self.data, x=x_column, y=y_column, hue=hue)
        plt.title(f'Диаграмма рассеяния {y_column} от {x_column}')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.legend()
        plt.show()
    
    def plot_correlation_matrix(self):
        """
        Построение матрицы корреляции
        """
        plt.figure(figsize=(12, 10))
        corr = self.data.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Матрица корреляции')
        plt.show()
    
    def plot_boxplot(self, column, hue=None):
        """
        Построение боксплота
        """
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=self.data, x=column, hue=hue)
        plt.title(f'Боксплот {column}')
        plt.show()