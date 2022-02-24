from fastapi import  FastAPI
from typing import  List
from clas import ModelInput, ModelOutput, APIModelBackEnd
import subprocess
import requests


#Creamos el objeto app
app = FastAPI(title="API Team 5", version='1.0')

#Con el decorador, ponemos en el endpoint /predict la funcionalidad de la función predict_proba
# response_model=List[ModelOuput] es que puede responder una lista de instancias válidad de ModelOutput
# En la definición, le decimos que los Inputs son una lista de ModelInput.
# Así, la API recibe para hacer multiples predicciones
@app.post("/predict", response_model=List[ModelOutput])
async def predict_df(Inputs: List[ModelInput]):
    '''Endpoint de predicción de la API'''
    #Creamos una lista vacía con las respuestas
    response = []
    #Iteramos por todas las entradas que damos
    for Input in Inputs:
        # Usamos nuestra Clase en el backend para predecir con nuestros inputs.
        # Esta sería la línea que cambiamos en este archivo, podemos los inputs que necesitemos.
        # Esto es, poner Input.Nombre_Atributo
        Model = APIModelBackEnd(Input.Bcpp, Input.Potencia, Input.Cilindraje, Input.PesoCategoria,
                                Input.Marca, Input.Clase, Input.Fechas)
        response.append(Model.predict()[0])
    # Retorna  la lista con todas las predicciones hechas.
    return response