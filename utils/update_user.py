import requests

URL = "http://127.0.0.1:5000/users"

url = URL + "/" + id
response = requests.put(url, json=user)
if response.status_code == 204:
    print("Successfully updated user")
else:
    print("Something went wrong")    


if __name__ = "__main__":
    id = input("Type n the user's id")
    fname = input("Type in the user's first name")
    lname = input("Type in the user's last name")
    hobbies = input("Type in the user's hobbies")
    update_user(id, fname, lname, hobbies)  