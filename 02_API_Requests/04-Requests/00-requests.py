import requests


def main():
    response = requests.get("http://www.google.com")
    # response = requests.get("http://www.google.com/random-addres")
    print("Status code: ", response.status_code)
    # print("Headers: ", response.headers)
    # print("Content-Type: ", response.headers['Content-Type'])
    print("Content: ", response.text)


if __name__ == "__main__":
    main()
