# Authentication

Platform of Trust authentication is OAuth2 based. It's typically a good idea to explain the whole authentication process, because even to this day not everyone is familiar with how they work. In a nutshell [this is what we use](https://www.oauth.com/oauth2-servers/single-page-apps/#authorization)

* You can read **practical authentication example** from Developer Portal [App development guide](https://developers.oftrust.net/guides/build-apps) 

* You also take a look at sample app from Github if you prefer code driven learning. 

> Example how Bearer is expected to be used in headers. 

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/messages/v1/3a9e31ff-b654-4069-8361-6b446dc04c95 \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```

```java
System.out.println("Java example missing. Why not contribute one for us?");
```

### Use Bearer token and how to get it? 

You have two options how to obtain Bearer token depending of your needs. 

To learn and get familiar with APIS:

- Login to Sandbox environment World application (https://world-sandbox.oftrust.net)
- Get the `Authorization` cookie value from your browser. Cookie contains your `Bearer` token. Cookie is valid for several hours, enough for testing.

Here's an example from Chrome Browser DevTools

![](images/chrome-cookie.png)

For production:

- To get Bearer token, you need to set up your application with OAuth logic. 
-  Sample app contains information about the Bearer token as well. 

Most of the APIs require bearer token in header ("Authorization: Bearer"). Exceptions to the rule are CORS enabled endpoints and Broker API. 


### Exception 1: CORS enabled APIs

APIs with CORS enabled endpoints which do not require any tokens: 

* GET [/products/v1/](#products-version)
* GET [/products/v1/{product_code}](#products-version-product_code)

> Example how Broker API headers are expected to be given. 

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/broker/v1/fetch-data-product \
-H "Content-Type: application/json" \
-H "X-Pot-Signature: Ioma1gqOVFUBrXiziWSCLqBG4vFozG3YgzPzillNip0=" \
-H "X-Pot-App: 379780e4-b511-4fa9-aef8-bda9bd58ab89" \
-H "X-Pot-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf" \
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```
### Exception 2: Broker API   

Second exception is the [Broker API](#broker-api) is a bit more complex and requires header parameters:

* X-Pot-Signature (HMAC-SHA256 signature in base64 encoded format), 
* X-Pot-App and (The requesting application's client ID)
* X-Pot-Token (The currently logged in user's OAuth access token) as well. 

Read more from [Broker API](#broker-version-fetch-data-product). 

## Get client credentials

Before jumping into development you might want to get the client credentials. Getting those now let's you jump into code level testing right away without detours.  
**For each application you develop, you need to obtain new client credentials.** These include a client identifier and a client shared-secret. 

Recommended next step is to register new app:

1. Login to World app and initiate new application registration. 
2. Fill in the required information and submit. 
3. Upon successful application registration, you will be shown client credentials. 

## Authentication code example

Now you have client credentials and you can start fiddling code and run you app in our [sandbox](https://developers.oftrust.net/guides/sandbox) environment. 
Code speaks for it self! Thus we have open source (MIT license) React sample app which contains authentication implementation among other things. You can clone the sample app from Github. 

