--- 

title: Platform Of Trust Documentation 

language_tabs: 
   - shell 
   - java
   - python
   - javascript

toc_footers: 
   - <a href='https://developers.oftrust.net'>Developer Portal</a> 

includes: 
   - authentication
   - ontologies
   - errors 
   - feedback
   

search: true 

--- 


# Platform of Trust API Documentation


## What is Platform of Trust?

> Some instructions and tips to make your life easier (and less support requests to us): 

> - Endpoints related code examples are constructed against **SANDBOX environment `https://api-sandbox.oftrust.net/`**. 

> - In **PRODUCTION** use, change domain in api endpoints to `https://api.oftrust.net/`

> If you found a bug or missing information in the documentation, contact us at dev@oftrust.net or create an [issue in Github](https://github.com/PlatformOfTrust/docs/issues/new). 



Communally built Platform of Trust provides a trustworthy and easy-to-use surrounding where you can utilize a vast data pool and develop everyday services for your`
customers with the help from the developer community and without a need for pricey and time-consuming integrations.  
``
Platform of Trust has Finnish origins, but it’s built to expand globally through the network of built environment innovation hubs.

**Developer Portal**

Our [Developer Portal](https://developers.oftrust.net) is your one-stop-shop. From there you'll find getting started guides, use case descriptions and 

**Market place**

Market place is the bazaar to find more data products to use in application development. Visa versa, it is also the service where your data products are added during the integration process. 

# Getting started

## Auth Flow

It's typically a good idea to explain the whole authentication process, because even to this day not everyone is familiar with how they work. In a nutshell [this OAuth single page auth flow is what we use](https://www.oauth.com/oauth2-servers/single-page-apps/#authorization)

The basic flow of how it goes is:

1. user gets redirected from YOUR frontend to YOUR backend's `/login` endpoint or similar

2. the `/login` endpoint generates a `state` parameter for it's own security by e.g. signing the current timestamp with a secret from it's config

3. the `/login` endpoint redirects the user to the login portal with parameters that define the application the user is coming from (client_id, redirect_uri) as well as the state and that we're going to do a code exchange

4. login portal takes care of identifying the user

5. login portal sends user back to YOUR backend's "return url", e.g. `/login/complete` with the new code and the state you provided etc.

6. you validate the state seems valid, isn't too old, etc.

7. you send this code with your client secret to the authorization backend in a server to server -request and get back the actual login token

8. you set the token in a cookie (preferably with `httpOnly; secure; SameSite=strict`)


## Standards used

**Dates**: we use a subset of ISO-8601 - [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt). Example <code>2008-09-15T15:53:00+05:00</code>

**Core Ontology**: The Platform Of Trust core ontology can be found as a JSON-LD ontology file under [ontologies/pot.jsonld](https://github.com/PlatformOfTrust/standards/blob/master/ontologies/pot.jsonld).

Each identity type has their own context which
describes the attributes the identity has. The context file name gives a notion
of whether the context is for an `identity` or a `link`. 

The identity describes the real world identities, such as apartments, 
buildings, rooms etc. The links are the relations between identities. 
As an example, the `Tenant`-link can be applied between
a user identity and an apartment identity, meaning that the user is a tenant
in the apartment.

If only a link between identities is needed, without any kind
of role, the generic `link-link.jsonld` can be used 
[contexts/link-link.jsonld](https://github.com/PlatformOfTrust/standards/tree/master/contexts/link-link.jsonld).

Read more from [Github](https://github.com/PlatformOfTrust/standards/blob/master/README.md)

## Code Examples 

<aside class="warning">
All the documentation code examples use our sandbox environment. When you are done with testing, you should switch to production environment. Easiest way is to store API root url in variable and when needed, change it there. Thus the code examples contain API-root variable as an exmaple. 
</aside>


# OAuth

To make API requests, you need to authenticate to Upwork API. Currently, we support OAuth 2.0 authentication. All API requests MUST be signed following the RFC 5849 specification.


## Client credentials

For each application you develop, you need to obtain new client credentials. 
These include a client identifier and a client shared-secret. 
You can find these credentials at https://developers.oftrust.net/profile 
while logged into your account. 

You will receive a public and a private key for each client identifier and 
client shared-secret you API request.


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

# Broker API

The Broker API provides means to connect a service to a translator that will
return desired data from different sources. The data broker does not mangle
the data in any way, it only functions as a proxy between services and
translators.
 

**Version:** v0.1 

## /fetch-data-product
### **post** 

**Description:** Fetch data product

#### http request 


 > Example for: POST /fetch-data-product 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/broker/v0.1/fetch-data-product \
-H "Content-Type: application/json" \
-H "X-Pot-Signature: Ioma1gqOVFUBrXiziWSCLqBG4vFozG3YgzPzillNip0=" \
-H "X-Pot-App: 379780e4-b511-4fa9-aef8-bda9bd58ab89" \
-H "X-Pot-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf" \
-d '{
	"timestamp": "2019-02-27T14:38:00+02:00",
	"productCode": "business-identity-test",
	"parameters": {
		 "businessId": "1234567-8"
	}
}'
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://platformoftrust.github.io/standards/contexts/prh-data-product.jsonld",
  "data": {
    "@context": "https://platformoftrust.github.io/standards/contexts/prh-data-product-parameters.jsonld",
    "@type": "BusinessIdentity",
    "totalResults": 1,
    "offset": 0,
    "items": [
      {
        "name": "Example Company Oy",
        "businessId": "1234567-8",
        "companyForm": "OY",
        "registrationDate": "2015-02-05"
      }
    ]
  },
  "signature": {
    "type": "RsaSignature2018",
    "created": "2019-03-14T10:33:31+00:00",
    "creator": "https://example.com/example.pub",
    "signatureValue": "MJWJxS3rh0hylgGyIILROiF4t+/w+gH...iTuKR8KhPMe4XVQ1I="
  }
}

```


**POST** /fetch-data-product 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 422 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
# Calendar API

The calendar API provides means to create calendar entries to identities.
You can e.g. create an event for a housing company identity, a reservation
to a room identity, or just a regular calendar entry to any identity you want.

The calendar entry requires a `"to"`-identity, the ID of the identity to which
the calendar entry applies to. Specify a type for the entry, e.g.
`Event`, `Reservation`, `CalendarEntry`. Give the calendar entry a title, e.g.
"Housewarming party", a start date, when the entry starts, and an end date
when the entry ends. The dates are in RFC3339 format, and will be saved in UTC
time.
You can specify if an entry repeats, as defined in ISO 8601 repeating
intervals. A location can be added as well, if needed, as a string, e.g.
"Living room".
The `cc` is a list of user IDs to whom the calendar entry can be CC'd to.
A notification about the entry will be sent to these users.
 

**Version:** v1 

## /calendar
### **post** 

**Description:** Create a new calendar entry

#### http request 


 > Example for: POST /calendar 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/calendar/v1/calendar \
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf" \
-d '{
	"toIdentity": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "type": "Event",
	"title": "Autumn feast 2",
	"startDate": "2019-08-10T17:00:00+02:00",
	"endDate": "2019-08-10T20:00:00+02:00",
	"repeats": null,
	"content": "Autumn feast",
	"location": "Courtyard",
	"cc": [
		"34fe0b13-e031-4ef2-822e-17eabad63259"
	]
}'
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 201 Created

