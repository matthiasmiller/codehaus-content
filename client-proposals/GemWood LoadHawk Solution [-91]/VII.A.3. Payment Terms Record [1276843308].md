7.1.3. Payment Terms Record

  


Requirements

Overview: The Payment Terms record is a custom record, and is used to track various payment terms, both for GemWood in paying Members and for Buyers paying GemWood.

  


Accessed via: Configure Payment Terms Report

  


Sections and Fields: 

  * Payment Terms Overview section:
    * Active (checkbox; defaults to checked) 
    * Available For (required; drop list of "Members" and "Buyers"; defaults to blank; read-only for shipped records) 
    * Name (required; plain text field; used to set the Payment Terms name, such as "2/10 Net 30"; with the following behaviors: 
      * validate against duplicates;  
      * read-only for shipped records) 
    * Description (optional; plain text field; can be used to document an explanation of the configured terms if desired) 



  


  * Early Payment section:
    * Uses Optional Early Payment (checkbox; defaults to not checked)
    * Early Pay Window [   ] Calendar Days from Ticket Date (visible and required if "Uses Optional Early Payment" checkbox is checked; number; 0 decimals; defaults to 10; this is the number of calendar days from the "Ticket Date" for which the Early Pay Discount is available)
    * Early Pay Discount % (visible and required if "Uses Optional Early Payment" checkbox is checked; number; 2 decimals; allows entries of 1-99; defaults to "2.00")



  


  * Due Date section:
    * Payment Due In (required; number; 0 decimals; defaults to blank; used to set the number of days in which the full payment amount is due) 
    * Day Type (no label; required; drop list of "Business Days" / "Calendar Days"; defaults to blank; used to set the type of days that are to be counted)
    * Date Baseline (label displays "from"; required; drop list of "Buyer Settlement" / "Ticket Date"; defaults to blank; used to set the starting point for the due date countdown) 



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users
  * Editability: Create and edit only for users with the "Manage Financials" Permission.



  


Special Considerations: 

  * Copy Record: N/A (disallowed)
  * Delete Record: 
    * Shipped records: N/A (disallowed)
    * Manually-created records: Allow deletion until the record has been referenced by another record, then disallow. 
  * Merge Record: N/A (disallowed)



  


Other Notes:

  * The Solution includes some Payment Terms that are "shipped" \- see the following proposal subsection. 
  * The Solution also allows users to create user-specified Payment Terms, if desired.
  * Payment Terms are sorted in alphabetical order throughout the Solution (i.e. in drop lists). If an alternate sorting sequence is desired at some point, a "Sort Order" field could be added to the record to give full control to sorting.



  


Development Specification

Mockup:[https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1900233076#gid=1900233076](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=1900233076#gid=1900233076)

Tim Reitz 01/23/2025: Updated today. 

  


Ellis Miller 12/16/2024:

[ ] Lookup record (Payment Terms, Term Name is the list field)

[ ] Define detail screen as spec'ed. We'll do calculations elsewhere.

BID: 1.5 day
