3.4. People

  


Requirements

The sections and fields are outlined in the mockups.

  


Person section:

  * Person # (automatic number)
  * Person (read-only in the format of "LastName/MiddleName, FirstName, MiddleName #PersonNumber"; if the child is stillborn without a name, show "Stillborn son/daughter/child of (Parents) #PersonNumber"). NOTE: The wife's name in the system will remain as her maiden name.
  * Gender (required unless stillborn)
  * Last/Maiden Name (show "Last Name" for men, and "Maiden Name" for women; required unless stillborn)
  * First Name (required unless stillborn) 
  * Middle Name



  


Birth section:

  * Stillborn
  * Birth Date
  * Birth City
  * Birth State (list of states)



  


Death section:

  * Deceased (checkbox)
  * Deceased Date (visible if deceased)
  * Burial City (visible if deceased)
  * Burial State (visible if deceased; list of states)



  


Parents section:

  * Parents (list of all marriages, formatted as "Husband and Wife (Household #534)", using the formatting described in the Person section). The household will be omitted if no household number has been assigned.
    * The wife will be listed by her maiden name. However, she can be found by entering her current last name, since it will match on her husband's last name in the list.
  * Father (read-only; link to the father, if specified)
  * Mother (read-only; link to the mother, if specified)



If the parents are not specified, show the following fields:

  * Father First Name
  * Father Middle Name
  * Father Last Name
  * Mother First Name
  * Mother Middle Name
  * Mother Maiden Name



  


Head of Household section:

  * Household # (read-only; stored a read-only number assigned by the Renumber Households feature; automatically calculated for spouse and children)
  * Head of Household (checkbox; shows/hides all other controls in section; required to be true for husbands or fathers; can NOT be true for wives or widows; optional for unmarried men and women)
  * Active Household (checkbox; warn if active and both parents are deceased, no children are living at home, and the household is still active)
  * Church # (list field similar to magazine entries)
  * Book # (text input)
  * Address
  * City
  * State (list of states)
  * ZIP Code
  * Phone
  * Occupation



  


Ordination section (only visible for men who are a head of household or married)

  * Minister Ordination Year (number)
  * Bishop Ordination Year (number)
  * Deacon Ordination Year (number)



  


Marriages section (editable for husband; read-only for wife; for the wife; only visible for people who are "Minimum Married Age" or older)

  * Spouse (required; drop list of unmarried females, including widows, who are "Minimum Married Age" or older; validate against spouse being Head of Household):
  * Anniversary (date)
  * Deceased (read-only date)
  * View (link to Spouse record)



  


This list will be reverse-sorted by Anniversary.

  


Notes & Follow-up section:

  * Needs followup (checkbox)
  * Notes (memo)



  


Children section (read-only, in reverse age order):

  * Name
  * Gender
  * Birth Date
  * Birth Place
  * Household #
  * Marriage Date
  * Spouse
  * Deceased Date
  * View (link to child record)



  


Warn if any of the following fields are missing:

  * Last/Maiden Name
  * First Name
  * Church # (if Head of Household)
  * Address (if Head of Household; including City, State, ZIP)



  


Notes:

  * Unnamed stillborn children can be entered as "Stillborn son", "son", "Son", etc. They would be displayed as Name stillborn Apr. 12, 2021



  


Development Specification

Ellis Miller 05/05/2021:

[ ] Use a lookup record "Church Directory Person" with an auto-formatted list field that includes the person #.

[ ] TODO: Matthias, do you think it's helpful about starting the person number at a base of 50K or 100K to not confuse with Household # or don't you care?

Matthias Miller 05/06/2021: It would probably be nice, yes.

[ ] Use "Prevent Delete If Referenced"

Included with basic screen.

  


[ ] Add basic screen without links or virtual RG's.

1 day.

  


[ ] Auto-format the name as specified.

1/2 day.

  


[ ] Optimizing the Parents list:

We will have a ChurchDirMarriages.ndx of:

ListNum(Husband)

ListNum(Wife)

ListNum(Household#)

1-byte Husband Deceased T/F -- used for the spouses list below.

  


Rough pseudo-code, Ellis will help polish.

ListSubstitute( ChurchDirectoryPersons,

Assign vHusband = ListSubsubstituteItem;

Assign vSpouseKeys = MarriagesNdxConcat( ListNum(vHusband), String(ReverseBinString( Mid(NdxKey, 4)));

ListSubstitute( vSpouseKeys, vHusband + " and " \+ ListString( Value(ListSubstituteItem))

)

1/2 day.

  


[ ] Marriage Virtual RG.

1/2 day.

  


[ ] Defining the Spouse options list:

Besides the ChurchDirMarriages.ndx we will need a PersonAndGender.ndx (ListNum(Person) + "M/F"

  


ListSubstitute( ChurchDirectoryPersons, if (IsFemale and NOT HasMarriage Or HusbandDeceased))

1/2 day.

  


[ ] Children's Virtual RG.

PersonsByParents.ndx -- 4-byte Father ID + 4-byte Mother ID

6 hours

  


[ ] Behaviors  \-- all of the various visibility and required validation above.

[ ] Clear entered parent names on save if one is selected list.

[ ] Assign Household#

1 day.
