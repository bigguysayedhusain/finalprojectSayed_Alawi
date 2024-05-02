

# Download an image
import requests

url = "https://movies-tv-shows-database.p.rapidapi.com/"

querystring = {"movieid":"tt0103064"}

headers = {
	"Type": "get-movies-images-by-imdb",
	"X-RapidAPI-Key": "192b8070d4mshdce2e96668d0f65p180a1ejsn041cca2faf18",
	"X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())


#get movie info

# import requests
#
# url = "https://movies-tv-shows-database.p.rapidapi.com/"
#
# querystring = {"movieid":"tt0103064"}
#
# headers = {
# 	"Type": "get-movie-details",
# 	"X-RapidAPI-Key": "192b8070d4mshdce2e96668d0f65p180a1ejsn041cca2faf18",
# 	"X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())