# Make an ics file to import into Google Calendar or any online calendar that supports this file..

## Configuration
You need to install requirements.txt first to run any code.
```bash
pip install -r requirements.txt
```
In all files, there are
```py
EMAIL  =  ""
PASSWORD  =  ""
```
You need to edit the credentials needed for the code to run properly.

## Running
### main.py
Generate a calendar that matches exactly the one that shows on the portal page.
### for_weekly.py
Generate a calendar that is only for the week that is currently on.
### for_semester.py
Generate a calendar that only uses the semester table and does not account for days off.