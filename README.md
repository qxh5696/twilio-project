# twilio-project
Twilio project I made to simplify downloading of music and manga to my phone. 

The Project in a nutshell: 

The above project was a simple hack I put together to download songs, manga, and send alerts to my computer using a command line web-scraper from a text.

First I would start the SMSresponse.py python script in a terminal window on my laptop. 

Next I would start an ngrok tunneling service with the message url I have under my Twilio profile under my twilio phone number

Next I would text a request to the number in which the flask server would receive the body of the message thanks to ngrok tunneling and I would split the message body apart and then use the python "os" library to run the webscraper from the command line. The scraper then handled the request, for example, to download the song. 

Once the process was completed I would get a text message response from the twilio number letting me know the song download was completed. I had a similar set up of commands for Manga (japanese web comics) and alerts, which remains unfinished.

