# CFG 2018. Advanced Python. Music Application.

A Python app which uses Spotify API.

## Getting Started

### Prerequisites

Next things are needed to be installed:
```
Python 2.7 or Python 3.6
pip or pipenv
flask and requests packages
```

To be able to use the Spotify Web API, you will need a Spotify user account and registered application.
All the instructions can be found at
```
 https://developer.spotify.com/web-api/tutorial/
```

At the end you will have Client ID and Secret Key.  You will need them to make calls from your application to the Spotify web services.

### Prepare the app

To clone the sample application so that you have a local version of the code that you can run on your local machine for development and testing purposes, execute the following commands in your local command shell or terminal:

```
$ git clone https://github.com/CodeFirstGirls2018/ProjectTeam1.git
$ cd ProjectTeam1
```

## Running Locally

Next link should be added to the Redirect URIs whitelist at Your Spotify Application:

```
http://localhost:8888/callback
```

To run application locally execute the following command in your local command shell or terminal:

For Python3 version
```
$ CLIENT_SECRET=YourSpotifySecretKey python3 my_music_app.py
```

For Python2 version
```
$ CLIENT_SECRET=YourSpotifySecretKey python2 my_music_app.py
```

Your app should now be running on localhost:8888.

## Deploying to Heroku
Install the Heroku CLI

Create an app on Heroku, which prepares Heroku to receive your source code:

```
$ heroku create
```

Set config vars: CLIENT_SECRET and HEROKU_HOSTNAME:

```
$ heroku config:set CLIENT_SECRET=YourSpotifySecretKey
$ heroku config:set HEROKU_HOSTNAME=YourSpotifySecretKey
```

Deploying your code

```
$ git push heroku master
```

Now visit the app at the URL generated by its app name. As a handy shortcut, you can open the website as follows:

```
$ heroku open
```

### Using different versions of Python

To specify the running version of Python of your app make corresponding changes in Procfile and Pipfile.
For more information visit:
```
https://devcenter.heroku.com/articles/python-runtimes
```


### Collaborating with Other Developers on Your App

This article shows app owners how to share their app with collaborators:

```
https://devcenter.heroku.com/articles/collaborating
```



## Authors
