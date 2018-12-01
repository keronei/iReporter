[![Build Status](https://travis-ci.org/keronei/iReporter.svg?branch=develop)](https://travis-ci.org/keronei/iReporter)

# iReporter
Platform for reporting corruption and other issues that needs government intervention

## Basic Info
This platform has its backend build on `python Flask`  microframework. The frontend is `HTML` , `vanilla Js` & some `css`, The frontend is currently available [here](https://keronei.github.io/iReporter/UI/) on github pages.

On the other end, the backend to this platform is hosted [here](http://ireporter-platform.herokuapp.com/) on Heroku.

In order to use the backend, the following endpoints are to be utilised:

            To Retrieve all entries:
                
                    ```http://ireporter-platform.herokuapp.com/api/v1/red-flag```
                    ```http://ireporter-platform.herokuapp.com/api/v1/intervention```
            To Retrieve a single entry:

                ```http://ireporter-platform.herokuapp.com/api/v1/red-flag/<id>```

            To update a specific entry's location using PATCH request:

                ```http://ireporter-platform.herokuapp.com/api/v1/red-flag/<id>/location```

            To Update a specific entry's comment:
                ```
                http://ireporter-platform.herokuapp.com/api/v1/red-flag/<id>/comment
                ```

The version 2 bit of this platform uses PostgreSql as the backend while the initial uses a simple Dictionary. In order to consume / provide data to V2 endpoint, you will only replace /v1/ with /v2/


