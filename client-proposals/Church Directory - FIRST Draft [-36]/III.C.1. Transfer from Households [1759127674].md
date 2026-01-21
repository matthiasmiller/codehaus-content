3.3.1. Transfer from Households

  


Requirements

TODO_CH: Please review all of this and clean it up. If it's too detailed, move it to the Dev Spec.

  


A "Transfer from Households" button shows a prompt to support transferring a member of another household to become the Head of Household or the Spouse for the displayed record. 

  * A child from another household can be selected in the event of a marriage or a child leaving home to form their own household. In this case, the child will be moved from the "Children with No/New Households" table to the "Children Outside of Household" table in the source record. 
  * A single head of household can be selected in the event of a single head of household marrying another. TODO_CH: I added this case, but I think it's legit. I presume we fill in the "Next Marriage Household #" and uncheck "Active Household"?
  * A head of household can be selected if their spouse is deceased for the situation of a widow or widower remarrying. In this case, the source record's "Next Marriage Household #" will be filled in with the new household # and the Marriage Status is changed to "Previous Marriage". If there are no children in the home, the record will also be deactivated.
  * If the head of household is deceased and the spouse is selected, a message is displayed: "In order to transfer a remaining spouse, first use the "Assign as Head of Household" to make them the head of the household." TODO_CH: Are you OK with this, it does make things simpler. Should the main detail screen give a warning if the spouse is living and the Head of Household is deceased that they should use the "Assign as Head of Household" option?
  * If both spouses are living, they will not be listed as members in the drop list. TODO_CH: Is this better or should we just show an error message: "A member cannot be transferred if their spouse is still living."
  * TODO_CH: Should we filter out deceased children and spouses? I presume yes. The only possibility is if someone is wanting to enter historical data or something. I don't have a preference.



  


To ensure that data is not inadvertently overwritten, we do not let you transfer to the Head of Household if the Head First Name is specified. An message is displayed:

  


Transfer Head of Household is not available because one is already specified. If you wish to overwrite existing information, first blank out the Head First Name.

  


Similarly for Spouse:

  


Transfer Spouse is not available because spouse is already specified. If you wish to overwrite existing information, first blank out the Spouse First Name.

  


For clarity, we will have the Member drop list use prefixes:

Head of Household: Henry R Yoder

Spouse: Susan Joann

Child: John Mark

Child: Mary Sue

This avoid the problem where a parent and a child have the same name. The last name is included for the head of household. For the spouse and children, both the first and middle name are displayed.

  


Development Specification

We will have a child screen with a set of fields:

[ ] HouseholdShouldTransferHead

[ ] HouseholdTransferHeadFromNum

[ ] HouseholdTransferHeadMember

[ ] HouseholdShouldTransferSpouse

[ ] HouseholdTransferSpouseFromNum

[ ] HouseholdTransferSpouseMember -- string field with member name

  


We can't do it if Household # is not filled in. Show a red label at the top of the child screen if it is not specified:

  


Please assign Household # before transferring from other households.

  


Hide the button and all fields if the number is not specified.

  


The above warnings and validations need to be added.

1.5 days.

  


The "Std Transfer from Households.x30list" needs to then pass the displayed Household# as an ask prompt into the x30. Use [SaveRecord] to ensure that the record is first saved.

  


Make sure this works with a brand-new record that isn't saved yet as long as the Household # is specified. Presumably we will pass the household # on fine.

  


the x30list will have several x30's:

  


The "Std Transfer from Households - Import to Target.x30" will use transfer statements for each of these:

  


Condition: HouseholdShouldTransferHead; HouseholdHeadImportIniData = LocLookupHeadImportData

Condition: HouseholdShouldTransferSpouse; HouseholdSpouseImportIniData = LocLookupSpouseImportData

....

  


You will need some supporting fields/macros:

  * _____ImportIniData is an editable macro that takes a long import string that is essentially Field=Value^nField=Value and uses OnChange statements to set all of the appropriate fields.
  * Lookup_____ImportData is a macro that wraps calls LookupField calls to a number of macros to return IniData: HouseholdHeadIniData,  HouseholdSpouseIniData, HouseholdChildIniData, etc. We will use similar macros for other creation logic.



  


The  "Std Transfer from Households - Scrub Source.x30" takes the same ask prompt, but modifies the source record as detailed above.

  


The  "Std Transfer from Households - Scrub Target.x30" cleared the temporary fields:

HouseholdShouldTransferHead = false

HouseholdTransferHeadFromNum = ""

HouseholdTransferHeadMember = ""

...

  


Bid at 5 days
