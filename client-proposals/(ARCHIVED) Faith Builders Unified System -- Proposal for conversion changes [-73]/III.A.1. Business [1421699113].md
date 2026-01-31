3.1.1. Business

  


Requirements

The Business record will be migrated to Contacts.

  


There will be EITC and Postcard sections added to the contact record. The visibility of the sections will be controlled by an "EITC" checkbox, similar to how the Member Details and Member Reports sections are currently visible according to the "Eligible for SPE" checkbox.

  


Development Specification

New Contact fields:

EITC section:

  * ContactBusinessEITC (boolean)
  * ContactBusinessEntityType (list)
  * ContactBusinessIncorporatedInPA (boolean)
  * ContactBusinessRegisteredinPA (boolean)
  * ContactBusinessPassThroughEntity (boolean)
  * ContactBusinessNAICSCode (string)
  * ContactBusinessFEIN (string)
  * ContactBusinessPARevenueNum (string)
  * ContactBusinessEnterpriseType (list, single field RG)
  * ContactBusinessTaxYearEndDay (number)
  * ContactBusinessTaxYearEndMonth (list)
  * ContactBusinessIsPostcard (boolean)
  * ContactBusinessIsAnonymous (boolean)
  * ContactLegacyMigrationCEOFirstName (string)
  * ContactLegacyMigrationCEOLastName (string)
  * ContactLegacyMigrationCEOTitle (list)
  * ContactBusinessMunicipality (string)



  


Postcard section:

  * ContactBusinessPostcardOverrideAddr (boolean)
  * ContactBusinessPostcardName (string)
  * ContactBusinessPostcardAddress (string)
  * ContactBusinessPostcardAddress2 (string)
  * ContactBusinessPostcardCity (string)
  * ContactBusinessPostcardState (list)
  * ContactBusinessPostCardZip (string)
  * ContactBusinessPostcardLogo (memo)
  * ContactBusinessPostcardMessage (memo)



  


Hidden fields:

  * ContactBusinessHistRegression (boolean)
  * ContactLegacyBusinessID (string)
  * ContactLegacyBusinessNumID (number)



  


See [migration spreadsheet](https://docs.google.com/spreadsheets/d/16b-Jtu-QJnQMcTIItlgQSDuK9cZ6L1B9YGbwkk8rNa8/edit#gid=0 "https://docs.google.com/spreadsheets/d/16b-Jtu-QJnQMcTIItlgQSDuK9cZ6L1B9YGbwkk8rNa8/edit#gid=0").
