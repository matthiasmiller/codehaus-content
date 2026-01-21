11.9.3. Distributions - <Paperwork Type> Scholarship Funds Section

  


Requirements

<Paperwork Type> Scholarship Funds section (section header has the following behaviors:

  * if "Paperwork" = "School Managed", displays as "School-Managed Scholarship Funds";
  * if "Paperwork" = "PASS Managed", displays as "PASS Managed Scholarship Funds"):



  


  * Table of (visible if "Paperwork" = "PASS Managed"):

  
| Pre-K| K-12| OSTC| Non-EITC| Total  
---|---|---|---|---|---  
Scholarship to Allocate| expr(editable)| expr(editable)| expr(editable)| expr(editable)| expr  
  
  


  * Preview Scholarship Calculation (report link; visible if "Paperwork" = "PASS Managed")
  * Calculate Scholarship (button; visible if "Paperwork" = "PASS Managed" and if Check Date, Check Number, and Check Amount are all blank; populates the spreadsheet below if empty)
  * Embedded spreadsheet (no label; with the following if the "Legacy School-managed Distribution" checkbox is not checked):
    * Columns: 
      * Family (visible if "Paperwork" = "PASS Managed"; read-only macro; displays the Family name for the Student; name displayed in red text if the "Requires Documentation" checkbox is checked on the corresponding Family Application record)
      * Family (visible if "Paperwork" = "School Managed"; required; plain text field; defaults to blank)
      * Household Income (visible if "Paperwork" = "School Managed"; required; number field with no decimals; defaults to blank; warning on the field if the number entered is higher than the government base limit or any school's custom limit on the school application for the current year: "This family does not meet the income eligibility requirements for one or more schools." (note that this column uses the same calculations as the "Income" field on the Family Application record to determine if the validation message should be shown))
      * Adults (visible if "Paperwork" = "School Managed"; required; number field with no decimals; defaults to blank)
      * Dependents (visible if "Paperwork" = "School Managed"; required; number field with no decimals; defaults to blank)
      * County (visible if "Paperwork" = "School Managed"; required; drop list of "Counties" list items; defaults to blank)
      * School District (visible if "Paperwork" = "School Managed"; required; drop list of "School Districts" list items; defaults to blank)
      * Student (visible if "Paperwork" = "PASS Managed"; required; drop-list of active students for the selected school)
      * Student (visible if "Paperwork" = "School Managed"; required; plain text field; defaults to blank)
      * Grade # (visible if "Paperwork" = "PASS Managed"; read-only macro; displays the Grade from the linked Family Application)
      * Grade # (visible if "Paperwork" = "School Managed"; required; drop list of "Grades" list items; defaults to blank)
      * Family Tuition Owed (visible if "Paperwork" = "PASS Managed"; number field allowing two decimal places; auto-calculated to display the sum of all "Student Tuition Owed" columns for Students in that Family)
      * Student Tuition Owed (visible if "Paperwork" = "PASS Managed"; number field allowing two decimal places; if "Family Tuition Owed" is edited, auto-calculates to evenly distribute that number between all Students in that Family)
      * Student Tuition Owed (visible if "Paperwork" = "School Managed"; required; number field allowing two decimal places; defaults to blank)
      * Student Award (number field allowing two decimal places; auto-calculated and read-only macro; displays the sum of the Pre-K, K-12, OSTC, and Non-EITC columns for that RG row)
      * Pre-K (optional; number field allowing two decimal places)
      * K-12 (optional; number field allowing two decimal places)
      * OSTC (optional; number field allowing two decimal places)
      * Non-EITC (optional; number field allowing two decimal places)
      * Eligible for OSTC (visible if "Paperwork" = "PASS Managed"; checkbox; auto-set and read-only macro; displays the corresponding checkbox from the linked Family Application)
      * Eligible for OSTC (visible if "Paperwork" = "School Managed"; checkbox; defaults to unchecked)
      * Learning Disability (visible if "Paperwork" = "PASS Managed"; checkbox; auto-set and read-only macro; displays the corresponding checkbox from the linked Family Application)
      * Learning Disability (visible if "Paperwork" = "School Managed"; checkbox; defaults to unchecked)
      * Exclude from Calculation (visible if "Paperwork" = "PASS Managed"; checkbox)
      * Application (visible if "Paperwork" = "PASS Managed"; link to the family application for the year)



  


  * Sorted by:
    * Family + Grade #



  


  * Buttons to add/remove rows :
    * If "Paperwork" = "PASS Managed": N/A
    * If "Paperwork" = "School Managed":
      * "+" \- insert row
      * "-" \- delete selected row



  


  * Shows 23 rows without scrolling



  


Validation:

  * Error on save: if a student is receiving an award and their family does not meet income requirements.
    * Error Message: "The student is receiving an award, even though they do not meet the income requirements. (Field: Student; Row: <Row Name>)"
  * Warning on save: if Student Award is greater than Student Tuition Owed.
    * Warning Message: "The student's award cannot exceed the scholarship owed. (Field: Student Tuition Owed; Row:<Row Name>)"
  * Warning: if OSTC is greater than zero and Eligible for OSTC is not checked.
    * Warning Message: "This student is not eligible for OSTC funds. (Field: OSTC; Row: <Row Name>)"
  * Warning on save: if Pre-K is greater than zero and Grade # is not Pre-K.
    * Warning Message: "Pre-K amount must only be specified for Pre-K grade. (Field: Pre-K; Row: <Row Name>)"



  


Additional Behaviors:

If "Paperwork" = "PASS Managed"and if OSTC, Pre-K, K-12, or Non-EITC are modified, Exclude from Calculation is checked.

  


Additional Notes:

  * If "Paperwork" = "PASS Managed", family tuition is distributed equally for each child.
  * If "Paperwork" = "PASS Managed", modifying an individual child's tuition updates the combined family amount.
  * If "Paperwork" = "PASS Managed", distributions use the income limits (listed in Apphosting.zone Settings) based on the date that the application is processed.



  


Development Specification

Ellis Miller 05/05/2025: 

Note that we some expressions are shared, but many are a macro for PASS and a field for School managed. I'm guessing you want something like:

  * DistPMMyField \-- for pass-managed macro (these used to be OM for Org-Managed)
  * DistSMMyField -- for school managed field
  * DistMyField \-- for a wrapper macro that returns the right one (used in exports)


