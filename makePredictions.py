import pandas as pd
import pickle

#Load model 1 -- Placed or not
model1 = pickle.load(open('modelTrainedFromCollegePlaced.sav', 'rb'))
#Load model 2 -- Rough estimate of salary
model2 = pickle.load(open('modelTrainedFromSalary.sav', 'rb'))

# Initialize the values to -1/False
Data1   =   {
                    "Age":-1,
                    "Internships":-1,
                    "CGPA":-1,
                    "Hostel":-1,
                    "HistoryOfBacklogs":-1, 
                    "Gender_Female" : False ,
                    "Gender_Male"  : False, 
                    "Stream_Civil" : False, 
                    "Stream_Computer Science": False, 
                    "Stream_Electrical"  : False,
                    "Stream_Electronics And Communication" : False, 
                   "Stream_Information Technology" : False, 
                    "Stream_Mechanical" : False
            }

Data2 = [[0 for i in range(23)]]
#Lets consider the 10th & 12th percentage are 80 for now & B.tech course

def Data2Fill(metadata):

        Data2[0][0] = 80.00
        Data2[0][1] = 80.00
        Data2[0][2] = metadata['CGPA'][0]
        Data2[0][3] = metadata['Gender_Female']
        Data2[0][4] = metadata['Gender_Male']
        Data2[0][5] = True #'Degree_B.Tech/B.E.',
        Data2[0][6] = 0   #'Degree_M.Tech./M.E.', 
        Data2[0][7] = 0   #'Degree_MCA'

# 'Specialization_civil engineering', 'Specialization_computer application', 'Specialization_computer engineering',
#  'Specialization_computer science & engineering', 'Specialization_electrical engineering', 'Specialization_electronics & telecommunications',
#  'Specialization_electronics and communication engineering', 'Specialization_electronics and electrical engineering',
#  'Specialization_electronics and instrumentation engineering', 'Specialization_electronics engineering', 'Specialization_information science engineering',
# 'Specialization_information technology', 'Specialization_instrumentation and control engineering', 'Specialization_mechanical engineering', 'Specialization_other'
      
        Data2[0][8] = metadata["Stream_Civil"]
        Data2[0][9] = metadata["Stream_Computer Science"]
        Data2[0][10] = metadata["Stream_Computer Science"]
        Data2[0][11] = metadata["Stream_Computer Science"]
        Data2[0][12] = metadata["Stream_Electrical"]
        Data2[0][13] = metadata["Stream_Electrical"]
        Data2[0][16] = metadata["Stream_Electrical"]
        Data2[0][13] = metadata["Stream_Electronics And Communication" ]
        Data2[0][15] = metadata["Stream_Electronics And Communication" ]
        Data2[0][17] = metadata["Stream_Electronics And Communication" ]
        Data2[0][18] = metadata["Stream_Information Technology"]
        Data2[0][19] = metadata["Stream_Information Technology"]
        Data2[0][20] = metadata["Stream_Mechanical"]
        Data2[0][21] = metadata["Stream_Mechanical"]

def precondition(data):
        flag = True        
        #Minimum CGPA value must be 7 (PASS)
        if data["CGPA"][0]<=7:
                flag = False

        #Maximum Allowed backlogs is 1 (As per the trained data)
        if data["HistoryOfBacklogs"][0] > 1 :
                flag = False

        #conditions

        return flag

def predict(metaData):

        Data1.update(metaData)

        Data2Fill(Data1)

        try:

                if(precondition(Data1)): 
                        placement_prediction = model1.predict(pd.DataFrame(Data1))[0]
                        Salary = model2.predict(pd.DataFrame(Data2))[0]

                        print(placement_prediction)
                        print(Salary)
                        return [placement_prediction,Salary]
                
                        
                
                else:
                        #Not Placed
                        return [0,0] 
              

        except:
                print("\n\t\tINVALID META DATA (Insufficient Data)\n")
                return [-1,-1]

hmm = {'Age': [22], 'Internships': [0], 'CGPA': [8.7], 'Hostel': 1, 'HistoryOfBacklogs': [0], 'Gender_Female': True, 'Stream_Computer Science': True}
print(predict(hmm))