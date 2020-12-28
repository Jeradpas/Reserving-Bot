# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
#account_sid = os.environ['ACc42fc3af1f5fc2b8482ef4da48155ff6']
#auth_token = os.environ['ca67d35fa8d0a35324d85837b17951a2']
client = Client('ACc42fc3af1f5fc2b8482ef4da48155ff6','ca67d35fa8d0a35324d85837b17951a2')
def send(text):
    message = client.messages \
        .create(
             body=text,
             from_='+12017201014',
             to='+33698985198'
         )
        
    print(message.sid)

