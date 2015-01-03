##Parser project

[TOC]



###Document version

Date | Version | Author
---- | --- | ---
22-12-14 | 1.0 | Thomas





###Introduction
Parser project is writing software in python to extract product information from CADint generated sflt files and moving that information into a csv file that can be used to populate a MRP system database without manual entry.

###Current versions:

Work is being done on version 1.7 and 2.2.

Version 2.2 was converted to class based system for incorporation into flask

Best version is currently 1.7





###1.7 Documentation
Files located in /home/thomas/PythonProjects/parser/ver1/

####System requirements
Ubuntu based system with python 2.7.6
####Libraries used:
Lib | Link
---|---
xml.dom / minidom | https://docs.python.org/2/library/xml.dom.minidom.html
csv | https://docs.python.org/2/library/csv.html
os | https://docs.python.org/2/library/os.html
sys | https://docs.python.org/2/library/sys.html
glob | https://docs.python.org/2/library/glob.html

Includes:
* Ensures the input file is an SFLT document (auto detects sflt via loop but would shut down if that functionality was overwritten).
* Parses regardless of a or A keys.
* Loops through all sflt documents in the project folders and parses out csv bom files based on original file names.
* Adds all items to master_stock_list.csv found in the same directory.
* Class system dropped in favour of ease of use.


Excludes(for now):
* Does not check for duplicate entries.
* Only looks in folder specified in the code. Needs to ask for user input as to where it is looking.


###2.2 Documentation

Includes:
* Code broken up into classes/objects.
* Broken up into seperate files for input file, parsing and running app.
* Asks for raw_input from user as to which file to parse and where to write the result.

Excludes:
* Does not loop through multiple sflt files nor outputs to seperate files.
