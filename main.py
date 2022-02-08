import pandas as pd
import matplotlib.pyplot as plt

data_patients = pd.read_csv("patient_data.csv")  # to read the file
print("\n the data frame is \n")
print(data_patients)
maximum = data_patients.max()  #to get the maximum in each column
print("the maximum values of each field are \n")
print(maximum)
minimum = data_patients.min()  #to get the minimum of each column
print("\n\nthe minimum values of each field are \n")
print(minimum)
avg = data_patients.mean()  #to get the average of each column
print("\n\nthe average values of each field are \n")
print(avg)
NumberOfPatient = data_patients[(data_patients['Age'] > 50) & (data_patients['BloodPressure'] >= 70)].shape[0]
print("\nthe number of patient: ")
print(NumberOfPatient)
data_patients['Gender'].value_counts().plot.bar(rot=10)
plt.show()