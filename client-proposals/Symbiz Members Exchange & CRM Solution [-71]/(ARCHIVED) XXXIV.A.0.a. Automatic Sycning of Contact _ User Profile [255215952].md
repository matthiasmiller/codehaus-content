34.0.0.1. Automatic Sycning of Contact / User Profile

_IDD: Tim Reitz 06/14/2023:  This was down below "Possible Future Enhancements", but I think it's included in the membership handling that we've specced out for Phase 1. We should confirm. And if it is already included we should archive it. 

Tim Reitz 06/15/2023: Reviewed the spec Membership Details and confirmed that these are covered there. 

  


  


Think through keeping email addresses & username in sync (create, modify, deactivate)

Tim Reitz 04/06/2023: Activate/deactivate user accounts based on the membership dates on the Contact record -- is this something we want to do?

  * If the user profile is not set on the contact record,
  * x30 list:
    * #1: Create or update user profiles: 
      * Level: User profiles
      * Input: All members (active & inactive) and all Contacts with a User profile (active & inactive)
      * Match on: user profile if set on contact; otherwise primary email address
      * Set: First Name, Middle Name, Last Name, Email, User Group, Account Disabled
    * #2: Assign new user profiles to contact
      * Level: Contacts (member-type only)
      * Match on: primary email address
      * Set: User profile (if blank)


