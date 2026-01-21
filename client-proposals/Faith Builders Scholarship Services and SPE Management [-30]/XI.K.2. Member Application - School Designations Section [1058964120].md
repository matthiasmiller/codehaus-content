11.11.2. Member Application - School Designations Section

  


Requirements

School Designations:

Embedded spreadsheet (RG):

Columns:

  * School (required; drop-list of active school contacts marked Eligible to Receive SPE Donations)
  * County (required; drop-list of Pennsylvania counties)
  * Scholarship Organization (required; drop-list of active scholarship organization type contacts)
  * % of Total (editable; defaults to Amount / Total Amount)
  * Amount (required; defaults to the Total Amount - Total Designated Amount) 



Buttons:

  * "+" \- insert row
  * "-" \- delete selected row



  


  * View School Change PDF (link to School Change PDF)
  * Total (label)
    * (unlabeled percentage; uneditable; sum of % of Total column)
    * (unlabeled number; uneditable; sum of Amount column)
  * Anticipated Tax Credit Amount (auto-set and read-only; displays 90% of the total amount)



  


Additional behaviors:

  * When School is set, Scholarship Org. is set to the Default Scholarship Organization from the school.
  * Changing % of Total updates the school amount to the nearest $10.



  


Validation:

  * Error on save: if multiple rows have the same School and Scholarship Org.
    * Error Message: "Multiple school designations entered for school '<school>' and scholarship organization '<ScholarshipOrg>'. Consider adding the total designation for the school and scholarship organization in a single row. (Field: School; Row: <RowName>)
  * Error on save: if County does not match the County on the school contact record. 
    * Error Message: "The specified county does not match the school's county <county>'. (Field: County; <RowName>)"
  * Warning on save if one or more designated Schools is no longer active and/or is no longer eligible: "The following School(s) are not active and/or are not eligible to receive SPE donations.".
    * Warning Message: "The following School(s) are not active and/or are not eligible to receive SPE donations: <ListOfSchools>."



  


Development Specification

Change Requests: 

  * Tim Reitz 09/05/2024: [[[IN10261](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10263&)]] - XFB - Member Application Record - Warning for Inactive/Ineligible Schools
  * Tim Reitz 09/19/2024: [[[IN10388](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10390&)]] - XFB - WSGI: SPE Online Submission: School Selection Page 
  * Tim Reitz 09/30/2024: [[[IN10608](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10610&)]] - XFB - Main System: Additional Items - SPE Online Submission: School Selection Page


