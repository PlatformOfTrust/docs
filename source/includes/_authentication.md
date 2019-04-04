# Authentication

It's typically a good idea to explain the whole authentication process, because even to this day not everyone is familiar with how they work. In a nutshell [this is what we use](https://www.oauth.com/oauth2-servers/single-page-apps/#authorization)

The basic flow of how it goes is:

1. user gets redirected from YOUR frontend to YOUR backend's `/login` endpoint or similar

2. the `/login` endpoint generates a `state` parameter for it's own security by e.g. signing the current timestamp with a secret from it's config

3. the `/login` endpoint redirects the user to the login portal with parameters that define the application the user is coming from (client_id, redirect_uri) as well as the state and that we're going to do a code exchange

4. login portal takes care of identifying the user

5. login portal sends user back to YOUR backend's "return url", e.g. `/login/complete` with the new code and the state you provided etc.

6. you validate the state seems valid, isn't too old, etc.

7. you send this code with your client secret to the authorization backend in a server to server -request and get back the actual login token

8. you set the token in a cookie (preferably with `httpOnly; secure; SameSite=strict`)

You can read practical authentication example from  


## Authentication code example

We have React based sample app which contains authencation implementations. Take a look at the source code to see complete example. 

## How to get Bearer token?

To get these tokens, you need to set up your application with login capabilities

1. You start developing an application
2. You realize you need a token for some API calls
3. You integrate into the PoT Login (see above)
4. You can now log in to your own application to get your login token and use it for those calls

## Client credentials

For each application you develop, you need to obtain new client credentials. 
These include a client identifier and a client shared-secret. 


## OAuth 2.0 workflow

## Get request token

**Endpoint**

POST /api/auth/v1/oauth/token/request

HTTPS is required. All the names of variables follow OAuth specification (see RFC 5849).

```python

import upwork
client = upwork.Client(public_key, secret_key, **credentials)
client.auth.get_request_token()

```

