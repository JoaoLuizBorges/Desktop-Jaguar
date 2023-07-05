import requests

response = requests.get("/solar_api/GetAPIVersion.cgi")

print(response.json())