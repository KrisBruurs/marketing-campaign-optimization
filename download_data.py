import requests

url = "https://www.absentdata.com/wp-content/uploads/2022/08/Campaign-Data.csv"

response = requests.get(url)

with open("data/campaign_data.csv", "wb") as f:
    f.write(response.content)

print("Download complete.")