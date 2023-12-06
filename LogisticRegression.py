import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np
import pickle

# Load the dataset
data = pd.read_csv('Placement_Data_Full_Class.csv')
data.drop('sl_no', axis=1, inplace=True)

# Encode categorical variables
label_encoder = LabelEncoder()
data['gender'] = label_encoder.fit_transform(data['gender'])
data['ssc_b'] = label_encoder.fit_transform(data['ssc_b'])
data['hsc_b'] = label_encoder.fit_transform(data['hsc_b'])
data['hsc_s'] = label_encoder.fit_transform(data['hsc_s'])
data['degree_t'] = label_encoder.fit_transform(data['degree_t'])
data['workex'] = label_encoder.fit_transform(data['workex'])
data['specialisation'] = label_encoder.fit_transform(data['specialisation'])
data['status'] = label_encoder.fit_transform(data['status'])


# Split the data into features (X) and targets (Y)
X = data.drop(['status', 'salary'], axis=1)
y = data['status']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy * 100}%')
print(f'Classification Report:')
print(report)

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
TN, FP, FN, TP = conf_matrix.ravel()
print(f"True Positives (TP): {TP}")
print(f"True Negatives (TN): {TN}")
print(f"False Positives (FP): {FP}")
print(f"False Negatives (FN): {FN}")

feature_importances = {}
for feature in X_train.columns:
    X_perturbed = X_test.copy()
    X_perturbed[feature] = np.random.permutation(X_perturbed[feature])

    perturbed_accuracy = accuracy_score(y_test, model.predict(X_perturbed))
    feature_importances[feature] = accuracy - perturbed_accuracy

# Print feature importances
print()
print("Feature Importances (approximated by change in accuracy):")
for feature, importance in feature_importances.items():
    print(f"{feature}: {abs(importance * 100)}%")

print()

with open("LogisticModel.sav", "wb") as fobj:
    pickle.dump(model, fobj)
    print("The Model is saved to LogisticModel.sav")