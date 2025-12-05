import os
import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

model_path = os.path.join(os.path.dirname(__file__), 'model', 'model.pkl')
print(f"Carregando modelo de: {model_path}")
model = joblib.load(model_path)
print("Modelo carregado com sucesso")

@app.route('/predict',methods=['POST'])
def predict():
    """Recebe dados JSON e retorna uma predição"""

    try:
        data = request.get_json()
        size=data['size_m2']
        prediction = model.predict([[size]])

        return jsonify({
           'size_m2_input': size,
            'predicted_price': prediction[0]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/', methods=['GET'])
def health_check():
    return "API do Modelo AutoScaler está no ar!", 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)