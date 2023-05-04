from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"
#INPUTS 
#List of websites to monitor
#Proxies for monitoring and purchasing
#Whatever it needs to communicate with the discord bot
#User Information if it's specific to a user requesting to purchase an item. (MAYBE)

#OUTPUTS
#message to the discord bot for pinging
#recording user purchases (MAYBE)
#recording diagnostics for if it crashes / gets blocked
