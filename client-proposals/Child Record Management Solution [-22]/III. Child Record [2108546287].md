3\. Child Record

  


Requirements

The Child screen is the primary record in the database.

  


  * Warn if there are no phone numbers specified for this child.
  * Django ID (hidden; for imports)
  * Section: Summary (maybe use child’s name as the label)
    * Termination date (date)
    * Notes (memo)
    * Last modified by user/date (read-only)
    * Print (see attached template)
  * Section: Demographics (with fields from the demographics tab)
    * Column 1
      * First name (required)
      * Middle name
      * Last name (required)
      * Address (required)
      * City (required)
      * County (required); list of:
        * Chaffee
        * Custer
        * El Paso
        * Fremont
        * Pueblo
      * State (required; list of 2-letter codes)
      * Zip code (required; text)
      * Unborn child (checkbox)
    * Column 2
      * Birthdate (required)
      * Gender (required; list of Male/Female)
      * School district (list of):
        * C-1 - Custer
        * OTH - Other
        * RE-1 - Fremont
        * RE-2 - Fremont
        * RE-3 - Fremont
        * Preschool / Child Care
        * Home School
      * Preschool / Child Care (text field)
        * When migrating, if the old system had a school district of blank, and the Health and Development preschool setting is set to “yes”, set the school district to “Preschool / Child Care” and fill in the value. (Do NOT override Other school district.)
      * Referral Source (moved from Programs tab); list of:
        * Behavioral Health
        * CCB
        * Child Care
        * Dev. Ops - Starpoint
        * Early Head Start
        * Echo
        * First Steps
        * Friend/Relative
        * Head Start
        * Hospital
        * Human Services
        * Mental Health
        * Other
        * Parents
        * Physician
        * Public Health
      * Referred by (text)
      * Eng Pri Lang (Yes/No list)
      * Hispanic/Latino (Yes/No list)
      * Race; multiple choice of:
        * New List:
          * American Indian / Alaskan Native
          * Asian
          * Black / African American
          * White
          * Native Hawaiian / Other Pacific Islander
          * Two or more races (yes/no)
        * Old List:
          * American Indian or Alaskan Native
          * Asian/Pacific Islander (blank out in migration)
          * Black
          * Hispanic (should migrate over to White)
          * Other
          * White Not Hispanic



