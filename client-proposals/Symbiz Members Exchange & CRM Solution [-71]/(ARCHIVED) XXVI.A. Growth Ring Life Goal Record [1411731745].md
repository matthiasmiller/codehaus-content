26.1. Growth Ring Life Goal Record

DONE_MM: Tim Reitz 02/10/2023: Is there a reason to have a separate record for this rather than having it on a custom section on the Contact record?

DONE_CH: Tim Reitz 02/14/2023: two new custom sections on the Contact record. Let's do a spec and see what it looks like. 

  


Overview: This record tracks a member's life goals, values, and vision, as well as annual goals. 

  


It contains the following section(s) and fields:

  


  * Growth Ring Life Goals Overview section:
    * Member (automatic and read-only; current user) not needed
    * Date (date; default to today; required) on annual goals RG
    * Growth Ring Group ID not needed
    * Review On (default to end of year) on annual goals RG



  


  * Core Values section:
    * Instructions (read-only text; from AppHosting.zone settings) on annual goals RG
    * Embedded spreadsheet of:
      * Core Values Word (text; required) on annual goals RG
      * Description (text; required) on annual goals RG



  


  * Life Vision section: separate section
    * Instructions (from AppHosting.zone settings) 
    * Life Vision (memo)



  


  * Annual Goals section:
    * Instructions (from AppHosting.zone settings) on annual goals RG
    * Embedded spreadsheet of: on annual goals RG - one column each Branch
      * Life Branch (list of life branches; required; auto-generates one row for each Life Branch)
      * Description (text; required)



  


Validations: 

  * One set of goals per year.


