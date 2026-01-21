19.8. Done: Proposal Record: Signature Tracking

_VA: Tim Reitz 07/03/2025: Client wants to move forward with this for Phase 1.

  


The following feature could be added to remind users of Proposals that are lacking signature documentation. The general idea is as follows: Sales Reps would receive a recurring alert about any of their own Proposals that are marked as "Awarded" but do not have a signature documented. Proposals in this state could still be marked as Scheduled. Any user could complete the documentation, which would resolve the alert. Note that in its current form, this would be dependent on the Digital Signature Collection / Tracking feature.

  


[X] Estimated Cost: $400-700

  


Initial Spec:

[X] Part 1: New "Proposals Lacking Signatures" report alert:

Overview/Purpose: This is a report alert that serves as a reminder to Sales Reps about Awarded Proposals lacking a documented signature.

  


Details: 

  * Title: "<#> Proposal(s) Lacking Signatures" (with "#" = the number of corresponding records)
  * Displays: Every Monday if there are any Proposals that meet the following criteria:
    * "Status" = "Awarded" or "Job Scheduled" and 
    * "Proposal Signed" = not checked / blank
  * Action: Opens the "Proposals Lacking Signatures" report (see corresponding spec)
  * User(s) to notify: All Sales Reps with one or more Proposals that meeting the criteria
  * Dismiss type: Auto-dismiss when all items are resolved



  


Other Notes:

  * N/A



  


[X] Part 2: New filter on the "Master Proposals" report:

  * Limit to Proposals Lacking Signatures (checkbox; defaults to not checked; if checked, the report includes only items for which "Proposal Signed" is blank, also respecting other filter selections)
    * Note that this is located at the bottom of the filters list.



  


_EM: Tim Reitz 07/02/2025: For the "Limit to Proposals Lacking Signatures" filter: should this be:

1\. at the top of the ask prompts and handle all the logic (statuses + blank field; overrides other filter selections), or

2\. at the bottom and handle only the blank field?

For now, I've specced it as #2.

_VA Ellis Miller 07/03/2025: That's fine. 

  


Tim Reitz 07/02/2025:

If 1, then we don't need to set "Status" for the new report (remove the spec), and we need to update the spec for the filter checkbox.

If 2, probably no change needed for the spec (unless Ellis has tweaks).

  


[X] Part 3: "Proposals Lacking Signatures" report:

Overview: This is the All Proposals Report, filtered to display Proposals that need a signature documented.

  


Accessed from:

  * The "Proposals Lacking Signatures" report alert
  * Main Menu | Proposals | Proposals Lacking Signatures (opens the filter screen, with the filters defaulted as noted below)



  


The following filter(s) are set differently from the main report:

  * "Status": Set to "Awarded" and "Job Selected"
  * "Limit to Proposals Lacking Signatures": Set to checked



  


_VA: Tim Reitz 07/03/2025: Per Ellis, we could add a column to the documentation RG for "Document Type"(could be left blank). Have a type of "Signed proposal", and could set the signed checkbox automatically. Within the scope of this price.

_EM: Tim Reitz 07/03/2025: Right that the user would need to set this Document Type on the RG after the file has been uploaded? Or would it be added to the upload screen somehow? (I'm thinking that it wouldn't save time for the user to do this manually vs. checking the checkbox.

_VA Ellis Miller 07/03/2025: It would have to be after. A checkbox is fine for now.
