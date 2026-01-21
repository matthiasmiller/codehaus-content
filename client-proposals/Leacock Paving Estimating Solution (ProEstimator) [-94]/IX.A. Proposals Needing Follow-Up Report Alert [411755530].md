9.1. Proposals Needing Follow-Up Report Alert

  


Requirements

Overview/Purpose: This is a report alert that serves as a reminder to Sales Reps about Proposals needing follow-up.

  


Details: 

  * Title: "<#> Proposal(s) Needing Follow-Up" (with "#" = the number of corresponding records)
  * Displays: Two days before and the day after the "Initial Follow-Up Due" or "Secondary Follow-Up Due" dates, for any Proposals with "Status" = "Follow-Up Needed" (i.e. if "Sent to Customer" is checked and if "Proposal Result" = blank) and "Follow-Up Complete" not checked for the corresponding "Follow-Up Due" date. 
  * Action: Opens the "My Proposals Needing Follow-Up" report - see corresponding spec
  * User(s) to notify: All Sales Reps with one or more Proposals that meeting the criteria
  * Dismiss type: Auto-dismiss when all items are resolved



  


Other Notes:

  * Note that since this is based on the Proposal's Status, the alert will not be sent if "Proposal Result" is not blank, even if one or both of the Follow-Up Due dates is due or in the past.



  


Development Specification

Ellis Miller 06/17/2025: 

  


BID: 2 HOURS

  


SCOPE: Tim Reitz 05/14/2025: Not included in the HLD.
