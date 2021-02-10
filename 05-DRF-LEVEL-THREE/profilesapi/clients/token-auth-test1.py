import requests


def client():
    token_h = "Token fdc8baf64c70ae1ca1bfa83cbba6bf3af5bf5b1a"
    # credentials = {"username": "admin@localhost", "password": "qwerty"}
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
    #                             data=credentials)

    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles", headers=headers)
    print(f"Status code: {response.status_code}")
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
