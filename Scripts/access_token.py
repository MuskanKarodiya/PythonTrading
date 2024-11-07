from fyers_apiv3 import fyersModel

# Define your Fyers API credentials
client_id = "YZTQZ73EZC-100"  # Replace with your client ID
secret_key = "QXA8EWPQ6K"  # Replace with your secret key
redirect_uri = "https://www.google.com"  # Replace with your redirect URI
response_type = "code"
grant_type = "authorization_code"

# The authorization code received from Fyers after the user grants access
auth_code = ("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE3MzA5ODMwNzcsImV4cCI6MTczMTAxMzA3NywibmJmIjoxNzMwOTgyNDc3LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImF1dGhfY29kZSIsImRpc3BsYXlfbmFtZSI6IllNMjEwMDEiLCJvbXMiOiJLMSIsImhzbV9rZXkiOm51bGwsIm5vbmNlIjoiIiwiYXBwX2lkIjoiWVpUUVo3M0VaQyIsInV1aWQiOiI1ZjY3MDE1NjZkNmI0MTYzOTU5YjBjZDBjOWQwMGNkYSIsImlwQWRkciI6IjEwMy4yNDYuMTkzLjM0LCAxNzIuNjguMTQ2LjI0NiIsInNjb3BlIjoiIn0.lFqer3jQpW9lO0xX6W2ws_GiqUd39UdzeSoRgDy_8Sk")

# Create a session object to handle the Fyers API authentication and token generation
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type,
    grant_type=grant_type
)

# Set the authorization code in the session object
session.set_token(auth_code)

# Generate the access token using the authorization code
response = session.generate_token()

# Print the response, which should contain the access token and other details
print(response)