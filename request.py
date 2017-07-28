# get info from w3schools site and ptint it
import requests
url = "https://www.w3schools.com/js/demo_file.php"
resp = requests.get(url)
data = resp.json()
for item in data:
    print(item + " is " + str(data[item]))