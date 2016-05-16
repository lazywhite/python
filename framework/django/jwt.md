## Get Token
```
curl -X POST -d "username=admin&password=adminP@ssword" http://localhost:8000/api-token-auth/
{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwidXNlcl9pZCI6MSwiZW1haWwiOiJhZG1pbkBsb2NhbC5jb20iLCJleHAiOjE0NjI5NTQyMjF9.ja2d1hUBabumZqelLyilD2Q5M_CRyVGEkfdo5GEMicg"}
```
## Refresh Token
```
curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwib3JpZ19pYXQiOjE0NjI5NTM1MTQsInVzZXJfaWQiOjEsImVtYWlsIjoiYWRtaW5AbG9jYWwuY29tIiwiZXhwIjoxNDYyOTUzNjAwfQ.DAYBahC714L6DDJ3iEvpWOk9AEtZjExYG57qxZXDQFk"}' http://localhost:8000/api-token-refresh/
```

## Verify Token
```
curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwib3JpZ19pYXQiOjE0NjI5NTM1MTQsInVzZXJfaWQiOjEsImVtYWlsIjoiYWRtaW5AbG9jYWwuY29tIiwiZXhwIjoxNDYyOTUzNjAwfQ.DAYBahC714L6DDJ3iEvpWOk9AEtZjExYG57qxZXDQFk"}' http://localhost:8000/api-token-verify/
```
