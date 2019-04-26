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
