10.2. Payments

  


Requirements

Payments could be handled withing the software solution through the AppHosting Payments Module, with added customizations. This provides the following features: 

  * Receive/record check and cash payments
  * Run/record credit card payments from the software
  * Store credit card numbers on a per-customer basis
  * Allow for automatic/repeating payments on a per-customer basis
  * Be able to handle partial payments/multiple payments per invoice. 
  * Be able to batch charge customers



  


To manually collect payments, there would be a Payments section on the Main Menu that would include the following options (see more in the corresponding sections of this proposal):

  * Payments Due
  * Receive Payment



  


As mentioned elsewhere, the payment type information would be stored in the Notes fields on the Paid invoice detail such as, "Paid with card ending in xxxx", etc.

  


There should be a way to override a late fee for a customer - this would be done by deleting the Late Fee line item from the invoice detail OR by editing the Late Fee amount on the Payments Due Report.

  


Rather than having any integration with QuickBooks, there should be the reports to provide information for entering income into QuickBooks. This information would be manually entered into QuickBooks. These reports are described in their corresponding sections of this proposal.

  


Development Specification

Restrictions:

  * Full Admins: Full access
  * Publication Admins: Can only run payments for customers in their assigned publication
  * Standard Users: Can only run payments for customers in their assigned publication



  


Tim Reitz 02/08/2021: If we need to cut something, I think we could cut/hold off on the card processing and receive card payment like we do check/cash (and he could collect the payment separately until he wants to build it out). 

  


Payment integration costs - $50/mo

  


Tim Reitz 11/24/2020: From Matthias: May need work from Matthias or Josh to be included in the proposal; currently can only pay one invoice at a time; no way to charge multiple clients at a time

  


Tim Reitz 02/26/2021: We need to account for Josh/Matthias' time if further customizations are needed to build this out. 

  


Tim Reitz 02/26/2021: Ellis, how much of this will become standard? How much of the cost might be split?
