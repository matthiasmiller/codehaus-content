1.4. Design & Development Phases

The full Solution is anticipated to be deployed in multiple phases, as described below. 

  


Phase 1: Initial database and integration with Traccar: This is the phase that is covered by this design proposal. This focus of this first phase is getting the main features designed and coded, to have a functional product available for a "live test" phase, in which <Service Name> users can familiarize themselves and work out additional details before going fully live for end users.

  


This phase lays the groundwork for use and further expansion with the following integrated approach of three main software tools:

  


A. <Service Name> Silverloom software : A web application on the Silverloom Business Suite, by CodeCrafters, that serves as the "back-end" database for providers (Resellers, Group Admins, and Master Administrators). This stores & tracks information for accounts, account groups, contacts (account managers, drivers, etc.), devices, vehicles, and various data points from Traccar.

Core functionality for the Silverloom software include the following:

  * Database to store and manage data for the following:
    * Account Groups
    * Accounts
    * Contacts (end users, providers, and other contacts) 
    * Devices (both OBD "dongles" and Traccar Client app information)
    * Vehicles
  * Web interface for providers to view and manage the data, with various roles & permissioning levels for different users. 
  * Reporting on the various data types above. 
  * Integration with Traccar for data syncing.
  * Various outbound emails related to the data managed in Silverloom, such as:
    * Welcome emails for new Account members, with instructions for accessing Traccar and the Portal
    * Notifications about changes to Account Groups and Accounts
    * etc.
  * Notifications for users and accountability partners about vehicle health and driving events, including high-risk activity. 



TODO_: Tim Reitz 11/14/2025: This actually would be done directly from Traccar, I think

In Phase 1, only provider users have direct access into this software.

  


B. Traccar: The service and interface is provided by Tananaev Solutions. The <Service Name> Silverloom software integrates with Traccar via API. A Traccar server connects with devices installed on vehicles or on mobile devices, then data tracked by Devices is sent directly to and stored in the Traccar server, and then is passed on to the <Service Name> Silverloom software as needed.

Users (both providers and end users) can also install the Traccar Manager mobile app or access the Traccar Web Interface to view Traccar-specific data.

In Phase 1, all users (both providers and end users) have access to Traccar via the Traccar Web Interface and the Traccar mobile apps. This access is based on a "Traccar Login Email" and permission controls specified in Silverloom.

  


  


C. <Service Name> End User Portal: This is a special software tool built & supported by CodeCrafters, to link Silverloom and Traccar, and to end users (account managers and drivers) a portal to view their account details from Silverloom. End users can log in via one-time links, view details, agree to the <Service Name> End User Agreement, and contact their service providers with various requests via email.

In Phase 1, the Portal is mainly used only by end users (as providers have access to Silverloom directly).

  


  


Phase 2: Additional Features & Enhancements: 

  * Subscription Management feature: 
    * Subscription activation/deactivation/pausing 
    * Invoicing 
    * Etc. 
  * End User Portal: 
    * Possible enhancements, such as the ability for users to make payments toward their account. 
  * Additional changes as needed, based on <Service Name> "live test" use. 
  * Other possible future items. 



  


  


  


Phase 3 / Future: Integration with insurance software: Long-term, integration could be considered with insurance software, such as Weaverland's self-insured vehicle management software.

  


For example, driving data could be synced across from <Service Name> to the WMVAP Solution for all participating vehicles, incentivizing app usage by offering a teen driver / safe driver discount by installing the app.
