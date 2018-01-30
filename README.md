# lyfttest
This project is a very small web app built for the Lyft Software Engineer Apprenticeship application, to fulfill the following functional specification:

```
If you don’t have a current code sample you can share, please write a small web application in
one of the above languages (Python/Ruby/Node). It only needs to accept a POST request to the route
“/test” which accepts two arguments “x” and “y” and returns a JSON object {“sum”: x+y}. To see
expected behavior you can test against a current working example with the command: curl -X POST 
https://lyft-interview-test.herokuapp.com/test --data '{"x": 4, "y": 2}' \ 
-H 'Content-Type: application/json'
```

This application was written with heavy help from the following tutorials:
1. The official Flask Tutorial by Armin Ronacher
   http://flask.pocoo.org/docs/0.12/tutorial/`

2. Implementing a RESTful Web API with Python & Flask by Luis Rei
   http://blog.luisrei.com/

3. Flask: Parsing JSON data
   https://techtutorialsx.com/2017/01/07/flask-parsing-json-data/   

## Installing / Getting started

The following instructions are written for a system running Fedora 26. To install and run this program on a different linux distribution, replace dnf with your respective package manager.

1. Download this project.

2. If you don't have pip and/or virtualenv, install them with the following commands:
```shell
sudo dnf install python-pip
sudo pip install virtualenv
```
3. Setup your virtual environment with the following command, replacing [venv name] with whatever you would like to name your virtual environment.
```shell
sudo virtualenv [venv name]
```
4. Install the Flask with the following commands, again replacing [vnev name] with your chosen virtual environment name.
```shell
source [venv name]/bin/activate
sudo pip install Flask
```
5. Finally, install lyfttest by running the following command from the root directory of the project:
```shell
pip install
```

The lyfttest app should now be installed in your virtual environment.

## Running the app
Once installed, you can run the application using the following commands:
```shell
export FLASK_APP=lyfttest
export FLASK_DEBUG=true
flask run
```

Test the application by running the following command in terminal:
```shell
curl -X POST https://lyft-interview-test.herokuapp.com/test --data '{"x": 4, "y": 2}' \
-H 'Content-Type: application/json'
```

## Licensing

The code in this project is licensed under MIT license.
