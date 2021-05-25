import requests


def client():

    # data = {
    #     "username": "resttest",
    #     "email": "test@gmail.com",
    #     "password1": "qwerty_123",
    #     "password2": "qwerty_123"
    #     }

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
    #                             data=data)

    token_h = "Token 1e1378cc1cdba14662bd5b6d397b01761f2deedc"
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles", headers=headers)

    print(f"Status code: {response.status_code}")
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
