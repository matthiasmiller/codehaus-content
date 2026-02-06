3.4.1. Links to Enter Persons

  


Requirements

There will be four links on a Person record to enter other persons:

  * Enter Unrelated Person -- easily create a record for another person that is not linked to the displayed person
  * Enter Sibling -- shown in Parent section to create a record for a sibling of the displayed person
  * Enter Husband -- shown in Marriages section for unmarried women to create a record for a husband who is not in the system
  * Enter Child -- shown in the Children section to create a record for a child of the displayed person



  


The links will be available after a person record is first for the first time. Before that gray text will be displayed:

Enter Child (available after save)

  


Each of these links will first prompt for:

  * Last/Maiden Name
  * First Name
  * Middle Name
  * Birth Date



  


To ensure that we are not creating duplicate records, it will first show a report for all people matching on:

  * First Name, Middle Name, and Last Name
  * First Name, Last Name, Birth Date
  * First Name, Middle Name, Birth Date
  * Middle Name, Last Name, Birth Date



  


The report will have the following columns:

  * Last/Maiden Name
  * First Name
  * Middle Name
  * Birth Date
  * Parents
  * Spouse



  


Clicking one of these will open the record, linking them back to the source family (for spouse/child/siblings).

  


The report will also have a New Person button in case none of the rows match. This will default the fields in the screen the entered values.

  


Development Specification

Ellis Miller 05/05/2021: This is a simple Persons report that filters the prompts shown. It will also pass through multiple optional source persons as hidden prompts:

  * Set Father to
  * Set Mother to
  * Set Wife to



  


Links + Report: 1.5 days, only pass in the non-blank fields whether using Detail Screen: or New Record:
