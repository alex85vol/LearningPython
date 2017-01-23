from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACf0cf56ad8764c233b664bbd438e6d76d"
auth_token = "507f7dc0609ebb739bf8168cf08d97a5"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(body="Your boss has birthday today?",
                                 to = "+380673749275",
                                 from_="+12402521668" )
print  message.sid