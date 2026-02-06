10.1. Prompts

  


Requirements

Step 1: Member Type and Eligibility

  


Prompt whether the application is for an individual or a business.

  


Show a checkbox with a configurable confirmation prompt that they are eligible for the SPE.

  


Step 2a: Business Information (only shown for businesses)

  


It would prompt for:

  * Business Name
  * Contact Name
  * Contact Preferred Name
  * Contact Address
  * Contact City
  * Contact County
  * Contact State
  * Contact Zip
  * Contact Phone Number
  * Contact Email
  * EIN
  * Entity Type
  * Owner SSN
  * PA Revenue #
    * Use the same validation as specified in the Contacts screen.
    * Include a notice, "It can be found on a form from the Pennsylvania Department of Revenue called Notice of Registration for Employer Withholding Tax below the Account ID or on the business’s PA tax return from last year."
  * Anonymous Donor
    * Include a notice, "Check here if you want your contribution to be anonymous to the school(s) you designate."



  


Businesses are implicitly eligible for SPE, as long as they fall within one of the listed entity types.

  


Note that the visibility/requirements for the additional business fields should match the requirements described in the Contacts section (depending on the business entity type).

  


Step 2b: Individual Information (only shown for individuals)

  


It would prompt for:

  * First Name
    * Include a notice, "Legal name for tax documents"
  * Middle Name or Initial
    * Include a notice, "For tax documents"
  * Preferred Name
    * Include a notice, "For email communication from us and contribution info sent to schools (if not anonymous).  If left blank, we will use first name."
  * Last Name
  * Address
  * City
  * County
  * State
  * Zip
  * Phone Number
  * Email
  * SSN
  * Anonymous Donor
    * Include the same notice as for Business Information.



  


It will include an eligibility checkbox:

  


[ ] I certify that I qualify to join this SPE, and that I am

(1) a partial owner of a PA for-profit business (NOT a sole proprietor), OR

(2) a W-2 employee of a for-profit business, OR

(3) a stockholder of a PA registered business

  


Step 3: Recommended School Designation

  


It would prompt for the initial contribution amount. Indicate and enforce a $3,000 minimum.

  


After that, it would prompt for a list of schools and an amount. When specifying the school designations, it will prompt for the school name and the county. Applicants will be able to select existing schools, or enter new ones.

  


Applicants will be able to enter new schools. If the school is not already in the system, they will be required to specify a name, and either a phone or email:

  * Contact Name
  * Contact Phone
  * Contact Email



  


Note that the visibility and data requirements should match the Members/Businesses detail screen.

  


Step 4: Agreement

The applicant will be required to confirm the following items by checking them off:

  


The undersigned hereby agrees to become a member of a Faith Builders Special Purpose Entity in accordance with the foregoing Operating Agreement, and with the following conditions:

  


[ ] The initial contribution is $______ (minimum $3,000). The member takes responsibility for deciding the amount in consultation with his tax adviser. Faith Builders Special Purpose Entities are not responsible for any unusable tax credit issued to a member.

  


[ ]  The member will contribute the same amount in the succeeding calendar year within 30 days of notification by a Faith Builders Special Entity, LLC representative OR the member will recruit a replacement person or entity to fulfill the obligation. In any case, the signer is responsible to arrange for the same amount to be paid for the following year.

  


[ ] The applicant is currently tax compliant with the state of Pennsylvania.

  


[ ] The applicant acknowledges and agrees that there is no expectation for any economic benefit as a result of the investment other than the allocation of the applicable state tax credits and federal charitable contribution deduction.

  


[ ]  The applicant has recommended where to direct the contribution; schools will receive 95% of this amount after deducting Faith Builders Scholarship Services administration fee.

  


The applicant will then be required to enter his/her full name:

  


Enter your FULL NAME to confirm that you have read and agree to the terms and conditions.

  


Step 5: Confirmation

  


Once the application has been submitted, show a confirmation with payment instructions. For example:

  


Thank you for your application. You have two payment options:

  


  * Mail a check made payable to Faith Builders Special Entity.  We will not deposit the check until your application is admitted.
    * Attn: Lucy Miller



Faith Builders Special Entity

28527 Guys Mills Rd.

Guys Mills, PA  16327

  


  * Wait to send payment.  We will contact you to send the money upon admittance and will need the check in 20 days or less.



  


Development Specification

[ ] TODO_CH: Update mockups to use First Name/LastName/Preferred Name/etc -- also makes ure submissions detail matches
