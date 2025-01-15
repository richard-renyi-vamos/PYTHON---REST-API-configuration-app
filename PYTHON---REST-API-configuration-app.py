import requests

class APIClient:
    def __init__(self, base_url, api_key=None, auth=None):
        """
        Initialize the API Client.
        
        :param base_url: Base URL of the API.
        :param api_key: API Key for authentication (if required).
        :param auth: Tuple of (username, password) for basic auth (if required).
        """
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"
        self.auth = auth

    def get(self, endpoint, params=None):
        """Send a GET request."""
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, auth=self.auth, params=params)
        return self._handle_response(response)

    def post(self, endpoint, data=None):
        """Send a POST request."""
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, headers=self.headers, auth=self.auth, json=data)
        return self._handle_response(response)

    def _handle_response(self, response):
        """Handle the API response."""
        if response.status_code in range(200, 300):
            return response.json()
        else:
            raise Exception(
                f"API call failed: {response.status_code} {response.reason} - {response.text}"
            )

# Example usage
if __name__ == "__main__":
    # Replace with the app's API details
    BASE_URL = "https://api.example.com/v1"
    API_KEY = "your_api_key_here"  # Replace with your API key

    # Initialize the API client
    client = APIClient(base_url=BASE_URL, api_key=API_KEY)

    # Example GET request
    try:
        response = client.get("endpoint", params={"param1": "value1"})
        print("GET Response:", response)
    except Exception as e:
        print("Error:", e)

    # Example POST request
    try:
        data = {"key": "value"}
        response = client.post("endpoint", data=data)
        print("POST Response:", response)
    except Exception as e:
        print("Error:", e)
