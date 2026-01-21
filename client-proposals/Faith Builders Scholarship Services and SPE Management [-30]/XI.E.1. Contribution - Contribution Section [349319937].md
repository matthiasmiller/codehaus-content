11.5.1. Contribution - Contribution Section

  


Requirements

Contribution section:

  * Business (drop-list of active businesses; required)
  * Anonymous (checkbox; uneditable; value of Anonymous Donor field in the Contacts Details section of the selected business)
  * Amount (number; two decimals)
  * Date Entered (date; required; defaults to the current date)
  * Application Year (number; required)
  * Business Application (drop-list of business applications for the selected business; required if the list is not empty)
  * SPE Application (visible if the selected Business Application is entered in the SPE's Business Application field on an SPE Application record; link to the SPE Application)
  * Type (drop-list of "Pre-K", "K-12", "OSTC", and "Non-EITC")
  * Receipt to DCED Sent by FBSS (checkbox)
  * Reviewed (checkbox; defaults to unchecked; editable for users with the "Review contribution" permission)
  * Contribution Receipt Printed (hidden date field; auto-set when the Contribution Receipt is printed)



  


Validation:

  * Error on save: if Amount is not equal to the sum of the Gross Amount column in the Schools RG.
    * Error Message: "The contribution amount must equal the total of the school gross amounts. (Field: Amount)"
  * Warning on save: if Amount does not match the Amount from the linked Business Application.
    * Warning Message: "The application amount does not match the contribution amount. The application amount is <BusAppAmount>, but the contribution amount is <ContributionAmount>. (Field: Amount)"
  * Warning on save: if Type is not "Non-EITC", there is a business application for the selected business and year, and Type does not match the business application type.
    * Warning Message: "The contribution is "<ContributionType>" but the business application is "<BusAppType>". (Field: Type)"



  


Additional Behaviors:

  * When Business is changed:
    * Business Application is set to the appropriate application for the business and year, if such an application exists.
    * Type is set to the value of the Type field from the Business Application.
  * When Postmarked Date is changed: School Year is set to the latest default school year from AppHosting settings for which the Effective As Of date is before the new Postmarked Date.
  * When School Year is changed in the Contribution section: School Year is updated for all rows in the Schools RG.
  * When Business Application is changed: Type is set to the value of the Type field on the business application.



  


Development Specification

TODO_NM: 

  * If we make DollarToDisplayString available for XFB, use in the validation on ContributionAmount.
  * Use an Assign statement for BusinessApplicationField( ContributionBusApp, BusAppType) in validation on ContributionType.



  


Change Requests: 

  * Tim Reitz 09/05/2024: [[[IN8625](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8627&)]] - XFB - FBSS - Misc Items for 2023/2024
  * Ben Reitz 06/24/2025: [[[IN10717](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10719&)]] - XFB - Communications - Add New "Notification of Payment Received" Email Template


