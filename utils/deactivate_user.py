import requests

URL = "http://127.0.0.1:5000/users"

def deactivate_user(id):
    url = URL + "/" + id
    response = requests.delete(url)
    if response.status_code == 204:
        print(
            "You have been successfully removed")
    else:
        print(
            "Something went wrong") 

    if __name__ == "__main__":
        id = input("Type in user's id to deactivate")
        deactivate_user(id)              
        