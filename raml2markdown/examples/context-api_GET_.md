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