{
  "@context": "https://platformoftrust.github.io/standards/contexts/calendar.jsonld",
  "@type": "Event",
  "@id": "67fa7be3-0c7d-4318-a09a-585181d1e6f3",
  "toIdentity": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "title": "Autumn feast 2",
  "startDate": "2019-08-10T15:00:00+00:00",
  "endDate": "2019-08-10T18:00:00+00:00",
  "repeats": null,
  "content": "Autumn feast",
  "location": "Courtyard",
  "cc": [
    "34fe0b13-e031-4ef2-822e-17eabad63259"
  ],
  "createdBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "updatedBy": null,
  "createdAt": "2019-03-14T14:02:29+00:00",
  "updatedAt": "2019-03-14T14:02:29+00:00"
}

```


**POST** /calendar 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 422 |  |

## /calendar/{id}
### **get** 

**Description:** Read one calendar by id

#### http request 


 > Example for: GET /calendar/{id} 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/calendar/v1/calendar/67fa7be3-0c7d-4318-a09a-585181d1e6f3 \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://platformoftrust.github.io/standards/contexts/calendar.jsonld",
  "@type": "Event",
  "@id": "67fa7be3-0c7d-4318-a09a-585181d1e6f3",
  "toIdentity": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "title": "Autumn feast 2",
  "startDate": "2019-08-10T15:00:00+00:00",
  "endDate": "2019-08-10T18:00:00+00:00",
  "repeats": null,
  "content": "Autumn feast",
  "location": "Courtyard",
  "cc": [
    "34fe0b13-e031-4ef2-822e-17eabad63259"
  ],
  "createdBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "updatedBy": null,
  "createdAt": "2019-03-14T14:02:29+00:00",
  "updatedAt": "2019-03-14T14:02:29+00:00"
}

```


