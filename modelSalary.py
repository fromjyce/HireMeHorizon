import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

dataset = r"D:\PaperPresentation\code\Engineering_graduate_salary.csv"

df =pd.read_csv(dataset)#Load the dataset

#Replace '&' characters 
df['Specialization'] = df['Specialization'].str.replace('electronics & instrumentation eng','electronics and instrumentation engineering')

# Remove unnecessary columns (axis-to check on column names, inplace - make changes on actual data)
df.drop(['ID','DOB', '10board','12graduation','12board' ,'CollegeID' ,'CollegeTier',
          'CollegeCityID','CollegeState','GraduationYear',
         'CollegeCityTier','English', 'Logical', 'Quant',
       'Domain', 'ComputerProgramming', 'ElectronicsAndSemicon',
       'ComputerScience', 'MechanicalEngg', 'ElectricalEngg', 'TelecomEngg',
       'CivilEngg', 'conscientiousness', 'agreeableness', 'extraversion',
       'nueroticism', 'openess_to_experience'], axis = 1, inplace = True)


def cgpaCalculation(df):
    data = df.copy()
    data.insert(4, 'CGPA',None)
    
    '''Filling CGPA values with respective gpa's (divide by 8)'''
    for index, row in data.iterrows():
        college_gpa = row['collegeGPA']
        cgpa = round((college_gpa / 8), 2)
        data.at[index, 'CGPA'] = cgpa if cgpa <= 9.8 else -1
        
    return data[ data['CGPA'] > 0]



df = cgpaCalculation(df)

#Remove collegeGPA column from dataframe
df.drop(['collegeGPA'],axis=1,inplace=True)


## Need to learn
# create the copy of dataframe
data = df.copy()
# count of unique categories in specialization
value_count = data['Specialization'].value_counts()

def map_to_other_specialization(var):
    ''' if count of unique category is less than 10, replace the category as other '''
    if var in value_count[value_count<=10]:
        return 'other'
    else:
        return var
    
# apply the function to specialization to get the results    
df['Specialization'] = df.Specialization.apply(map_to_other_specialization)
###


#Generate hot-keys  for given dataframe
hot_keys = ['Gender', 'Degree', 'Specialization']
df = pd.get_dummies(df, columns=hot_keys)


#To split data set for train & testing
X = df.drop('Salary',axis=1)
y = df['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)



print("***Training Model***")
#Train using LinearRegression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
#evaluate - LinearRegression model
y_pred_linear = linear_model.predict(X_test)
linear_reg_score = linear_model.score(X_test, y_test)

print("Linear Regression Score: {:.4f}".format(linear_reg_score))

#Train using RandomForestRegression model

Random_model = RandomForestRegressor(n_estimators=1000, random_state=42)
Random_model.fit(X_train, y_train)

#evaluate Random Forest Regressor model
y_pred_random = Random_model.predict(X_test)
Ranndom_reg_score = Random_model.score(X_test, y_test)

print("Random Forest Regression  Score: {:.4f}".format(Ranndom_reg_score))

# Using above scores , we choose Linear Regression model (Save the model)
with open('modelTrainedFromSalary.sav', 'wb') as f:
    pickle.dump(linear_model,f)
    print("Model Saved Successfully!!!")