# **Expenditure Tracker App**

## **Contents**

* Brief
    * Additional Requirements
    * My Approach

* Design
    * Databae ERD
    * CI pipeline for Integration Tests

* Project and Progress Tracking
    * Project Tracking
    * Progress Tracking

* Risk Assessment
    * Before
    * Final Risk Assessment

* Tests
    * Unit Tests
    * Integration Tests

* App Design

* Future Improvements

* Author



## **Brief**
The project brief is to design a CRUD application with "utilisation of all the supporting tools, methodologies and technologies that encapsulate all core modules covered during training". It should meet the requirements set by my knaban board designed specifically for this project. The project should contain at least 2 tables as per the project spec, a functioning front end built using flask, full automated testing and integration into a version control system with testing carried out through a CI server and the project, and be deployed to a cloud-based virtual machine.

### **Additional Requirements**
In addition to what has been set out in the brief, I am also required to provide:
* A risk assessment report containing all the possible risks and those responsible for said risks as well as how they can be mitigated.

### **My Approach**
Towards this end, I have chosen a simple expenditure tracking app as my project and it contains the following functionality which have been included:
* Create an Account that stores:
    * *Account Name*
    * *Balance*
    * *Customer Name* - or nickname for customer
    * *Transactions*
    This satisfies the Create functionality of the CRUD application. It also functions as the one in the one to many relationship for the DataBase (DB) model.

* Create a Transaction Account:
    * *Transaction* - The individual transaction being recorded
    * *Transaction Amount*
    * *Transaction Completed* - A marker as to whether the transaction has taken place successfully or is pending
    * *Transaction Date* 
    This also satisfies a Create functionality and provided the second table in the one to many relationship, this being the many.
* The customer can also view and update both Transactions and Accounts, satisfying the Read and Update functionality
* The customer can Delete the account and accompanying transactions, or can delete indiidual transactions, satysfying the Delete functionaliity

Additional functionality not included are the following:
* For the customer to create the user account via a login functionality. This would eliminate the need for a Customer Name/ nickname in the account set up.
* The completed/incomplete markers should reflect in the statement, i.e when a transaction is marked incomplete, it should not reflect in the balance unless marked completed.
These are additional functionality ideally for the next sprint of the project.


## **Design**

### **Database ERD**
The entity relationship diagram (ERD) captured the structure of the database and the relationships intended for the app to utilize. Below is the initial ERD for the project

![ERD1][erd1]

As shown, the app was set out to model a one to many relationship from the customer to the account, and a one to many relationship from the account to the statements. The initial plan was for the project to be a mock banking app where you created bank accounts and created statements.

![ERD2][erd2]

After discussions and consultations, it was decided to have this simply be an app for tracking a customer's expenditure for each of the customer's own bank accounts seeing as this would be more practical and meaningful, as can be seen in the erd above.

![ERD3][erd3]

In the final ERD for the final iteration of the app, as can be seen above, the payments_status in the accounts table was changed to a transaction_completed status in the statements/transaction table indicating that this was a transactions side item and not an accounts side item. The final ERD also shows the parts of the project that could not be completed in this sprint. These are highlighted in red.

### **CI Pipeline for Integration tests**

![CI][ci]

Pictured above is the continous integration pipeline with the associated frameworks and services. The pipeline integrates the integration testing phase of the app, as can be seen in the diagram. So once I produce code on my local machine or local VM and push it to github, there is immediately a test carried out of the code which is pushed to jekins via a webhook. The tests are carried out via jenkins automatically, and reports are produced.

The tests carried out on jenkins follow build stages on a pipeline job which ensures that you can pinpoint where the app fails to build and tests fail. Jenkins will provide you with information on where your build failed. The stages are:
* Checkout from Git Repository
* Installation
* Test

##  **Project and progress Tracking**

Trello was the knaban tool used to track the progress of the project in an Agile sprint style. 
The link to the final trello board can be found here : https://trello.com/b/bKCG609s/project-1

### **Project Tracking**

The project tracking for the final iteration during this sprint are shown from left to right in the kanban board on trello indicating the starting point up until the point of completetion marked under "Done". The cards are colour coded and name-marked according to the area of the project they each involved. Below are the lists of the project items in time from left to right with left being the starting phase and right being the final phase:

* *Project Resources*
    This section contains links to the github repository and the jenkins pipeline for the project.

* *User Stories*
    This contains the initial requirements from the customers point of view. It is also marked with MOSCOW requirements with the final two entries not being able to be carried out in this phase of the project.

* *Planning*
    This includes the parts of the project that are in the planning phase right before they're implementation. The parts of the project that could not be carried out are still in this planning phase.

* *In Progress*
    These are the parts of the project that are being carried out at the moment. Under this phase we still have aspects of the project that need to be performed and have had code written for them.

* *Testing*
    These are the elements of the project that need to be tested after the code has been completed for them. Here we still have some aspects of the project that need to be tested on an ongoing basis for this sprint.

* *Done*
    This is where all the aspects of the project that have had their code written and have been fully tested are moved. It is the final stage whithin which all the elements on the trello board need to be moved in orderfor the user requirements to be fully met.

### **Progress Tracking**

The project took a few iterations before the final project was made. There were intitial trello boards produced to track the project and requirements for different stages. Below are captures of the three phases of the trello boards up to the final phase:

![trello1][trello1]

The initial kanban board was very basic. It reflected the stage of the project where a topic had just been chosen, but the tools for carrying out the project were still largely unavailable, i.e learn flask, python, carry out a risk assessment, make an ERD etc. 

