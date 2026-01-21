5.7. Litter Record

TODO_IDD: Tim Reitz 05/08/2023: Anything that isn't needed for Housing should be saved in the "main" Litter record section. 

  


  


Overview: This record is used to track which animals are in the same litter.

  


The record includes the following sections and fields:

  


  * Type (Canine vs Porcine)
  * Litter Serial (read-only; in the format of "<Female Serial> \- <Male Serial> \- <YYYY-MM-DD>", where the date is the date of birth)
  * Date of Birth 
  * Weaned Date
  * Person Responsible



  


  * Mother Serial (field to enter and link to open)
  * Father Serial (field to enter and link to open)



TODO_JB: Ben Reitz 05/03/2023: Will this need to be tracked if you're simply housing the animals?

  * Date Bred



TODO_JB: Ben Reitz 05/03/2023: Will this need to be tracked if you're simply housing the animals?

  


  * Avg. Born Weight (lbs; auto-calculated)
  * Avg. Wean Weight (lbs; auto-calculated)



  


  * Temperament Score (list)
  * General Care Score (list)
  * Weaned (number; read-only and automatic)
  * Live Born (number; read-only and automatic)
  * Still Born (number; read-only and automatic)
  * Mortality Rate (%; read-only and automatic)



  


  * Actions; Embedded spreadsheet of:
    * Name
    * Date
    * Initials



  


  * New Animal (link to open a new Animal record with Type and Litter defaulted) 



  


The bottom part of the screen would show a list of all animals in the litter, with their serial # and color markings. It will include a link to open as well.
