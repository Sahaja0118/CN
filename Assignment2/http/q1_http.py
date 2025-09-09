# http_client.py

import requests

def send_requests():
    """Send GET and POST requests and display responses."""
    try:
        # GET request
        get_response = requests.get("https://httpbin.org/get")
        print("GET Request:")
        print("Status Code:", get_response.status_code)
        print("Headers:", get_response.headers)
        print("Body:", get_response.text)

        # POST request
        payload = {"name": "Sahaja", "course": "Computer Networks"}
        post_response = requests.post("https://httpbin.org/post", data=payload)
        print("\nPOST Request:")
        print("Status Code:", post_response.status_code)
        print("Headers:", post_response.headers)
        print("Body:", post_response.text)

    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

def main():
    send_requests()

if __name__ == "__main__":
    main()
