
from distutils.command.config import config
from flask import Flask, jsonify, render_template, request
from Models.utils import MedicalInsurance
import config

app = Flask(__name__)# make instance of flask

@app.route('/')
def hello_flask():
    print("Welcome to Medicle Insurance Charges Prediction")
    return render_template("asd.html")


@app.route('/predict_charges', methods = ["POST", "GET"])
def get_insurance_charges():


    if request.method == "GET":
        print("We are using GET Method")
       
        # data = request.form
        # print("Data ::",data)
        # age = eval(data['age'])
        # sex = data['sex']
        # bmi = eval(data['bmi'])
        # children = eval(data['children'])
        # smoker = data['smoker']
        # region = data['region']

        age = int(request.args.get("age"))
        sex = request.args.get("sex")
        bmi = float(request.args.get("bmi"))
        children = int(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")

        print("age, sex, bmi, children, smoker, region\n",age, sex, bmi, children, smoker, region)

        med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges = med_ins.get_predicted_price()

        return render_template("asd.html", prediction = charges)
        # return jsonify({"Result" : f"Predicted Charges for Medical Insurance is {charges}/- Rs. Only"})

    else:
        print("We are using POST Method")

        age = int(request.form.get("age"))
        sex = request.form.get("sex")
        bmi = float(request.form.get("bmi"))
        children = int(request.form.get("children"))
        smoker = request.form.get("smoker")
        region = request.form.get("region")

        print("age, sex, bmi, children, smoker, region\n",age, sex, bmi, children, smoker, region)

        med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges = med_ins.get_insurance_charges()

        return render_template("asd.html", prediction = charges)
        # return jsonify({"Result" : f"Predicted Charges for Medical Insurance is {charges}/- Rs. Only"})


if __name__ == "__main__":
    # app.run(host='0.0.0.0' , port= config.PORT_NUMBER, debug=True)
    app.run()