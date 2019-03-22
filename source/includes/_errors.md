# Errors

The Platform of Trust APIs all use the following error codes:


Error Code | Meaning
---------- | -------
400 | Bad Request -- Your request is invalid.
401 | Unauthorized -- Your API key is wrong.
403 | Forbidden -- The item requested is hidden for administrators only.
404 | Not Found -- The specified item could not be found.
405 | Method Not Allowed -- You tried to access item with an invalid method.
406 | Not Acceptable -- You requested a format that isn't json.
410 | Gone -- The requested item has been removed from our servers.
422 | Unprocessable -- Entity is missing
429 | Too Many Requests -- You're requesting too many times! Slow down!
500 | Internal Server Error -- We had a problem with our server. Try again later.
503 | Service Unavailable -- We're temporarily offline for maintenance. Please try again later.
