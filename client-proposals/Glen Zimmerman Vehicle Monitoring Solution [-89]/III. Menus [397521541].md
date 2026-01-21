3\. Menus

The Solution includes the following menu tabs, and the following menu options not listed elsewhere in this spec:

  


  * Providers (custom menu; visible to all users)
    * Accounts 
      * Menu options specced on individual record & report specs
    * Account Groups (visible to Group Admins and Master Administrators) 
      * Menu options specced on individual record & report specs
    * Devices 
      * Menu options specced on individual record & report specs 
      * Administrators | Device Management | New Devices Batch Entry (__



Tim Reitz 09/29/2025: Could be a new records report, to batch add a lot of Devices. 

_NM: Tim Reitz 01/17/2026: How much work is a new records report? Would it be worth including it here in Phase 1, or bumping to the future when they would be more likely to batch-add Devices? 

TODO_VA: Tim Reitz 01/20/2026: Per Nic, would require some research, but likely would be 4-8 hours to build one and make sure it's working correctly. 

Here's an example in testzch: [https://testzch.apphosting.zone/Reports/Standard/Designer/Std_Create?Asks=AskType%3D%22Field%22%2CAskParentID%3D7.00&State=ctLVLwm53iQ&_=SRjT4&](https://testzch.apphosting.zone/Reports/Standard/Designer/Std_Create?Asks=AskType%3D%22Field%22%2CAskParentID%3D7.00&State=ctLVLwm53iQ&_=SRjT4&). 

[ ] Probably include this as an optional add-on / possible future item. 

  * Contacts 
    * Menu options specced on individual record & report specs
  * Vehicles 
    * Menu options specced on individual record & report specs
  * Integrations 
    * Traccar Web Interface (__



_NM: Tim Reitz 01/17/2026: Presumably we'd have a System Switch to specify the Traccar URL, and look at that here? 

TODO_VA: Tim Reitz 01/20/2026: Correct. This could be an unchangeable system switch, since it's such a core part of the solution. 

  * End User Portal (opens the "Enter Email" Screen of the End User Portal - see corresponding spec) 



  


  * Administrators (custom menu; visible to users with the "Full Access" Permission) 
    * Manage Contacts
      * Menu options specced on individual record & report specs
    * Manage Devices
      * Menu options specced on individual record & report specs
    * Manage SIM Cards
      * Hologram Account



_NM: Tim Reitz 01/17/2026: Presumably we'd have a System Switch to specify the Hologram URL, and look at that here? 

TODO_VA: Tim Reitz 01/20/2026: Correct. Maybe editable?? 

  


  * Advanced (standard menu; custom visibility: visible only to users with the "View Advanced Menu" Permission; some menu options can be disabled or hidden based on permissions) 



  


TODO_GZ: Discuss sidebar menu icons with the client. Can send image file (and link if desired): [[[W0569](https://zch.apphosting.zone/Detail/Edit/2?RecordType=WikiPages&NumberID=-570&)]] - Silverloom Sidebar Menu Icons.
