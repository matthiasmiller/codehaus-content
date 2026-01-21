6\. Production Calendar

TODO_AP: Tim Reitz 07/20/2024: Needs spec

Tim Reitz 03/04/2025: See row 20 in the Delivery Feature proposal ([https://zch.apphosting.zone/Detail/Edit/2?RecordType=ClientProposals&NumberID=-45&State=ISwSvCyE0ts&](https://zch.apphosting.zone/Detail/Edit/2?RecordType=ClientProposals&NumberID=-45&State=ISwSvCyE0ts&)).

  


Accessed from Triple D Truss | Deliveries | Production Calendar

  


  


Tim Reitz 07/20/2024: From [[[IN8901](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8903&)]] - ZTD - Adding Hours fields to Production Calendar:

Changes to the Production Calendar:

  * Trvl Time (displays the travel time for the delivery; located to the right of the trucker's name)
  * NOTE - The calendar should continue to only show the trucker first name, from the corresponding Contact record.



  


  


Tim Reitz 07/20/2024: From [[[IN9790](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9792&)]] - ZTD - Delivery Record & Calendar - Changes to Travel Time (prev. Changes to Hours fields): 

  * Trvl Time TT (displays the Travel Time for the delivery; located to the right of the trucker's name; always displays the Travel Time for the delivery, even if no Trucker has been selected)



  


Tim Reitz 07/20/2024: From [[[IN9797](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9799&)]] - ZTD - Production Calendar - Add "RH" (Remaining Hours): 

  * RH (displays the current remaining hours for the selected Trucker; displays in red if negative; located between the Trucker's name and TT; blank if there is no selected Trucker or if an Other Trucker is set for the Delivery)



  


Tim Reitz 07/20/2024: From [[[IN9794](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9796&)]] - ZTD - Calendar - Fix "Trkr." Display (prev. "Other Trucker" not working): 

On the calendar delivery tile: "Tkr." should display: 

  * The selected "Trucker" if there is one
  * The entered "Other Trucker" if there is no selected "Trucker"
  * Remain blank if there is not a selected "Trucker" or an entered "Other Trucker"



  


Ben Reitz 05/08/2025: From [[[IN10789](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10791&)]] - ZTD - Allow for linking Orders and Deliveries: 

Item 5: Changes to the Production Calendar:

  * Calendar only displays Delivery records that meet one of the following criteria:
    * Have the "Scheduled" checkbox checked (located on the Calendar based on "Schedule Date");
    * Have the "Will Call" checkbox checked and "Quote / Order #" is blank or set to an Order record with "Status" = "Order" (located in the "Will Call" section at the bottom of the Calendar)



  


Ben Reitz 05/08/2025: From [[[IN11295](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11297&)]] - ZTD - Production Calendar - Unscheduled deliveries randomly appearing and disappearing:

  * Update the WSGI logic so that it checks if the new "Scheduled" checkbox has been checked when the Calendar is refreshed.



  


Ben Reitz 05/08/2025: From [[[IN11272](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11274&)]] - ZTD - Calendar - Drag and drop only allowing placement in certain boxes:

  * Fix the Calendar so that it filters out non-scheduled Deliveries by keeping it from assigning sequence numbers to Deliveries that don't have the "Scheduled" checkbox checked.


