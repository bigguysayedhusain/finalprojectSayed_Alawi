# TODO create Reviewed Movie page

# TODO Create My portal page

# TODO Create Home page

# TODO adjust the links to be left and right

# TODO fix the add review. it should be a button (Add Review). Also, the same user can not create more than 1 review

# TODO add date published to reviews

# TODO make sure the README is correct

import requests

url = "https://streaming-availability.p.rapidapi.com/get"

querystring = {"output_language":"en","imdb_id":"tt0120338"}

headers = {
	"X-RapidAPI-Key": "192b8070d4mshdce2e96668d0f65p180a1ejsn041cca2faf18",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
