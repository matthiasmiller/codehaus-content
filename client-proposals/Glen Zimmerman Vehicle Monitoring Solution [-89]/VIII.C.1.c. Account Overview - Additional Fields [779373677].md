7.3.1.3. Account Overview - Additional Fields

*Done. 

  


  * Account Group (required; drop list of active Account Groups, displaying the "Group Name"; with the following details / behaviors:
    * editable for "Upline Provider Roles" users for the Account;
    * on the first Save after this is changed from its previously-saved non-blank value, the "Account Group Changed" email is sent to the impacted parties (the Account Reseller, the Primary Group Admin for both the old and the new Groups, and the Account Managers) - see corresponding spec)
  * View Account Group (visible if "Account Group" is not blank; link; opens the selected Account Group record) 
  * New Account Group (visible to all "Group Admins" for the selected "Account Group" and "Upline Groups" and to all users with the "Full Access" Permission if "Account Group" = blank; link; opens a new Account Group record)
  * Contact a Group Admin or Master Administrator if a new Group is needed. (on-screen message in gray text; visible to the linked "Account Reseller" / "Reseller Reps" if "Account Group" = blank) 



  


  * Account Address (read-only macro; displays the Primary address for the "Primary Account Manager", in the standard multi-line format without the addressee name)
  * Church Affiliation (read-only macro; displays the "Church Affiliation", or "Other Church Affiliation" if "Church Affiliation" = "Other", for the "Primary Account Manager") 



  


  * Service Start Date (date; with the following details / behaviors: 
    * editable if "Stored Account Status" = "In Setup", "Active", "Paused", or "Inactive";
    * required if "Stored Account Status" = "Active", "Paused", or "Inactive";
    * defaults to the current date when "Stored Account Status" is set to "Active" \- see corresponding spec; 
    * error on the field if set to a date more than 3 months in the past or more than 3 months in the future: "Must be within 3 month (past or future) of today.";
    * is cleared on the first Save after "Stored Account Status" is set to "Closed" \- see corresponding spec; 
    * note that in Phase 2, this likely will be moved to a separate section with other Subscription management-related fields) 
  * Renewal Anniversary Date (hidden; read-only macro; date; with the following details / behaviors: 
    * displays the first date of the month of the "Service Start Date"; i.e., if "Service Start Date" = "08/14/2026", this displays "08/01/2026"; 
    * this is used to drive the "Renewal Anniversary" macro and as a reference point for the annual renewal and the "Prepare Annual Renewals" automatic process - see corresponding specs; 
    * note that in Phase 2, additional capabilities could be added to this; 
    * note that in Phase 2, this likely will be moved to a separate section with other Subscription management-related fields) 
  * Renewal Anniversary (read-only macro; plain text; with the following details / behaviors: 
    * displays the first day of the month for the "Service Start Date", in the following format: "MMMM D"; i.e., if "Service Start Date" = "08/14/2026", this displays " August 1"; 
    * note that there is no year associated with this, as the renewal is a recurring annual event; 
    * note that in Phase 2, this likely will be moved to a separate section with other Subscription management-related fields)


