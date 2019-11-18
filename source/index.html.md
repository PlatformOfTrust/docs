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
   - errors 
   - feedback
   

search: true 

--- 


# Platform of Trust API Documentation


### What is Platform of Trust?

Communally built Platform of Trust provides a trustworthy and easy-to-use surrounding where you can utilize a vast data pool and develop everyday services for your customers with the help from the developer community and without a need for pricey and time-consuming integrations.  

Platform of Trust has Finnish origins, but it’s built to expand globally through the network of built environment innovation hubs.

### Developer Portal

Our [Developer Portal](https://developers.oftrust.net) is your one-stop-shop. From there you'll find getting started guides, API descriptions, use case descriptions and link to API documentation. 


### End-to-end developer experience

APIs play crucial role in our end-end-end developer experience from integrating data to creating valuable applications. API -first experience and consistent APIs are important to us and thus we have created (work in progress) [API Design Guide](https://platformoftrust.gitbook.io/api-design-guide/) to offer guidance for our distributes API development teams. 

![End-to-end developer experience in Platform of Trust](images/dx.png)

### Market place

Market place is the bazaar to find more data products to use in application development. Visa versa, it is also the service where your data products are added during the integration process. 
You can list data products in the market place with [Product API](#product-api). 

# Getting started

> Some instructions and tips to make your life easier (and less support requests to us): 

> - **Create an account in sandbox** environment from https://world-sandbox.oftrust.net/

> - Endpoints related code examples are constructed against **SANDBOX environment `https://api-sandbox.oftrust.net/`**. 

> - In **PRODUCTION** use, change domain in api endpoints to `https://api.oftrust.net/`

> - To test APIs you need **to get needed Bearer Token** See [Authentication section](#use-bearer-token-and-how-to-get-it)

> If you found a bug or missing information in the documentation, contact us at dev@oftrust.net or create an [issue in Github](https://github.com/PlatformOfTrust/docs/issues/new). 

* First **create an account in sandbox** version of World app. If you have an account in production environment, that does not work in the sandbox environment.  


* You should **get familiar with [Authentication](#authentication) process** regardless of are you integration data sources or building applications. 

* Related to authentication is the **Bearer Token** which is needed in some of the API calls. Check out the [How to get Bearer token?](#use-bearer-token-and-how-to-get-it) 

* Some of the API endpoints are CORS enabled and they are marked in the description. 

* Another thing to understand is the harmonised data models. We recommend that you **[get familiar with core ontologies](https://github.com/PlatformOfTrust/standards/blob/master/README.md)** especially if you are integrating data sources to the Platform of Trust. 

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


# Broker API

> **Get Broker API related resources:**

> <div class='hexagon'><div class='hexagon-inside'><div class='hexagon-inside2'><a href='./specs/oas/broker-api.json' title='Get OpenAPI Specification Resources'><img src='images/oas.png' class='openApiSpec-lg'></a></div></div></div>
> <div class='hexagon'><div class='hexagon-inside'><div class='hexagon-inside2'><a href='./specs/raml/broker-api.zip' title='Get RAML Specification Resources'><img src='images/raml.png' class='ramlSpec-lg'></a></div></div></div>


The Broker API provides means to connect a service to a translator that will
return desired data from different sources. The data broker does not mangle
the data in any way, it only functions as a proxy between services and
translators.
 

**Version:** v1 

## /broker/v1/fetch-data-product
### **post** 

**Description:** Request data from an external service defined by the data product, and
 product code. The data broker will validate the signature of the
 payload and when verified, relay the request to the translator
 connected to the data product. The translator will translate the
 information fetched from an external source into a standardized format
 that will be returned to the requester.


#### http request 


 > <b>Example for: POST /broker/v1/fetch-data-product 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```bash

curl -X POST https://api-sandbox.oftrust.net/broker/v1/fetch-data-product \
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
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://standards.oftrust.net/contexts/prh-data-product.jsonld",
  "data": {
    "@context": "https://standards.oftrust.net/contexts/prh-data-product-parameters.jsonld",
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


**POST** /broker/v1/fetch-data-product 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| version | path |  | Yes | string |
| X-Pot-Signature | header | A HMAC-SHA256 signature in base64 encoded format. The signature is created by taking the request payload, e.g. a Python dict, and converting it to a string. <br/><br/>  Python example: <br/><br/> <code>  body_string = json.dumps( <br/>   body, <br/>   sort_keys=True, <br/>   indent=None, <br/>   separators=(',', ': ') <br/> ).strip() <br/><br/> </code> The keys MUST be sorted, without indentation and separators comma (,) and colon (:) specified. <br/><br/>  Get the digest by passing the app access token (generated when creating a new app) and the body string to `hmac`:<br/><br/> <code> digest = <br/> hmac.new(app_access_token.encode('utf-8'), <br/> body_string.encode('utf-8'),<br/> hashlib.sha256).digest()<br/><br/> </code><br/> Return the digest in base64 encoded format:<br/> <code> X-Pot-Signature = base64.b64encode(digest).decode()<br/> </code>  | Yes | string |
| X-Pot-App | header | The requesting application's client ID. | Yes | string |
| X-Pot-Token | header | The currently logged in user's OAuth access token.  | No | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 422 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
# Calendar API

> **Get Calendar API related resources:**

> <div class='hexagon'><div class='hexagon-inside'><div class='hexagon-inside2'><a href='./specs/oas/calendar-api.json' title='Get OpenAPI Specification Resources'><img src='images/oas.png' class='openApiSpec-lg'></a></div></div></div>
> <div class='hexagon'><div class='hexagon-inside'><div class='hexagon-inside2'><a href='./specs/raml/calendar-api.zip' title='Get RAML Specification Resources'><img src='images/raml.png' class='ramlSpec-lg'></a></div></div></div>


The calendar API provides means to create calendar entries to identities.
You can e.g. create an event for a housing company identity, a reservation
to a room identity, or just a regular calendar entry to any identity you want.<br/>

The calendar entry requires a `"to"`-identity, the ID of the identity to which
the calendar entry applies to. Specify a type for the entry, e.g.
`Event`, `Reservation`, `CalendarEntry`. Give the calendar entry a title, e.g.
"Housewarming party", a start date, when the entry starts, and an end date
when the entry ends. The dates are in RFC3339 format, and will be saved in UTC
time. <br/>

You can specify if an entry repeats, as defined in ISO 8601 repeating
intervals. A location can be added as well, if needed, as a string, e.g.
"Living room".<br/>

The `cc` is a list of user IDs to whom the calendar entry can be CC'd to.
A notification about the entry will be sent to these users.
 

**Version:** v1 

## /calendars/v1
### **post** 

**Description:** Create a new calendar entry

#### http request 


 > <b>Example for: POST /calendars/v1 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/calendars/v1/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN" \
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
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 201 Created

{
  "@context": "https://standards.oftrust.net/contexts/calendar.jsonld",
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


**POST** /calendars/v1 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| version | path |  | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 422 |  |

## /calendars/v1/{id}
### **get** 

**Description:** Read one calendar by id

#### http request 


 > <b>Example for: GET /calendars/v1/{id} 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/calendars/v1/67fa7be3-0c7d-4318-a09a-585181d1e6f3 \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://standards.oftrust.net/contexts/calendar.jsonld",
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


**GET** /calendars/v1/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the calendar | Yes | string |
| version | path |  | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

### **put** 

**Description:** Update a calendar by id

#### http request 


 > <b>Example for: PUT /calendars/v1/{id} 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X PUT https://api-sandbox.oftrust.net/calendars/v1/67fa7be3-0c7d-4318-a09a-585181d1e6f3 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN" \
-d '{
	"toIdentity": "34fe0b13-e031-4ef2-822e-17eabad63259",
	"title": "Autumn feast 3",
}'
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 201 Created

{
  "@context": "https://standards.oftrust.net/contexts/calendar.jsonld",
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


**PUT** /calendars/v1/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the calendar | Yes | string |
| version | path |  | Yes | string |
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


 > <b>Example for: DELETE /calendars/v1/{id} 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X DELETE https://api-sandbox.oftrust.net/calendars/v1/67fa7be3-0c7d-4318-a09a-585181d1e6f3 \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return header structured like this:

```json
HTTP/1.0 204 No Content
```


**DELETE** /calendars/v1/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the calendar | Yes | string |
| version | path |  | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |

## /calendars/v1/{toidentity}/list
### **get** 

**Description:** List calendars created for "to"-identity.

#### http request 


 > <b>Example for: GET /calendars/v1/{toIdentity}/list 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/calendars/v1/34fe0b13-e031-4ef2-822e-17eabad63259/list \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://schema.org/",
  "@type": "collection",
  "ItemList": [
    {
      "@context": "https://standards.oftrust.net/contexts/calendar.jsonld",
      "@type": "Event",
      "@id": "67fa7be3-0c7d-4318-a09a-585181d1e6f3",
      "toIdentity": "34fe0b13-e031-4ef2-822e-17eabad63259",
      "title": "Autumn feast",
      "startDate": "2019-08-10T14:00:00+00:00",
      "endDate": "2019-08-10T18:00:00+00:00",
      "repeats": null,
      "content": "Autumn feast stuff to do",
      "location": "Courtyard",
      "cc": [
        "34fe0b13-e031-4ef2-822e-17eabad63259"
      ],
      "createdBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
      "updatedBy": "34fe0b13-e031-4ef2-822e-17eabad63259",
      "createdAt": "2019-03-14T14:02:29+00:00",
      "updatedAt": "2019-03-14T14:02:29+00:00"
    }
  ]
}


```


**GET** /calendars/v1/{toIdentity}/list 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| toIdentity | path | The identity to which the calendar belongs to. | Yes | string |
| version | path |  | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
# Context API

> **Get Context API related resources:**

> <div class='hexagon'><div class='hexagon-inside'><div class='hexagon-inside2'><a href='./specs/oas/context-api.json' title='Get OpenAPI Specification Resources'><img src='images/oas.png' class='openApiSpec-lg'></a></div></div></div>
> <div class='hexagon'><div class='hexagon-inside'><div class='hexagon-inside2'><a href='./specs/raml/context-api.zip' title='Get RAML Specification Resources'><img src='images/raml.png' class='ramlSpec-lg'></a></div></div></div>


The Context API provides means to list available JSON-LD contexts in the
PlatformOfTrust/standards repository in GitHub.

The contexts defines the semantic meaning of the keys in the responses from the APIs.
When creating a new identity, choose which type of identity to create by
choosing the correct context. The context will then define the attributes the
identity can have.
 

**Version:** v1 

## /contexts/v1
### **get** 

**Description:** Returns a list of all defined contexts

#### http request 


 > <b>Example for: GET /contexts/v1 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/contexts/v1/
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://schema.org/",
  "@type": "collection",
  "ItemList": [
    {
      "type": "Identity",
      "name": "Apartment",
      "url": "https://standards.oftrust.net/contexts/identity-apartment.jsonld"
    },
    ...
    {
      "type": "Link",
      "name": "Owner",
      "url": "https://standards.oftrust.net/contexts/link-owner.jsonld"
    }
  ]
}

```


**GET** /contexts/v1 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| version | path |  | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
# Identity API

> **Get Identity API related resources:**

> <div class='hexagon'><div class='hexagon-inside'><div class='hexagon-inside2'><a href='./specs/oas/identity-api.json' title='Get OpenAPI Specification Resources'><img src='images/oas.png' class='openApiSpec-lg'></a></div></div></div>
> <div class='hexagon'><div class='hexagon-inside'><div class='hexagon-inside2'><a href='./specs/raml/identity-api.zip' title='Get RAML Specification Resources'><img src='images/raml.png' class='ramlSpec-lg'></a></div></div></div>


The Identity API provides means to create, update and delete digital twins
(identities) and manage links between them.
The links provides the direction and type (sometimes called role) of the link.
 

**Version:** v1 

## /identities/v1
### **get** 

**Description:** List all identities created by currently logged in user

#### http request 


 > <b>Example for: GET /identities/v1 
</b>

```python
import requests
import json
import sys

endpoint = 'https://api-sandbox.oftrust.net/identities/v1/'
api_token= 'REPLACE_WITH_YOUR_TOKEN'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

# Get the indentities
try:
        json_response = (requests.get(endpoint, headers=headers).json())
        print(json.dumps(json_response, indent=4, sort_keys=True))
except:
        print("Oops!",sys.exc_info()[0],"occured.")
```

```shell
curl https://api-sandbox.oftrust.net/identities/v1/ \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
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


**GET** /identities/v1 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| type | query | If given to `GET /identities/v1?type=App`, will list only the identities of `@type: "App"`  | No | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

### **post** 

**Description:** Create a new identity

#### http request 


 > <b>Example for: POST /identities/v1 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/identities/v1/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN" \
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
System.out.println("Java example missing. Why not contribute one for us?");
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


**POST** /identities/v1 

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

## /identities/v1/{id}
### **get** 

**Description:** Read one identity by id

#### http request 


 > <b>Example for: GET /identities/v1/{id} 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/identities/v1/fbd106c5-c594-4416-a87e-f61e578fe829 \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
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


**GET** /identities/v1/{id} 

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


 > <b>Example for: PUT /identities/v1/{id} 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X PUT https://api-sandbox.oftrust.net/identities/v1/fbd106c5-c594-4416-a87e-f61e578fe829 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN" \
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
System.out.println("Java example missing. Why not contribute one for us?");
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


**PUT** /identities/v1/{id} 

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


 > <b>Example for: DELETE /identities/v1/{id} 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X DELETE https://api-sandbox.oftrust.net/identities/v1/fbd106c5-c594-4416-a87e-f61e578fe829 \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 204 No Content

```


**DELETE** /identities/v1/{id} 

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

## /identities/v1/{from_identity}/link/{to_identity}
### **post** 

**Description:** Creates a new link between two identities

#### http request 


 > <b>Example for: POST /identities/v1/{from_identity}/link/{to_identity} 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/identities/v1/fbd106c5-c594-4416-a87e-f61e578fe829/link/86201e7d-6784-454b-9839-f7a6286f1791 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN" \
-d '{
	"context": "https://standards.oftrust.net/contexts/link-link.jsonld",
	"type": "Link",
}'
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 201 Created

{
  "@context": "https://standards.oftrust.net/contexts/link-link.jsonld",
  "@type": "Link",
  "@id": "6ca1e7fb-48a7-4e2c-bb4f-98e2b934aa80",
  "from": "fbd106c5-c594-4416-a87e-f61e578fe829",
  "to": "86201e7d-6784-454b-9839-f7a6286f1791",
  "createdBy": "93767688-4017-4952-b2d9-89286adca0c5",
  "updatedBy": "93767688-4017-4952-b2d9-89286adca0c5",
  "createdAt": "2019-04-10T08:27:00+00:00",
  "updatedAt": "2019-04-10T08:27:00+00:00"
}

```


**POST** /identities/v1/{from_identity}/link/{to_identity} 

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

## /identities/v1/{from_identity}/link/{to_identity}/{type}
### **get** 

**Description:** Read a link by type

#### http request 
**GET** /identities/v1/{from_identity}/link/{to_identity}/{type} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| type | path | The `@type` of the link, for example `Link`, `Tenant` or `Owner` | Yes | string |
| from_identity | path | The starting identity ID of the link | Yes | string |
| to_identity | path | The ending identity ID of the link | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

### **put** 

**Description:** Update a link

#### http request 


 > <b>Example for: PUT /identities/v1/{from_identity}/link/{to_identity}/{type} 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X PUT https://api-sandbox.oftrust.net/identities/v1/fbd106c5-c594-4416-a87e-f61e578fe829/link/86201e7d-6784-454b-9839-f7a6286f1791/Link \
-H "Content-Type: application/json" \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN" \
-d '{
	"context": "https://standards.oftrust.net/contexts/link-owner.jsonld",
	"type": "Owner",
}'
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://standards.oftrust.net/contexts/link-owner.jsonld",
  "@type": "Owner",
  "@id": "6ca1e7fb-48a7-4e2c-bb4f-98e2b934aa80",
  "from": "fbd106c5-c594-4416-a87e-f61e578fe829",
  "to": "86201e7d-6784-454b-9839-f7a6286f1791",
  "createdBy": "93767688-4017-4952-b2d9-89286adca0c5",
  "updatedBy": "93767688-4017-4952-b2d9-89286adca0c5",
  "createdAt": "2019-04-10T08:27:00+00:00",
  "updatedAt": "2019-05-10T08:27:00+00:00"
}

```


**PUT** /identities/v1/{from_identity}/link/{to_identity}/{type} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| type | path | The `@type` of the link, for example `Link`, `Tenant` or `Owner` | Yes | string |
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


 > <b>Example for: DELETE /identities/v1/{from_identity}/link/{to_identity}/{type} 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X DELETE https://api-sandbox.oftrust.net/identities/v1/fbd106c5-c594-4416-a87e-f61e578fe829/link/86201e7d-6784-454b-9839-f7a6286f1791/Link \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 204 No Content

```


**DELETE** /identities/v1/{from_identity}/link/{to_identity}/{type} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| type | path | The `@type` of the link, for example `Link`, `Tenant` or `Owner` | Yes | string |
| from_identity | path | The starting identity ID of the link | Yes | string |
| to_identity | path | The ending identity ID of the link | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |
| 422 |  |

## /identities/v1/{id}/links
### **get** 

**Description:** List all links for a given identity

#### http request 


 > <b>Example for: GET /identities/v1/{id}/links 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/identities/v1/35ee9e31-acee-42b4-ac7b-675790cc2721/links?type=Link \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://schema.org/",
  "@type": "collection",
  "ItemList": [
    {
      "@context": "https://standards.oftrust.net/contexts/link-link.jsonld",
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


**GET** /identities/v1/{id}/links 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the identity | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| type | query | If given to `GET /identities/v1/{id}/links?type=Owner`, will list only the links of `@type: "Owner"`  | No | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
# Message API

> **Get Message API related resources:**

> <div class='hexagon'><div class='hexagon-inside'><div class='hexagon-inside2'><a href='./specs/oas/message-api.json' title='Get OpenAPI Specification Resources'><img src='images/oas.png' class='openApiSpec-lg'></a></div></div></div>
> <div class='hexagon'><div class='hexagon-inside'><div class='hexagon-inside2'><a href='./specs/raml/message-api.zip' title='Get RAML Specification Resources'><img src='images/raml.png' class='ramlSpec-lg'></a></div></div></div>


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

## /messages/v1
### **post** 

**Description:** Create a new message

#### http request 


 > <b>Example for: POST /messages/v1 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/messages/v1/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN" \
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
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 201 Created

{
  "@context": "https://standards.oftrust.net/contexts/message.jsonld",
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


**POST** /messages/v1 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| version | path |  | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 422 |  |

## /messages/v1/{id}
### **get** 

**Description:** Read one message by id

#### http request 


 > <b>Example for: GET /messages/v1/{id} 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/messages/v1/3a9e31ff-b654-4069-8361-6b446dc04c95 \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://standards.oftrust.net/contexts/message.jsonld",
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


**GET** /messages/v1/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the message | Yes | string |
| version | path |  | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

### **put** 

**Description:** Update a message by id

#### http request 


 > <b>Example for: PUT /messages/v1/{id} 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X PUT https://api-sandbox.oftrust.net/messages/v1/3a9e...04c95 \
-H "Content-Type: application/json" \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN" \
-d '{
	"subject": "Updated Test message",
	"content": "Testing the message api"
}'
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://standards.oftrust.net/contexts/message.jsonld",
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


**PUT** /messages/v1/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the message | Yes | string |
| version | path |  | Yes | string |
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


 > <b>Example for: DELETE /messages/v1/{id} 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X DELETE https://api-sandbox.oftrust.net/messages/v1/3a9e31ff-b654-4069-8361-6b446dc04c95 \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return header structured like this:

```json
HTTP/1.0 204 No Content
```


**DELETE** /messages/v1/{id} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the message | Yes | string |
| version | path |  | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |

## /messages/v1/{id}/read
### **post** 

**Description:** Marks a message read by the currently logged in user.

#### http request 


 > <b>Example for: POST /messages/v1/{id}/read 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/messages/v1/3a9e31ff-b654-4069-8361-6b446dc04c95/read
-H "Content-Type: application/json" \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK
```


**POST** /messages/v1/{id}/read 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the message | Yes | string |
| version | path |  | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 403 |  |

## /messages/v1/{toidentity}/list
### **get** 

**Description:** List messages sent to "to"-identity.

#### http request 
**GET** /messages/v1/{toIdentity}/list 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| toIdentity | path | The identity to which the message belongs to. | Yes | string |
| version | path |  | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
# Product API

> **Get Product API related resources:**

> <div class='hexagon'><div class='hexagon-inside'><div class='hexagon-inside2'><a href='./specs/oas/product-api.json' title='Get OpenAPI Specification Resources'><img src='images/oas.png' class='openApiSpec-lg'></a></div></div></div>
> <div class='hexagon'><div class='hexagon-inside'><div class='hexagon-inside2'><a href='./specs/raml/product-api.zip' title='Get RAML Specification Resources'><img src='images/raml.png' class='ramlSpec-lg'></a></div></div></div>


The Product API provides means to manage products provided by PoT core.
The product defines the URL to the translator, as well as a product code to
use when requesting data from the translator.
 

**Version:** v1 

## /products/v1
### **post** 

**Description:** Create a new product

#### http request 


 > <b>Example for: POST /products/v1 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/products/v1/ \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN" \
-H "Content-Type: application/json" \
-d '{
  "dataContext": "https://standards.oftrust.net/contexts/product-data.jsonld",
  "parameterContext": "https://standards.oftrust.net/contexts/product-parameters.jsonld",
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
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 201 Created
{
  "@context": "https://standards.oftrust.net/contexts/product.jsonld",
  "@type": "Product",
  "@id": "https://api-sandbox.oftrust.net/product/v1/products/business-identity-test",
  "productCode": "business-identity-test",
  "dataContext": "https://standards.oftrust.net/contexts/product-data.jsonld",
  "parameterContext": "https://standards.oftrust.net/contexts/product-parameters.jsonld",
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


**POST** /products/v1 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| version | path |  | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 422 |  |

### **get** 

**Description:** Lists all available products. *NOTE*: This is a CORS enabled endpoint.
Supports pagination.


#### http request 


 > <b>Example for: GET /products/v1 
</b>

```python
import http.client

try:
    conn = http.client.HTTPSConnection('api-sandbox.oftrust.net')
    conn.request("GET", "/products/v1/")
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


```

```shell
curl https://api-sandbox.oftrust.net/products/v1/
```

```javascript
<!doctype html>
<html lang="en">
<head>
  <script src="http://code.jquery.com/jquery-3.3.1.min.js"></script>
</head>
<body>

<script>
$( document ).ready(function() {
  var potAPI = "https://api-sandbox.oftrust.net/products/v1/";
  $.getJSON( potAPI, function( data ) {
        alert(JSON.stringify(data));
    });
});
</script>

</body>
</html>
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://schema.org/",
  "@type": "collection",
  "ItemList": [
    {
      "@context": "https://standards.oftrust.net/contexts/product.jsonld",
      "@type": "Product",
      "@id": "https://api-sandbox.oftrust.net/product/v1/products/prh-business-identity-data-product",
      "productCode": "prh-business-identity-data-product",
      "dataContext": null,
      "parameterContext": "https://standards.oftrust.net/contexts/product-parameters.jsonld",
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


**GET** /products/v1 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| version | path |  | Yes | string |
| offset | query | Offset of a query | No | integer |
| limit | query | Limit the result of a query | No | integer |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

## /products/v1/{product_code}
### **get** 

**Description:** Reads a single product by product code. *NOTE*: This is a CORS enabled endpoint.


#### http request 


 > <b>Example for: GET /products/v1/{product_code} 
</b>

```python
import http.client

try:
    conn = http.client.HTTPSConnection('api-sandbox.oftrust.net')
    conn.request("GET", "/products/v1/business-identity-test")
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
```

```shell
curl https://api-sandbox.oftrust.net/products/v1/business-identity-test
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://standards.oftrust.net/contexts/product.jsonld",
  "@type": "Product",
  "@id": "https://api-sandbox.oftrust.net/product/v1/products/business-identity-test",
  "productCode": "business-identity-test",
  "dataContext": "https://standards.oftrust.net/contexts/product-data.jsonld",
  "parameterContext": "https://standards.oftrust.net/contexts/product-parameters.jsonld",
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


**GET** /products/v1/{product_code} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| product_code | path | The product code of the product. | Yes | string |
| version | path |  | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |
| 404 |  |

### **put** 

**Description:** Update a product by product code

#### http request 


 > <b>Example for: PUT /products/v1/{product_code} 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X PUT https://api-sandbox.oftrust.net/products/v1/business-identity-test \
-H "Content-Type: application/json" \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN" \
-d '{
	"dataContext": "https://standards.oftrust.net/contexts/product-data.jsonld",
	"parameterContext": "https://standards.oftrust.net/contexts/product-parameters.jsonld",
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
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 200 OK

{
  "@context": "https://standards.oftrust.net/contexts/product.jsonld",
  "@type": "Product",
  "@id": "https://api-sandbox.oftrust.net/product/v1/products/business-identity-test",
  "productCode": "business-identity-test",
  "dataContext": "https://standards.oftrust.net/contexts/product-data.jsonld",
  "parameterContext": "https://standards.oftrust.net/contexts/product-parameters.jsonld",
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


**PUT** /products/v1/{product_code} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| product_code | path | The product code of the product. | Yes | string |
| version | path |  | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
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


 > <b>Example for: DELETE /products/v1/{product_code} 
</b>

```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X DELETE https://api-sandbox.oftrust.net/products/v1/business-identity-test \
-H "Authorization: Bearer REPLACE_WITH_YOUR_TOKEN"
```

```javascript
console.error("Javascript example missing. Why not contribute one for us?");
```


```java
System.out.println("Java example missing. Why not contribute one for us?");
```

> The above example should return `JSON` structured like this:

```json
HTTP/1.0 204 No Content
```


**DELETE** /products/v1/{product_code} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| product_code | path | The product code of the product. | Yes | string |
| version | path |  | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
