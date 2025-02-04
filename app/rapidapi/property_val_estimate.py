import requests

url = "https://realty-mole-property-api.p.rapidapi.com/salePrice"

querystring = {"address":"1664 Oleander Ave, Chula Vista, CA, 91911",
               "propertyType":"Single Family"}

headers = {
	"X-RapidAPI-Key": "c645f72725mshdfefe8976e73b37p154361jsn10b88cee790a",
	"X-RapidAPI-Host": "realty-mole-property-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())