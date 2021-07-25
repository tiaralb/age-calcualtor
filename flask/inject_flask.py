import requests 


def HTTP_POST(API_ENDPOINT,BODY):
    HEADER = {"Content-Type": "application/json"}
    r = requests.post(url = API_ENDPOINT, json = BODY, headers=HEADER) 
    return r.text 

def HTTP_GET(API_ENDPOINT,BODY):
    HEADER = {"Content-Type": "application/json"}
    r = requests.get(url = API_ENDPOINT, json = BODY, headers=HEADER) 
    return r.text 

if __name__ == "__main__":

    context={
        'name': 'tiara',
        'date':16,
        'month':8,
        'year':1997
    }

    print(HTTP_GET('http://127.0.0.1:5000/api/age',context))