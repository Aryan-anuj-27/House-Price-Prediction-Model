#falsk,scikit-learn,pandas-mixin using pip install
import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np

app= Flask(__name__)
#put the absolute path of cleaned data
data= pd.read_csv(r'D:\flaskProject4\cleaned_data.csv')
#put the absolute path of ridge model
file_path=r'D:\flaskProject4\RidgeModel.pkl'
with open(file_path,'rb') as file:
    pipe=pickle.load(file)
# pipe = pickle.load(open("RidgeModle.pkl",'rb'))
@app.route('/')
def index():

    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)
@app.route('/predict',methods=['POST'])
def predict():
    try:
        location = request.form.get('location')
        bhk = request.form.get('bhk')
        bath = request.form.get('bath')
        sqft = request.form.get('total_sqft')

        # print(location,bhk,bath,sqft)
        app.logger.info(f"Received data: Location - {location}, BHK - {bhk}, Bath - {bath}, Sqft - {sqft}")
        input = pd.DataFrame([[location, sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
        prediction = pipe.predict(input)[0] * 1e5

        return str(np.round(prediction, 2))
    except Exception as e:

        app.logger.error(f"Error during prediction: {e}")
        return "Error occurred during prediction"




if __name__ == "__main__":
    app.run(debug=True, port=5001)

