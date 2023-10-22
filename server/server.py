from flask import Flask, request, jsonify
import util
from util import get_location_names
app=Flask(__name__)


@app.route('/home')
def home():
    
    return 'Hello!!'


# we will now write 2 routines in this servers...the first routine will return the list of locations in banglore city, stored in '.json' file
# the 'jsonify method will help in getting location names, which are randoml;y stored in the file...for more details, check the 'collumns.json' file

@app.route('/get_location_names')
def get_location_names():
    response=jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access -Control-Allow-Origin','*')
    print('Working!!')
    return response

#'util.py' will contain all the core routines, which will handle the process of retrieving location names, while the server will do the routing of requests and responses...

# Now, the second routine, will return you the estimated price, given the pre-definet set of input categories like bhk, sqft etc..

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    # Here, we will use the 'request' library -> whenever, we make a http call from our html, we will get
    # inputs in request.form format
    total_sqft=float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])

    response=jsonify({
        'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access -Control-Allow-Origin','*')
    return response


if __name__=='__main__':
    print('The Flask server is starting!!')
    util.load_saved_artifacts()
    app.run(debug=True)

