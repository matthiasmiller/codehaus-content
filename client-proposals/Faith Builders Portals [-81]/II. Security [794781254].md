2\. Security

  


Requirements

User Authentication:

The specifics vary between portals, but the general solution is to validate users based on the Contact records related to their relationship with the system. For example, the email address listed on a Family-type Contact record would be used to validate that the user requesting access to the Family Portal should indeed have access.

  


General Authentication Flow:

  * Pre-authenticated:
    * User selects the desired portal on fbep.org
    * User enters their email
      * If the entered email address is linked to more than one Contact record, the multiple Contact names will be displayed as options.



Jonathan Bergen 10/30/2024: I don't want to do this anymore. We should limit each email to one portal.

  * One-time login link is sent to the email address entered


  * Authenticated:
    * Clicking the link in the email leads to the portal, with the HMAC key and Contact record ID stored in the Flask session data.



  


Database Security and Activity Monitering:

  * All DB actions will be executed by a dedicated Silverloom User, allowing for easy Audit Trail tracking in the case of damaged records.
    * A regular scheduled task will be created to send a summary of portal activity to the Database admin. (Justin for now)



  


Uploaded Document Security:

  * Users will upload sensitive documents that need to be retained indefinitely. This includes tax returns, earnings reports, and paystubs.
  * These documents will be stored in a AWS S3 bucket and will be linked to the portal.
    * This solution avoids the vulnerability that would be introduced by having documents stored in the database and preserved in backups.
    * The documents will be double-encrypted. (through AWS standard encryption as well as Silverloom encryption)



  


Added Silverloom Permissions:

  * "view S3 documents."
    * This permission controls the visibility for the links that lead to the uploaded documents.
    * This permission would be linked to the Administrator group



  


Development Specification

Added permissions:

  * "view S3 documents."
    * This permission controls the visibility for the links that lead to the uploaded documents.
    * TODO_ this permission would be linked to the Administrator group



  


Added activity monitoring:

  * Add a user named "portal worker" to perform all actions interfacing the portal and Silverloom.
    * Add a report to show all activity done by the portal worker in the last week.
    * Add a email that gets sent to justin every week with the results of this report.



  


Jonathan Bergen 02/17/2025: TODO_JK: Do you want a checkbox on the Related Contacts RG for portal access?
