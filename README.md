# Google Geolocation System (HitManager)


## Description

This is a geolocation system focus on hitmen industry, uses the google maps API to search  the addresses of your target and obtain the latitude, longitude coordinates also can make
the reverse operation.

## Stack

the project have an api folder where are a Django Rest API that uses Sqlite as DB, and a ui folder that contains a React Web App

## Prerequisites 

* npm
* pip
* python3.8
* some virtual environment tool for python

## Installation API

Set environment variable 
```
$ export GOOGLE_MAPS_API_KEY=<your_google_maps_api_key>
```


Activate the virtualenviroment
```
$ source venv/bin/activate
```

Install python dependencies
```
$ pip install -r requirements.txt
```

Apply Django Migrations 
```
$ cd api
$ ./manage.py migrate
```

Runserver on localhost:8000

```
$ ./manage.py runserver
```

Test Endpoints
```
$ ./manage.py test
```

### Installation UI

Set environment variable 
```
$ export REACT_APP_GOOGLE_MAPS_API_KEY=<your_google_maps_api_key>
```
Install React Dependencies
```
$ npm i
```

Run Application on localhost:3000
```
$ npm start
```

