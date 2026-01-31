1\. Simplified Overview

  


Requirements

Faith Builders is a scholarship organization for a scholarship tax credit program in the state of Pennsylvania. They are currently using AppHosting to manage these funds.

  


The state of Pennsylvania allows Special Purpose Entities (SPEs), which are LLCs dedicated to receiving EITC contributions from individuals as well as businesses. The SPE is comprised of members, which can be individuals or businesses. The SPE applies for tax credits from the state just like any other Pennsylvania business, and the associated tax credits received by the SPE are then passed through to the members.

  


Faith Builders currently has five SPEs. They are currently using an Excel spreadsheet to manage the details. However, they are looking to create a solution to manage these SPEs, member applications, contributions, and distributions.

  


They will manage accounting in QuickBooks, but the solution will include reports to help reconcile between the two systems.

  


This proposal includes an overview of the organizational workflow (Simplified Storyline) and the software requirements (following that).

  


Development Specification

Timeline of SPE Applications, Approvals, and Associated Tax Credit Years:  [[  File:Flow chart example.pdf]]

  


  


  


Tim Reitz 10/28/2020: 

Timeline

  * Needs to be ready to deploy no later than September 1, 2021
  * Sept. 1 - Jan. 31 - we would not want to do integration of new software
  * We have to be able to move everything over to the new system by Sept. 1
  * We are at a growth stage
  * From my perspective, it feels crucial that if we move forward, that we could have this live Sept. 2021
  * If not able to hit the Sept. 1 deadline, then we'd wait until Feb. 1 to start the design phase
  * If you feel that we can, we're ready to jump into the design as soon as Matthias is ready



  


Availability

  * Available through 22nd
  * Available again 2nd week of Jan



  


Tim Reitz 01/25/2021: Is there any restricted data on this system? 

Mindy - you can update the Data Restrictions Notes tab on the mockups as needed, and let me know if you have questions.

Matthias Miller 01/29/2021: No data restrictions.

  


Matthias Miller 02/23/2021: Negotiations from Proposal:

  


In reviewing the various components, Glen and I are thinking that with a few tweaks to existing reports and one new Contacts report, most of the email communication could be done with our templates and mail merges from Excel exports of those reports.  There are a few, however, that don’t seem obviously easy to convert to mail merge format, specifically any that include member school designations and amounts.  For the mail merge to work, each record (row) in Excel has to include all information, and I’m not “seeing” a report that could do that without special behind-the-scenes work on your part.  Currently, I use Excel’s concatenate feature to combine two fields to be able to email using mail merge.  Maybe you’ll look at this and say, “That was easy!”  Here are the emails that would be affected:

  * The Communication to Schools email (pp. 37-38)
    * This includes all contributors to that school and 95% amounts for a particular school for a particular SPE disbursement.
  * Two member email communications that list school designations and (100%) amounts contributed to each:
    * Receipt of Member Application (pp. 25-26)
    * Receipt of Payment (pp. 33-34)



 

The other piece of that Communications package we would still need is the automatic PDF creation of pre-filled Joinder Agreement renewal applications.

 

If it’s not possible to create a report that makes mail merge possible, we would need these three emails possible from within the program somehow.  The main question with this is whether it’s fair to ask for a reduced price if we reduce what we’re asking from you, or whether the developers still need to do primarily the same amount of work.  We’re not trying to say your work is not worth what you’re asking, but we are trying to be responsible with the resources we have and are finding it hard to justify spending $27,000 for this feature.

 

Please let me know if you have other input or if it would be better to talk than try to explain in writing.

  


Ellis -

The kind of report that you can use to drive a mail merge is quite possible and we'd be happy to work with you on that. We'd have to work out what that would take, but it would be much smaller.

  


There are also ways to significantly simplify the Communications package. There are three things that make it more expensive:

  * Ability for FB to easily modify the template contents without a system update.
  * Integration with the Reminders package.
  * Adding platform support for attaching the redacted tax return PDF's to emails. This sounds relatively simple, but we need to do a fair bit of coding in order to be able to attach archived documents to emails. 



  


