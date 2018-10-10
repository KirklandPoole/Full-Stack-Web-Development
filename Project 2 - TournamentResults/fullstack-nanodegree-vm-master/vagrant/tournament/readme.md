Project 2 - Tournament Results
=========

##About

Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

##Creator
Kirkland Poole

##Quick Start
1. Setup the virtual environment as outline in the Tournament Results: Getting Started guide.
	https://docs.google.com/a/knowlabs.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true
2. Replace the 3 files in the tournament folder:
	○ tournament.sql
	○ tournament.py

3. Start the Vagrant Virtual Machine as outline in the Tournment Results: Gettng Started guide.
4. Launch the PSQL database by using the psql command.
5. Setup the tournament database schema by running loadind the tournament.sql file by using \i tournament.sql command.
6. Exit PSQL by using the \q command.
7. Test your implementation of functions in tournament.py by running the python tournament_test.py command
8. Review the results

###Dependencies
This app was developed using Python 2.7.9 or above.
The pre-configured Vagrant Virtual Machine environment from github: https://github.com/udacity/fullstack-nanodegree-vm
The implemented database schema file and phython methods:
	○ tournament.sql
	○ tournament.py

The following files must exist in the same file directory (vagrant/tournament):
	○ tournament.sql
	○ tournament.py
	○ tournament_test.py

