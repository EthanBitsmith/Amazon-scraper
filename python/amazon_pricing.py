import requests
  
url = "https://scraper-api.smartproxy.com/v2/scrape"
  
payload = {
      "target": "amazon_pricing",
      "query": "B09H74FXNW",
      "page_from": "1",
      "parse": True
}
  
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic [your basic authentication token]"
}
  
response = requests.post(url, json=payload, headers=headers)
  
print(response.text)