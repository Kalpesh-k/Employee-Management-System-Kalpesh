Problem Staement


Employee Manager
A minimal Employee management system. It will have 3 modules
Employee Management Department Management Employee Salary Management
Employee can have designation either Associate, TL, Manager
Employee needs to have a reporting_manager who has to be a employee (designation -TL or Manager). This specifies who this employee is reporting to.
Employee belongs to 1 department only.
Apart from these attributes Employee can have other attributes like Name, Email, address etc. Department can have attributes like Name, Floor, etc.
Employee Salary Management has information regarding which employee had what salary in which period of time.
For eg.
Rakesh had salary of 10,000 from Jan 2022 to Dec 2023.
After appraisal Rakesh has now salary of 50,000 from Jan 2023 to Dec 2024 Both above entries will be stored with the date range.
	

Features Required in above modules:
Employee module will have admin page to add, update and delete employee. Department module will have admin page to add, update and delete departments.
Department module should have a reporting page to display employee hierarchy to show who is reporting to which other employee inside every department. Department will always have 1 manager on top and can have multiple TLs who in turn can multiple associates working under them.
For eg.

Employee Salary Management will have an admin page to add,update and delete employee salary entries
This also needs a reporting page where we should be able to enter daterange and see department-wise cost in salaries. For eg.
Date range: 1 Jan to 1 November

Department	Salary Costs
HR	100000
Python Team	200000
PHP Team	150000
IT Team	100000
 
Filters need to added as per requirement.

PS. Django Admin customization needs to be used for pages to add update and delete. For reporting pages you can use views with Javascript (Jquery or datatables) as comfortable.
Required Tech Stack - Python, Django, MySQL/MariaDB/Mongo/SQLite and other required libraries of your choice. Please upload the code on to GitHub or any other code repo and share the link for the same.
This assignment is to gauge your technical expertise along with project management.

So please revert back with the estimations, a small suggestion is to break down the problem on paper and be clear on how you are gonna approach this.
Please take a week to complete this. Reach out to me in case you need any clarifications.
