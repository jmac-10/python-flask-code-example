# remove duplicates
run the remove_dupes.py script to clean the csv, if that wasnt
self explanatory.

# run app
install requirements by running `pip install -r reqirements.txt`
in the project directory
run app locally with `python app.py` from project directory

# other comments
directions were not too clear about whether the csv data source is liable to be updated over the course of the apps
usage (ie: new records being added).

if that's a likely case, I'd probably want to add code to drop duplicates from the search results in app.py, in case the
remove_dupes.py script had not been run since duplicates had been added, although that script should probably just be
run any time the csv is updated.