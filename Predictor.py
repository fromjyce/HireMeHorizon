import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from collections import Counter

# Load model
model1 = pickle.load(open('LogisticModel.sav', 'rb'))
model2 = pickle.load(open('SVMModel.sav', 'rb'))
model3 = pickle.load(open('KNNModel.sav', 'rb'))

def predict(metaData, model):
    try:
        # Prepare data for prediction
        df = pd.DataFrame([metaData])  # DataFrame with provided metadata
        
        # Ensure the same encoding is applied as during training for 'Gender' and 'Stream'
        label_encoder = LabelEncoder()
        df['gender'] = label_encoder.fit_transform(df['gender'])
        df['ssc_b'] = label_encoder.fit_transform(df['ssc_b'])
        df['hsc_b'] = label_encoder.fit_transform(df['hsc_b'])
        df['hsc_s'] = label_encoder.fit_transform(df['hsc_s'])
        df['degree_t'] = label_encoder.fit_transform(df['degree_t'])
        df['workex'] = label_encoder.fit_transform(df['workex'])
        df['specialisation'] = label_encoder.fit_transform(df['specialisation'])

        # Create a list of expected features for prediction (excluding the target column)
        expected_features = ['gender', 'ssc_p', 'ssc_b', 'hsc_p' ,'hsc_b', 'hsc_s', 'degree_p', 'degree_t', 'workex', 'etest_p', 'specialisation', 'mba_p']

        # Check if all expected features are present in the prediction data
        missing_features = [feature for feature in expected_features if feature not in df.columns]
        if missing_features:
            raise ValueError(f"Missing features: {', '.join(missing_features)}")

        placement_prediction = model.predict(df[expected_features])  
        return placement_prediction[0]
              
    except Exception as e:
        print(f"\n\t\tERROR: {str(e)}\n")
        return False
        

Data = {
    "gender": "M",
    "ssc_p": 67.00,
    "ssc_b": "Others",
    "hsc_p": 91.00,
    "hsc_b": "Others",
    "hsc_s": "Commerce",
    "degree_p": 58.00,
    "degree_t": "Sci&Tech",
    "workex": "No",
    "etest_p": 55,
    "specialisation": "Mkt&HR",
    "mba_p": 58.8
}

predict1 = predict(Data, model1)
predict2 = predict(Data, model2)
predict3 = predict(Data, model3)
predict_list = [predict1, predict2, predict3]
print(predict_list)
# Count occurrences of each prediction
counter = Counter(predict_list)

# Get the most common prediction and its count
most_common_prediction = counter.most_common(1)

# Print the most common prediction and its count
if most_common_prediction[0][0] == 1:
    print("The student would get placed!")
else:
    print("We're sorry, the student won't get placed!")