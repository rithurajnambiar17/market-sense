import joblib

model = joblib.load("../models/historical-data/historical-data-TATAMOTORS-NS.h5")

def predict(data):
    target_variable = 'Close'
    window_size = 5
    prevClose = data[target_variable][-window_size:]
    
    pred = model.predict([prevClose])
    return pred[0]