![trello2][trello2]

By the second phase above, user stories had been created and the initial phases that were in the product backlog above had already been carried out to a minor extent. This was when the project was beginning to take shape.

![trello3][trello3]


![trello4][trello4]


What is indicated in the snapshot above is the final trello board that was used to perform the final project work. This is where the user stories were properly demarcated in a MOSCOW fashion, and as can be seen there are elements at the buttom that "can't" be done. There are also aspects of the final project that were completed in this sprint marked under "done".

## **Risk Assessment**

There were two risk assessments drawn up for the project. An initial sparsely populated one and a full risk assessment carried out after. It covers some of the major risks that could affect the project both during and after completion. The risks are not all inclusive as there would still be many risks that have not yet been covered. A link to the full risk assessment is available at: https://docs.google.com/spreadsheets/d/1957LvQ6fw0zyt0tWMfNZcQU0DGxp7J4zqLzWXm0L71Q/edit?usp=sharing


### **Before**
There were intial risk assesments when the project was starting. Below are screenshots of the initial risk assessments:

![riskassessment1][riskassessment1]

### **Final Risk Assessment**
Below is a screenshot of the final risk assesment for the project:

![riskassessment2][riskassessment2]

## **Tests**

pytest was uses to run the unit and integration tests on the app. The unit test was designed to assert that the output of a certain function is the expected output when it is run. Jenkins produces outputs that inform the developer of the tests performed and the degree to which it covers the code.
The out put can be seen below:

![coverage][coverage]

The unit tests cover all the functions in the application. It is in effect testting all the CRUD functionality of the application with a 100% coverage.

### **Unit Tests**
The unit test results can be seen below on the pytestconsole

![unittests][unittests]

### **Integration Tests**
The integration tests are carried out with the use of selenium web-driver on top of pytest. They test the connectivity and the working of the whole application as a whole. This includes whether the front end is working properly, and the connectivity to the backend. The coverage for this test is low and can be seen below. This is because the test only covers the front end functionality and itws working with the backend by checking that when a particular action is performed on a front end page, it leads to the iput being saved on the database and the next page results reflect what is in the database. Rather than testing individual functions, it is testing the app as a whole.

Below is the coverage

![coverage2][coverage2]

The coverage of the integration test as can be seen above is 44%. However the functionality and connectivity of the CRUD applications in the HTML front end and their adequate connectiivity and functionality with the backend database layer have been tested to be working.

And the console output of the integration tests are below:

![integrationtests][integrationtests]

The integration tests are **not** perfromed on jenkins.

## **App Design**

The app is at a very rudimentary stage, and this is reflected by the simplicity of the front end which is built with very simple HTML. However after the tests carried out, it has proved to be largely stable without any known breaks.

The user is directed to the home page when they navigate to the URL:

![homepage][homepage]

They are then able to add new Bank accounts to monitor:

![addnewaccount][addnewaccount]

From here the customer is taken to the Customer Home page where they can view transactions on their various accounts which they have added

![customerhome][customerHome]

If the customer clicks the add deposit or add withdrawal, it takes them to a new page where they can add new deposits or new withdrawals to their balance. In the screenshot below,a deposit of 5000 is being added.

![adddeposit][adddeposit]

After adding the deposit, it takes them back to the customer home page.

![cutomerhomedepositadded][cutomerhomedepositadded]

And if they click on the view statement page, it takes them to the Statements page.

![statements][statements]

And if they want, they can sort the statement results by Date most recent or last first, or amount highest or lowest first.

1[statements2][statemets2]

They can also update account information from the customer home page:

![update][update]

You can also delete the statement entry on the statements page.



## **Future improvements**
There are a few improvements that could be included to future iterations of this project in a future sprint. These include:
* Implementation of a customer login function and a customer table in the database
* Connect the transaction_completed functionality to the balance so that if a transaction is completed, it would be subtracted or added to the balance, and if it is then marked incomplete, the transaction will be reversed in the balance.
* Connect to external apis so that a customer can connect to their actual bank account
* Improve security and provide encryption to avoid data theft or leakage



## **Author**
Ope Orekoya


[erd1]: https://imgur.com/8TmFnZe.png
[erd2]: https://imgur.com/DWQducW.png
[erd3]: https://imgur.com/yURDZWs.png
[riskassessment1]: https://imgur.com/Gvia8xH.png
[riskassessment2]: https://i.imgur.com/YAkT1A3.png
[trello1]: https://imgur.com/WKqiB1P.png
[trello2]: https://imgur.com/U2wHTYn.png
[trello3]: https://i.imgur.com/7u4IbLP.png?1
[trello4]: https://imgur.com/QTgS3pi.png
[ci]: https://i.imgur.com/oCjLlFc.jpg
[coverage]: https://i.imgur.com/ZmxhFaA.png?1
[coverage2]: https://i.imgur.com/dPiVdiV.png?1
[unittests]: https://i.imgur.com/Wo92Lk5.png?1
[integrationtests]: https://i.imgur.com/ZdY8PC1.png?1
[homepage]: https://i.imgur.com/E6pfaOX.png
[addnewaccount]: https://i.imgur.com/uYkcXEi.png
[customerHome]: https://i.imgur.com/5TyAfOh.png
[adddeposit]: https://i.imgur.com/9xTk9N8.png
[cutomerhomedepositadded]: https://i.imgur.com/YxkhufM.png?1
[statements]: https://i.imgur.com/iLx4K53.png
[statemets2]: https://i.imgur.com/sEr5weP.png
[update]: https://i.imgur.com/bVGr9NF.png?1