**GET** /calendar/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the calendar | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

### **put** 

**Description:** Update a calendar by id

#### http request 


 > Example for: PUT /calendar/{id} 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X PUT https://api-sandbox.oftrust.net/calendar/v1/calendar/67fa7be3-0c7d-4318-a09a-585181d1e6f3 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf" \
-d '{
	"toIdentity": "34fe0b13-e031-4ef2-822e-17eabad63259",
	"title": "Autumn feast 3",
}'
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 201 Created

{
  "@context": "https://platformoftrust.github.io/standards/contexts/calendar.jsonld",
  "@type": "Event",
  "@id": "67fa7be3-0c7d-4318-a09a-585181d1e6f3",
  "toIdentity": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "title": "Autumn feast 2",
  "startDate": "2019-08-10T15:00:00+00:00",
  "endDate": "2019-08-10T18:00:00+00:00",
  "repeats": null,
  "content": "Autumn feast",
  "location": "Courtyard",
  "cc": [
    "34fe0b13-e031-4ef2-822e-17eabad63259"
  ],
  "createdBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "updatedBy": null,
  "createdAt": "2019-03-14T14:02:29+00:00",
  "updatedAt": "2019-03-14T14:02:29+00:00"
}

```


**PUT** /calendar/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the calendar | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |
| 422 |  |

### **delete** 

**Description:** Delete a calendar by id

#### http request 


 > Example for: DELETE /calendar/{id} 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X DELETE https://api-sandbox.oftrust.net/calendar/v1/calendar/67fa7be3-0c7d-4318-a09a-585181d1e6f3 \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return header structured like this:

```json
HTTP/1.0 204 No Content
```


**DELETE** /calendar/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the calendar | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |

## /calendar/{toidentity}/list
### **get** 

**Description:** List all calendars belonging to the "to" identity.

#### http request 
**GET** /calendar/{toIdentity}/list 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| toIdentity | path | The identity to which the calendar belongs to. | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
# Context API

The Context API provides means to list available JSON-LD contexts in the
PlatformOfTrust/standards repository in GitHub.

The contexts defines the semantic meaning of the keys in the responses from the APIs.
When creating a new identity, choose which type of identity to create by
choosing the correct context. The context will then define the attributes the
identity can have.
 

**Version:** v1 

## /contexts
### **get** 

**Description:** Returns a list of all defined contexts

#### http request 


 > Example for: GET /contexts 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
cURL example not found. Why not contribute one for us?
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  ...
}

```


**GET** /contexts 

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
# Identity API

The Identity API provides means to create, update and delete digital twins
(identities) and manage links between them.
The links provides the direction and type (sometimes called role) of the link.
 

**Version:** v1 

## /identity
### **post** 

**Description:** Create a new identity

