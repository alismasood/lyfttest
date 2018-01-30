# lyfttest
This project is a very small web app built for the Lyft Software Engineer Apprenticeship application, to fulfill the following functional specification:

```
 If you don’t have a current code sample you can share, please write a small web application in one of the above languages (Python/Ruby/Node). It only needs to accept a POST request to the route “/test” which accepts two arguments “x” and “y” and returns a JSON object {“sum”: x+y}. To see expected behavior you can test against a current working example with the command: curl -X POST https://lyft-interview-test.herokuapp.com/test --data '{"x": 4, "y": 2}' -H 'Content-Type: application/json'
```

## Installing / Getting started

The following instructions use syntax required to install on a Fedora 26 machine. To install and run this program on a different linux distribution, replace dnf with your respective package manager.

### 1. Download this project.
Fork or download this project.

### 2. Install Dependencies 
If you don't have pip and/or virtualenv, install them with the following commands:
```shell
sudo dnf install python-pip
sudo pip install virtualenv
```
Setup your virtual environment with the following command, replacing [venv name] with whatever you would like to name your virtual environment.
```shell
sudo virtualenv [venv name]
```
Install the Flask with the following commands, again replacing [vnev name] with your chosen virtual environment name.
```shell
source [venv name]/bin/activate
sudo pip install Flask
```
Finally, install lyfttest by running the following command from the root directory of the project:
```shell
pip install
```

The lyfttest app is now installed in your virtualenv

## Running
Once installed, you can run the application using these commands:
```shell
export FLASK_APP=lyfttest
export FLASK_DEBUG=true
flask run
```

Test the application by running the following command in terminal:
```shell
curl -X POST https://lyft-inter    view-test.herokuapp.com/test --data '{"x": 4, "y": 2}' -H 'Content-Type: application/json'
```

## Licensing

The code in this project is licensed under MIT license.
