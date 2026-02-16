#data_processing.py

def preprocess_data(df, target_column):
    """
    Предобработка данных для модели.
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]

    numeric_features = ['Length', 'Diameter', 'Height',
                       'Whole weight', 'Shucked weight',
                       'Viscera weight', 'Shell weight']
    categorical_features = ['Sex']

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(drop='first')

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    X_processed = preprocessor.fit_transform(X)

    processed_feature_names = (
        numeric_features +
        preprocessor.named_transformers_['cat']
        .get_feature_names_out(categorical_features)
        .tolist()
    )

    return {
        'X': pd.DataFrame(X_processed, columns=processed_feature_names),
        'y': y,
        'preprocessor': preprocessor
    }