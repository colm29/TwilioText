from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)

call = client.messages.create(
    to=config.my_no,
    from_=config.trial_no,
    body='Very Important Message alert'
)

print(call.sid)
