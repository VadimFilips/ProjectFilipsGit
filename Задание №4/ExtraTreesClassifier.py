from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import GridSearchCV

def optimize_extra_trees(X_train, y_train):
    # Параметры для поиска
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'bootstrap': [True, False]
    }

    # Инициализация модели с поиском по сетке
    et_model = GridSearchCV(
        ExtraTreesClassifier(random_state=42),
        param_grid,
        cv=5,
        scoring='accuracy',
        n_jobs=-1
    )

    # Обучение с подбором гиперпараметров
    et_model.fit(X_train, y_train)

    # Возврат лучшей модели
    return et_model.best_estimator_