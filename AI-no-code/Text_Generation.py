import json
import requests

global headers
headers = {"Authorization": f"Bearer {'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'}"}

#def GetAPI():
 #API_URL= "https://api-inference.huggingface.co/models/bert-base-uncased"
 #return API_URL

def GetAPI():
 API_URL= (input("Ingrese el URL de la API: "))
 return API_URL

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", GetAPI(), headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
    
data = query({"inputs": "The answer to the universe is [MASK]."})

print (data)