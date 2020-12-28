# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

client = Client('account_sid','auth_token')
def send(text):
    message = client.messages \
        .create(
             body=text,
             from_='+12017201014',
             to='***********' #Your telephone number
         )
        
    print(message.sid)

