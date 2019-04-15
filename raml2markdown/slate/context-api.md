--- 

title: Context 

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

The Context API provides means to list available JSON-LD contexts in the
PlatformOfTrust/standards repository in GitHub.

The contexts defines the semantic meaning of the keys in the responses from the APIs.
When creating a new identity, choose which type of identity to create by
choosing the correct context. The context will then define the attributes the
identity can have.
 

**Version:** v1 

# /CONTEXTS/{VERSION}
## ***GET*** 

**Description:** Returns a list of all defined contexts

### HTTP Request 
`***GET*** /contexts/{version}` 

**Parameters**

| Name | Located in | Description | Required | Type |
| ---- | ---------- | ----------- | -------- | ---- |
| version | path |  | Yes | string |

**Responses**

| Code | Description |
| ---- | ----------- |
| 200 |  |

<!-- Converted with the swagger-to-slate https://github.com/lavkumarv/swagger-to-slate -->
