--- 

title: Platform Of Trust Data Broker 

language_tabs: 
   - shell 

toc_footers: 
   - <a href='#'>Sign Up for a Developer Key</a> 
   - <a href='https://github.com/lavkumarv'>Documentation Powered by lav</a> 

includes: 
   - errors 

search: true 

--- 

# Introduction 

The Broker API provides means to connect a service to a translator that will
return desired data from different sources. The data broker does not mangle
the data in any way, it only functions as a proxy between services and
translators.
 

**Version:** v1 

# /BROKER/{VERSION}/FETCH-DATA-PRODUCT
## ***POST*** 

**Description:** Request data from an external service defined by the data product, and
 product code. The data broker will validate the signature of the
 payload and when verified, relay the request to the translator
 connected to the data product. The translator will translate the
 information fetched from an external source into a standardized format
 that will be returned to the requester.


### HTTP Request 
`***POST*** /broker/{version}/fetch-data-product` 

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
