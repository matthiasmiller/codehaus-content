5.1. SPE Applications

  


Requirements

This report will show SPE applications.

  


It will filter by:

  * SPE (optional; blank = all; default to blank)
  * Application Year # (multiple choice; choice of "Year 1 of 2" or "Year 2 of 2"; blank = all)
  * Application Date (blank = all)
  * Application Year (blank = all; number)
  * Status (Pending, Approved, Denied; blank = all)
  * Funded (choice of Yes or No; blank = all)
  * Tax Year (blank = all; number field default to the current tax year)



  


The report should group by SPE.

  


The report should reverse sort by first approval date, then by application date (newest on top).

  


Its columns should be:

  * SPE
  * Year # (Year 1 of 2 or Year 2 of 2)
  * Application Date
  * Application Amount
  * Status
  * Tax Year
  * Approved SPE Amount
  * Admitted Member Total
  * Pending Member Total (total only; see below)
  * Balance



  


The Admitted Member Total would be the total contributions for all member applications admitted into this SPE.

  


The Pending Member Total would be the total contribution for all pending member applications. Because pending applications are not associated with any specific SPE or approval, this number would only be shown on the report's total row. For example:

  
| See Above Columns| Approved| Admitted| Pending| Balance  
---|---|---|---|---|---  
SPE 1|   
| 100,000| 75,000|   
| 25,000  
SPE 2|   
| 50,000| 0|   
| 50,000  
  
|   
| 150,000| 75,000| 210,000| -135,000  
  
  


The Balance would be the Approved Amount minus the admitted and pending totals. This may be negative if there are more member applications than available remaining funds.

  


The report will have a New SPE Application button.

  


NOTE: Because member applications are not assigned to an approval until the member is admitted, the Pending column will remain blank for all approvals. Because of this, the total row for the Balance will not correspond with the non-total rows.

  


Development Specification

Tim Reitz 01/26/2021: Should this include the Application Name, perhaps instead of SPE since the report is grouped by SPE? Or not since most/all of that info is included in other columns? And just have the SPE column link to the application detail screen? Matthias Miller 01/27/2021: I think it's fine like this.

  


Ellis Miller 02/08/2021: 

TODO_CH: Let's change mockups to use a range for Application Date 

  


TODO_CH: The mockup is missing the total for SPE 2 grouping.

  


Ask prompts: 4 hours

Basic report: 4 hours

Number macros: 8 hours
