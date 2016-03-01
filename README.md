# bottle-example

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

A simple Python web server using the Bottle framework.

## Overview

This project implements a simple, [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)-compliant web server. We use the [Bottle](http://bottlepy.org/docs/dev/index.html) framework to define our routes but there are several other production-quality frameworks available:

* [CherryPy](https://en.wikipedia.org/wiki/CherryPy)
* [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
* [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))
* [webapp2](https://webapp-improved.appspot.com/)

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

There are many ways you can deploy the server to a hosting provider. We will be using [Heroku](https://www.heroku.com/), a platform provider, because it is free and because they provide a simple way to deploy. To deploy your service, simply click the "Deploy to Heroku" button at the top of this document. You will need to take note of the URL of your project. You can find the app name from your Heroku dashboard. Usually it will look something like http://your-app-name.herokuapp.com/.

#### Infrastructure as a Service

The major categories of providers are Infrastructure as a Service (IaaS) or Platform as a Service (PaaS). IaaS providers give you a more traditional server environment where you provision individual machines instances and interact with the operating system. Your server will run as a process within the operating system and you are responsible for theits lifecycle. You must also handle scaling of your infrastructure and load balancing between instances. Many IaaS providers offer advanced features that can help you manage instances more easily. Examples of IaaS providers are [Amazon Web Services](http://aws.amazon.com/), [Google Cloud Platform](https://cloud.google.com/), and [Rackspace Public Cloud](https://www.rackspace.com/en-us/cloud).

#### Platform as a Service

PaaS providers provide you with a simpler way to deploy and manage your application. Most PaaS providers will handle automatically scaling your service in times of load and are typically less expensive. However, your server must be written to conform with the platform's specifications. Most PaaS providers implement common standards, so this is typically not an issue. For example, most J2EE, node.js, and WSGI-compliant servers will run on PaaS providers. Examples of PaaS providers are [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/), [Google App Engine](https://cloud.google.com/appengine/), [Heroku](https://www.heroku.com/), and [PythonAnywhere](https://www.pythonanywhere.com/).

## Modifying the Server

For the purpose of this example, let us assume that the server is deployed at http://bottle-example.test/. If you are running locally, this address will be http://127.0.0.1:8080/. If the server is deployed to Heroku, it will be something like http://your-app-name.herokuapp.com/. You can find the app name from your Heroku dashboard.

### Adding an Endpoint

Now that you have a running server, let's try modifying it. First, let's add a new endpoint. Open [server.py](server.py) in an editor (or edit it directly from within GitHub) and add the following code:

```python
import random

@APP.get('/random')
def random_integer():
  return str(random.randint(0, 100))
```

Now, restart your server (or redeploy it), open the server in your web browser, and add "/random" to the end of your URL. For example, http://bottle-example.test/random. If you refresh the page several times, you should notice that the return value is different each time.

### Adding and Endpoint with Parameters

We can also send parameters to our server. In Bottle, this is accomplished by specifying variables in the URL. Open [server.py](server.py) and add the following code:

```python
@APP.get('/greet/<salutation>/<name>')
def greet(salutation, name):
  return '<p>Hello %s %s</p>' % (salutation, name)
```

Again, restart/redeploy your server and visit http://bottle-example.test/greet/Dr/Jekyll and http://bottle-example.test/greet/Mr/Hyde. You will notice that the displayed text changes depending on the parameters you have specified in your URL.

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

Again, restart/redeploy your server and visit http://bottle-example.test/index.html. You should see the contents of your HTML file displayed in your web browser.
