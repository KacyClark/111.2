import requests

URL = "http://127.0.0.1:5000/update"

def update_users(first_name, last_name, hobbies):
    update = {
        'first_name": first_name,
        "last_name": last_name,
        "hobbies": hobbies
    }
    url = URL + "/" + id
    response = requests.put(url, json=update)
    if response.status_code == 204:
        print
        "Successfully updated old record, GOT: %s"
    else:
        print 
        "Somethiung went wrong"   