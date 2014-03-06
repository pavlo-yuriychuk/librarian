=Author

==Create new author

Request:

POST

/v1/authors

~~~json
{
  "name": "I me mine"
}
~~~

X-Auth-Token: jlkjdslfkjsdlkfjlkdsfjlkdsjflkjslkdf

Response:

{
 "id": "213hkj21h3kj1h2k3jh21kj3hk123",
 "name": "I me mine"
}

==Get author

GET

/v1/authors/<id>

{
 "id": "213hkj21h3kj1h2k3jh21kj3hk123",
 "name": "I me mine"
}

X-Auth-Token: jlkjdslfkjsdlkfjlkdsfjlkdsjflkjslkdf

==Get all authors

GET 

/v1/authors

[
  {
    "id": "213hkj21h3kj1h2k3jh21kj3hk123",
    "name": "I me mine"
  },
  {
    "id": "213hkj21h3kj1h2k3jh21kj3hk123",
    "name": "I me mine"
  }
]

