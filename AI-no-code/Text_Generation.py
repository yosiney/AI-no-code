import json
import requests


def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

def Main():
    global headers, API_URL
    headers = {"Authorization": f"Bearer {'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'}"}
    API_URL= "https://api-inference.huggingface.co/models/bert-base-uncased" 
    data = query({"inputs": "The answer to the universe is [MASK]."})
    print (data)



Main()