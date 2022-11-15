import numpy as np
import json
import pickle
#import config

class MedicalInsurance():
    def __init__(self, age, sex, bmi, children, smoker, region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = "region_" + region

    def load_model(self):
        with open(r"C:\Users\Ashutosh\Desktop\Velocity\6_Flask_API\2_Medi_ins\Models\Linear_model.pkl", "rb") as f:
            self.model = pickle.load(f)

        with open(r"C:\Users\Ashutosh\Desktop\Velocity\6_Flask_API\2_Medi_ins\Models\project_data.json", "r") as f:
            self.json_data = json.load(f)

    def get_insurance_charges(self):
        self.load_model()
        
        region_index = self.json_data["columns"].index(self.region)
        test_array = np.zeros(len(self.json_data["columns"]))

        test_array[0] = self.age
        test_array[1] = self.json_data["sex"][self.sex]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.json_data["smoker"][self.smoker]
        test_array[region_index] = 1

        print("test_array: ", test_array) # there are total 9 value in this array

        predicted_charges = np.around(self.model.predict([test_array])[0],2)
        return predicted_charges

if __name__ == "__main__":

    age = 19
    sex = "male"
    bmi = 25
    children = 2
    smoker = "yes"
    region = "southwest"

    mde_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
    charges = mde_ins.get_insurance_charges()
    print()
    print(f"Predicted Charges for Medical Insurance is {charges}/- Rs. Only")


