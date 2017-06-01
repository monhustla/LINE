from line import LineClient, LineGroup, LineContact

client= LineClient("mythlegend101@gmail.com", "Bboy123!")
authToken=client.authToken
print authToken

client = LineClient(authToken=authToken)

