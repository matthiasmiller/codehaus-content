19.4. Outlook Integration / Outbound Emails

  


Requirements

_VA: Tim Reitz 05/19/2025: To archive. Per Ellis, let's use mailto. 

  


  


  


: Tim Reitz 01/03/2025: What to spec out here? 

Tim Reitz 01/29/2025: Per HLD call, the client likes to be able to view & edit the email before sending it out. Fine with doing it either in Silverloom or in Outlook. 

He likes the way that Quickbooks does invoice emailing -- option to send email from the software, opens an email draft in Outlook with the PDF attached + body template filled in. 

Tim Reitz 03/18/2025: Let's settle on this -- see Dev Spec notes. 

  


EM: Tim Reitz 04/22/2025: Approximate / wild ballpark costs for each of these?  Ellis Miller 05/06/2025: _VA: Recommend mailto. That's cheap.

  


We have the following options for Outlook integration:

  


  * The simplest is changing the attachments to be links, and simply embedding the link into the email contents.



  


  * We may be able to provide an application to install that would allow you click a link to open a draft email in Outlook.



  


  * We can provide the ability to send emails within the software, providing limited editability of the recipient and the message contents.



  


  * We can provide the ability to send emails within the software, with full editability of the email and contents.



  


The specifics will be determined in the in-depth design.

  


Development Specification

_EM:

  * For the Outlook integration:
    * Requires Negotiation with Josh - Add a system switch for "Allowed Redirect Protocol Handlers". Just like mailto and tel, these would be embedded directly as links and would not pass through the /Redirect entrypoint
    * Create a Python executable that registers the "silverloom-outlook" protocol handler like "silverlook-outlook:ProposalID" (or something similar). It would run a JSON report to pull the to, subject, attachment, and body (using RichTextTOHTML)
    * Note that the Python executable would need to have authentication information
    * This would then use COM to launch a new draft (ask ChatGPT to write the basic code)
  * For sending emails, I would simply prompt for the first line in the outbound email



Tim Reitz 02/04/2025: Ellis is planning to discuss this with Josh. It would require an additional software tool be to set up on each computer that would send Proposals. It's another piece that can break.

Tim Reitz 02/19/2025: Josh talked with Ellis. The above approach could work, but it's not what we specialize in. Also, it would only work on the computers that the tool is installed on (would not work on a tablet, etc.). 

_AF.: Let's find out what their goal / ideal is for outbound emails, and then figure out how we can help work toward that goal. 

_EM: Tim Reitz 05/02/2025: Client likes the way Quickbooks does it. They like having the email in his Outlook Sent folder. They also want to be able to edit the email before sending (text, attachments). 

[ ] As of today, clients are fine with the approach that we use for Send Email in Incidents, with a link to the Proposal Printout PDF. Then they could manually download and attach a PDF copy if desired. 

[ ] Confirm that we can do default TO email(s) and body text with the MailTo links approach 

Ellis Miller 05/06/2025: _VA: 

Tim Reitz 02/19/2025: We could use the approach that we're using for GW (or the approach that we initially planned for for GW). 

We can also set the BCC to go to the user, and the Reply To as well.
