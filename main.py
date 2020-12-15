import praw
import requests
import os
reddit = praw.Reddit(client_id=os.environ['client_id'], client_secret=os.environ['client_secret'], user_agent=os.environ['user_agent'] )
for submission in reddit.subreddit("furry_irl").new(limit=20):
  yiff = submission.over_18
  if yiff == False:
    owop1 = submission.permalink 
    title= submission.title
    break
def telegram_bot_sendtext(bot_message):
    bot_token = os.environ['bot_api']
    bot_chatID = os.environ['chat_id']
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
owop2 = r"https://reddit.com" +  owop1  
text = "[" + title + "]" + "(" + owop2 + ")"
test = telegram_bot_sendtext(text)
