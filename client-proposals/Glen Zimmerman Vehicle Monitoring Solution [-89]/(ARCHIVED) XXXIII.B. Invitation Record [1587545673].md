33.2. Invitation Record

  


Requirements

_VA: Ben Reitz 07/22/2025: Would it make more sense to have this sent as an email and/or text from the Account record, rather than have its own record?

Tim Reitz 08/14/2025: Good question. Maybe! I'm curious 

_EM.: Tim Reitz 09/11/2025: Thoughts on why this was specced to be a record in the HLD? 

Tim Reitz 10/31/2025: I'm not sure if this is still relevant, since we're not doing our own mobile interface. And maybe not having the end users in Silverloom at all. 

_VA: Tim Reitz 10/31/2025: Ellis doesn't remember the details. Matthias or Ben might have more context. 

**Tim Reitz 12/10/2025: I was about to ask Matthias and Ben, but then did a search for "invitation", and found a clue in the "Mobile Support (App)" section: The idea is to use the Invitation record to track / provide access to new users who are invited to the Service / an Account. 

I'm not sure if we'll do it the same way or not. 

_NM: Tim Reitz 01/15/2026: Thoughts on whether we should do an Invitation record, or just rely on the Welcome Email? 

_VA: Tim Reitz 01/15/2026: Nic doesn't think we need an Invitation record.

We're not giving end users access to Silverloom at this point, and the Welcome email would have what is needed for Traccar and the portal.

Tim Reitz 01/15/2026: Archiving this section today. 

  


  


_GZ: Tim Reitz 08/14/2025: How do you envision the invitation process working?

_: Tim Reitz 08/14/2025: At a high level, would be an email or text with a link to follow to set up the Traccar / Silverloom accounts... Does this need to be 2 separate invites, one for each interface? Or can we do a shared account? 

  


_: Tim Reitz 08/21/2025:

[ ] We need to spec out the user invitation process.

_GZ: Tim Reitz 08/21/2025: How do you envision this looking? (Silverloom & Traccar access) 

_: Tim Reitz 08/28/2025: There should be some sort of email with link(s) for the person to access their account(s) easily and get started on setup. 

Tim Reitz 01/15/2026: This might be covered with the Welcome Email...

There would be certain information required to actually activate the account: 

[ ] Required contact details 

[ ] Account holder logged in 

[ ] Initial payment received? 

[ ] Login activation

  


_: Tim Reitz 07/23/2025: Note from HLD: NOTE: Drivers can only be added by an invite basis (i.e. send an invite by email and the driver opts in). This allows individuals to have multiple rules with the same account, without disclosing their account to another party without prior permission.

\-------------

  


This would be used to track invitations:

  


  * ID (automatic & read-only)
  * Code (automatic & read-only)
  * Date (automatic & read-only)
  * Time (automatic & read-only)
  * Contact (required; list of contacts)
  * Type; list of Reseller, Group, or Account
  * Phone Number (required)



  


Development Specification

Mockup:
