# GUI-testing-

This is my small personal project to do automated GUI testing. There are 2 versions of a GUI app that I built.

They can be found at (Websites up and running as of 04/07/23):
Version 1 - http://34.171.206.146:3200/
Version 2 - http://34.30.10.83:3200/

You can also host them on your local machine by running the flask apps - ./GUI1/GUI1.py and ./GUI2/GUI2.py

15 successful unit tests are created for the version 1 using Playwright and pytest. Version 2 is then tested using the same test cases, but few of them are going to fail to demonstrate the credibility of test cases. You can change the website address being tested in ./tests/test_first.py file in line number 4.