#### http request 


 > Example for: POST /identity 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/identity/v1/identity \
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf" \
-d '{
	"context": "http://platformoftrust.github.io/standards/contexts/identity-person.jsonld",
	"type": "Person",
	"name": "John Doe",
	"data": {
		"firstName": "John",
		"lastName": "Doe"
	}
}'
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 201 Created

{
  "@context": "http://platformoftrust.github.io/standards/contexts/identity-person.jsonld",
  "@type": "Person",
  "@id": "fbd106c5-c594-4416-a87e-f61e578fe829",
  "name": "John Doe",
  "data": {
    "firstName": "John",
    "lastName": "Doe"
  },
  "createdBy": "4c276e02-719c-4415-abba-a7afc4edc0c0",
  "updatedBy": null,
  "createdAt": "2019-03-14T10:50:51+00:00",
  "updatedAt": "2019-03-14T10:50:51+00:00",
  "status": 0,
  "inLinks": [],
  "outLinks": []
}

```


**POST** /identity 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 422 |  |

## /identity/{id}
### **get** 

**Description:** Read one identity by id

#### http request 


 > Example for: GET /identity/{id} 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/identity/v1/identity/fbd106c5-c594-4416-a87e-f61e578fe829 \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "http://platformoftrust.github.io/standards/contexts/identity-person.jsonld",
  "@type": "Person",
  "@id": "fbd106c5-c594-4416-a87e-f61e578fe829",
  "name": "John Doe",
  "data": {
    "firstName": "John",
    "lastName": "Doe"
  },
  "createdBy": "4c276e02-719c-4415-abba-a7afc4edc0c0",
  "updatedBy": null,
  "createdAt": "2019-03-14T10:50:51+00:00",
  "updatedAt": "2019-03-14T10:50:51+00:00",
  "status": 0,
  "inLinks": [],
  "outLinks": []
}

```


**GET** /identity/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the Identity | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

### **put** 

**Description:** Update an identity by id

#### http request 


 > Example for: PUT /identity/{id} 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X PUT https://api-sandbox.oftrust.net/identity/v1/identity/fbd106c5-c594-4416-a87e-f61e578fe829 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf" \
-d '{
	"context": "http://platformoftrust.github.io/standards/contexts/identity-person.jsonld",
	"type": "Person",
	"name": "John Doe",
	"data": {
		"firstName": "John",
		"lastName": "Doe",
		"gender": "Male"
	}
}'
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "http://platformoftrust.github.io/standards/contexts/identity-person.jsonld",
  "@type": "Person",
  "@id": "fbd106c5-c594-4416-a87e-f61e578fe829",
  "name": "John Doe",
  "data": {
    "firstName": "John",
    "lastName": "Doe",
    "gender": "Male"
  },
  "createdBy": "4c276e02-719c-4415-abba-a7afc4edc0c0",
  "updatedBy": "4c276e02-719c-4415-abba-a7afc4edc0c0",
  "createdAt": "2019-03-14T10:50:51+00:00",
  "updatedAt": "2019-03-14T11:17:35+00:00",
  "status": 0,
  "inLinks": [],
  "outLinks": []
}

```


**PUT** /identity/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the Identity | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |
| 422 |  |

### **delete** 

**Description:** Delete an identity by id

#### http request 


 > Example for: DELETE /identity/{id} 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X DELETE https://api-sandbox.oftrust.net/identity/v1/identity/sdssSsAaASew342SD3as14 \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 204 No Content

```


**DELETE** /identity/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the Identity | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |

## /identities
### **get** 

**Description:** List all identities created by currently logged in user

#### http request 


 > Example for: GET /identities 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/identity/v1/identities \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://schema.org/",
  "@type": "collection",
  "ItemList": [
    {
      "@context": "http://platformoftrust.github.io/standards/contexts/identity-person.jsonld",
      "@type": "Person",
      "@id": "fbd106c5-c594-4416-a87e-f61e578fe829",
      "name": "John Doe",
      "data": {
        "firstName": "John",
        "lastName": "Doe",
        "gender": "Male"
      },
      "createdBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
      "updatedBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
      "createdAt": "2019-03-14T10:50:51+00:00",
      "updatedAt": "2019-03-14T11:17:35+00:00",
      "status": 0,
      "inLinks": [],
      "outLinks": []
    },
    ...
  ]
}}

