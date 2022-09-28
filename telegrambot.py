
import requests

base_url = "https://api.telegram.org/bot5531087741:AAHNuNbYL267FWRBGHrKkblzPVo5PREIPC4"


def read_msg(offset):

  parameters = {
      "offset" : offset
  }

  resp = requests.get(base_url + "/getUpdates", data = parameters)
  data = resp.json()

  message = data["message"]
  chat_id = message["chat"]["id"]
  text = message.get("text","")
  print("Message received ->",text)


# def send_msg(chat_id, text):

#   parameters = {
#       "chat_id" : chat_id,
#       "text" : text,
#       "reply_to_message_id" : message_id
#   }

#   resp = requests.get(base_url + "/sendMessage", data = parameters)
#   print(resp.text)

# offset = 0

while True:  
  offset = read_msg(offset)
 
