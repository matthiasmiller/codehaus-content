6.9.3. Changes to Contact Record for Phase 3c

The following changes will be applied to the existing Contacts records:

  


Add the following fields to the existing Customer Details custom section:

  * Preferred Invoice Format (required; drop list of Email / Fax / Print; defaults to blank) 



_IDD: have a plan for setting all of these when we add the feature 

TODO_JM: editable report or an export/import? 

  * Agreements by Customer (link to report; see corresponding section of this proposal)



  


Make the following customizations to Standard sections and fields: 

  * Standard "Active" checkbox:
    * Add the following validation: error on field if the Contact is linked to an Agreement record with Status = Pending or Active - "This Contact cannot be deactivated because they are linked to the following Active or Pending Agreements: <comma-separated list of Agreement Names>"



  


  * Standard AppHosting Settings section:
    * Receive Agreements Pending for Over 1 Week Alert (checkbox; visible if ___; defaults to unchecked; if checked, the User will receive the Agreements Pending for Over 1 Week alert)


