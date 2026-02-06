1\. Overview

  


Requirements

This is a proposal for a new feature in the Triple D Truss custom software solution. 

  


After a truss order has been entered in the software, truss print requests are created as needed and given to the truss designer, who draws up the full plans/prints. Currently someone fills out these requests manually on paper and gives them to the designer. Triple D Truss would like a way to digitally generate these more automatically and avoid double entry of information. 

  


The truss print requests are generated on a per-row basis (one sheet/request for each row from the order that needs prints). 

  


The general idea for this is that clicking a button could open a prompt with fields for everything needed on the form. Some things would be auto-filled from the line item & order, and the rest could be filled manually or left blank.

  


Development Specification

See the incident in MYS: [https://mys.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-4615&State=ISwSvCyE0ts&](https://mys.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-4615&State=ISwSvCyE0ts&)

  


  


Note that Triple D does not need a printout of the print requests. However, see their current sheet.

The following fields from the current printout are not needed: 

  * ASAP 
  * Rush Time 
  * Wall-to-Wall
  * Attic storage 
  * Room Loading
  * Room Size 
  * Both instances of "both 0-10-8"
  * BCLL
  * Ag Default
  * Res/Com Default
  * Job Name
  * Truss ID



  


A goal is to keep historical truss prints for items that have been changed and have more than one print request/print. 

  


Mockups: [https://docs.google.com/spreadsheets/d/1oQST0RH6jVoVkhYr8bBhs0a2RpgnToDuj5ERlxiow30/edit#gid=930270704](https://docs.google.com/spreadsheets/d/1oQST0RH6jVoVkhYr8bBhs0a2RpgnToDuj5ERlxiow30/edit#gid=930270704)
