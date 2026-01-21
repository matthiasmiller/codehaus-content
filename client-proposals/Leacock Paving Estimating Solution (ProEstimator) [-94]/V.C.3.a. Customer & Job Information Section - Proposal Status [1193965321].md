5.3.3.1. Customer & Job Information Section - Proposal Status

  


Requirements

  * Proposal Status (no label; read-only macro; located in the section header; displays the current Status item from the "Proposal Statuses" List, in the following format: "Status: <Proposal Status item>"; based on the logic specified below: 
    * "Lead Received" (Logic: If none of the other conditions apply; this is the initial Status for new Proposals; note that Proposals with this Status are not included in sales reporting)
    * "Appointment Scheduled" (Logic: If "Appointment Date" is not blank and is on or after the current date and if none of the other status logic conditions apply; note that Proposals with this Status are not included in sales reporting)
    * "Appointment Date Past" (Logic: If "Appointment Date" is not blank and is before the current date and none of the other status logic conditions apply; note that Proposals with this Status are not included in sales reporting)
    * "Estimating in Progress" (Logic: If any rows are present in the "Sections" embedded spreadsheet and "Ready to Send to Customer checkbox is not checked; note that Proposals with this Status are not included in sales reporting) 
    * "Ready to Send" (Logic: If "Ready to Send to Customer" is checked and "Sent to Customer" checkbox is not checked; note that Proposals with this Status are not included in sales reporting) 
    * "Follow-Up Needed" (Logic: If "Sent to Customer" checkbox is checked and "Proposal Result" = blank; note that this is the default status until both the "Initial" and "Secondary" follow-ups are marked as complete, unless a "Proposal Result" is specified sooner; also note that "Proposal Result" is required if both follow-ups are complete, which moves the Status to one of the following) 
    * "Pending" (Logic: If "Proposal Result" = "Pending") 
    * "Awarded" (Logic: If "Proposal Result" = "Awarded" and the "Job Scheduled" checkbox is not checked) 
    * "Lost" (Logic: If " Result" = "Lost") 
    * "Archived" (Logic:Proposal If "Proposal Result" = "Archived"; note that Proposals with this Status are excluded from sales reporting) 
    * "Canceled" (Logic: If "Proposal Result" = "Canceled"; note that Proposals with this Status are excluded from sales reporting)
    * "Job Scheduled" (Logic: If the "Job Scheduled" checkbox is checked)



  


Development Specification

Ellis Miller 06/17/2025: 

NOTE: You'll want to code this after the main fields and behaviors are coded.

[ ] You'll want to code an ifs in reverse order, but the logic above is clear.

[ ] Test carefully.

BID: 4 HOURS
