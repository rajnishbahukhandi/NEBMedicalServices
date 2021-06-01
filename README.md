NEBMedicalServices

Neb Medical is a trusted source of high-quality, affordable breast pumps, maternity accessories, and nebulizers.
At Neb Medical, help give every child the best possible start in life – whether that is through providing breast pumps to moms so they can feed and nurture their babies, or delivering lifesaving nebulizers to administer medication to children who suffer from asthma, helping them breathe more easily.



Automations script work flow:-

I used the data from the excel sheet. This data used for inputs fields for NEB Medical “InsuranceInformation” and “PersonalInformation”.

I first converted the excel sheet into the .csv. After that, I have provided a path of that .csv sheet to open the file in reading mode. 

It iterating over each row and append values to the empty list.After that complete, the process of information fills from the .csv (list data) sheet into the input field. And submit the form. It will send an email to the user-provided email id.

Now the email account will open on the next tab with valid credentials And will verify the unread email with the "NEB Medical" email subject line. 
And will open the matched subject line email.



python --version Python 2.7.16

POM(Page Object Module) Contains:-

CredentialsFile -

  - It having the credentials, user can edit.

  - .csv read file method. User need to convert the excel sheet into the .csv file.

  - Gmail account file method.
 
Locator - It having all the webElements.

Module - It having the calling method of .py file for “Getstarted”, “InsuranceInformation”, “PersonalInformation” pages.

TestCases - It having the unittest.TestCase class for run the test cases.


User Controls :- UserInputs.py 

  - User need to edit the values of UserInputs.py (CredentialsFile).
    
  - User enter the row number of the .csv file for taking data. (example:- csvrowvalue = 5)
         
  - User enter the email id for NEB Medical. And enter the valid credentials of email id and password of Gmail account.
           

CSVFileData.py - User can provide the local path of .csv file into CSVFileData.py (CredentialsFile). User need to convert excel sheet into the . csv file. The indexing start from the 0. 



Need To Install :-

The Python Package Index (PyPI) is a repository of software for the Python programming language. PyPI helps you find and install software developed and shared by the Python community.

https://pypi.org/

1. The selenium package is used to automate web browser interaction from Python. Supported Python Versions Python 2.7, 3.4+

   pip3 install selenium

2. The main idea is to simplify management of binary drivers for different browsers. For install the ChromeDriverManager

   from webdriver_manager.chrome import ChromeDriverManager

   pip3 install webdriver-manager

3. Faker is a Python package that generates fake data for you.

   from faker import Faker

   pip3 install Faker
   
4. Read .csv file.

   filename = open('/Users/ray.rajnish/Downloads/AutoApplyListforITH-HighEndCoverage.csv', 'r')

   file = csv.DictReader(filename)
 
   import csv
