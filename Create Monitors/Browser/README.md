# Create Browser Monitor

This script will create a single URL browser (Chrome or Firefox) monitor.

## Dependencies 
Python's 'requests' module 

## Usage
To run:

``` python create_browser_monitor.py <username> <password> <Google Chrome|Firefox> ```

Example:

``` python create_browser_monitor.py 'devops@corp.com' 'supersecretpw' 'Google Chrome' ```

If successful, the script will return the ID of the newly created monitor. 

Change the field values accordingly. For a list of all available locations visit https://www.alertsite.com/cgi-bin/helpme.cgi?page=monitoring_locations.html
