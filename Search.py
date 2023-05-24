import requests
import json
TOKEN = "Bearer AAAAAAAAAAAAAAAAAAAAAF7aAAAAAAAASCiRjWvh7R5wxaKkFp7MM%2BhYBqM%3DbQ0JPmjU9F6ZoMhDfI4uTNAaQuTDm2uO9x3WFVr2xBZ2nhjdP0"
def guest_key(TOKEN):
	headers = {
		'authorization': TOKEN,
		}
	response = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers=headers)
	guest_token = response.json()["guest_token"]
	return guest_token
	
def check_usernames(username):
    headers={
        "authorization": TOKEN,
        "x-guest-token": guest_key(TOKEN)
        }
    response = requests.get(
        f"https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={username}",
    headers=headers)
    try:
    	info = response.json()["errors"]
    	response = requests.get(
        f"https://twitter.com/i/api/i/users/username_available.json?username={username}",headers=headers)
    	return response.json()["reason"]
    except:
    	return "unavailable"