Note: New system has just the new list. Old list is for documentation, etc.

  * Home Phone
  * Leave a Message Phone (renamed from “Message Phone”)


  * Contacts. These fields will be read-only and will reflect the values in the caregiver sections below.
    * Mother Email
    * Mother Cell Phone
    * Mother Work Phone
    * Father Email
    * Father Cell Phone
    * Father Work Phone
    * Caregiver Email
    * Caregiver Cell Phone
    * Caregiver Work Phone
  * Primary Doctor (text field)
  * Insurance; choice of:
    * Applied - DNQ
    * CHP+
    * Medicaid
    * None
    * Private
  * Primary Caregiver; choice of:
    * Parents
    * Mother
    * Father
    * Guardian
    * Relative
    * Kinship Placement
    * Foster Care (formerly “DHS”)
    * Other


  * Section: Caregiver - Mother
    * (always be visible)
    * First Name
    * Middle Name
    * Last Name
    * Address
    * Cell Phone
    * Work Phone
    * Email (Require a choice of Yes/No/Blank; require an address if Yes)
    * Marital Status; choice of:
      * Divorced
      * Married
      * Never Married
      * Partner
      * Separated
      * Widowed
    * Eng Pri Lang (Yes/No list)
    * Maternal Age (number)
    * Total Pregnancies (number)
    * Prenatal Care (Yes/No list)
    * Employment Status; list of:
      * Employed
      * Unemployed
      * Student
      * Not In Work Force
    * Occupation (visible if Employed is selected in Employment Status above)
      * Corrections
      * Education
      * Laborer
      * Medical
      * Professional
      * Sales/Technical
    * Occupation Import; hidden field that requires value to be a blank, or an item in one of the above lists; sets the appropriate field based on the value
    * Education (number)
    * Custody (checkbox)
  * Section: Caregiver - Father
    * (always be visible)
    * First Name
    * Middle Name
    * Last Name
    * Address
    * Cell Phone
    * Work Phone
    * Email (Require a choice of Yes/No/Blank; require an address if Yes)
    * Marital Status (same as Caregiver - Mother)
    * Eng Pri Lang (Yes/No list)
    * Paternal Age (number)
    * Employment Status (same as Caregiver - Mother)
    * Occupation (same as Caregiver - Mother)
    * Occupation Import (same as Caregiver - Mother)
    * Education (number)
    * Custody (checkbox)
  * Section: Caregiver - Guardian
    * (visible when Guardian is set as primary Caregiver type)
    * First Name
    * Middle Name
    * Last Name
    * Address
    * Cell Phone
    * Work Phone
    * Email (Require a choice of Yes/No/Blank; require an address if Yes)
    * Employment Status (same as Caregiver - Mother)
    * Occupation (same as Caregiver - Mother)
    * Occupation Import (same as Caregiver - Mother)
    * Education (number)
    * Custody (checkbox)
  * Section: Caregiver - Relative
    * Separate set of fields matching Guardian
  * Section: Caregiver - Kinship Foster Family
    * (visible when kinship placement is set as primary Caregiver type) 
    * First Name
    * Middle Name
    * Last Name
    * Address
    * City
    * State (list of 2-letter codes)
    * Zip code
    * Cell Phone (migrate from Phone)
    * Work Phone
    * Email (Require a choice of Yes/No/Blank; require an address if Yes)
  * Section: Caregiver - Foster Family
    * (visible when foster care is set as primary Caregiver type)
    * First Name
    * Middle Name
    * Last Name
    * Address
    * City
    * State (list of 2-letter codes)
    * Zip code
    * Cell Phone (migrate from Phone)
    * Work Phone
    * Email (Require a choice of Yes/No/Blank; require an address if Yes)
  * Section: Housing
    * (always visible)
    * Housing; choice of:
      * Other
      * Own
      * Rent
    * House Members (number)
    * Children in Household (number)
  * Section: Family Income
    * (always visible)
    * Income; choice of:
      * 0% - 75%
      * 76% - 100%
      * 101% - 130%
      * 131% - 150%
      * 151% - 185%
      * 186% - 225%
      * Over Income
    * Income Import: remove consecutive spaces and treat “151% - 225%” as blank
    * Income Source (multiple checkboxes)
      * Technical details: Let’s make this a virtual RG with checkboxes that’s based on a hidden list RG.
      * CCAP
      * Disability
      * Food Stamps
      * Other
      * Social Security
      * TANF
      * Veteran
      * Child Support/Alimony
      * Employment
      * No Income
      * Pension/Retirement
      * SSI
      * Unemployment
    * Lunch (formerly Meets F/R); list of:
      * Free
      * Reduced
      * Not Eligible
  * Section: State Risk Factors (checkboxes)
    * (always visible)
    * Parent Information (new items)
      * Poverty (Uneditable, Sets automatically. The threshold is 130% it should fill the "Poverty" checkbox for the first 3 list items, not the last 4)
      * Educational Level of Mom <12 yr:
      * Educational Level of Dad <12 yr:
      * Age of Mom at Child’s Birth (17yr or Younger):
      * Age of Dad at Child’s Birth (17yr or Younger):
      * English as Second Language (Child)
    * Screening/Test Results (new items)
      * In Need of Language Development
    * High Social Need (existing items)
      * Abusive Adult in Home: 
      * DHS for Neglected/Dependent Child: 
      * Poor Social Skills/Needs Social Emotional Development: 
    * Family Crisis (existing items)
      * Frequent Moves (>2/yr): 
      * Homelessness (McKinney-Vento) 
    * High Family Risk (existing items)
      * Drug/Alcohol Abuse:
  * Section: Local Risk Factors (checkboxes)
    * (always visible)
    * Parent Information (mostly new items)
      * Siblings in SPED in Public School
      * Mother Employed 
      * Father Employed
      * Two parents
      * One parent
      * Grandparent(s)
      * Other relative
      * Friend
      * Other caretaker
    * Screening/Test Results (new items)
      * ASQ Questionable
      * Overall developmental concerns
      * In need of fine and/or gross motor development
      * DASE
    * Family Crisis (mostly new items)
      * Chronic Illness/Terminal Illness/Death of Parent (migrated from Terminal Illness/Death in Family)
    * High Family Risk (mostly new items)
      * Mental Illness/Disability (migrated from Mental Illness/Disabled)
      * Parent in the military
      * Parent in jail or in prison
      * Serious child health problem
  * Section: Programs
    * For each program, the additional fields should only be visible if the Active? setting is Yes or Terminated. The Active? setting should be automatic based on whether Today is in the range of Enroll Date and Termination. This will be an embedded spreadsheet in the following format. It will allow to track multiple enrollments in the same program.



  