```


**GET** /identities 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

## /identities/{from_identity}/link/{to_identity}
### **post** 

**Description:** Creates a new link between two identities

#### http request 
**POST** /identities/{from_identity}/link/{to_identity} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| from_identity | path | The starting identity ID of the link | Yes | string |
| to_identity | path | The ending identity ID of the link | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 404 |  |
| 422 |  |

## /identities/{from_identity}/link/{to_identity}/{type}
### **put** 

**Description:** Update a link

#### http request 
**PUT** /identities/{from_identity}/link/{to_identity}/{type} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| type | path | The link type | Yes | string |
| from_identity | path | The starting identity ID of the link | Yes | string |
| to_identity | path | The ending identity ID of the link | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 404 |  |
| 422 |  |

### **delete** 

**Description:** Delete a link by type

#### http request 
**DELETE** /identities/{from_identity}/link/{to_identity}/{type} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| type | path | The link type | Yes | string |
| from_identity | path | The starting identity ID of the link | Yes | string |
| to_identity | path | The ending identity ID of the link | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |
| 422 |  |

## /identities/{id}/links
### **get** 

**Description:** List all links for a given identity

#### http request 
**GET** /identities/{id}/links 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the identity | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

## /identities/{id}/links/{type}
### **get** 

**Description:** List all links of type {type} for given identity

#### http request 


 > Example for: GET /identities/{id}/links/{type} 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/identities/35ee9e31-acee-42b4-ac7b-675790cc2721/links/Link \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://schema.org/",
  "@type": "collection",
  "ItemList": [
    {
      "@context": "https://platformoftrust.github.io/standards/contexts/link-link.jsonld",
      "@type": "Link",
      "@id": "10fab397-db00-424c-8281-8115b1985d23",
      "from": "86201e7d-6784-454b-9839-f7a6286f1791",
      "to": "35ee9e31-acee-42b4-ac7b-675790cc2721",
      "createdBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
      "updatedBy": null,
      "createdAt": "2019-03-14T13:46:15+00:00",
      "updatedAt": "2019-03-14T13:46:15+00:00"
    }
  ]
}

```


**GET** /identities/{id}/links/{type} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| type | path | The link type | Yes | string |
| id | path | The ID of the identity | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
# Message API

The message API provides means to create/send messages to identities.
You can send a message to any identity, e.g. a housing company, where all
users who has access to the housing company identity and its messages can
read the message.

The message requires a `"to"`-identity, the ID of the identity to which
the message applies to.
A message `subject` and its `content` should be added as well.

The `cc` is a list of user IDs to whom the message can be CC'd to.
A notification about the message will be sent to these users.
 

**Version:** v1 

## /message
### **post** 

**Description:** Create a new message

#### http request 


 > Example for: POST /message 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/message/v1/message \
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf" \
-d '{
	"toIdentity": "34fe0b13-e031-4ef2-822e-17eabad63259",
	"subject": "Test message nr 1",
	"content": "Testing the message api",
	"cc": [
		"34fe0b13-e031-4ef2-822e-17eabad63259"
	]
}'
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 201 Created

{
  "@context": "https://platformoftrust.github.io/standards/contexts/message.jsonld",
  "@type": "Message",
  "@id": "3a9e31ff-b654-4069-8361-6b446dc04c95",
  "toIdentity": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "subject": "Test message nr 1",
  "content": "Testing the message api",
  "cc": [
    "34fe0b13-e031-4ef2-822e-17eabad63259"
  ],
  "readBy": [],
  "createdBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "updatedBy": null,
  "createdAt": "2019-03-14T13:55:12+00:00",
  "updatedAt": "2019-03-14T13:55:12+00:00"
}

