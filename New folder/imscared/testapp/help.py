import requests

url = "https://twitter154.p.rapidapi.com/user/id"

querystring = {"user_id":"96479162"}

headers = {
	"X-RapidAPI-Key": "e9d983c1c6msh0d355fc3cdab908p19d82bjsn74bb573ffe2f",
	"X-RapidAPI-Host": "twitter154.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)