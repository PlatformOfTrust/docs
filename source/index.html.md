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


## What is Platform of Trust?

Communally built Platform of Trust provides a trustworthy and easy-to-use surrounding where you can utilize a vast data pool and develop everyday services for your customers with the help from the developer community and without a need for pricey and time-consuming integrations.  

Platform of Trust has Finnish origins, but it’s built to expand globally through the network of built environment innovation hubs.

**Developer Portal**

Our [Developer Portal](https://developers.oftrust.net) is your one-stop-shop. From there you'll find getting started guides, use case descriptions and 

**Market place**

Market place is the bazaar to find more data products to use in application development. Visa versa, it is also the service where your data products are added during the integration process. 

# Getting started

> Some instructions and tips to make your life easier (and less support requests to us): 

> - Endpoints related code examples are constructed against **SANDBOX environment `https://api-sandbox.oftrust.net/`**. 

> - In **PRODUCTION** use, change domain in api endpoints to `https://api.oftrust.net/`

> - **How to get needed Bearer Token?** See [Authentication section](#how-to-get-bearer-token)

> If you found a bug or missing information in the documentation, contact us at dev@oftrust.net or create an [issue in Github](https://github.com/PlatformOfTrust/docs/issues/new). 

* You should get familiar with [Authentication](#authentication) process regardless of are you integration data sources or building applications. 

* Related to authentication is the Bearer Token which is needed in some of the API calls. Check out the [How to get Bearer token?](#how-to-get-bearer-token) 

* Some of the API endpoints are CORS enabled and they are marked in the description. 

* Another thing to understand is the ontologies. We recommend that you [get familiar with core ontologies](#ontologies) especially if you are integrating data sources to the Platform of Trust. 

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


<aside class="warning">
All the documentation code examples use our sandbox environment. When you are done with testing, you should switch to production environment. Easiest way is to store API root url in variable and when needed, change it there. Thus the code examples contain API-root variable as an exmaple. 
</aside>


# Broker API

The Broker API provides means to connect a service to a translator that will
return desired data from different sources. The data broker does not mangle
the data in any way, it only functions as a proxy between services and
translators.
 

**Version:** v1 

## /fetch-data-product
### **post** 

**Description:** Fetch data product

#### http request 


 > Example for: POST /fetch-data-product 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell

X-Pot-App and X-Pot-Token is given upon application registration.

X-Pot-Signature is....TBD

Timestamp is security requirement. Intention is that you cannot just resend
the same captured request, you have to update timestamp and thus
re-sign at the minimum



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

## /


 > Example for:  POST 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/calendars/v1/ \
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
System.out.println("Java example missing. Why not contribute one for us?");
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


### **post** 

**Description:** Create a new calendar entry

#### http request 
**POST** / 

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

## /{id}
### **get** 

**Description:** Read one calendar by id

#### http request 


 > Example for: GET /{id} 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/calendars/v1/67fa7be3-0c7d-4318-a09a-585181d1e6f3 \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
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


**GET** /{id} 

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


 > Example for: PUT /{id} 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X PUT https://api-sandbox.oftrust.net/calendars/v1/67fa7be3-0c7d-4318-a09a-585181d1e6f3 \
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
System.out.println("Java example missing. Why not contribute one for us?");
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


**PUT** /{id} 

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


 > Example for: DELETE /{id} 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X DELETE https://api-sandbox.oftrust.net/calendars/v1/67fa7be3-0c7d-4318-a09a-585181d1e6f3 \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
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


**DELETE** /{id} 

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

## /{toidentity}/
### **get** 

**Description:** List calendars created for "to"-identity.

#### http request 


 > Example for: GET /{toIdentity}/ 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/calendars/v1/34fe0b13-e031-4ef2-822e-17eabad63259/list \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
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
      "@context": "https://platformoftrust.github.io/standards/contexts/calendar.jsonld",
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


**GET** /{toIdentity}/ 

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

## /
### **get** 

**Description:** Returns a list of all defined contexts

#### http request 


 > Example for: GET / 


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
      "url": "https://platformoftrust.github.io/standards/contexts/identity-apartment.jsonld"
    },
    ...
    {
      "type": "Link",
      "name": "Owner",
      "url": "https://platformoftrust.github.io/standards/contexts/link-owner.jsonld"
    }
  ]
}

```


**GET** / 

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

## /
### **get** 

**Description:** List all identities created by currently logged in user

#### http request 


 > Example for: GET / 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/identities/v1/ \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
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


**GET** / 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| type | query | If given to `GET /?type=App`, will list only the identities of `@type: "App"`  | No | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

### **post** 

**Description:** Create a new identity

#### http request 


 > Example for: POST / 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/identities/v1/ \
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


**POST** / 

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

## /{id}
### **get** 

**Description:** Read one identity by id

#### http request 


 > Example for: GET /{id} 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/identities/v1/fbd106c5-c594-4416-a87e-f61e578fe829 \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
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


**GET** /{id} 

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


 > Example for: PUT /{id} 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X PUT https://api-sandbox.oftrust.net/identities/v1/fbd106c5-c594-4416-a87e-f61e578fe829 \
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


**PUT** /{id} 

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


 > Example for: DELETE /{id} 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X DELETE https://api-sandbox.oftrust.net/identities/v1/fbd106c5-c594-4416-a87e-f61e578fe829 \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
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


**DELETE** /{id} 

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

## /{from_identity}/link/{to_identity}
### **post** 

**Description:** Creates a new link between two identities

#### http request 
**POST** /{from_identity}/link/{to_identity} 

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

## /{from_identity}/link/{to_identity}/{type}
### **put** 

**Description:** Update a link

#### http request 
**PUT** /{from_identity}/link/{to_identity}/{type} 

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
**DELETE** /{from_identity}/link/{to_identity}/{type} 

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

## /{id}/links
### **get** 

**Description:** List all links for a given identity

#### http request 


 > Example for: GET /{id}/links 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl https://api-sandbox.oftrust.net/identities/v1/35ee9e31-acee-42b4-ac7b-675790cc2721/links?type=Link \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
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


**GET** /{id}/links 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | The ID of the identity | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| type | query | If given to `GET /{id}/links?type=Owner`, will list only the links of `@type: "Owner"`  | No | string |

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

## /
### **post** 

**Description:** Create a new message

#### http request 


 > Example for: POST / 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/messages/v1/ \
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
System.out.println("Java example missing. Why not contribute one for us?");
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


**POST** / 

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

## /{id}
### **get** 

**Description:** Read one message by id

#### http request 


 > Example for: GET /{id} 


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


**GET** /{id} 

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


 > Example for: PUT /{id} 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X PUT https://api-sandbox.oftrust.net/messages/v1/3a9e...04c95 \
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
System.out.println("Java example missing. Why not contribute one for us?");
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


**PUT** /{id} 

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


 > Example for: DELETE /{id} 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X DELETE https://api-sandbox.oftrust.net/messages/v1/3a9e31ff-b654-4069-8361-6b446dc04c95 \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
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


**DELETE** /{id} 

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

## /{id}/read
### **post** 

**Description:** Marks a message read by the currently logged in user.

#### http request 


 > Example for: POST /{id}/read 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/messages/v1/3a9e31ff-b654-4069-8361-6b446dc04c95/read
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzY29w...DVs5aaf"
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


**POST** /{id}/read 

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

## /{toidentity}/
### **get** 

**Description:** List messages sent to "to"-identity.

#### http request 


 > Example for: GET /{toIdentity}/ 


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


**GET** /{toIdentity}/ 

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

## /
### **post** 

**Description:** Create a new product

#### http request 


 > Example for: POST / 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/products/v1/ \
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
System.out.println("Java example missing. Why not contribute one for us?");
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


**POST** / 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| Authorization | header |  | Yes | string |
| body | body |  | Yes |  |

**Responses**

| Code | Description |
| ---- | ----------- |
| 201 |  |
| 422 |  |

### **get** 

**Description:** Lists all available products. *NOTE*: This is a CORS enabled endpoint.


#### http request 


 > Example for: GET / 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
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
  var potAPI = "https://api-sandbox.oftrust.net/product/v1/products";
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


**GET** / 

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

## /{product_code}
### **get** 

**Description:** Reads a single product by product code. *NOTE*: This is a CORS enabled endpoint.


#### http request 


 > Example for: GET /{product_code} 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
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


**GET** /{product_code} 

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


 > Example for: PUT /{product_code} 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X PUT https://api-sandbox.oftrust.net/products/v1/business-identity-test \
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
System.out.println("Java example missing. Why not contribute one for us?");
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


**PUT** /{product_code} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| product_code | path | The product code of the product. | Yes | string |
| Authorization | header |  | Yes | string |
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


 > Example for: DELETE /{product_code} 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X DELETE https://api-sandbox.oftrust.net/products/v1/business-identity-test
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


**DELETE** /{product_code} 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| product_code | path | The product code of the product. | Yes | string |
| Authorization | header |  | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 204 |  |
| 404 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