```


**POST** /message 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 422 |  |

## /message/{id}
### **get** 

**Description:** Read one message by id

#### http request 


 > Example for: GET /message/{id} 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/message/v1/message/3a9e31ff-b654-4069-8361-6b446dc04c95 \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://platformoftrust.github.io/standards/contexts/message.jsonld",
  "@type": "Message",
  "@id": "3a9e31ff-b654-4069-8361-6b446dc04c95",
  "toIdentity": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "subject": "Test message nr 1",
  "content": "Testing the message api",
  "cc": [
    "34fe0b13-e031-4ef2-822e-17eabad63259"
  ],
  "readBy": [],
  "createdBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "updatedBy": null,
  "createdAt": "2019-03-14T13:55:12+00:00",
  "updatedAt": "2019-03-14T13:55:12+00:00"
}

```


**GET** /message/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the message | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

### **put** 

**Description:** Update a message by id

#### http request 


 > Example for: PUT /message/{id} 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X PUT https://api-sandbox.oftrust.net/message/v1/message/3a9e...04c95 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLC29w...DVs5aaf" \
-d '{
	"subject": "Updated Test message",
	"content": "Testing the message api"
}'
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://platformoftrust.github.io/standards/contexts/message.jsonld",
  "@type": "Message",
  "@id": "3a9e31ff-b654-4069-8361-6b446dc04c95",
  "toIdentity": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "subject": "Updated Test message",
  "content": "Testing the message api",
  "cc": [
    "34fe0b13-e031-4ef2-822e-17eabad63259"
  ],
  "readBy": [],
  "createdBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "updatedBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
  "createdAt": "2019-03-14T13:55:12+00:00",
  "updatedAt": "2019-03-14T13:58:13+00:00"
}

```


**PUT** /message/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the message | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |
| 422 |  |

### **delete** 

**Description:** Delete a message by id

#### http request 


 > Example for: DELETE /message/{id} 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X DELETE https://api-sandbox.oftrust.net/message/v1/message/3a9e31ff-b654-4069-8361-6b446dc04c95 \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return header structured like this:

```json
HTTP/1.0 204 No Content
```


**DELETE** /message/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the message | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |

## /message/{id}/read
### **post** 

**Description:** Marks a message read by the currently logged in user.

#### http request 


 > Example for: POST /message/{id}/read 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/message/v1/message/3a9e31ff-b654-4069-8361-6b446dc04c95/read
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK
```


**POST** /message/{id}/read 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the message | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 403 |  |

## /messages/{toidentity}/list
### **get** 

**Description:** List all messages belonging to the "to" identity.

#### http request 
**GET** /messages/{toIdentity}/list 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| toIdentity | path | The identity to which the message belongs to. | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
# Product API

The Product API provides means to manage products provided by PoT core.
The product defines the URL to the translator, as well as a product code to
use when requesting data from the translator.
 

**Version:** v1 

## /products
### **post** 

**Description:** Create a new product

#### http request 


 > Example for: POST /products 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/product/v1/products \
-H "Content-Type: application/json" \
-d '{
  "dataContext": "https://platformoftrust.github.io/standards/contexts/product-data.jsonld",
  "parameterContext": "https://platformoftrust.github.io/standards/contexts/product-parameters.jsonld",
  "productCode": "business-identity-test",
  "name": "Business identity",
  "translatorUrl": "http://translator-test-backend-app/business-identity",
  "organizationPublicKeys": [
    {
      "url": "https://example.com/example.pub",
      "type": "RsaSignature2018"
    }
  ],
  "description": "Test translator business information"
}'
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 201 Created
{
  "@context": "https://platformoftrust.github.io/standards/contexts/product.jsonld",
  "@type": "Product",
  "@id": "https://api-sandbox.oftrust.net/product/v1/products/business-identity-test",
  "productCode": "business-identity-test",
  "dataContext": "https://platformoftrust.github.io/standards/contexts/product-data.jsonld",
  "parameterContext": "https://platformoftrust.github.io/standards/contexts/product-parameters.jsonld",
  "translatorUrl": "http://translator-test-backend-app/business-identity",
  "name": "Business identity",
  "organizationPublicKeys": [
    {
      "url": "https://example.com/example.pub",
      "type": "RsaSignature2018"
    }
  ],
  "description": "Test translator business information",
  "imageUrl": null
}

