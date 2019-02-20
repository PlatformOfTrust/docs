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


## Authentication code example

The above is rather theoretical description of it. Lets have a look at one example. 