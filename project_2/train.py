# train.py
import numpy as np
import pandas as pd
import joblib
import warnings
warnings.filterwarnings('ignore')

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score

print("🚀 Loading Iris Data...")
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Algorithms aur unke parameters
models = {
    'KNN': {
        'model': KNeighborsClassifier(),
        'params': {'classifier__n_neighbors': range(1, 21)}
    },
    'Logistic Regression': {
        'model': LogisticRegression(max_iter=1000, random_state=42),
        'params': {'classifier__C': [0.1, 1, 10]}
    },
    'Decision Tree': {
        'model': DecisionTreeClassifier(random_state=42),
        'params': {'classifier__max_depth': [2, 3, 5, None]}
    },
    'Random Forest': {
        'model': RandomForestClassifier(random_state=42),
        'params': {'classifier__n_estimators': [50, 100], 'classifier__max_depth': [2, 3, None]}
    },
    'Gradient Boosting': {
        'model': GradientBoostingClassifier(random_state=42),
        'params': {'classifier__learning_rate': [0.05, 0.1], 'classifier__max_depth': [2, 3]}
    }
}

best_score = -1
best_pipeline = None
kf = KFold(n_splits=5, shuffle=True, random_state=42)

print("🔄 Training and Tuning Models with 5-Fold CV...")

for name, config in models.items():
    # Pipeline: Scaling -> Model
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', config['model'])
    ])
    
    grid = GridSearchCV(pipe, config['params'], cv=kf, scoring='accuracy', n_jobs=-1)
    grid.fit(X_train, y_train)
    
    cv_score = grid.best_score_
    test_acc = accuracy_score(y_test, grid.best_estimator_.predict(X_test))
    
    print(f"✅ {name}: CV Accuracy = {cv_score:.4f}, Test Accuracy = {test_acc:.4f}")
    
    if cv_score > best_score:
        best_score = cv_score
        best_pipeline = grid.best_estimator_

print(f"\n🏆 Best Model Selected with CV Score: {best_score:.4f}")

# Final model save karo
joblib.dump(best_pipeline, 'best_iris_pipeline.pkl')

# Labels save karo
with open('target_names.txt', 'w') as f:
    for name in iris.target_names:
        f.write(name + '\n')

print("💾 Model saved as 'best_iris_pipeline.pkl'")
print("✅ Training Complete! Ab 'app.py' chalayein.")