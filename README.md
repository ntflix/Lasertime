# Lasertime

RESTful API to log and access laser time for users of [The Space](https://lamm.space) 🛠

## API Reference
### Full API Documentation is [here](https://docs.api.lasertime.iron59.co.uk).
The Lasertime API is organized around [REST](https://en.wikipedia.org/wiki/Representational_State_Transfer).
The API accepts JSON, multipart, and XML request bodies, returns JSON response bodies, and uses standard [HTTP response codes](https://httpstatuses.com) and authentication.

The order of parameters in request bodies is not important.

### Base URL
```http
https://api.lasertime.iron59.co.uk
```
The API may only be used with TLS.

# Deploying to Docker 🐳

## Example usage
```sh
docker run -d -p8080:8080 -e DATABASE_HOST="dev" -e DATABASE_PASSWORD="epicpassword123" fozflow/lasertime:latest
```

## Environment variables 🌈

Name | Description | Example | Default value
--- | --- | --- | ---
`DATABASE_HOST` | The hostname or IP address of the MySQL server to connect to | `172.16.55.241` | `hostname`
`DATABASE_PORT` | The port to use when connecting to the MySQL server | `33060` | `3306`
`DATABASE_USERNAME` | Username of the MySQL user | `gary` | `root`
`DATABASE_PASSWORD` | Password for said user | `mmmm cheese on toast` | `password`
`DATABASE_NAME` | Name of the database for lasertime | `worm_on_a_string` | `laser`
