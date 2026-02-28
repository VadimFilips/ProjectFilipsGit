#lightgbm_module.py
import lightgbm as lgb
from sklearn.model_selection import GridSearchCV

def optimize_lightgbm(X_train, y_train):
    """Оптимизация LightGBM"""
    lgbm_params = {
        'num_leaves': [15, 31],
        'learning_rate': [0.01, 0.03, 0.1],
        'n_estimators': [100, 200],
        'reg_alpha': [0, 0.1, 0.5],
        'reg_lambda': [0, 0.1, 0.5],
        'min_child_samples': [10, 20],
        'subsample': [0.8, 0.9],
        'colsample_bytree': [0.8, 0.9]
    }

    lgbm = GridSearchCV(
        lgb.LGBMClassifier(
            objective='binary',
            random_state=42,
            force_row_wise=True,
            verbose=-1
        ),
        lgbm_params,
        cv=3,
        n_jobs=-1,
        scoring='neg_log_loss'
    )
    lgbm.fit(X_train, y_train)

    best_lgbm = lgbm.best_estimator_
    print(f"LightGBM: лучшие параметры — {lgbm.best_params_}")
    return best_lgbm