from flask import Flask, render_template, request, url_for
import pickle
import sklearn
import pandas as pd
model= pickle.load(open('model.pkl','rb'))
app= Flask(__name__)

@app.route('/')
def first_page():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Mileage = int(request.form['Mileage'])
        State = request.form['State']
        City = request.form['City']
        Make = request.form['Make']
        Model = request.form['Model']

        input_df= pd.DataFrame({'Year':[Year],'Mileage':[Mileage],'City':[City],'State':[State],'Make':[Make],'Model':[Model]})
        prediction = model.predict (input_df)
        output=round(prediction[0],3)
        return render_template('index.html',prediction_text="You Can Sell Your Car at {} ".format(output))


if __name__ == "__main__":
    app.run(debug=True)