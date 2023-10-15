import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import pickle


df = pd.read_csv('collegePlace.csv')

#To remove multiple values at column and make as one-hot value
data = pd.get_dummies(df, columns=['Gender', 'Stream'])

x = data.drop('PlacedOrNot', axis=1)  # Supporting variable (all columns except 'PlacedOrNot')
y = data['PlacedOrNot']  # Target variable ('PlacedOrNot')

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=23)

model = GradientBoostingClassifier(n_estimators=1000, random_state=42)
#model = DecisionTreeClassifier(random_state=0, criterion='entropy')
# Train the model
model.fit(x_train, y_train)
print("Model trained Successfully!!!")


# Evaluate the model
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Trained @ Accuracy: {accuracy:.2f}')

#Save the trained model (all models must saved with .sav extension)
with open('modelTrainedFromCollegePlaced.sav', 'wb') as f:
    pickle.dump(model,f)
    print("Model Saved Successfully!!!")

