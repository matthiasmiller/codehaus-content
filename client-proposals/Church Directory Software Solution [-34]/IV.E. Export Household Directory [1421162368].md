4.5. Export Household Directory

  


Requirements

This export will export all active Heads of Households as a single Word document, using the template defined in AppHosting.zone settings.

  


The template should model the Word document sample that was provided.

  


For the current marriage (whether the husband is living or deceased), the format is:

HouseholdNumber. LastName, *FirstName MiddleName, (ChurchNumber-BookNumber) Address, City, State, ZIP b BirthDate BirthLocation, d DeceasedDate BurialCity, BurialState son/dau of Parents, m AnniversaryDate to SpouseInformation Occupation, Deacon DeaconYear Minister MinisterYear Bishop BishopYear.  Children: ChildFirstName ChildMiddle ChildHouseholdNumber b/stillborn ChildBirthDate ChildBirthLocation m ChildSpouseFullName d ChildDeceasedDate ChildBurialLocation.

  


SpouseInformation will be formatted as:

*FirstName MiddleName MaidenName b BirthDate BirthLocation, d DeceasedDate BurialCity, BurialState, son/dau of Parents

  


Parent names are formatted as:

*FatherFirstName FatherMiddleName and *MotherFirstName MotherMiddleName (MotherMaidenName) MotherLastName ParentsHouseholdNumber

  


For the previous marriages, the format is:

SpouseFirstName SpouseMiddleName SpousePreviousLastName previously married AnniversaryDate FirstName MiddleName LastName b BirthDate BirthCity, BirthState, d DeceasedDate DeceasedBurialLocation, son/dau of Parents.  Children: ...

  


Notes:

  * Because of how prior marriages are numbered, we only need to show information for the current spouse.
  * "d Date" is only included if the individual is deceased.
  * Asterisks are used to prefix names of deceased individuals. The example above shows all possible locations.
  * The comma after the BirthLocation is only used when a BirthLocation is specified.
  * Dates are formatted as "Jan. 1, 2001".
  * "BirthCity, BirthState" are reduced to "BirthCity" if State is missing.
  * ChildBirthLocation and ChildBurialLocation are only included if the child is within the parents' household.
  * The Deacon, Minister, and Bishop labels are eliminated if the respective year is blank.
  * Children are repeated in the same format, separated by semicolons.
  * Children are always listed in order of descending age.
  * Maiden names will be displayed as "Anna F. (Stoltzfus) Beiler".
  * Note that the maiden name is the woman's surname at birth. The directory will never reference a surname from a prior marriage.



  


Sort by Household #

  


Development Specification

Getting template and "configure formatting" working correctly.

Bid: 5 days
