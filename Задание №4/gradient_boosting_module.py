from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV

def optimize_gradient_boosting(X_train, y_train):
    """Оптимизация Gradient Boosting"""
    gbc_params = {
        'n_estimators': [100, 200],
        'max_depth': [3, 4, 5],
        'learning_rate': [0.05, 0.1, 0.2]
    }

    gbc = GridSearchCV(
        GradientBoostingClassifier(random_state=42),
        gbc_params,
        cv=3,
        n_jobs=-1,
        scoring='accuracy'
    )
    gbc.fit(X_train, y_train)

    best_gbc = gbc.best_estimator_
    print(f"Gradient Boosting: лучшие параметры — {gbc.best_params_}")
    return best_gbc