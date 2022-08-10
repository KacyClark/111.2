url = URL + "/" + id
response = requests.put(url, json=user)
if response.status_code == 204:
    print ("Successfully deactivated id")
else:
    print ("Something went wrong")