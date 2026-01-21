18.0.2.4. Admittance Meeting Report

  


Requirements

This is a report of pending "Completed by Member" SPE member applications.

  


Accessed from: Faith Builders SPE | Member Applications | Admittance Meeting Report

  


Title: Admittance Meeting Report: <SPE Application>

  


Columns:

  * Member
  * Member City
  * Application Date
  * # of Prior Admitted Application
  * Total Contribution Amount (total type = sum)
  * Proposed Accepted by SPE (editable)
  * SPE Approval Balance



  


Filters:

  * SPE Application (required; drop-list of approved SPE applications for the current tax year)



  


Sorted by: Member

  


Grouped by: Member

  


  


  


The admittance meeting report will be a 4-pane report, as illustrated in the attached mockups.

  


The top two panes will show member information.

  


  * The top-left pane will show all pending members, sorted by Member Name. It will link to the member application. It should show only include pending applications, not accepted applications. The SPE Approval balance at the top of the report will take into account any previously accepted (paid or unpaid) member applications. Then, each row will subtract an amount if its Proposed Accepted.



  


  * The top-right pane will show the school designations for the member selected in the top-left pane. It does not need any linked columns.



  


The bottom two panes will show school information.

  


  * The bottom-left pane will show all schools with pending designations (not just the "Proposed Accepted by SPE"). 



  


  * The bottom-right pane will show which pending members designated contributions to this school.



  


The report will have a "Proposed Accepted by SPE" column. Modifying the report would simply modify whether the application is proposed as being accepted. These changes would not be finalized until clicking an "Accept Proposed Applications" button.

  


Development Specification

Ellis Miller 02/09/2021:

[ ] Upper-left: All pending members

[ ] Prior Admitted: See macro from Member Application

[ ] For the approval balance:

  * Hidden running sum column on the total amount
  * Use this to calculate Approved Amount from SPE Approval minus the above total



[ ] The Proposed field is a editable field in the upper-right pane that is not displayed on the detail screen.

[ ] This hidden field should be unchecked if a member application is set to inactive or accepted (FIeldChangExpr)

[ ] The top pane is an instant save report.

[ ] Hide the running sum column if the report is click sorted.

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
