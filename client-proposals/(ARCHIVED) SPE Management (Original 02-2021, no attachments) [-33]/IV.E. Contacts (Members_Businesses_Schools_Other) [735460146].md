4.5. Contacts (Members/Businesses/Schools/Other)

  


Requirements

The members and businesses will be tracked in AppHosting. We will use our built-in Contacts module, and include the following fields:  

  


  * Contact Type (required; with an option for Business, Individual, School, Scholarship Organization)



  


  * County (always visible; visible and required for eligible members and schools; prepopulated to include a list of all Pennsylvania counties)



  


  * Hold Solicitations Until Date (for all contacts)



  


The contact would also include the following sections and fields: 

  * Eligible for SPE (visible for Individual and Business contact types; used to distinguish between accountants, etc and members)



  


  * Business section (visible if eligible for SPE and a Business):
    * EIN (required)
    * Entity Type (required), list of:
      * Single Member LLC
      * LLC - Partnership
      * LLC - filing as S Corp
      * S Corp
      * Partnership
      * Estate
      * Trust
      *  LLP
      *  C Corp
    * Owner SSN (visible and required if Single Member LLC)
    * PA Revenue ID # (visible and required for S Corp, LLC Filing as S Corp, and C Corp).
      * If required, it must be a 10-digit number (no letters, spaces, hyphens, etc). Warn if it begins with a number other than 1.
    * Business Contacts (read-only spreadsheet showing all contacts linked back to this business). This will show all contacts that have a Business/Organization specified that links them back to this record (i.e. employees, officers, etc). This is different from the Related Contacts, which includes employees who are not members of the business.



  


  * Individual section (visible if eligible for SPE):
    * SSN (required)
  * Anonymous Donor (visible if eligible for SPE, for both businesses and individuals)



  


  * An embedded spreadsheet for Related Contacts, linking to a contact with a user-configurable list of titles. The name is a drop-list of all Individuals. For example: 

Name| Title| Phone| Email  
---|---|---|---  
Primary Contact Name| Primary Contact| Read-only from Contact Record| Read-only from Contact Record  
Accountant Name| Accountant|   
|   
  
Owner Name| Owner|   
|   
  
  
  


  


It will include the following report links for Businesses and Individuals:

  * Member Applications
  * Payments



  


It will include the following report links for Scholarship Organizations:

  * QuickBooks Disbursements



  


It will include the follow report links for Schools:

  * Annual Contribution Summary (by School)



  


It will include a Communications Title for all users who are allowed to log into the system. This is used in the salutation of email communications.

  


Individual contacts will also include a Middle Name and Preferred Name field. To prevent duplicates, also add the Contact ID to the end. Thus, the individual's name will appear in lists as as LastName, FirstName MiddleName "PreferredName" #0041.

  


Businesses, schools, and scholarship organizations will also have a Preferred Name. It will appear as BusinessName "PreferredName" #0065.

  


Warn about any changes to EIN, Owner SSN, or individual SSN.

  


NOTE: We do not need to track proof of eligibility. This is part of the agreement, and the onus is on the applicant to establish eligibility. (The criteria are ownership or employment in a for-profit business that pays tax in Pennsylvania, i.e. not including sole proprietorships, or holding stocks in a publicly funded business, i.e. mutual funds or individual stocks.)

  


Development Specification

Tim Reitz 01/11/2021: Notes for mockups: 

  


Business and Individual: 

Contact Information / General Information section:

  * Eligible for SPE (used to distinguish between accountants, etc and members)
  * Anonymous Donor (visible if eligible for SPE)
  * Hold Solicitations Until Date
  * County (for marketing purposes)



  


Related Contacts section: 

It will also included an embedded spreadsheet for Related Contacts, linking to a contact with a user-configurable list of titles. For example:

Name| Title| Phone| Email  
---|---|---|---  
Primary Contact Name| Primary Contact| Read-only from Contact Record| Read-only from Contact Record  
Accountant Name| Accountant|   
|   
  
Owner Name| Owner|   
|   
  
  
  


  


Business: 

  * Business section (visible if eligible for SPE):
    * EIN (required)
    * Entity Type (required), list of:
      * Single Member LLC
      * LLC- Partnership
      * LLC- filing as S Corp
      * S Corp
      * Partnership
      * Estate
      * Trust
      *  LLP
      *  C Corp
    * Owner SSN (if Single Member LLC)
  * PA Revenue ID # (for S Corp, LLC Filing as S Corp, and C Corp)



Mindy Hilbert 01/12/2021: 

  * Ten-digit number
  * Usually begins with a 1
  * It can be found on a form from the Pennsylvania Department of Revenue called Notice of Registration for Employer Withholding Tax below the Account ID or on the business’s PA tax return from last year.


  * Business Contacts (read-only spreadsheet showing all contacts linked back to this business)



  


  


Individuals: 

  * Individual section (visible if eligible for SPE):
    * SSN (required)



  


Ellis Miller 02/08/2021: 

[ ] Contact Details Section: Target: 4 hrs

[ ] Related Contacts RG

[ ] List of active contacts.

[ ] RelatedContactTitles list.

[ ] Two lookup macros

Target: 4 hours

  


[ ] Business Contacts - RO Virtual RG

[ ] TODO_CH: I'm not seeing the Business Contacts in the mockups.

[ ] RepeatList for virtualRG is a SortPipeList from a ContactByOrgNdxConcat

[ ] Add columns for all desired fields.

Target: 4 hours

  


[ ] Member details Sections

Target: 4 hours

  


Extra work:

[ ] Changing the configuration of DisplayName takes a Config_ContactDefaultLookupName macro. We'll also have to add OnChange for fields like PreferredName that modify it.  Also needs to retrofit base system to use it.

[ ] Other things we missed

Target: 2 Days
