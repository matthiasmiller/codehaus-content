11.11. Member Application Record

  


Requirements

Accessed from: Faith Builders SPE | Member Applications | Member Applications

  


At the top of the record:

  * New Member Application (link to create new member application)



  


Additional notes:

  * Note that "Accepted" and "Admitted" are two distinct terms. Accepted refers to the SPE's selection of the applicant. Admitted refers to the member officially becoming a member of the SPE.



  


If one member takes over for another member in Year 2:

  * Mark the application Inactive for Original Member. This will also clear the Renew checkbox.
  * Create a new member application for Original Member if they want a reduced amount.
  * Create a new member application for Replacement Member



  


TODO_AP: Tim Reitz 02/24/2025: Bring in the Record Snippet for the standard pieces for this overview section. Also update the record sections below as able/needed.

  


Development Specification

Ellis Miller 02/08/2021: The terms "Accepted" and "Admitted" can be confusing. Think of this like applying to go to university:

  * First you apply for the university
  * If the university likes you, you are accepted
  * Once you do all the paperwork, you are approved



  


In this case:

  * The member makes an application
  * If FB would like to see them in the program, the member application is Accepted by SPE
  * If the SPE is approved by the govt, the SPE Application is Admitted by the govt (this is a macro expr, because it comes from the SPE Application record). This then requires payment from the member.



  


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
