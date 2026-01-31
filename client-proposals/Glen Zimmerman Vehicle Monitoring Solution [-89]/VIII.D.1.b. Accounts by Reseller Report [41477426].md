8.4.1.2. Accounts by Reseller Report

  


Requirements

Overview: This is the "Master Accounts" report, filtered to a single Account Reseller.

  


Accessed from:

  * Providers | Accounts | My Reseller Accounts (opens the report directly, bypassing the filter screen, setting "Account Reseller" filter to the Contact for the current user) 



TODO_VA: Tim Reitz 10/24/2025: For Reseller Reps, this would be set to the the Account Reseller(s) for which they are a rep. 

TODO_VA: Tim Reitz 10/24/2025: How to handle situations where the user is a Reseller and/or Rep for multiple resellers? Is it enough to Group By reseller (see below)? 

_GZ: Tim Reitz 01/17/2026: Do you envision this happening? If yes, would they be logging in with different logins for each Reseller? 

TODO_VA: Tim Reitz 01/23/2026: Per Glen today, it would be possible for a person to be assisting multiple Reseller orgs as tech support, etc. and in that case it would make sense to make him a Rep for those Reseller orgs. 

  * "For <#> Account(s)" link on the Account Reseller's Contact record



  


The following filter(s) are set differently than on the main report:

  * "Account Reseller" = Set to non-blank, based on the place from which the report is opened. 
  * "Group By" = "Account Reseller" (to account for Account Resellers / Reseller Reps who oversee Accounts under multiple Account Resellers) 



  


Other Notes:

  * N/A



  


Development Specification

Mockup: N/A
