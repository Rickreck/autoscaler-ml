import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

print ("iniciando o treinamento do modelo")

data ={ "Size_m2": [50,60,70,80,100, 120, 200],
        "Price_R$":[150000,200000,300000,400000,500000,600000,700000 ]}

df = pd.DataFrame(data)
x = df[["Size_m2"]]
y = df["Price_R$"]

model = LinearRegression()
model.fit(x,y)

print("Modelo treinado com sucesso")

model_dir = 'model'
os.makedirs(model_dir, exist_ok=True)


model_filename = os.path.join(model_dir, 'model.pkl')
joblib.dump(model, model_filename)

print(f"Modelo salvo em: {model_filename}")


loaded_model=joblib.load(model_filename)
c = 90
prediction = loaded_model.predict([[c]])
print(f"Teste de predição para {c}m²: R$:{prediction[0]:.2f}")
