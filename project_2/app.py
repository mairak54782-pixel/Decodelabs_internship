from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)   # <-- Yeh line exactly aisi honi chahiye, template_folder nahi

pipeline = joblib.load('best_iris_pipeline.pkl')
with open('target_names.txt', 'r') as f:
    target_names = [line.strip() for line in f.readlines()]

@app.route('/')
def home():
    return render_template('index.html', prediction=None, probabilities=None)

@app.route('/predict', methods=['POST'])
def predict():
    features = np.array([[
        float(request.form['sepal_length']),
        float(request.form['sepal_width']),
        float(request.form['petal_length']),
        float(request.form['petal_width'])
    ]])
    
    pred_idx = pipeline.predict(features)[0]
    pred_label = target_names[pred_idx]
    
    probs = pipeline.predict_proba(features)[0] * 100
    prob_dict = {target_names[i]: round(probs[i], 2) for i in range(len(target_names))}
    
    return render_template('index.html', prediction=pred_label, probabilities=prob_dict)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)