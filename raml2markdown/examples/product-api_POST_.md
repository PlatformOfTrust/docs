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
