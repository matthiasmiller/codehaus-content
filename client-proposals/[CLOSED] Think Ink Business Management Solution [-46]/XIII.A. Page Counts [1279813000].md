13.1. Page Counts

TODO_IDD: add to Phase 4 Lists, with explanations 

Page Count Collection Types:  

  * Manual: Can be done in a few ways:
    * Think Ink sends the print count request
    * Customer gets the page count and sends it back via email/fax/call
    * Think Ink enters the information into the Solution
    * Rarely Think Ink might be on-site and collect the information
  * MPS Monitor: A data collection agent that runs either on the printer itself of on a computer; Think Ink can see current printer status and details and can receive a spreadsheet report of page counts
  * KFS: Another data collection agent that can do the same thing as MPS monitor; sometimes one works better for a printer than the other, but some printers can have both. 



TODO_EM: Tim Reitz 08/24/2023: Sometimes a printer will be reported on by both MPS Monitor and KFS. In this case they would probably prefer to go with the KFS report. What if they'd run the KFS import first, then the MPS Monitor import, and have the Solution ignore duplicates imported on the same date? 

  * Prorated: Sometimes Think Ink cannot get a page count for a printer, so they will use an average



TODO_IDD: calculations for prorated

TODO_IDD: Handle situations where the last "collection" was an estimate. 

  


  


TODO_IDD: Tim Reitz 08/24/2023: Spec out the import for the automatic page counts. Let's give him a format for the spreadsheet. 

TODO_IDD: Tim Reitz 08/24/2023: How to distinguish between MPS Monitor and KFS? Separate imports (separate menu items)?
