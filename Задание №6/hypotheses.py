# hypotheses.py - модуль с гипотезами исследования

class EDAHypotheses:
    def __init__(self):
        self.seasonality_hypothesis = {
            "description": "Существует сезонная зависимость частоты и силы землетрясений",
            "metrics": ["autocorrelation", "seasonal_decomposition"],
            "tests": ["ADF-тест", "KPSS-тест"]
        }
        
        self.geographical_hypothesis = {
            "description": "Магнитуды землетрясений группируются по регионам",
            "metrics": ["кластеризация", "пространственные корреляции"],
            "visualizations": ["тепловые карты", "пространственные графики"]
        }
        
        self.temporal_patterns = {
            "description": "Наличие определенных временных паттернов в последовательности землетрясений",
            "metrics": ["автокорреляция", "частичная автокорреляция"],
            "tests": ["тест на стационарность"]
        }
        
        self.correlation_hypothesis = {
            "description": "Существует взаимосвязь между магнитудой и другими параметрами",
            "metrics": ["корреляционный анализ", "парные зависимости"],
            "visualizations": ["матрица корреляций"]
        }
        
        self.anomaly_hypothesis = {
            "description": "Наличие выбросов в данных, требующих дополнительного анализа",
            "metrics": ["IQR", "Z-score"],
            "methods": ["DBSCAN", "Изолирующий лес"]
        }

class MLModelHypotheses:
    def __init__(self):
        self.lstm_hypotheses = {
            "long_term_dependencies": "Модель сможет уловить долгосрочные зависимости",
            "nonlinear_patterns": "Эффективное распознавание нелинейных паттернов",
            "accuracy": "Точность выше классических методов"
        }
        
        self.gru_hypotheses = {
            "convergence_speed": "Более быстрая сходимость",
            "memory_efficiency": "Эффективное использование памяти",
            "short_sequences": "Лучшая работа с короткими последовательностями"
        }
        
        self.transformer_hypotheses = {
            "complex_dependencies": "Улавливание сложных зависимостей",
            "long_sequences": "Высокая точность на длинных последовательностях",
            "parallel_processing": "Эффективность параллельной обработки"
        }
        
        self.cnn_hypotheses = {
            "local_patterns": "Эффективное выявление локальных паттернов",
            "multidimensional_data": "Работа с многомерными данными",
            "generalization": "Хорошая обобщающая способность"
        }
        
        self.autoencoder_hypotheses = {
            "anomaly_detection": "Эффективное обнаружение аномалий",
            "data_compression": "Сохранение важной информации при сжатии",
            "hidden_patterns": "Выявление скрытых паттернов"
        }