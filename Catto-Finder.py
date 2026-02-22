import requests


base_url = "https://cataas.com"
webhook_url = "[YOUR WEBHOOK HERE]"

cat_message = "i-eat-gator"

discord_message ="kibby"



#Gets the catto

def get_catto(message, type):

    if message:
        url = f"{base_url}/cat/says/{message}"

    else:
        url = f"{base_url}/cat/{type}"
    
    response = requests.get(url)

    if response.status_code == 200:
        print("Got Cat!")


        return url
    
    else:
        print("no cat :(")



#Webhook thingy

def SendDiscordMessage(cat_message, discord_message):
    catto_image = get_catto(cat_message, None)    

    data = {
        "content":f"{discord_message} {catto_image}"
    }

    requests.post(webhook_url, json=data)


SendDiscordMessage(cat_message, discord_message)