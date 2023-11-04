from flask import Flask, render_template, request, url_for, flash, redirect

from Diabetes_API.app import d_ValuePredictor
from Heart_API.app import h_ValuePredictor
from Breast_Cancer_API.app import b_ValuePredictor
from Kidney_API.app import k_ValuePredictor
from Liver_API.app import l_ValuePredictor

app = Flask(__name__, template_folder='templates')


@app.route("/")
def cancer():
    return render_template("index.html")


@app.route("/Diabetes")
def diabetes():
    return render_template("diabetes.html")

@app.route('/predict', methods = ["POST"])
def predict_diabetes():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #diabetes
        print("**"*80)
        print(to_predict_list)
        print("**"*80)
        if(len(to_predict_list)==6):
            result = d_ValuePredictor(to_predict_list,6)
    
    if(int(result)==1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return(render_template("result_diabetes.html", prediction_text=prediction))       

@app.route("/Kidney")
def Kidney():
    return render_template("kidney.html")

@app.route('/k_predict', methods = ["POST"])
def k_predict():
    print("**"*80)
    print(request.method)
    print("**"*80)
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #diabetes
         
        print("**"*80)
        print(to_predict_list)
        print("**"*80)
        if(len(to_predict_list)==7):
            result = k_ValuePredictor(to_predict_list,7)
    
    if(int(result)==1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return(render_template("result_kidney.html", prediction_text=prediction))       


@app.route("/liver")
def liver():
    return render_template("liver.html")

@app.route('/l_predict', methods = ["POST"])
def l_predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         
        if(len(to_predict_list)==7):
            result = l_ValuePredictor(to_predict_list,7)
    
    if(int(result)==1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return(render_template("result_liver.html", prediction_text=prediction))

@app.route("/Breast cancer")
def b_cancer():
    return render_template("cancer.html")

@app.route('/bc_predict', methods = ["POST"])
def bc_predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         
        if(len(to_predict_list)==5):
            result = b_ValuePredictor(to_predict_list,5)
    
    if(int(result)==1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return(render_template("result_bc.html", prediction_text=prediction))

@app.route("/Heart disease")
def heart():
    return render_template("heart.html")

@app.route('/h_predict', methods = ["POST"])
def h_predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         
        if(len(to_predict_list)==7):
            result = h_ValuePredictor(to_predict_list,7)
    
    if(int(result)==1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return(render_template("result_heart.html", prediction_text=prediction))

if __name__ == "__main__":
    app.run(debug=True)
