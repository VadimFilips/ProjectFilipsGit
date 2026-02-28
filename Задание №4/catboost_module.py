import catboost as cb
from sklearn.model_selection import GridSearchCV

def optimize_catboost(X_train, y_train):
    """Оптимизация CatBoost"""
    cbc_params = {
        'depth': [4, 6, 8],
        'learning_rate': [0.03, 0.1],
        'l2_leaf_reg': [1, 3, 5]
    }

    cbc = GridSearchCV(
        cb.CatBoostClassifier(
            verbose=False,
            random_seed=42,
            early_stopping_rounds=20
        ),
        cbc_params,
        cv=3,
        n_jobs=-1,
        scoring='accuracy'
    )
    cbc.fit(X_train, y_train)

    best_cbc = cbc.best_estimator_
    print(f"CatBoost: лучшие параметры — {cbc.best_params_}")
    return best_cbc