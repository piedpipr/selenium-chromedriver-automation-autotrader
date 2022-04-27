from twilio.rest import Client


account = "TWILIO_ACCOUNT_SID"
token = "TWILIO_TOKEN"
client = Client(account, token)

call = client.calls.create(to="+880XXXXXXXXXX",
                           from_="+15XXXXXXX",
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print(call.sid)