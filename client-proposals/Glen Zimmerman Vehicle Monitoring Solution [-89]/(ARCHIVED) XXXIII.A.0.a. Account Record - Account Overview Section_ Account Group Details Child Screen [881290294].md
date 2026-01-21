33.1.0.1. Account Record - Account Overview Section: Account Group Details Child Screen

  


Requirements

_GZ (see mockup): Tim Reitz 12/12/2025: Is this necessary now that end users aren't in Silverloom?  

_VA: Tim Reitz 12/18/2025: Child screen not needed. Let's add a link to open the selected Group. 

Tim Reitz 12/23/2025: Archiving this section today. 

  


_VA: Tim Reitz 12/04/2025: If we don't keep this, then let's remove the corresponding button from the main screen.

  


_VA: Tim Reitz 12/18/2025: In the portal, let's include: 

  * Account Group 
  * Primary Group Admin + phone + email + address
  * Not upline groups



Tim Reitz 12/04/2025: For purposes of the WSGI / portal, is it helpful to have information from other linked records fielded or displayed on macros here, if we want to display it in the portal? Or can the WSGI easily look through to linked records?

Tim Reitz 12/23/2025: Added notes to the portal spec section. 

  


  * Account Group Details child screen (opens when the "Account Group Details" button is clicked): 
    * Group (read-only macro; displays the "Group Display Name" for the selected "Account Group"; not a link to the record) 
    * Group State (read-only macro; displays the "Group State" for the selected "Account Group") 



  


  * Account Group Admins (read-only memo (macro); with the following details: 
    * displays the "Account Group Admins" from the linked "Account Group", in the following format: 



<Group Admin "Short Display Name"> 

Phone: <Group Admin Phone> 

Email: <Group Admin Email> 

Address: <Group Admin Address, in the standard multi-line format without the addressee name> 

  * in addition to this format, the information for the "Primary" Group Admin includes a "Primary" prefix; 
  * this information is sorted the same as the "Account Group Admins" embedded spreadsheet on the Account Group (Primary first, then alphabetically after that); 
  * does not include linking to the Account Group, as the end user does not have the necessary Permissions to view that screen directly) 



_NM: Tim Reitz 10/27/2025: Thoughts on doing this read-only expression memo? (rather than macros for just the Primary, or trying to do macros for everyone) 

Another approach would be a a virtual RG that mimics the the RG on the Account Group record. 

Tim Reitz 10/28/2025: From a data standpoint, he prefers a virtual RG for both of these. We could display the addresses in an MRG memo below it. 

Tim Reitz 12/16/2025: Follow up on this. 

  


  * Upline Group(s) (visible if the selected "Account Group" has an "Upline Group" selected; read-only memo (macro); with the following details: 
    * displays the "Upline Group(s)" for the selected "Account Group" for the Account, in the following format: 



<Group Display Name>

Primary Group Admin: <Primary Group Admin "Short Display Name">

Phone: <Primary Group Admin Phone> 

Email: <Primary Group Admin Email> 

Address: <Primary Group Admin Address, in the standard multi-line format without the addressee name> 

  * does not include linking to the Upline Groups)



  


Development Specification

_MOCKUPS: Tim Reitz 12/04/2025: Let's not mock this up yet - we might not be keeping it.

  


Tim Reitz 10/27/2025: For abundance of clarity, this is what I am envisioning for the "Account Group Admins" read-only memo: 

Primary: <Primary Group Admin "Short Display Name"> 

Phone: <Group Admin Phone> 

Email: <Group Admin Email> 

Address: <Group Admin Address, in the standard 2- or 3-line format> 

  


<Secondary Group Admin 1 "Short Display Name"> 

Phone: <Group Admin Phone> 

Email: <Group Admin Email> 

Address: <Group Admin Address, in the standard 2- or 3-line format> 

  


<Secondary Group Admin 2 "Short Display Name"> 

Phone: <Group Admin Phone> 

Email: <Group Admin Email> 

Address: <Group Admin Address, in the standard 2- or 3-line format> 

  


etc.
