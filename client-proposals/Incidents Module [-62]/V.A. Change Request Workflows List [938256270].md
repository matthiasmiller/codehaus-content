5.1. Change Request Workflows List

  


Requirements

This is a non-editable simple list used to track Change Request workflows / statuses. It includes the following items. 

  


Note that the each item below includes the logic for setting the statuses documented on the Change Request detail screen: 

  


  * Deferred by Vendor (logic: "Vendor Approval" = "Deferred") 
  * Declined by Vendor (logic: "Vendor Approval" = "Declined")
  * Deferred by Client (logic: "Client Approval" = "Deferred", unless "Vendor Approval" is not blank or "Approved")
  * Declined by Client (logic: "Client Approval" = "Declined", unless "Vendor Approval" is not blank or "Approved")
  * Awaiting Design (logic: "Vendor Approval" is not set, or no other status matched; this is the default)
  * In Design (logic: "Design Started" is checked and "Draft Complete" is not checked; note that it should have this status even if Vendor Approval = "Approved", to allow the Vendor to approve it but send it back for final revisions) 
  * Awaiting Vendor Approval (logic: "Draft Complete" is checked and "Vendor Approval" is blank) 
  * Send to Client (logic: "Draft Complete" is checked, "Vendor Approval" = "Approved" and "Sent to Client" is not checked)
  * Awaiting Client Approval (logic: "Sent to Client" and all preceding checkboxes are checked, and "Vendor Approval" = "Approved", and "Client Approval" is blank)
  * Coding (logic: "Send to Client" and all preceding checkboxes are checked, and "Vendor Approval" and Client Approval" both = "Approved", and "Coded" is not checked)
  * Testing (logic: "Coded" and all preceding checkboxes are checked, and "Vendor Approval" and "Client Approval" both = "Approved", and "Tested" is not checked)
  * Ready to Deploy (logic: "Tested" and all preceding checkboxes are checked, and "Vendor Approval" and "Client Approval" both = "Approved", and "Deployed" is not checked)
  * Needs Billing (logic: "Deployed" is checked and "Billing Type" = blank or does not start with "No Charge" and "Billed" is not checked)
  * Needs Documentation (logic: "Client Approval" and "Vendor Approval" both = "Approved" and all checkboxes except "Documented" are checked)
  * Complete (logic: "Billing Type" = blank or does not start with "No Charge" and "Billed" is checked OR "Billing Type" = blank or does not start with "No Charge" and "Deployed" is checked)



  


This list is universal for all users.

  


Note that this sequence is static, so it should always be displayed in this sequence throughout the Solution.

  


This list will be set up by CCI as part of the main development. If changes need to be made to this list, it will require some coding work.

  


Development Specification

Internal list name: "ChangeRequestsWorkflows". 

  


  


Change Requests: 

  * Tim Reitz 12/13/2024: [[[IN10311](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10313&)]] - CORE - Change Requests - Improvements for Managing Projects 
  * Tim Reitz 02/05/2025: [[[IN10972](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10974&)]] - CORE - Change Requests - Update CR Status Macro Logic to Fix "Awaiting Design" Status


