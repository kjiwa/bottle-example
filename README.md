# Bottle Web Service Example

A simple Python web server using the Bottle framework.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Overview

This project implements a simple, [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)-compliant web server. We use the [Bottle](http://bottlepy.org/docs/dev/index.html) framework to define our routes but there are several other production-quality frameworks available:

* [CherryPy](https://en.wikipedia.org/wiki/CherryPy)
* [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
* [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))
* [webapp2](https://webapp-improved.appspot.com/)

## Prerequisites

In order to follow this guide you will need a [GitHub](https://github.com/) account. If you intend to deploy this service to [Heroku](https://www.heroku.com/) as described below, you will also need to sign up for an account with them.

Note that both GitHub and Heroku accounts are free.

In order to modify the server and add your own endpoints, first you will need to [fork this repository](https://help.github.com/articles/fork-a-repo/). To do so, click the "Fork" button at the top-right of this page.

## Running the Server

### Running the Server Locally

To run the server locally, you must have [Python](https://www.python.org/) installed. The server has been tested with Python 2.7.

Download [server.py](server.py) and [bottle.py](https://raw.githubusercontent.com/bottlepy/bottle/master/bottle.py) to the same directory. Then double click ```server.py``` to run it. Alternatively, you may execute the server from a terminal with ```python server.py```.

If everything is setup correctly, you should see the following text appear in your console:

```shell
Bottle v0.13-dev server starting up (using WSGIRefServer(application=<bottle.Bottle object at 0x7f4e9bca9510>))...
Listening on http://127.0.0.1:8080/
Hit Ctrl-C to quit.
```

Then, open a web browser and visit http://127.0.0.1:8080/ and you should see the message "Hello" appear.

### Running the Server with a Hosting Provider

There are many ways you can deploy the server to a hosting provider. We will be using [Heroku](https://www.heroku.com/), a platform provider, because it is free and because they provide a simple way to deploy code from GitHub.

To deploy your service, simply click the [Deploy to Heroku](https://heroku.com/deploy) button at the top of this document. You will be directed to Heroku where you can optionally enter an application name. A name will be automatically generated for you if you leave this field blank. Click "Deploy for Free" and then "View App".

You will need to take note of the URL of your project. You can find the app name from your Heroku dashboard -- usually it will have the form http://your-app-name.herokuapp.com/.

You may wish to follow Heroku's [GitHub Integration](https://devcenter.heroku.com/articles/github-integration) steps. This will cause Heroku to automatically update your app with changes you make in GitHub.

#### Infrastructure as a Service

The major categories of cloud service providers are *Infrastructure as a Service* (IaaS) providers and *Platform as a Service* (PaaS) providers. IaaS providers give you a more traditional server environment where you provision individual machine instances and interact directly with the operating system. Your server will run as an OS process and you are responsible for its lifecycle. You must handle scaling of your infrastructure and load balancing between instances during times of load. Examples of IaaS providers are [Amazon Web Services](http://aws.amazon.com/), [Google Cloud Platform](https://cloud.google.com/), and [Rackspace Public Cloud](https://www.rackspace.com/en-us/cloud).

#### Platform as a Service

PaaS providers provide you with a simpler way to deploy and manage your application. PaaS providers will manage the lifecycle of your server and automatically scale your service in times of load. As a result they are typically less expensive. However, your server must be written to conform with the platform's specifications. Most PaaS providers implement common standards, so this is typically not an issue. For example, most [J2EE](https://en.wikipedia.org/wiki/Java_Platform,_Enterprise_Edition), [Node.js](https://nodejs.org/), and WSGI-compliant servers will run on PaaS providers. Examples of PaaS providers are [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/), [Google App Engine](https://cloud.google.com/appengine/), [Heroku](https://www.heroku.com/), and [PythonAnywhere](https://www.pythonanywhere.com/).

## Modifying the Server

For the purpose of this example, let us assume that the server is deployed at http://bottle-example.test/. The actual URL of your server will differ. If you are running the server locally, this address will be http://127.0.0.1:8080/. If the server is deployed to Heroku, it will be something like http://your-app-name.herokuapp.com/. You can find the app name from your Heroku dashboard.

### Adding an Endpoint

Now that you have a running server, let's try modifying it. First, let's add a new endpoint. Open [server.py](server.py) in an editor (or edit it directly from within GitHub) and add the following code:

```python
import random

@APP.get('/random')
def random_integer():
  return str(random.randint(0, 100))
```

Now, restart your server (or redeploy it), open the server in your web browser, and add "/random" to the end of your URL. For example, [http://bottle-example.test/random](http://bottle-example.test/random). If you refresh the page several times, you should notice that the return value is different each time.

### Adding an Endpoint with Parameters

We can also send parameters to our server. In Bottle, this is accomplished by specifying variables in the URL. Open [server.py](server.py) and add the following code:

```python
@APP.get('/greet/<salutation>/<name>')
def greet(salutation, name):
  return '<p>Hello %s %s</p>' % (salutation, name)
```

Again, restart/redeploy your server and visit [http://bottle-example.test/greet/Dr/Jekyll](http://bottle-example.test/greet/Dr/Jekyll) and [http://bottle-example.test/greet/Mr/Hyde](http://bottle-example.test/greet/Mr/Hyde). You will notice that the displayed text changes depending on the parameters you have specified in your URL.

### Serving Static Content

It is not ideal for us to be generating HTML from directly within our server code. Instead, it's better to keep files written in a single language. Most larger projects will have build and analysis tools that are capable of detecting errors or optimizing files based on their content types. Separating the files based on language enables us to make use of these tools.

Create a new file called ```index.html``` and add the following contents to it:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Home</title>
  </head>
  <body>
    <p>Welcome to my home page.</p>
  </body>
</html>
```

Now, edit [server.py](server.py) and add the following code:

```python
@APP.get('/index.html')
def index():
  return bottle.static_file('index.html', '.')
```

Again, restart/redeploy your server and visit [http://bottle-example.test/index.html](http://bottle-example.test/index.html). You should see the contents of your HTML file displayed in your web browser.
