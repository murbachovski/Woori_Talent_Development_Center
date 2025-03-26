# Twilio

from twilio.rest import Client

'''
account_sid = 'YourToken'
auth_token = 'YourToken'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="YourMessage",
    from_='+16203903227',
    to='+YourNumber'
)

print(message.sid)
'''