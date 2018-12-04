[![Build Status](https://travis-ci.org/keronei/iReporter.svg?branch=develop)](https://travis-ci.org/keronei/iReporter)

# iReporter
Platform for reporting corruption and other issues that needs government intervention

## Basic Info
This platform has its backend build on `python Flask`  microframework. The frontend is `HTML` , `vanilla Js` & some `css`, The frontend is currently available [here](https://keronei.github.io/iReporter/UI/) on github pages.

## Installation & Usage
In order to make use of the backend API's , You will need set up the environment and launch the server.
Here is a step by step guide that will help you achieve this:
1. Make sure you have `Python 3.+` installed in your device. In order to ascertain this, run
 `$-> python` from your terminal(In the cases of Unix variant operating system).
 This is the kind of the response to expect:
 ```
 Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28)
 [Clang 6.0 (clang-600.0.57)] on darwin
 Type "help", "copyright", "credits" or "license" for more information.
 >>>
 ```

Once you are here, you can procede to step 2 of the process.
2. This backend is run with a python virtual environment in order to keep things organized, therefore, go ahead and install `virtualenv` , which is the virtual environment deployer (In this case you will require either `brew` or any other package manager that will help you install `pip` which is streamlined with virtualenv for convenience).
From here, run:
```
$->virtualenv env
```
This creates a virtual environment, and afterwards you will see that your working directory has been tweaked a litle bit, like so:
          env --|
                   |-bin
                   |-include
                   |-lib
From here, things aren't far, now lets get the actual repository(Assuming you have git installed):
```
$-> git clone https://github.com/keronei/iReporter
```
Give it 5 seconds of your life, let it count the objects, compress, download, decompress...
At this point you might need to take a minute to check the files just to get farmiliar with how things are structured, you will notice a file named `requirements.txt`, now that is the guy, he has all the dependencies for the project, dont just let him go.

In order to install  the dependencies, the `pip` will be required once again, so go ahead an do:
```
$-> pip install -r requirements.txt
```
In other scenarios, you will be required to use `pip3` which actually does happens when you have several `python` installs in your system, therefore `pip3` will do the trick of selecting what to use, git it a moment and you should be good to go.

Once all is installed, its time to fire-up the server. Go ahead and do:
```
$-> source env/bin/activate
```
This step activates the environment so that all the python procedures are done securely within the virtualizes envidronment. You will see something of this sort:
```
(env) MacBook-Air:iReporter your-user-name$
```
Now run the server:
```
$-> Python run.py
```
Just a few notes:
Make sure that  you didn't skip a step, failing to activate the environment is enough trouble to see some really anoying errors!
You are now ready to test a few things here and there, you are free to modify the code or create a `PR`, back to this repo.

If you would wish to get a taste of how things feel like without following the above steps, then you are free to proceed.
## Running Instance
The backend to this platform is hosted [here](http://ireporter-platform.herokuapp.com/) on Heroku.

In order to use the backend, the following endpoints are to be utilised:

To Retrieve all entries:

        http://ireporter-platform.herokuapp.com/api/v1/red-flag
        http://ireporter-platform.herokuapp.com/api/v1/intervention
To Retrieve a single entry:

        http://ireporter-platform.herokuapp.com/api/v1/red-flag/<id>

To update a specific entry's location using PATCH request:

        http://ireporter-platform.herokuapp.com/api/v1/red-flag/<id>/location

To Update a specific entry's comment:

        http://ireporter-platform.herokuapp.com/api/v1/red-flag/<id>/comment
                

The version 2 bit of this platform uses PostgreSql as the backend while the initial uses a simple Dictionary. In order to consume / provide data to V2 endpoint, you will only replace /v1/ with /v2/


