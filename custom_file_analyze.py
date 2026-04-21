import pickle
import feature_extract

with open(r'./models/smartshield-V1.pkl', 'rb') as file:
    model = pickle.load(file)

def custom_analyze_file(file_path):
    dataV = feature_extract.extract_features(file_path)
    print("Extracted features:", dataV)
    return (model.predict(dataV))
