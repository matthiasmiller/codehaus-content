5.1.2. Pack Record

Overview: This is a custom record type, used to track packs created in the yard via the app.

  


Accessed via: Main Menu | Mobile App | Packs

  


Sections and Fields: 

  * Overview section: <Thickness> <Species> <Grade> \- <BF Qty> (header label)
    * Num ID (hidden; Silverloom record ID)
    * Rand ID (hidden; auto-sets to a random integer between 1 and 10^3 on record creation)
    * Load Request (number; no decimals)
    * "..." (Select Load Request choice report; used to select linked Load Request; see corresponding spec)
    * Date (created date; uneditable)
    * GW PO ID (plain text; GW PO #) 
    * Visible # (number; no decimals; number to be written on the pack)
    * Member (drop-list of active member contacts; required)
    * Thickness (drop-list of Lumber Thicknesses; required)
    * Species (drop-list of Species; required)
    * Grade (drop-list of Lumber Grades; required)
    * BF Qty (number; no decimals; required)
    * LR Item ID (number; no decimals; required if Load Request is not blank)
    * PO Item ID (number; no decimals; required if PO ID is not blank)


