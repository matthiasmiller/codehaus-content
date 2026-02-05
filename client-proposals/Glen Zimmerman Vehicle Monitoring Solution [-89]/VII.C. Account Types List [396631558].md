7.3. Account Types List

  


Requirements

*Done. 

  


Overview: This is a custom non-editable simple list used to track types of Accounts. 

  


It includes the following items: 

  


  * Business 
  * Household



  


This list is universal for all users.

  


Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

  


This list will be set up by CodeCrafters as part of the main development. If changes need to be made to this list, it will require some coding work.

  


Development Specification

Tim Reitz 08/13/2025: Account Types not included in HLD.

  


Niccolas Miller 02/02/2026: Unchangeable unsorted list.

  


Bid: 1 hour

  


  


  


  


  


\---------------

Tim Reitz 08/21/2025: I had considered making this a record type instead of a simple list. At this point in time I don't see the need for that, but if we end up going that route, the controls on the Account detail screen probably should change to something like this: 

  * Account Type (drop list of "Account Types" list items; with the following details / behaviors:
    * visible to and editable for:
      * the selected "Account Reseller";
      * all "Account Group Managers" for the selected "Account Group";
      * all users with the "Full Access" Permission;
    * required;
    * no ellipsis button or link to the record;
    * note that if very few Business accounts are set up, this could be changed to default to "Household")
  * View Account Type (label displays as "Account Type"; read-only macro; with the following details / behaviors:
    * visible to __ users;



basically whoever can't see the main field (the end users).

  * displays the selection in the "Account Type" field;
  * not a link to the record;
  * note that this is included to provide a read-only version for users who cannot edit the field)


