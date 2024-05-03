import requests

url = "https://streaming-availability.p.rapidapi.com/get"
querystring = {"output_language": "en", "imdb_id": 'tt0137523'}
headers = {
    "X-RapidAPI-Key": "192b8070d4mshdce2e96668d0f65p180a1ejsn041cca2faf18",
    "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)
data = response.json()['result']

us_streaming_info = data.get('streamingInfo', {}).get('us', {})

streaming_services = []
for service in us_streaming_info:
    if (service.get('quality', 'uhd') == "uhd") and (service['streamingType'] == "rent" or
                                                     service['streamingType'] == "subscription"):
        streaming_services.append({
                            'service': service['service'],
                            'link': service['link']
                        })

print(streaming_services)

# details.get('link')


