4.6. Export Household Directory

  


Requirements

This export will export all active households as a single Word document, using the template defined in AppHosting.zone settings.

  


The template should model the Word document sample that was provided. The format is:

  


HouseholdNumber. HeadOfHouseholdLastName, *HeadOfHouseholdFirstName HeadOfHouseholdMiddleName, (ChurchNumber-BookNumber) Address, City, State, ZIP b HeadOfHouseholdBirthDate HeadOfHouseholdBirthLocation, d HeadOfHouseholdDeceasedDate HeadOfHouseholdBurialLocation son/dau of HeadOfHouseholdParents, m AnniversaryDate to *SpouseFirstName SpouseMiddleName SpouseMaidenName b SpouseBirthDate SpouseBirthLocation, d SpouseDeceasedDate SpouseDeceasedBurialLocation, son/dau of SpouseParents Occupation, Deacon DeaconYear Minister MinisterYear Bishop BishopYear.  Children: ChildFirstName ChildMiddle ChildHouseholdNumber b/stillborn ChildBirthDate ChildBirthLocation m ChildSpouseFullName d ChildDeceasedDate ChildBurialLocation.

  


Parent names are formatted as:

*FatherFirstName FatherMiddleName and *MotherFirstName MotherMiddleName (MotherMaidenName) MotherLastName ParentsHouseholdNumber

  


Previous marriages are formatted as:

HeadOfHouseholdFirstName HeadOfHouseholdMiddleName HeadOfHouseholdMaidenOrLastName previously married AnniversaryDate SpouseFirstName SpouseMiddleName SpouseMaidenOrLastName b SpouseBirthDate SpouseBirthLocation, d SpouseDeceasedDate SpouseDeceasedBurialLocation, son/dau of SpouseParents.  Children: ...

  


Notes:

  * "d Date" is only included if the individual is deceased.
  * Asterisks are used to prefix names of deceased individuals. The example above shows all possible locations.
  * The comma after the BirthLocation is only used when a BirthLocation is specified.
  * Dates are formatted as "Jan. 1, 2001".
  * ChildBirthLocation and ChildBurialLocation are only included if the child is within the parents' household.
  * The Deacon, Minister, and Bishop labels are eliminated if the respective year is blank.
  * Children are repeated in the same format, separated by semicolons.
  * Children are always listed in order of descending age.



  


Sort by:

  * Head Last Name
  * Head First Name
  * Head Middle Name
  * Head Age (oldest first)



  


Development Specification

Getting template and "configure formatting" working correctly.

Bid: 5 days
