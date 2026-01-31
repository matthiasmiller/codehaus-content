9.1. Auto-Create SPE Applications

  


Requirements

AppHosting will auto-create SPE applications. It will include Preview New SPE Applications report that will show:

  


  * SPE
  * Year #
  * Application Date
  * Application Year
  * Application Amount



  


The report will have a button called "Create New SPE Applications" that generates the corresponding applications. The only fields that should be specified on the newly created records are the columns listed above.

  


Determining Year 2 Applications

This report will consolidate all approved Year 1 applications for each SPE for the prior tax year into one Year 2 application.

  


Determining Year 1 Applications

If the SPE does NOT have any approved Year 2 applications for the prior year, duplicate all unapproved Year 1 applications for the prior tax year to the current year.

  


If the SPE DOES have any approved Year 2 applications for the prior year, create a Year 1 application for the current year in the amount of $830,000 minus the current year's Year 2 application amount and any Year 1 approvals for the current or future tax years.

  


Development Specification

Ellis Miller 02/15/2021: This is a standard report. It has a button to run an x30 that uses this report as the input file.

  


We'll likely need to use models (or Suppress Duplicate Sort) to ensure that we merge items correctly. 

  


I will spec out more before we code.

  


Target: 2 days
