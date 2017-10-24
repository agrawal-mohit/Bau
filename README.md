# Bau

### What is this repository for? ###

* This is an Support Wheel of Fate system that allots daily shifts to engineer for business support

### Tech Stack ###
* This API is made in Python using Flask framework which is a lightweight framework suitable for creating Web services <br/>
* MongoDB is used for database as it is a  NoSQL based, open source, scalable database solution <br/>
* The client interface is a single page application made using Angular JS <br/>

### How do I get set up? ###

* Create and activate virtual environment with python 3 <br/>
    $ virtualenv -p python3 venv <br/>
    $ source venv/bin/activate


* Install and run MongoDB on port 27017

* Install dependencies from the requirements.txt file <br/>
    $ pip install -r requirements.txt


* Initialize  - Add engineer data to database <br/>
    $ python manage.py init

* Run the application <br/>
    $ python manage.py runserver

* Goto localhost:9090 to interact with the UI 
