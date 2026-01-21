9.8. Distributions

  


Requirements

Accessed via: FaithBuilders Scholarship Services | School | Distributions

  


Sections and Fields: 

Summary:

  * School
  * Year
  * Date Entered
  * Paperwork (drop-list of "School Managed", "PASS Managed")
  * All For Tuition (read-only; checkbox; lookup from the relevant school application)
  * Table of:

  
| Pre-K| K-12| OSTC| Non-EITC| Total  
---|---|---|---|---|---  
Starting Balance|   
|   
|   
|   
|   
  
Minimum Distribution|   
|   
|   
|   
|   
  
Funds to Allocate|   
|   
|   
|   
|   
  
  
  


Discretionary Funds:

  * Table of:

  
| Pre-K| K-12| OSTC| Non-EITC| Total  
---|---|---|---|---|---  
Max. Discretionary Amount|   
|   
|   
|   
|   
  
# of Families|   
|   
|   
|   
|   
  
Application Fees|   
|   
|   
|   
|   
  
School Discretionary Portion|   
|   
|   
|   
|   
  
  
  


PASS Managed Scholarship Funds (only visible for PASS Managed distributions)

  * Table of:

  
| Pre-K| K-12| OSTC| Non-EITC| Total  
---|---|---|---|---|---  
Scholarship to Allocate|   
|   
|   
|   
|   
  
  
  


  * Preview Scholarship Calculation (report link)
  * Calculate Scholarship (button; populates the spreadsheet below if empty)
  * Embedded spreadsheet of:
    * Family (read-only; lookup from selected student)
    * Student (drop-list of students for the selected school)
    * Family Tuition Owed (number)
    * Student Tuition Owed (number)
    * Student Award (auto-calculated; read-only)
    * OSTC (number)
    * Pre-K (number)
    * K-12 (number)
    * Non-EITC (number)
    * Grade # (read-only; lookup from the selected student)
    * Eligible for OSTC (checkbox; read-only; lookup from the selected student)
    * Learning Disability (checkbox; read-only; lookup from the selected student)
    * Exclude from Calculation (checkbox)
    * Application (link to student's family application)



  


School-Managed Scholarship Funds (only visible for School Managed distributions)

  * Embedded spreadsheet of:
    * Family (plain text)
    * Household Income (number)
    * Household Size (number)
    * County (drop-list of PA counties)
    * Pre-K #
    * Pre-K $
    * K-8 #
    * K-8 $
    * 9-12 #
    * 9-12 $
    * EITC Award $ (read-only; sum of previous $ fields)
    * OSTC K-8 #
    * OSTC K-8 $
    * OSTC 9-12 #
    * OSTC 9-12 $
    * OSTC Award $ (read-only; sum of OSTC $ fields)
    * Non-EITC #
    * Non-EITC $



  


Payment:

  * Table of:

  
| Pre-K| K-12| OSTC| Non-EITC| Total  
---|---|---|---|---|---  
School Discretionary Portion|   
|   
|   
|   
|   
  
School Scholarship Portion|   
|   
|   
|   
|   
  
School Check|   
|   
|   
|   
|   
  
FBSS Application Fees|   
|   
|   
|   
|   
  
Ending Balance|   
|   
|   
|   
|   
  
  
  


  * Check Date
  * Check Number
  * Check Amount



  


Reports:

  * Print Award Review Form Today (last sent on 01/01/2000) (checkbox; visible for PASS Managed distributions)
  * PDF (link to PDF for award review form (visible if the checkbox is checked)
  * Email (link to email for award review form; visible if the checkbox is checked)
  * Print Award Check Letter Today (last sent on 01/01/2000) (checkbox)
  * PDF (link to PDF for award check letter; visible if the checkbox is checked)
  * Award Notification (link to PDF)
  * Family Envelopes (link to PDF)
  * Business Postcards (link to PDF)
  * School Envelope (link to PDF)



  


Other Notes:

  * If the school is PASS managed and is flagged for "All for Tuition", the discretionary fund only contains the application fees.
  * Application fees are taken from OSTC if any child is OSTC. Otherwise, they are taken from the respective EITC fund.
  * For PASS managed distributions, a red label is displayed if the number of students entered in the discretionary funds table is less than the number of families in the scholarship funds RG: "This distribution is missing 1 student."
  * Family tuition is distributed equally for each child.
  * Modifying an individual child's tuition updates the combined family amount.



  


Development Specification

Matthias Miller 04/06/2018:

  * The VIrtual RG should include items from the stored RG, even if they would not otherwise be in the list of students. Then we should warn if the receiving student is inactive/ineligible.



  


[ ] Vivian - what EITC fund should get defaulted, Pre-K or K-12?

Matthias Miller 04/25/2018: This is moot issue b/c we never would do both.

  


  * Should we have a report that shows them the age of the money, for things close to the 2 years? --- (If there were no more distributions, when would the balance hit zero or negative, and what's the time?)
    * Matthias Miller 04/25/2018: She does it school by school, and says "you have this amount of money that came in last fiscal year, and you must use this money and you must use it."
    * Matthias Miller 04/25/2018: Per Vivian, another option would be to have a report that would show contributions that have not been used up (with the amount remaining), either sorted or filtered by date of contribution (for fiscal year)
    * Matthias Miller 04/25/2018: Per Vivian --- the report that gets sent to schools w/ their contribution information -- we would show:
      * contributions sorted by date (and grouped by fiscal year)
      * available/carryover balance



  


[ ] Vivian - what if on the distribution we had a grid showing:

  * Matching contributions
  * Contribution date
  * Contribution type (OSTC/EITC/Etc)
  * full contribution amount
  * Remaining contribution balance
  * Age of contribution



Then on the distribution, show balance OF THE CURRENT DISTRIBUTION, as well as age of money, and we could also show the corresponding contributions

  


[ ] Later, we could add validation for the age of money
