2.1. Glossary

  


Requirements

*Done. 

  


Overview: The purpose of this glossary is to provide a description of key terms, roles, and other things referred to in this proposal. These are listed below:

  


  * Device: A generic term for the on-board device or app that is used for tracking:  
    * OBD-II (sometimes shorted to OBD): An "on-board device" that plugs into a vehicle to track it. It pulls data from the vehicle and GPS, then reports it back to a central location. It's used to capture error codes, fuel level, driving behavior, location, etc.
    * Traccar Client App: A basic open-source app that installs on a phone to track and report information to the Traccar server. This app is available for both Android and iOS - see [https://www.traccar.org/client/](https://www.traccar.org/client/). 



  


  * Traccar: An open-source software that manages data from on-board devices. See [https://www.traccar.org/](https://www.traccar.org/) for details. 



  


  * Traccar Services: 
    * Traccar Manager App: An open-source app that app mirrors the Traccar Web Interface in a mobile app. It is available for both Android and iOS: [https://www.traccar.org/manager/](https://www.traccar.org/manager/). 



  


  * Traccar Server: Traccar offers both default servers and dedicated servers for hosting the tracking accounts and data. Dedicated servers offer various benefits, including customized branding, domain name, and configurations. The <Service Name> service utilizes two cloud-based dedicated servers: a "test" server and a "live" server, which normally would be configured almost identically. 



  


  * Traccar Web Interface: An open-source browser-based interface to manage Traccar accounts and details. This can be used by all users, from the Standard Driver with read-only permissions all the way up to the Master Administrator. Each user has both a Traccar account and a Silverloom account. 



  


  * Account: An account normally corresponds to a single household or business. Each account has one primary "Account Manager" and may have multiple secondary Account Managers. Each account may have one or multiple Devices linked to it. In Phase 2 and beyond, additional features, such as subscription management, invoicing, additional reporting, etc., may be added to the Account.



  


  * Account Group: An association of Accounts, based on some commonality between the Accounts, such as geographical region, church association, etc. Groups can be linked together or "nested", creating a series of "upline" and "downline" Groups. 



For example, there could be Account Groups such as: 

  * "Weaverland Conference" (for the larger, top "upline" Group), 
    * "Weaverland PA", 
    * "Weaverland NY", 
    * etc. 



An Account can be linked to only one Account Group at a time. Account Groups are overseen by Group Admin.

  


  * <Service Name> Roles: 
    * Master Administrator: An administrative role for a user who has access to the entire Solution, via a "Full Access" permission. Note that this includes CodeCrafters support users (User IDs with a "CCI_" prefix) with regards to system access, but not with regard for <Service Name> roles and notifications.



  


  * Group Admin: An administrative role for a person who oversees an Account Group. Note that all non-"CCI_" Master Administrators can function as Group Admins.



  


  * Account Reseller: An individual or organization that resells Devices / Accounts to end users and can profit from the accounts under them. The Reseller is the main point of contact for the end users, setting up accounts and providing the main support for accounts and end users under them. A big goal is to keep the accountability and general account management at the Account Manager & Account Reseller level whenever possible, and have less involvement by the Group Admin and Master Admin. Note that all non-"CCI_" Master Administrators can function as Resellers. Also note that if an Individual reseller switches to a business (or hires someone else to help them), CodeCrafters might need to provide some guidance on how to make the switch within the Solution from an individual to an organization.



  


  * Reseller Rep: An individual who works for or operates under an organization Account Reseller



  


  * Account Manager: The person or people in a household or business who have permissions to manage an Account. There is one required "Primary Account Manager", and there can also be multiple "Secondary Account Managers", all with the same permissions to manage the Account.



  


  * Driver: An individual linked to an Account as a Driver, usually to be set as the "Primary Driver" on a Vehicle. Any individual Contact in the Solution can be a Driver.



  


  * Role Uplines: See the "Role Uplines" section of this design document for details.



  


Development Specification

TODO_NM (review) / TODO_T/J: Tim Reitz 01/29/2026: Let me know if there are other items that you would like me to add to the glossary.
