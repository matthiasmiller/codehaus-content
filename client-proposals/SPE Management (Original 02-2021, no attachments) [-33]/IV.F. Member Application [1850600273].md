4.6. Member Application

  


Requirements

AppHosting will track member applications.

  


Note that "Accepted" and "Admitted" are two distinct terms. Accepted refers to the SPE's selection of the applicant. Admitted refers to the member officially becoming a member of the SPE

  


Specifically, it will track:

  * Member (required; list of all members; links back to member contact)
  * Application Type (required; defaults to blank)
    * Prefilled by SPE
    * Completed by Member
  * Application Date (visible and required if completed by member; defaults to today)
  * Tax Year (auto-calculated; read-only; tax year of application date until admitted; year of admittance date after admitted)
  * Year # (required; default to Year 1 of 2 if the prior tax year didn't have Year 1 of 2; default to Year 2 of 2 if the prior year had only Year 1 of 2; default to blank if the prior year had both)
    * Year 1 of 2
    * Year 2 of 2
  * Inactive (checkbox; clears Renew checkbox; validate against any payments excepted shredded payments; validate against admittance date)
  * Renew (checkbox; default to checked)
  * Total Amount (entered)



  


  * Embedded Spreadsheet of:
    * School (required; list of all Schools in the database)
    * County (required; list of all Pennsylvania counties; default to blank)
    * Scholarship Organization (defaulted based on school; optionally overridden)
    * % of Total (editable; the % is auto-calculated from the Total Amount to a whole number; editable; changing it updates the school amount to the nearest $10)
    * Amount (required; validate that the total school designations matches the Total Amount) 



  


  * Admittance Status (automatic and read-only)
    * Inactive (if the application is marked inactive)
    * Pending (if none of the other conditions are met)
    * Waiting for Payment (if the Application Type is Completed by Member, and Accepted by SPE is checked)
    * Admitted (if the above conditions are met and payment has been received)
  * Admittance Date (visible if Admitted; calculated to the latest of Accepted by SPE and all check dates)
  * Accepted by SPE (checkbox + editable date; defaults to today when checked)
  * Payment Due Date (visible and required if Accepted by SPE; defaults to # of Days Until Member Payment Due from AppHosting.zone Settings; can be overridden as necessary)
  * SPE Application (choice of SPE Applications for the year of admittance; visible and required if accepted by SPE; must be an approved application; links back to SPE Application)



  


  * Payment section (visible unless the section is empty and the application is inactive); it shows:
    * Check Date (warn if year does not must match tax year)
    * Check Number (required)
    * Check Amount (required; must match total amount)
    * Check Status (required; Deposited / Scheduled for Deposit / Held / Shredded)
    * Deposit Date (required if deposited or scheduled for deposit; also used for generating Receipt of Payment)



  


  * Notes



  


When entering schools, validate that the county matches the school's county. This is used to reduce errors caused by similar school names.

  


Adding a row to the schools spreadsheet will automatically default the Amount for that row to the remaining amount.

  


If one member takes over for another member in Year 2:

  * Mark the application Inactive for Original Member. This will also clear the Renew checkbox.
  * Create a new member application for Original Member if they want a reduced amount.
  * Create a new member application for Replacement Member



  


Validate that the selected state approval (SPE Application) has available funds for this application.

  


Note that members can have a simultaneous Year 1 of 2 and Year 2 of 2 agreement. This allows members to easily adjust amounts of the proposal without needing to wait until their 2-year commitment is complete.

  


Development Specification

Ellis Miller 02/08/2021: The terms "Accepted" and "Admitted" can be confusing. Think of this like applying to go to university:

  * First you apply for the university
  * If the university likes you, you are accepted
  * Once you do all the paperwork, you are approved



  


In this case:

  * The member makes an application
  * If FB would like to see them in the program, the member application is Accepted by SPE
  * If the SPE is approved the govt, the SPE Application is Admitted by the govt (this is a macro expr, because it comes from the SPE Application record). This then requires payment from the member.



  


Application Details Section

Target: 4 hours

  


The payment details is not an RG.

  


  


School Designations

[ ] % of Total should be editable macro: Round (AppSchoolAmount / AppTotalAmt * 100, 0)

[ ] Has an OnChange of: AppSchoolAmount = Round( AppTotalAmt * AppSchool% / 100, -1)

[ ] Note that I've added Displayed Totals under the School Designation RG.

Target: 4 hours

  


Admittance Status Section: 4 Hours

  


Payment Section: 2 hours

  


  


Final instructions (after field list above):

[ ] County validation

[ ] Defaulting amounts

[ ] Taking over member

[ ] I believe the bullets are instructions mostly for FB, but maybe some behaviors. Discuss w/ CH before implementation.

[ ] Available fund validation

1 day