Program Type| Active?| Enroll Date| Termination Date| C2K Specialist| Behavior Team| Referral Date| District| Primary Care Provider| Pieces Category| Pieces Status| Welcome Baby| Welcome Baby Issue Date| Welcome Baby Home Visitor  
---|---|---|---|---|---|---|---|---|---|---|---|---|---  
[ECHO Screening]| Yes/No/Terminated|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
|   
  
  
  


  * ECHO Screening
    * Active? (Yes/No/Terminated list)
    * Enroll Date
    * Termination Date
  * Mental Health
    * Active? (Yes/No/Terminated list)
    * C2K Specialist (renamed from ECMH Specialist)
    * Behavior Team
    * Needs Enroll Date and Terms date fields //(with option to be blank for old records possibly)
    * Referral date
  * CPP
    * Active? (Yes/No/Terminated list)
    * District (list; same as district in demographics but without “Preschool / Child Care” and “Home School”)
    * Enroll Date
    * Termination Date
  * First Steps
    * Active? (Yes/No/Terminated list)
    * Enroll Date
    * Termination Date
  * Special Education
    * Active? (Yes/No/Terminated list)
    * District
    * Enroll Date
    * Termination Date
  * Early Headstart
    * Active? (Yes/No/Terminated list)
    * Enroll Date
    * Termination Date
  * Mother Wellness
    * Active? (Yes/No/Terminated list)
    * Primary Care Provider (text)
    * Enroll Date
    * Termination Date
  * Pieces
    * Active? (Yes/No/Terminated list)
    * Embedded Spreadsheet
      * Referral Date
      * Pieces Category; list of:
        * TDM
        * Diversion
        * Screenout
      * Enrollment date
      * Termination date
      * Status; list of:
        * Completed
        * Pending
        * No Contact
    * Migration?Mindy Hilbert 01/26/2021:?
      * Enroll date comes from earliest screening date //(with option to be blank for old records possibly)
  * CO Community Response
    * Active? (Yes/No/Terminated list)
    * Enroll Date
    * Termination Date
  * Headstart
    * Active? (Yes/No/Terminated list)
    * Enroll Date
    * Termination Date
  * Welcome Baby (renamed from Passport)
    * Active? (Yes/No/Terminated list)
    * Enroll Date
    * Termination Date
    * Welcome Baby (text) -- renamed from Passport
    * Issue Date
    * Home Visitor (migrate using first name and last name from the original record)


  * Section: Health and Development
    * (Each of these options has a Yes/No list, with a Comment if Yes)
    * Any problems during pregnancy?
    * Did child have problems at birth or in the first few weeks of life?
    * Has child been hospitalized?
    * Does child have any chronic health problems?
    * Does child have all recommended immunizations?
      * This question does not have the comments field
    * Do you have any concerns about your child?
    * Child’s birthplace (no choice; just text field)



  


Screenings

Screenings will be displayed in a list at the bottom of the screen (reverse sorted by date, with Screened By and single line Notes). We will have a New Screening button/link on the screen.

  


Development Specification

Matthias Miller 07/16/2020: Here are some design ideas for risk factors and programs:

  


Ellis is offering to pair program the virtual RGs.

  * Have a list called Risk Factor Categories to include "Parent Information", "Screening/Test Results", etc
  * Have a dictionary list Risk Factor Category Map to map from a state/local risk factor to a category.
  * Create a virtual RG based on a macro that generates a list such as:
    * State Risk Factors
    * [Tab]Category 1
    * [Tab][Tab]Risk Factor 1
    * [Tab][Tab]Risk Factor 2
    * [Tab]Category 2
    * [Tab][Tab]Risk Factor 3
    * [Tab][Tab]Risk Factor 3
    * Local Risk Factors
    * etc
  * Have two hidden RGs, with OnChange expressions to add/remove items from the RG when the risk factors are being modified.
  * If it's simpler to combine the risk factors into one list, and filter them for reporting, I'm fine with that as well.



  


Matthias Miller 07/31/2020: Could we change Pieces to 3 programs?

  * Pieces TDM
  * Pieces Diversion
  * Pieces Screenout



No, we can't. There's two issues with this approach: The category can change within the same enrollment period, and the category may be unknown.
