5.6. Admittance Meeting Report

  


Requirements

The admittance meeting report will be a 4-pane report, as illustrated in the attached mockups.

  


The top two panes will show member information. The left pane will show all pending members,. The right pane will show the school designations for the selected member.

  


The bottom two panes will show school information. The left pane will show all schools with pending designations. The right pane will show which pending members designated contributions to this school.

  


The report will have a "Proposed Accepted by SPE." Modifying the report would simply modify whether the application is proposed as being accepted. These changes would not be finalized until clicking an "Accept Proposed Applications" button.

  


Development Specification

Ellis Miller 02/10/2021: TODO_CH: Update this to match mockup (see descriptions below).

Matthias Miller 02/16/2021: Done, but more detail required? [https://docs.google.com/spreadsheets/d/1sdKY7W-5Rlfz7R7eOtD6OwSojzysQW1S4qofKLKKgUo/edit?userstoinvite=joshn%40joshnisly.com&ts=602a592e&actionButton=1#gid=1878646606](https://docs.google.com/spreadsheets/d/1sdKY7W-5Rlfz7R7eOtD6OwSojzysQW1S4qofKLKKgUo/edit?userstoinvite=joshn%40joshnisly.com&ts=602a592e&actionButton=1#gid=1878646606)

  


Ellis Miller 02/09/2021:

  


TODO_CH: We should remove the docs.google link above. The correct mockup is in the mockups package. We should describe that correctly up above:

[X] Upper-left: All pending members

[ ] Prior Admitted: See macro from Member Application

[ ] For the approval balance:

  * Hidden running sum column on the total amount
  * Use this to calculate Approved Amount from SPE Approval minus the above total



[ ] The Proposed field is a editable field in the upper-right pane that is not displayed on the detail screen.

[ ] This hidden field should be unchecked if a member application is set to inactive or accepted (FIeldChangExpr)

[ ] The top pane is an instant save report.

[ ]Hide the running sum column if the report is click sorted.

Target: 2 Days because of uncertainties.

[ ] Bottom-left: All schools with designations from non-accepted members (TotalsOnly RepeatRG on Designations non-accepted members and pass in the selected member from top grid as an ask prompt). This pane is not editable.

[ ] Total Pending is total amount of all pending members for this school.

[ ] Designations Accepted is the amount for all accepted members. Or Proposed is the amount for all Proposed members.

[ ] Remaining Pending is the amount for all appending, but not proposed.

Target: 2 Days 

[ ] Upper-right: Designations for highlighted member of upper-left. Pass member ask prompt from bottom-left, RepeatRG on that member's designations.

Target: 4 hours

[ ] Bottom-right: All non-accepted designations for highlighted school in bottom-left.

Target: 4 hours
