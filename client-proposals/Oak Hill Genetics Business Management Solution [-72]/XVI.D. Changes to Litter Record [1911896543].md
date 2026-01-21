16.4. Changes to Litter Record

  


Requirements

Overview: This record is used to track which animals are in the same litter.

  


The record includes the following sections and fields:

  


  * Type (Canine vs Porcine)
  * Litter Serial (read-only; in the format of "<Female Serial> \- <Male Serial> \- <YYYY-MM-DD>", where the date is the date of birth)
  * Date of Birth 
  * Weaned Date
  * Person Responsible



  


  * Mother Serial (field to enter and link to open)
  * Father Serial (field to enter and link to open)
  * Date Bred



  


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

  


Development Specification

TODO_IDD - Note that some fields might be conditional?

  


TODO_IDD: Tim Reitz 04/05/2023: The following was listed with Type, but Ben and I aren't sure why female/male is relevant for this: 

  * Type (Canine vs Porcine; can be automatic; validate Female / Male types type)


