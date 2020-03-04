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

> **More resources & support**

> - Make use of [previously asked questions in Stack Overflow](https://stackoverflow.com/questions/tagged/platform-of-trust)
 
> - [Create new question](https://stackoverflow.com/questions/ask?guided=false&tags=platform-of-trust) in Stack Overflow if it's "*How do I?*" or "*I got this error, why?*" type of question

> - [Sign up to our Slack](https://join.slack.com/t/platformoftrust/shared_invite/enQtNTU0NDI1MjQ1MjM0LTg3YmYxNzJkM2ZlZTBiM2Y4ZjdhZmU2ZTRjZDU4NDNhMjA4YTk0YzM1NjJiMzIzZDViNWYwZjhiZDFjY2UzODk)

> - [Sign up for mailing list](https://platformoftrust.net/newsletter) 

### Developer Portal

Our [Developer Portal](https://developers.oftrust.net) is your one-stop-shop. From there you'll find getting started guides, API descriptions, use case descriptions and link to API documentation. 


### End-to-end developer experience

APIs play crucial role in our end-end-end developer experience from integrating data to creating valuable applications. API -first experience and consistent APIs are important to us and thus we have created (work in progress) [API Design Guide](https://design.oftrust.net/) to offer guidance for our distributes API development teams. 

![End-to-end developer experience in Platform of Trust](images/dx.png)


# Getting started

> Some instructions and tips to make your life easier (and less support requests to us): 

> - **[Create an account in sandbox](https://world-sandbox.oftrust.net/api/login)** environment

> - Endpoints related code examples are constructed against **SANDBOX environment `https://api-sandbox.oftrust.net/`**. 

> - In **PRODUCTION** use, change domain in API endpoints to `https://api.oftrust.net/`

> - To test APIs you need **to get needed Bearer Token** See [Authentication section](#use-bearer-token-and-how-to-get-it)

> If you found a bug or missing information in the documentation, create an [issue in Github](https://github.com/PlatformOfTrust/collected-feedback/issues/new?assignees=&labels=APIs&template=api-wishlists.md&title=Feedback+about+getting+started). 

* Account in production environment, that does not work in the sandbox environment.  


* You should **get familiar with [Authentication](#authentication) process** regardless of are you integration data sources or building applications. 

* Related to authentication is the **Bearer Token** which is needed in some of the API calls. Check out the [How to get Bearer token?](#use-bearer-token-and-how-to-get-it) 

* Some of the API endpoints are CORS enabled and they are marked in the description. 

* Another thing to understand is the harmonised data models. We recommend that you **[get familiar with core ontologies](https://standards.oftrust.net/v1/)** especially if you are integrating data sources to the Platform of Trust. 

## Standards used

**Dates**: we use a subset of ISO-8601 - [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt). Example <code>2008-09-15T15:53:00+05:00</code>

**Core Ontology**: The Platform Of Trust core ontology can be found as a JSON-LD ontology from [https://standards.oftrust.net/v1/](https://standards.oftrust.net/v1/).



