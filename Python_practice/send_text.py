from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACed5916518c0de51e915e26651a1f5dd3"
auth_token  = "35dd8567845c0db5ea77d85ea3623e75"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="This is a ghost text! BooOOoOOo",
    to="+14802772654",    # Replace with your phone number
    from_="+16234280215") # Replace with your Twilio number
print message.sid
