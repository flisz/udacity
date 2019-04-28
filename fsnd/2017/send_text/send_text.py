from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "God, that was such a terrible idea"
# Your Auth Token from twilio.com/console
auth_token  = "I guess I was real stupid, right?"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15098230310", 
    from_="+15095712448",
    body="Who is this? I am a robot")

print(message.sid)
