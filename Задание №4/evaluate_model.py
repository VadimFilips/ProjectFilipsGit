def evaluate_model(model, X_train, X_test, y_train, y_test, model_name):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Основные метрики
    accuracy = accuracy_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # Кросс‑валидация для оценки устойчивости
    from sklearn.model_selection import cross_val_score
    cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')

    results[model_name] = {
        'accuracy': accuracy,
        'roc_auc': roc_auc,
        'f1_score': f1,
        'cv_mean': cv_scores.mean(),
        'cv_std': cv_scores.std(),
        'report': classification_report(y_test, y_pred),
        'confusion_matrix': confusion_matrix(y_test, y_pred)
    }

    print(f"\n{model_name}:")
    print(f" Точность (accuracy): {accuracy:.4f}")
    print(f" ROC-AUC: {roc_auc:.4f}")
    print(f" F1-score: {f1:.4f}")
    print(f" CV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

    return model