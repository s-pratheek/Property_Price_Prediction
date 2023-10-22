import json
import pickle
import numpy as np

#creating variables
__locations=None
__data_columns=None
__model=None



def get_estimated_price(location,sqft,bhk,bath):
    # the predict method will take 2-D array as input..
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1
    
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    
    if loc_index>=0:
        x[loc_index]=1
    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations 

# now we will create a function which loads the artifacts into variables created above, and addig global attribute
def load_saved_artifacts():
    print('loading saved artifacts...start')
    global __data_columns
    global __locations

    with open('server/artifacts/columns.json','r') as f:
        __data_columns=json.load(f)['data_columns']
        # 'json.load() will retireve the json file as a dictionary
        # '__data_columns' will store the values of dictionary having key='data_columns'
        __locations=__data_columns[3:]
    
    global __model
    with open('server/artifacts/banglore_home_prices_model.pickle','rb') as q: #'rb' used, since it is a binary model
        __model=pickle.load(q)
    print('loading artifacts is done!!!')



if __name__=='__main__':
    load_saved_artifacts()
    print(get_location_names())
    #print(__locations)
    print(get_estimated_price('1st Phase JP Nagar',1000,3,3))
    print(get_estimated_price('1st Phase JP Nagar',1000,2,2))
    print(get_estimated_price('Indira Nagar',1000,2,2)) # other location