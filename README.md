# Bau

* This is an Support Wheel of Fate system that allots daily shifts to engineer for business support. 

The allotment is made satisfying these rules-
1. An engineer can do at most one half day shift in a day.
2. An engineer cannot have half day shifts on consecutive days.
3. Each engineer should have completed one whole day of support in any 2 week period


### Tech Stack ###
* This API is made in Python using Flask framework which is a lightweight framework suitable for creating Web services <br/>
* MongoDB is used for database as it is a  NoSQL based, open source, scalable database solution <br/>
* The client interface is a single page application made using Angular JS <br/>

### Setup ###

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


### Approach ###

A schedule for the whole period (weeks) is generated at one go when the user requests for the day's allotment through the UI and saved in the database. Subsequent requests are served by fetching the schedule form the database until the period is over. When the user requests the shift for the next day after the last date of the generated period, the same procedure is repeated again.

### Algorithm ###

A pool of candidates is created that contains sets of the exhaustive list of all engineers. Each set contains an engineer name only once. The number of sets in the pool is equal to the number of shifts each engineer has to do in a period. So in this case there are 2 sets (1) & (2), each set containing 10 unique engineer records.

The ScheduleGenerator service generates the schedule, it loops through the slots in a period and for each slot, a random candidate is pulled from a set and evaluated to meet the 3 criterias. If the candidate is suitable he/she is alloted the slot and removed from the pool set. This is continued until the set(1) is exhausted and all slots in the first half(week) of the period are filled. For the next half, each slot is filled with candidates from the set (2). This improves the chances that each engineer gets atleast one full day of support per period (rule 3)

In case no suitable candidate is found, the generator is started again and a fresh schedule is generated. 

This is repeated until all the slots in the period are filled.








