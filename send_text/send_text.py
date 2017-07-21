from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACd4a64d36d0302b05db95b0f534593afb"
# Your Auth Token from twilio.com/console
auth_token  = "ffd29a497f3190906ce8b0b39bf33a89"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15098230310", 
    from_="+15095712448",
    body="Who is this? I am a robot")

print(message.sid)