7.9. User Profile Record

  


Requirements

_EM: Tim Reitz 12/10/2025: We need to think through how logins / User Profiles should work:

[ ] Login setup:

[ ] Silverloom access (providers & support users): Standard, User Profiles, UN & PW format

[ ] Traccar account access (all users):

_EM: Tim Reitz 12/10/2025: Thoughts on setting it up for providers and support users to have the same login credentials for both Silverloom & Traccar?

Tim Reitz 12/11/2025: Talk to Jonathan about our capabilities here, then Ellis will talk with Josh. 

TODO_JB (research): Tim Reitz 01/16/2026: For users who have access to both Silverloom and Traccar, it would seem handy to have the same UN + PW for both. 

Username seems easy, as Traccar uses the email address, and Silverloom has the capability to use it too. 

Password could be managed manually by the user, but do you have any thoughts on how we could sync over the password from the Silverloom User Profile to the corresponding user's Traccar account? There would be the challenge of this getting out of sync — the user could always hit the Reset Password link in Traccar and get mismatching passwords (presumably until the next time the sync runs and updates Traccar to match Silverloom again). If this isn't simple, I think we'd defer it, so it's not worth a lot of time at this point. 

  


[ ] <Service Name> portal access (all users): One-time login via a login link that the user requests. User ID for these sessions is the "Traccar Login Email" associated with the Account.

  


[ ] Data Access:

[ ] For Master Administrators & Support users, it's easy - can view and edit all.

[ ] For Group Admins and Resellers / Reseller Reps:

[ ] What should they be able to view / edit for each other?

_GZ: Tim Reitz 12/10/2025: Do you want them to be able to help each other with their logins?

TODO_VA: Tim Reitz 12/11/2025: Resellers can only be set up by Full Access users. There needs to be a reseller agreement between the Service and the reseller. 

TODO_VA: Tim Reitz 12/11/2025: Reseller Reps ideally could be be managed by the main Reseller user (could add/remove rows from the Reps RG). 

_NM: Tim Reitz 01/15/2026: Thoughts on this? 

TODO_VA: Tim Reitz 01/15/2026: Defer as a possible future item. Would be a lot of work, because we don't want non-Full Access users to be able to be able to edit the full User Profile record (don't want them to set other people as Master Administrators, etc.), so it would be a lot of work to narrow the editability permissions. 

We could consider adding an x30 that runs as another user, but let's defer that for now. 

TODO_GZ: Tim Reitz 01/15/2026: We don't currently allow for partial permissions for setting up or editing User Profiles / logins. So for now requests will need to go through Master Administrators. 

TODO_GZ: Tim Reitz 01/15/2026: We could give various approaches for a Primary Reseller Rep or Primary Group Admin to request a new user: 

  * MailTo draft with lines for the necessary fields
  * Request submission -- prompts for the necessary fields, sends a notification to the Master Administrators, who can open a report to view the request and click a button to set up the User Profile. 
    * Technical notes: 
      * RG (hidden?) on the Contact record of the person making the request, with all of the fields as columns + "Request Date" \+ "Approved" (list of Approved / Denied / blank) + "Approved By"; 
      * Report Alert for Master Administrators 
      * Report would show all blank & denied; 
      * Button on the report would run an x30list to set up the User Profiles and set the fields on the RG. 
      * Nic is thinking this could be $1K-2K (don't necessarily share with client) 



TODO_VA: Tim Reitz 12/11/2025: New Group Admins for existing or downline Groups can be managed by existing Group Admins (adding/removing rows on the RGs).

TODO_VA: Tim Reitz 01/15/2026: same as above) 

_VA: Tim Reitz 12/11/2025: Add a new report for "User Profiles by Reseller" (and maybe "User Profiles by Group), so that Glen can determine if/how to pass along user costs. 

Tim Reitz 01/15/2026: Adding spec. 

[X] What should they be able to view / edit for their own clients?

Tim Reitz 12/10/2025: They need to be able to set up their own clients, change email, maybe reset password, etc.

Tim Reitz 01/15/2026: Not relevant anymore because end users are not in Silverloom. 

[ ] What should they be able to view / edit for clients of others? [Traccar login, not Silverloom User Profile] 

_GZ: Tim Reitz 12/10/2025: Do you want them to be able to help clients of others with their logins?

TODO_VA: Tim Reitz 12/11/2025: Limited. Only the Reseller for the Account should be able to change the email address for logging into Traccar. 

TODO_VA: Tim Reitz 12/11/2025: I'm wondering if the Traccar login details ("Traccar User Record") need to live on the Account record (maybe on the RG), so that a Contact can have login access to multiple Traccar accounts under different Resellers. 

[ ] Note from 10/31/25: Per Ellis, Josh was not scared about adding record-level restrictions to the User Profile records. This would allow us to restrict the User Profile records so that users don't change the URL to see other records.

_EM: Tim Reitz 12/10/2025: Maybe this record level restriction would even be a standard feature to add?

TODO_VA: Tim Reitz 01/20/2026: If not needed for Phase 1, Elis isn't inclined to add it now.

  


Development Specification

Mockup: N/A
