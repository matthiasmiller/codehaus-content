3.3.2. Editing Parent Households

  


Requirements

TODO_CH: Please review this new spec:

  


Parent information can be entered in one of several ways:

  * If the parent household already exists in the system, the user can simply type in the household #. If the number exists in the system, the parent names will immediately be displayed as readonly.
  * The ellipsis button beside each of the Household # fields will open a choice report (popup on the same page, not a new page) that uses the same prompts as the View Households. It will show the search results. Selecting a search result will close the popup and enter the household # into the field. The parent names will again be displayed as readonly.
  * If the parent household is not yet in the system, a new number can be typed in along with the parent names. When the record is saved, the parent record will automatically be created. After save, the parent names will be displayed as readonly.
  * If the parent household will not be in the system (e.g. out of state parents), the parent names can be typed in without a household numbers. The names will continue to be editable. 



  


The Edit Household link will open the linked household. This will be visible if the household has already been entered into the system.

  


Development Specification

[ ] Choice Report

Time: 4 hours

  


[ ] We will need to validate that none of the Household #'s on the record duplicate each other.

  


[ ] Even though HouseholdHeadParentHouseholdNum is a list field, we will use a HouseholdHeadParentHouseholdEntry macro that lets them enter it as a number. If the number exists, it will store it in HouseholdHeadParentHouseholdNum. Otherwise it will be stored in a new HouseholdHeadParentNewHousehold field.

[ ] We will have fields for HouseholdHeadFatherNameStored, etc. These will be used for entering a name for new items or for ones that won't be in the system.

1 day for basic fields and wrapper macros.

[ ] We will use a record OnModify to add a new list item for this household. This can be done by setting HouseholdHeadParentHouseholdNum to a complex single-line ini string that starts with:

[ ] HouseholdHeadParentNewHousehold and adds all other fields:

51 [NewValues]HeadFatherFirst=John^nHeadFatherMiddle=R^nHeadFatherLast.....

[ ] We will need to add OnInit statements to the Directory record that will parse out the hidden list field and put the values into the correct fields. TODO_CH: Matthias, are you sure that the list value will be set before OnInit fields are triggered? I think so, but the whole design completely depends on that.

This will cause a new record to automatically be created.

[ ] We can use an OnModify field change expression to discard the extra additional portion.

EM: 1 day or Normal Dev: 3 Days

  


The Household ID would be used to autocreate records.

  * If the entered household # does not exist in the database, related fields are editable.
  * When saving, the household record would combine all related fields into a single string and save it as a new row in a hidden Created Households RG / list value. (The value must be single-line, but could be some form of INI configuration or string table). The detail screen would automatically create a linked record by that name. The new household detail screen would use field change expressions on the new record to initialize all the associated fields appropriately.
  * When saving, delete the source rows from the original RG, since the linked RG will be responsible for creating these.
  * Once the parent detail screen recognizes that a record exists for the Household #, it would make the fields read-only and load the values from the linked record. (This will require editable macros.)


