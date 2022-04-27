from twilio.rest import Client
 
account_sid = 'YOUR_TWILIO_ACCOUNT_SID' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='TWILIO_MESSAGING_SERVICE_SID', 
                              body='Your trader has started trading, Keep updated',      
                              to='+880XXXXXXXXXX' 
                          ) 
 
print(message.sid)