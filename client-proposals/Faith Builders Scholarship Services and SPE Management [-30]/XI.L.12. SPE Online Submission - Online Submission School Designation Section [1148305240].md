11.12.12. SPE Online Submission - Online Submission School Designation Section

  


Requirements

Online Submission School Designation: 

Embedded spreadsheet (RG):

Columns:

  * SPE School Name (drop-list of active school contacts marked Eligible to Receive SPE Donations)
  * SPE School County (uneditable lookup from the SPE School Name)
  * App. School Name (plain text)
  * App. School County (drop-list of PA counties)
  * App. School Contact Name
  * App. School Contact Phone
  * App. School Contact Email
  * App. School Amount



Buttons:

  * "+" \- insert row
  * "-" \- delete selected row



  


  * Designation Total Amount (auto-calculated and read-only; sum of App. School Amount column)
  * Anticipated Tax Credit Amount (auto-set and read-only; displays 90% of the Designation Total Amount)



  


Additional behaviors:

  * If App. School Name is set to a valid active school contact, SPE School Name is set to that school.



  


Development Specification

TODO_NM: SPESubmissionDesigAppSchoolName could be optimized to remove the second ContactField lookup.

  


  


Change Requests: 

  * Tim Reitz 09/19/2024: [[[IN10388](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10390&)]] - XFB - WSGI: SPE Online Submission: School Selection Page


