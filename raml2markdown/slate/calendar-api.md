--- 

title: Calendar 

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

# /CALENDAR
## ***POST*** 

**Description:** Create a new calendar entry

### HTTP Request 
`***POST*** /calendar` 

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

# /CALENDAR/{ID}
## ***GET*** 

**Description:** Read one calendar by id

### HTTP Request 
`***GET*** /calendar/{id}` 

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

## ***PUT*** 

**Description:** Update a calendar by id

### HTTP Request 
`***PUT*** /calendar/{id}` 

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

## ***DELETE*** 

**Description:** Delete a calendar by id

### HTTP Request 
`***DELETE*** /calendar/{id}` 

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

# /CALENDAR/{TOIDENTITY}/LIST
## ***GET*** 

**Description:** List all calendars belonging to the "to" identity.

### HTTP Request 
`***GET*** /calendar/{toIdentity}/list` 

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
