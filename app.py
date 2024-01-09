# import the necessary modules
from flask import Flask , render_template , request , jsonify

# importing sentiment_analysis file as sa
import sentiment_analysis as sa

app = Flask(__name__)

# app route for index page
@app.route('/')
def home():
    return render_template('index.html')

# write a route for post request
@app.route('/predict' , methods = ['POST'])
def predict():
    response = ""
    review = request.json.get('')
    if not review:

        return jsonify({'status' : 'error' , 
                        'message' : 'Empty response'})

   
    else:
        sentiment , emoji_url = sa.predict(review)
        response = jsonify({'status' : 'Success',
                            'prediction' : sentiment,
                            'url' : emoji_url})

    return response

if __name__  ==  "__main__":
    app.run(debug = True)