Just these three account for more than half of the Communications package. I'm sending Matthias some ideas I had on some for simpler options. He can explore with you whether some form of these would be a good fit or whether simply the reports for the mail merge are the best option right now.

  


In the past two weeks, I spent multiple hours going through Matthias's detailed spec with Nahian, our Solutions team lead, as we were working to come up with an estimate for each of the individual pieces. We tried to break out the substantial pieces that could be deferred.

  


I've just now reviewed the core system again. I don't see additional significant discretionary pieces that can be broken out or deferred.  The good news is that even if we go with a simple core system, we know the possibilities for additional automation or systemization in the future! :-)

  


Matthias will be reaching out to you on your various questions as well as finding the right solution for you for the email communications.

  


Lucy-

Matthias/Ellis,

I was planning to mention the option of holding a few things for possible later development even if we decide not to go with them now.  We still need to talk to Steven, who is out of town this week, but the direction we are thinking right now is to go with the core package and the online application platform, with modifications to the communications package.

  * The PDF splitting can easily be done with our FoxIt Phantom Pro (with some extra time for naming the split files), and the redaction process sounds messy for ongoing purposes.
  * We have other reminder options that make this part of the cost seem unwise, although it would have been nice.  Ellis’s comment about that being a complicating factor in the communications package confirms this direction.
  * We are going with a shared email internally that will be searchable.  IT has worked out the bugs that plagued Vivian with the scholarship emails.



Both of Matthias’s suggestions sound like good options. 

  * Glen and I will try to solidify the report modifications we would find helpful and get them to you.  We may have some questions that would be good to have ready for discussion next week.
  * The first part of next week looks very flexible to me.  I’ll let Glen speak regarding his schedule.



  


Matthias,

After receiving a brief response from Steven that he would like to discuss reasons for anything we cut from the proposal after he returns Monday, I am suggesting that we hold off on the specifics of the reports needed to do mail merge.  I would like to discuss Ellis’s proposals to simplify (and the associated cost savings with that simplification) at your earliest convenience next week.  I’m also fairly certain that we would still eliminate at least the creation of the redacted PDF’s and the Shared Inbox.

 

Here are a few items besides the emailing issues:

  * PP. 40-41 – Auto-Create Member Applications
    * We had planned that the PDF generated would have these characteristics:
      * Leave contribution amount is blank (cover letter mentions current contribution amount).
      * List schools currently designated but with a % of total for each one rather than a $ amount.
      * Matthias Miller 02/23/2021: This would be handled by the PDF generation. It's simplest to copy it over, but we can also leave it balnk if it really is better
    * Payment due date should be updated to September 1 (not 15) for year 1 of 2 renewals.
  * PP. 41-43 – Online Member Application
    * Second paragraph (p. 41) should say “Prefilled renewal applications will be created as PDFs to print and send by mail.”)
    * Contact Name for businesses should include a preferred name (Nickname) for email communications from us (see detail on individuals).
    * For both businesses and individuals, the Anonymous field should be a checkbox with the following text (I’m thinking it would be good to clarify to whom they are anonymous):
      * Check here if you want your contribution to be anonymous to the school(s) you designate.
    * For individuals, I think the following prompts would be good:
      * First Name: Legal name for tax documents
      * Middle Name or Initial: For tax documents
      * Preferred Name [We’d like to use this term rather than “Nickname”]: For email communication from us and contribution info sent to schools (if not anonymous).  If left blank, we will use first name.
    * The first checkbox on the agreement conditions could eliminate the last sentence about check options because of the payment instructions given at the end.
    * The second checkbox should have the last sentence reworded as follows:
      * In any case, the signer is responsible to arrange for the same amount to be paid for the following year.



  


Matthias Miller 02/23/2021: 

  * Looking at a way to simplify communicatios...



  


Base System

Email & Print Communications Package

NO Reminders

No PDFs

\+ Online Member Application

NO Shared Inbox
