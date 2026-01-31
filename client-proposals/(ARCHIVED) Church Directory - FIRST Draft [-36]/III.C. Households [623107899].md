3.3. Households

  


Requirements

The sections and fields are outlined in the mockups.

  


To make it easier to enter information, we will allow entering parent and child information on the household screen. This will automatically create associated household records for the parents and children, and will link them together. This is outlined in subsequent sections.

  


Warn if any of the following fields are missing:

  * Head of Household names Ellis Miller 04/25/2021: TODO_CH: Probably not middle name?
  * Church #
  * Address (including City, State, ZIP)



  


No other fields (except Household #) will be strictly required.

  


Ellis Miller 04/25/2021: TODO_CH: The Last/Maiden name is messy because it's really complex to think through behaviors of how it interacts with singles/married, husband/wife, left/right. The nuances are twisting my mind. We can reduce cost if we move Gender to the top of Head of Household section and then just display an editable "Maiden Name" if it is Female and a readonly "Last Name" if it is male. If you agree, then should Last Name be editable if the husband is on the right or should we just display the HeadLastName as readonly there? I'm fine either way. Another reason for this is for a single female, it's weird to have two places to enter last name. If it's labeled Maiden Name it will be clear whether it should be specified for her again.

  


There are a few special behaviors:

  


  * The household # will support up to 3 decimals (i.e. 0.001). This will be used to enter household numbers from the existing publication. In the future, decimal numbers will not be used.



  


  * The Assign New # will find the largest Household Number, then add 1 more. For example, if the latest number is 412.3, it will assign 413. If another user creates Household #413 before the first user saves, the first user will not be able to save and will have to pick yet another number.



  


  * A household should remain active as long as either the head of household or spouse is living, or as long one or more children are living in the household. Otherwise, the software will show a warning when saving the household. 



  


  * Deceased Date/Place should be hidden unless the checkbox is checked.



  


  * The "Assign as Head of Household" will swap the contents of the Head of Household and the Spouse section. This may cause loss of information, such as ordination information or spouse maiden name. The occupation and ministry information will be blanked out in this case.



  


When entering a new household, the software will make sure the individual is not listed as a child without a household on the parent household (matching on first name). Show a warning in this case.

  


Notes:

  * Unnamed stillborn children can be entered as "Stillborn son", "son", "Son", etc. They would be displayed as Name stillborn Apr. 12, 2021
  * The asterisks will be manually entered if the parents are deceased.
  * Maiden names will be displayed as "Anna F. (Stoltzfus) Beiler".



  


Development Specification

Ellis Miller 04/25/2021:

Let's make this a list-tied custom DB Level (similar to a lookup type). The Household # will be the the list key field.

  


[ ] Adding basic screen without button actions, parent fields, or the children RG's.

1 day.

  


[ ] Adding Behaviors (from above, maybe wait until parent and child fields are defined):

[ ] Missing field warnings

[ ] Validation that Household # is a positive number (with up to 3 decimals).

[ ] Warning that Active checkbox is in sync with fields.

[ ] Visibility on Deceased fields

[ ] Warning that isn't listed as a child on the parent record.

[ ] That entered household ID's are all different.

1.5 days.

  


[ ] Assign New Number

ListSubstitute on key list, Truncate values to find largest integer use. Go one higher.

2 hours.

  


Assign as Head of Household

Set up detail variables for each of the temp fields. I'd probably use:

varAssignHeadLastName

varAssignHeadMaidenName

varAssignHeadParentHouseholdNum

varAssignHeadFatherFIrstName

etc

You will then have a set of change expressions that copy everything out of the HouseholdSpouse fields into the AssignHead variables, then copy HouseholdHead fields over to HouseholdSpouse fields and finally copy AssignHead variables into the HouseholdHead fields.

  


Note that there are temporary fields that we sometimes use when setting up a record for the first time. I think the simplest solution is to simply have variables for those as well.

  


Head of Household is Male: Copy Head Last Name into Spouse Last/Maiden Name, don't update Head Last Name.

Head of Household is Female: Blank out Spouse Last/Maiden Name, don't update Head Last Name.

  


Blank out ministry and occupation fields.

1 Day.
