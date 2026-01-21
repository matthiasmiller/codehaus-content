2.1. Glossary

Overview: The purpose of this glossary is to provide a description of key terms, roles, and other things referred to in this proposal. These are listed in alphabetical order?? below:

  


  * Device: A generic term for the on-board device or app that is used for tracking:  
    * OBD-II (sometimes shorted to OBD): An "on-board device" that plugs into a vehicle to track it. It pulls data from the vehicle and GPS, then reports it back to a central location. It's used to capture error codes, fuel level, driving behavior, location, etc.
    * Traccar Client App: A basic open-source app that installs on a phone to track and report information to the Traccar server. This app is available for both Android and iOS: [https://www.traccar.org/client/](https://www.traccar.org/client/). 



  


  * Traccar: An open-source software that manages data from on-board devices. See [https://www.traccar.org/](https://www.traccar.org/) for details. 



  


  * Traccar Services: 
    * Traccar Manager App: An open-source app that app mirrors the Traccar Web Interface in a mobile app. It is available for both Android and iOS: [https://www.traccar.org/manager/](https://www.traccar.org/manager/). 



  


  * Traccar Server: Traccar offers both default servers and dedicated servers for hosting the tracking accounts and data. Dedicated servers offer various benefits, including customized branding, domain name, and configurations. The __ <service name> service utilizes two cloud-based dedicated servers: a "test" server and a "live" server, which normally would be configured almost identically. 



  


  * Traccar Web Interface: An open-source browser-based interface to manage Traccar accounts and details. This can be used by all users, from the Standard Driver with read-only permissions all the way up to the Master Administrator. Each user has both a Traccar account and a Silverloom account. 



  


  * Account: An account normally corresponds to a single household or business. Each account has one primary "Account Manager" and may have multiple secondary Account Managers. Each account may have one or multiple Devices linked to it. In Phase 2 and beyond, additional features, such as subscription management, invoicing, additional reporting, etc., may be added to the Account.



  


  * Account Group: An association of Accounts, based on some commonality between the Accounts, such as geographical region, church association, etc. Groups can be linked together or "nested", creating a series of "upline" and "downline" Groups. For example, there could be Account Groups such as "Weaverland Conference" (for the larger, highest "upline" Group), "Weaverland PA", "Weaverland NY", etc. An Account can be linked to only one Account Group at a time. Account Groups are overseen by Group Admin.



  


  * <Service Name> Roles: 
    * Master Administrator: 



TODO_: 

Tim Reitz 10/24/2025: Add a note somewhere that "Master Administrator" includes CCI users except when it has implications for Group Admins & Resellers, etc. 

  


  * Group Admin: An administrative role for a person who oversees an Account Group. 



  


  * Account Reseller: Normally an outside party that resells Devices / Accounts to end users, and can profit from the accounts under them. The Reseller is the main point of contact for the end users, setting up accounts and providing tech support for accounts under them. A big goal of the __ is to keep the accountability and general account management at the Account Manager & Account Reseller level whenever possible, and have less involvement by the Group Admin and Master Admin.



TODO_: All Group Admins (and maybe all (non-CCI) Master Administrators) are listed as Resellers, so this can be required and someone can be assigned as responsible for managing billing for Accounts not under a regular Reseller.

TODO_: May be an organization or an individual. 

  * Organization Resellers would have "Reps" doing the actual work. 
  * If an Individual reseller switches to a business (or hires someone else to help them), CCI might need to provide some guidance on how to make the switch from an individual to an organization.



  


  * Reseller Rep: 



TODO_: 

  


  * Account Manager: The person or people in a household or business who have permissions to manage an account. There is one "Primary Account Manager", and there can also be multiple "Secondary Account Managers", all with the same permissions to manage the Account.



  


  * Driver: 



TODO_: All

  


  * Role Uplines: 



TODO_:
