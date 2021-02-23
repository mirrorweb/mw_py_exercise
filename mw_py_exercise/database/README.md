## 1.1.1 Company Record Fields
| name   | safe_name | address | telephone | enterprise | active |
|--------|-----------|---------|-----------|------------|--------|
| (str)  | (str)     | (str)   | (int)     | (bool)     | (int)  |

- The 'safe_name' value should be the name value with all whitespace & special characters removed, in lowercase.
- The 'address' value should be a combination of the street, city, country, postcode
- The 'active' value should be 1 for True and 0 for False

## 1.1.2 Employee Record Fields
| username | email | firstname | lastname | address | department | job   |
|----------|-------|-----------|----------|---------|------------|-------|
| (str)    | (str) | (str)     | (str)    | (str)   | (str)      | (str) |

- The 'address' value should be a combination of the street, city, country, postcode

------

Every record should have an appropriate primary key, of your choosing.
The data should be relational.

Every record should have a 'created' datetime field and an 'updated' datetime field.
The 'created' value is set when the record is created & the 'updated' datetime is set whenever the record changes.


Once complete:
[write step-by-step instructions here on how to replicate the setup of your local database on another machine]
