23.1.1. Screens / Prompts

  


Requirements

General: 

  


  * The portal contains the FBEP logo at the top of the page 
  * This portal also contains the following informational note at the bottom of the page: 



For more information, please contact:

<"Name" in AppHosting.zone Settings - SPE Settings section>

<"Title" in AppHosting.zone Settings - SPE Settings section>

<"Phone" in AppHosting.zone Settings - SPE Settings section>

<"Email" in AppHosting.zone Settings - SPE Settings section>

  


Step 1: Member Type and Eligibility: 

  


Prompt whether the application is for an individual or a business: 

  * I am applying as: * (required; option to select one of the following)
    * an individual
    * a business (not a sole proprietorship)



  


After the user makes a selection and clicks "Continue", shows a checkbox with a configurable confirmation prompt that the applicant is eligible to donate to an SPE. The prompt is the New Member Eligibility Prompt memo from AppHosting.zone settings.

  


Step 2a: Business Information (only shown for businesses)

Prompts for:

  * Business Name (required; plain text) 
  * Primary Contact First Name (required; plain text) 
  * Primary Contact Middle Name or Initial 
  * Primary Contact Last Name (required; plain text) 
  * Primary Contact Preferred Name
  * Address (required; plain text) 
  * City (required; plain text) 
  * County (required; drop list of PA counties; defaults to blank) 
  * State (drop list of US State abbreviations; defaults to "PA")
  * Contact Zip (required; plain text) 
  * Contact Phone Number (required; plain text) 
  * Contact Email (required; must be in a valid email format) 
  * EIN (required; number; must be 9 digits long) 
  * Entity Type (required; drop list of Entity Type list items; defaults to blank) 



TODO_AP: Tim Reitz 09/23/2024: Add an Entity Types list to the spec. 

  * Owner SSN (visible and required if Entity Type = __; number; must be 9 digits long) 



TODO_AP

  * PA Revenue ID (visible and required if Entity Type = __; number; validates that the ID is 10 digits long and begins with a 1)



TODO_AP

  * Includes a note: "It can be found on a form from the Pennsylvania Department of Revenue called Notice of Registration for Employer Withholding Tax below the Account ID or on the business’s PA tax return from last year."


  * Anonymous Donor (checkbox; defaults to not checked) 
    * Includes a notice: "Check here if you want your contribution to be anonymous to the school(s) you designate."



  


Businesses are implicitly eligible for SPE, as long as they fall within one of the listed entity types.

  


The visibility/requirements for the additional business fields match the requirements described in the Contacts section (depending on the business entity type).

  


Step 2b: Individual Information (only shown for individuals): 

TODO_AP: Tim Reitz 11/18/2025: Spec out the field details. 

Prompts for:

  * First Name
    * Includes a notice, "Legal name for tax documents"
  * Middle Name or Initial
    * Includes a notice, "For tax documents"
  * Preferred Name
    * Includes a notice, "For email communication from us and contribution info sent to schools (if not anonymous).  If left blank, we will use first name."
  * Last Name
  * Address
  * City
  * County
  * State (drop list of US State abbreviations; defaults to "PA") 
  * Zip
  * Phone Number
  * Email
  * SSN
  * Anonymous Donor
    * Include the same notice as for Business Information.



  


Step 3: School Selection: 

  


Prompts for:

  * School (drop list of "(Other School)" and School-type Contacts from the database that meet the following criteria: 
    * Are active Contacts,
    * Are marked "Eligible to Receive SPE Donations", and 
    * Have not already been selected on the current Online Submission);
    * displayed as "<School Name> (<School County>)" (County is determined using the following order of events:
      * If there is a Physical address type with a County specified;
      * otherwise, if there is a "Mailing" address type with a County specified;
      * otherwise the County from the first address)
  * School Name * (visible, editable, and required if "(Other School)" is selected; plain text field)
  * School County * (visible, editable, and required if "(Other School)" is selected; plain text field)
  * Contact Name * (visible, editable, and required if "(Other School)" is selected; plain text field)
  * Contact Phone * (visible, editable, and required if "(Other School)" is selected; plain text field)
  * Contact Email * (visible, editable, and required if "(Other School)" is selected; plain text field)
  * Amount * (visible, editable, and required if a "(Other School)" or a School name is selected in the drop list; number field with no decimals; automatically rounds the entered value to the nearest 100)



  


Note that multiple schools may be selected, creating a table of schools and amounts.

  


This screen also contains the following:

  * Total Contribution (auto-calculated and read-only; displays the sum of School-specific Amounts; total must equal at least $3,000 - enforced by an error if the user attempts to continue to the next screen)
  * Anticipated Tax Credit (auto-calculated and read-only; displays the value of "Total Contribution" * .9) 
  * "*Contribution amounts must be in increments of 100." (message in smaller font) 
  * "*The minimum Total Contribution is $3,000." (message in smaller font)



  


Note that the visibility and data requirements should match the Members/Businesses detail screen.

  


  


Step 4: Agreement: 

The applicant is required to confirm the following items by checking them off:

  


The undersigned hereby agrees to become a member of a Faith Builders Special Purpose Entity in accordance with the foregoing Operating Agreement, and with the following conditions:

  


[ ] The initial contribution is $______ (minimum $3,000). The member takes responsibility for deciding the amount in consultation with his tax adviser. Faith Builders Special Purpose Entities are not responsible for any unusable tax credit issued to a member.

  


[ ]  The member will contribute the same amount in the succeeding calendar year within 30 days of notification by a Faith Builders Special Entity, LLC representative OR the member will recruit a replacement person or entity to fulfill the obligation. In any case, the signer is responsible to arrange for the same amount to be paid for the following year.

  


[ ] The applicant is currently tax compliant with the state of Pennsylvania.

  


[ ] The applicant acknowledges and agrees that there is no expectation for any economic benefit as a result of the investment other than the allocation of the applicable state tax credits and federal charitable contribution deduction.

  


[ ]  The applicant has recommended where to direct the contribution; schools will receive 95% of this amount after deducting Faith Builders Scholarship Services administration fee.

  


The applicant is then be required to enter his/her full name:

Enter your FULL NAME to confirm that you have read and agree to the terms and conditions.

  


Step 5: Confirmation: 

Once the application has been submitted, a confirmation is displayed with payment instructions. For example:

Thank you for your application. You have two payment options:

  


  * Mail a check made payable to Faith Builders Special Entity.  We will not deposit the check until your application is admitted.
    * Attn: Lucy Miller



Faith Builders Special Entity

28527 Guys Mills Rd.

Guys Mills, PA  16327

  


  * Wait to send payment.  We will contact you to send the money upon admittance and will need the check in 20 days or less.



  


Development Specification

Change Requests: 

  * Tim Reitz 09/16/2024: [[[IN9890](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9892&)]] - XFB - Online submission changes (WSGI changes) 
  * Tim Reitz 09/19/2024: [[[IN10388](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10390&)]] - XFB - WSGI: SPE Online Submission: School Selection Page 
  * Tim Reitz 09/23/2024: [[[IN10607](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10609&)]] - XFB - WSGI: Additional Items - SPE Online Submission: School Selection Page
  * Tim Reitz 09/23/2024: [[[IN10619](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10621&)]] - XFB - WSGI - SPE Online Submission - Business Screen - Default "State" to "PA"
  * Ben Reitz 05/01/2025: [[[IN10849](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10851&)]] - XFB - WSGI - SPE Member Application - Change School drop list behavior


