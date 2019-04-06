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

```bash

/* README
"X-Pot-App" and "X-Pot-Token" are given upon application registration.
"X-Pot-Signature" is....TBD
"timestamp" is security requirement. Intention is that you cannot just resend
the same captured request, you have to update timestamp and thus
re-sign at the minimum
------ */

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

## /calendars/{version}/


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


### **post** 

**Description:** Create a new calendar entry

#### http request 
**POST** /calendars/{version}/ 

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

## /calendars/{version}//{id}
### **get** 

**Description:** Read one calendar by id

#### http request 
**GET** /calendars/{version}//{id} 

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
**PUT** /calendars/{version}//{id} 

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
**DELETE** /calendars/{version}//{id} 

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

## /calendars/{version}//{toidentity}/
<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
# Context API

The Context API provides means to list available JSON-LD contexts in the
PlatformOfTrust/standards repository in GitHub.

The contexts defines the semantic meaning of the keys in the responses from the APIs.
When creating a new identity, choose which type of identity to create by
choosing the correct context. The context will then define the attributes the
identity can have.
 

**Version:** v1 

## /contexts/{version}/
### **get** 

**Description:** Returns a list of all defined contexts

#### http request 
**GET** /contexts/{version}/ 

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

The Identity API provides means to create, update and delete digital twins
(identities) and manage links between them.
The links provides the direction and type (sometimes called role) of the link.
 

**Version:** v1 

## /identities/{version}/
### **get** 

**Description:** List all identities created by currently logged in user

#### http request 
**GET** /identities/{version}/ 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| version | path |  | Yes | string |
| Authorization | header | The Authorization header, MUST be `Bearer {{access_token}}` | Yes | string |
| type | query | If given to `GET /?type=App`, will list only the identities of `@type: "App"`  | No | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

### **post** 

**Description:** Create a new identity

#### http request 
**POST** /identities/{version}/ 

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

## /identities/{version}//{id}
### **get** 

**Description:** Read one identity by id

#### http request 
**GET** /identities/{version}//{id} 

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
**PUT** /identities/{version}//{id} 

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
**DELETE** /identities/{version}//{id} 

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

## /identities/{version}//{from_identity}/link/{to_identity}
### **post** 

**Description:** Creates a new link between two identities

#### http request 
**POST** /identities/{version}//{from_identity}/link/{to_identity} 

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

## /identities/{version}//{from_identity}/link/{to_identity}/{type}
### **put** 

**Description:** Update a link

#### http request 
**PUT** /identities/{version}//{from_identity}/link/{to_identity}/{type} 

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
**DELETE** /identities/{version}//{from_identity}/link/{to_identity}/{type} 

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

## /identities/{version}//{id}/links
### **get** 

**Description:** List all links for a given identity

#### http request 
**GET** /identities/{version}//{id}/links 

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

## /messages/{version}/
### **post** 

**Description:** Create a new message

#### http request 
**POST** /messages/{version}/ 

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

## /messages/{version}//{id}
### **get** 

**Description:** Read one message by id

#### http request 
**GET** /messages/{version}//{id} 

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
**PUT** /messages/{version}//{id} 

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
**DELETE** /messages/{version}//{id} 

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

## /messages/{version}//{id}/read
### **post** 

**Description:** Marks a message read by the currently logged in user.

#### http request 
**POST** /messages/{version}//{id}/read 

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

## /messages/{version}//{toidentity}/
### **get** 

**Description:** List messages sent to "to"-identity.

#### http request 
**GET** /messages/{version}//{toIdentity}/ 

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

## /products/{version}/
### **post** 

**Description:** Create a new product

#### http request 


 > Example for: POST /products/{version}/ 


```python
import sys
sys.stdout.write("Python example missing. Why not contribute one for us?")
```

```shell
curl -X POST https://api-sandbox.oftrust.net/products/v1/ \
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


**POST** /products/{version}/ 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| version | path |  | Yes | string |
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


 > Example for: GET /products/{version}/ 


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


**GET** /products/{version}/ 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| version | path |  | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

## /products/{version}//{product_code}
### **get** 

**Description:** Reads a single product by product code. *NOTE*: This is a CORS enabled endpoint.


#### http request 


 > Example for: GET /products/{version}//{product_code} 


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


**GET** /products/{version}//{product_code} 

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
**PUT** /products/{version}//{product_code} 

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
**DELETE** /products/{version}//{product_code} 

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
