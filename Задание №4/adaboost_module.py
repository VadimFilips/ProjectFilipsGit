from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import GridSearchCV

def optimize_adaboost(X_train, y_train):
    """Оптимизация AdaBoost"""
    ada_params = {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.5, 1.0, 1.5],
        'algorithm': ['SAMME', 'SAMME.R']
    }

    ada = GridSearchCV(
        AdaBoostClassifier(random_state=42),
        ada_params,
        cv=3,
        n_jobs=-1,
        scoring='accuracy'
    )
    ada.fit(X_train, y_train)

    best_ada = ada.best_estimator_
    print(f"Ada Boost: лучшие параметры — {ada.best_params_}")
    return best_ada