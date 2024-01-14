import requests

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

querystring = {"from":"<REQUIRED>","to":"<REQUIRED>","amount":"10"}

headers = {
	"X-RapidAPI-Key": "d41b054c73msh562ffc028f3c701p138de1jsn777fe07e3558",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())