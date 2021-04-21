import flask
from flask import request
from werkzeug.exceptions import BadRequestKeyError
app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)

# main index page route



@app.route('/predict',methods=['GET'])
def predict():
    
    from sklearn.externals import joblib
    model = joblib.load('marriage_age_predictor.ml')
    predicted_age_of_marriage = model.predict([[int(request.args['gender']),
                                                
                            int(request.args['religion']),
                            int(request.args['caste']),
                            int(request.args['profession']),
                            int(request.args['country']),
                            int(request.args['height_cms']),
                                                
                           ]])
    return str(round(predicted_age_of_marriage[0],2))

                                                
                                                
    


if __name__ == "__main__":
    app.run(debug=True)



 