```


**POST** /products 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 422 |  |

### **get** 

**Description:** Lists all available products.

#### http request 


 > Example for: GET /products 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/product/v1/products
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://schema.org/",
  "@type": "collection",
  "ItemList": [
    {
      "@context": "https://platformoftrust.github.io/standards/contexts/product.jsonld",
      "@type": "Product",
      "@id": "https://api-sandbox.oftrust.net/product/v1/products/prh-business-identity-data-product",
      "productCode": "prh-business-identity-data-product",
      "dataContext": null,
      "parameterContext": "https://platformoftrust.github.io/standards/contexts/product-parameters.jsonld",
      "translatorUrl": "http://translator-test-backend-app/business-identity",
      "name": "PRH Business Identity",
      "organizationPublicKeys": null,
      "description": "Returns business information from the PRH Open Data API",
      "imageUrl": null
    },
    ...
  ]
}

```


**GET** /products 

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

## /products/{product_code}
### **get** 

**Description:** Reads a single product by product code

#### http request 


 > Example for: GET /products/{product_code} 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/product/v1/products/business-identity-test
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://platformoftrust.github.io/standards/contexts/product.jsonld",
  "@type": "Product",
  "@id": "https://api-sandbox.oftrust.net/product/v1/products/business-identity-test",
  "productCode": "business-identity-test",
  "dataContext": "https://platformoftrust.github.io/standards/contexts/product-data.jsonld",
  "parameterContext": "https://platformoftrust.github.io/standards/contexts/product-parameters.jsonld",
  "translatorUrl": "http://translator-test-backend-app/business-identity",
  "name": "Business identity",
  "organizationPublicKeys": [
    {
      "url": "https://example.com/example.pub",
      "type": "RsaSignature2018"
    }
  ],
  "description": "Test translator business information",
  "imageUrl": null
}

```


**GET** /products/{product_code} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| product_code | path | The product code of the product. | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

### **put** 

**Description:** Update a product by product code

#### http request 


 > Example for: PUT /products/{product_code} 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X PUT https://api-sandbox.oftrust.net/product/v1/products/business-identity-test \
-H "Content-Type: application/json" \
-d '{
	"dataContext": "https://platformoftrust.github.io/standards/contexts/product-data.jsonld",
	"parameterContext": "https://platformoftrust.github.io/standards/contexts/product-parameters.jsonld",
	"name": "Testing business identity",
	"translatorUrl": "http://translator-test-backend-app/business-identity",
	"organizationPublicKeys": [
    {
      "url": "https://example.com/example.pub",
      "type": "RsaSignature2018"
    }
  ],
  "description": "Test translator business information",
  "imageUrl": "http://example.com/image.png"
}'
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://platformoftrust.github.io/standards/contexts/product.jsonld",
  "@type": "Product",
  "@id": "https://api-sandbox.oftrust.net/product/v1/products/business-identity-test",
  "productCode": "business-identity-test",
  "dataContext": "https://platformoftrust.github.io/standards/contexts/product-data.jsonld",
  "parameterContext": "https://platformoftrust.github.io/standards/contexts/product-parameters.jsonld",
  "translatorUrl": "http://translator-test-backend-app/business-identity",
  "name": "Testing business identity",
  "organizationPublicKeys": [
    {
      "url": "https://example.com/example.pub",
      "type": "RsaSignature2018"
    }
  ],
  "description": "Test translator business information",
  "imageUrl": "http://example.com/image.png"
}


```


**PUT** /products/{product_code} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| product_code | path | The product code of the product. | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |
| 422 |  |

### **delete** 

**Description:** Delete a product by product code

#### http request 


 > Example for: DELETE /products/{product_code} 


```python
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X DELETE https://api-sandbox.oftrust.net/product/v1/products/business-identity-test
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.print("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 204 No Content
```


**DELETE** /products/{product_code} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| product_code | path | The product code of the product. | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
