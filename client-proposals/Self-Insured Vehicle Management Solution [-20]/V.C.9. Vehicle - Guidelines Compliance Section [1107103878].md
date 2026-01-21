5.3.9. Vehicle - Guidelines Compliance Section

  


Requirements

*Done. 

  


  * Guidelines Compliance section:
    * Guideline Compliance (no label; embedded spreadsheet with the following; note that rows are always added and deleted automatically when "Vehicle Type" and/or "Subtype" is set or changed - see corresponding spec: 
      * Columns: 
        * Question (auto-set and read-only; sets to "Question" from Silverloom Settings for the "Vehicle Type" / "Subtype")
        * Answer (drop-list of "Yes" / "No"; with the following details / behaviors: 
          * editable for Admins and the Owner's Agent; 
          * required when any coverage is active -- error on Save: "Guidelines compliance answers are required."; 
          * when set, the "Yes / No Statement" for the row is set based on the corresponding "Statement if Yes" and "Statement if No" values in Silverloom Settings)
        * Yes / No Statement (plain text field; with the following details / behaviors:
          * auto-set based on the selection in "Answer" for the row;
          * editable for Admins and the Owner's Agent;
          * required if there is a value in the corresponding "Statement if Yes" and "Statement if No" in Silverloom Settings for the selected Answer -- error on Save: "Guidelines compliance Yes / No statement is required.")
      * Automatically sorted by: N/A (none) 
      * Buttons: N/A (none) 
      * Shows 8 rows without scrolling 
      * Additional Validations: 
        * Error on Save if there is a row in the spreadsheet and Question is blank.
      * Other Notes: 
        * N/A



  


Development Specification

  * Error on Save if there is a row in the spreadsheet and Question is blank.



_VA: Austin Priest 10/15/2024: This is not possible since that column is read-only and you cannot add rows.

_CCI: Tim Reitz 08/15/2025: Could you confirm if this validation is still in the code? If yes, we'll probably add it to a CR, to remove it since it's not necessary. Thanks!

Murshid Rahman 09/01/2025: Yes, there is a validation "Guidelines compliance questions are required.". Since the questions are read-only and its populated from Silverloom Settings, it cannot be blank. We can remove this validation. Thanks.

_VA: Tim Reitz 09/01/2025: Follow up.

TODO_CR: Tim Reitz 09/15/2025: Let's add this to a CR to get it cleaned up (remove the validation).
