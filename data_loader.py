def load_csv(file_path):
    """
    Загрузка данных из CSV файла
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Ошибка загрузки CSV: {e}")
        return None