1\. Overview

  


Requirements

This proposal is for adding the Event Management Module to the Symbiz Members Exchange and CRM Solution. 

  


The Event Management feature as specced out in this proposal is a large and versatile feature that allows Symbiz to schedule various types of events, manage registrations for the events, track various details, and send notifications to registrants. There are many changes that could be done in the future to enhance this feature. 

  


History of the Events feature: 

  * In Phase 1, the General Meetings feature was included, with very basic capabilities for general meetings and Industry-specific meetings. 
  * The original design & development plan had Info Meetings coming in Phase 2 or 3, but with the transition away from Salesforce, Symbiz & CodeCrafters realized that a feature to manage Info Meetings was necessary sooner. 
  * In the design process for Info Meetings, it became apparent that the Solution would also need to handle Launch Meetings. 
  * Symbiz also asked to add registration tracking to the Summit ("General") meetings, and to add some basic tracking for the pre-Summit event. 
  * CodeCrafters realized that the Solution would be tracking multiple different meetings, with lots of commonalities. 
  * CodeCrafters decided to merge them all together under the "General Meeting" record type, with various categories for the different types. 
  * As the design progressed and the overall feature grew, it became apparent that it had grown beyond the existing General Meeting feature into a new feature or module, which is now called the "Events" feature, which completely replaces the existing General Meeting feature.



  


Development Specification

This was initially going to be a Phase 2 item, but the client requested that it be bumped to Phase 1. Design was started in [[[IN9119](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9121&)]] - ZSB - Info Meeting Feature but as it grew, we decided to move it to this proposal. Note this also includes the changes requested in [[[IN9097](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9099&)]] - ZSB - General Meeting - Misc changes.

  


  


Tim Reitz 06/26/2024: Pricing notes from Ellis today (via Signal): 

I'm estimating 18-22K (after 20%) discount for the event feature. If they want to move forward with it, we could do 6K downpayment and 6K / month for 2-3 additional months. If you want a wider range, then we could say 16-24, but I think the narrower range is fine.

  


I think it's unlikely that we'll get it down to 16.

  


But perhaps possible if everything goes really well. You can tell him that this is 15K words compared to the orig proposal of 45K. So it is a huge subsystem.

  


[X] _VA: Tim Reitz 07/01/2024: Prepare mockups PDF. 

Tim Reitz 07/02/2024: Printouts done this morning. Only need: 

[X] Contact record

[X] Event record

[X] Registration record

  


Tim Reitz 07/01/2024: Email draft: 

Subject: Events Management Module - Design Summary & Proposal

Body: 

Hello Jeremy, Matt, and the rest of the Symbiz team,

  


Attached please find the proposal for the Events Management module for the Symbiz Members Exchange & CRM, along with mockups for the main screens and printouts. 

  


As we've mentioned as design for this feature progressed, this has turned out to be a much larger feature than anticipated. Our T&M estimate for this as designed is $18,000-$22,000, after the 20% partnership discount. 

  


Adding features also increases the support & maintenance workload, so the cost of the annual maintenance contract would also be increasing by $2,000/year (approximately 10% of the cost of this module). 

  


A few notes on the size and price, anticipated project time-line, and a note about payment format: 

  * For context, by the word counts this feature is more than 1/3 the size of the original system (more than 15K words for the Events Management design compared to approximately 44K words for the Phase 1 proposal), so this is a very large and powerful subsystem, much more than just a feature enhancement or regular change request. As such, this could be considered Phase 2 of the project.



  


  * If things go very well, it is possible that the final price would be less that the lower end of the estimate ($18K) and we would be happy if we could give it to you for less than that. 



  


  * If accepted soon, we would aim for completion and deployment by the end of August, but ideally we would have it done even sooner than that. The development team is prepared to prioritize coding for this project in the month of July, and testing would be projected to start in early to mid-August. 



  


  * If you would like to move forward with this, Ellis is proposing the following payment arrangements. Note that this is different from our standard payment arrangements for change requests (where we bill the month after the feature is deployed), and instead is more in line with our standard procedure for new systems and phases. We can discuss details regarding monthly due date, etc., but the general idea is as follows: 
    * $6,000 down payment to start coding the feature. 
    * $6,000 per month for the next 2 - 4 months (depending on total cost).
    * Remainder of the balance in the final month.



  


A few more notes about the design: 

  * The PDF copies of the mockups are representations of what the final screens should look like, they are not exact (the written proposal is the source of truth for the feature design).



  


  * Please review the design and mockups and let us know if you have any questions or things you would like to discuss further, or how you would like to proceed. Also, now is a good time to request minor changes to layout of things on the mockups, if you notice things that you would like adjusted.  



  


  * If you have any interest in reducing scope by simplifying or removing any features to help reduce the cost, we are happy to have that discussion. However, we will note that we don't see any individual items that would significantly reduce the cost by being removed without reducing the effectiveness of the module. 



  


  


Please be in touch with any questions, and we would be glad to schedule a call to discuss any of this. 

  


Thanks! 

The CodeCrafters design team
