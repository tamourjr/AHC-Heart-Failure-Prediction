import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv(r"C:\ahc\heart_failure_prediction\heart_updated.csv")

# Encode categorical variables
df['Sex'] = df['Sex'].map({'Male': 1, 'Female': 0})
df['ChestPainType'] = LabelEncoder().fit_transform(df['ChestPainType'])
df['HeartDisease'] = df['HeartDisease'].map({'Yes': 1, 'No': 0})

# Choose features and target
features = ['Age', 'Cholesterol', 'ChestPainType', 'Sex']
target = 'HeartDisease'

# Split data
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)
print("Done")
# Train model
model = LogisticRegression()
model.fit(X_train, y_train)
