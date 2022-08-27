#!/usr/bin/env python3
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'my_twilio_account_id'
auth_token = 'my_twilio_auth_token'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_='+15017122661',
    to='+15558675310'
)

print(message.sid)
