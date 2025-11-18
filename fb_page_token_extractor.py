import requests

USER_ACCESS_TOKEN = "yahan apna user token dalo"
url = "https://graph.facebook.com/v20.0/me/accounts?fields=id,name,access_token&access_token=%s" % USER_ACCESS_TOKEN

response = requests.get(url)
data = response.json()

for page in data.get('data', []):
    print("Page Name:", page['name'])
    print("Page ID:", page['id'])
    print("Page Token:", page['access_token'])
