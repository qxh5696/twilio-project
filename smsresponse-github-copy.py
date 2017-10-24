from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
import twilio.twiml
import os
import time
import re

app = Flask(__name__)
sendToAaron = False
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    resp = twilio.twiml.Response()
    messageBody = request.values.get('Body', None)
    if "song" in messageBody.lower():
        os.chdir('/Users/qadirhaqq/')
        if "song" in messageBody:
            messageBody = messageBody.split("song")[1].strip()
        elif "Song" in messageBody:
            messageBody = messageBody.split("Song")[1].strip()            
        os.system('casperjs song-scrape-lazy.js "' + messageBody + '"')
    if "manga" in messageBody.lower():
        path = '/Users/qadirhaqq/Desktop/latestChapter/'
        os.chdir('/Users/qadirhaqq/Documents/ScrapingScripts/')
        if "1" in messageBody:
            print("Downloading One Piece")
            os.system('casperjs pictureGrab.js 1')
        if "2" in messageBody:
            print("Downloading Kingdom")
            os.system('casperjs pictureGrab.js 2')
        print("Messagebody: " + messageBody)
        pictures = open('/Users/qadirhaqq/Desktop/images.txt')
        account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        client = TwilioRestClient(account_sid, auth_token)
        first = True
        chapter = ""
        for line in pictures:
            if(first):
                    lineSplit = line.split('/')
                    chapter = lineSplit[6]
                    first = False
            if chapter not in line:
                    lineSplit = line.split('/')
                    newLine = lineSplit[0] + "/";
                    for i in range(1,6):
                        newLine += lineSplit[i] + "/"
                    newLine += chapter + "/" + lineSplit[len(lineSplit)-1]
                    line = newLine
            print(line)
            time.sleep(10)
            sendPicture(line.strip(), client, "+12157912925")
        os.chdir('/Users/qadirhaqq/Desktop')
        os.system('rm images.txt')
    if "alert" in messageBody.lower():
        # find consistent time layout
        alert = messageBody.split('-')[1]
        print(time.asctime( time.localtime(time.time() + 8000) ))
        resp = twilio.twiml.Response()
        resp.message(alert)
    print("Message  body: " + messageBody)
    resp = twilio.twiml.Response()
    resp.message("Process Completed")
    return str(resp)

def sendPicture(picture, client, number):
    message = client.messages.create(to=number, from_="+12679918238",                            
                                     media_url=[picture])
    return message

if __name__ == "__main__":
    app.run(debug=True)
