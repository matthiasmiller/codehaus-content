11.3.4. Export Tally Loading Screens

  


Requirements

Bookings List:

This screen displays a list of all Bookings with a Status of Open. This list has the following columns:

  * Booking ID
  * Description
  * Action ("Select" button to open the Booking)



  


When a Booking is selected from the list, the Tally screen is displayed.

  


Tallies List:

This screen displays the following navigation description: "Export Loading > <Booking ID>". Selecting "Export Loading" takes the user back to the Bookings List. 

  


This screen displays a list of all Export Tallies for the selected Booking. This list has the following columns:

  * Tally ID
  * Status
  * Action ("Edit" icon & label)



  


The list is sorted by Status (in the sequence of Confirmed, Open, Loaded). Only the Confirmed and Loaded tallies have the option to be opened in the Export Scaling side of the app (this is because tallies with a Status of Open should not be loaded until they are Confirmed). The Tallies with a Status of Open are displayed in gray font, to indicate that they are not available for loading. 

  


Selecting a Tally from the list results in one of the following: 

  * If Status = Confirmed: Displays the Logs screen (editable) 
  * If Status = Loaded: 
    * For Export Scaler/Loader users: __



Tim Reitz 01/22/2024: TBD (see [[[IN9327](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9329&)]]). 

  * For Admin users: __



Tim Reitz 01/22/2024: TBD (see [[[IN9327](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9329&)]]). 

  


Tally - Logs:

This screen displays the following navigation description: "Export Loading > <Booking ID>". Selecting the Booking ID takes the user back to the Tallies List; selecting "Export Loading" takes the user back to the Bookings List (after a warning that changes will be lost). 

  


This screen displays the tally details summary at the top of the screen:

  * Booking ID
  * Tally ID



  


This screen also displays the following: 

  * Removed Logs? (required; drop list of Yes/No; defaults to blank)
  * A table of all logs in the Tally with the following columns:
    * Logs (numbered list of all logs on the tally; displayed in the following format: "<Species Abbreviation> \- <Tag Number>"; i.e. "1\. OK - 12345")
    * Length (displays the abbreviation)
    * Diameter (displays the abbreviation)
    * Base Grade 
    * View (button to view the log in read-only mode)
    * Delete (button; if selected for a log, a prompt is displayed with options to delete the log or cancel)



  


There will be a "Continue" button that displays the next screen (Container Number) to begin loading. 

  


Data Entry for Loading: 

Note that each of these data entry screens contains the following: 

  * Displays the following navigation description: "Export Loading > <Booking ID>". Selecting one of the options opens a prompt to confirm, since going back will cause changes to be lost. Selecting the Booking ID takes the user back to the Tallies List; selecting "Export Loading" takes the user back to the Bookings List (after a warning that changes will be lost). 



  


Data Entry - Container Number:

This screen displays the following data entry field:

  * Container Number (plain text field; wide enough for at least 11 characters; the entry must be 11 characters long, with the first 4 characters being letters and the remaining 7 characters being numbers; the following message is displayed under the field when the field is selected and the entered text does not match the requirements: "Please enter the Container # in the format of "ABCD1234567.") 



  


When the Container Number is entered in the correct format, a "Continue" button appears.

  


This screen also shows the following tally loading summary information as a reference. Each of these displays the corresponding value and a small button to open the corresponding screen:

  * Booking ID
  * Tally ID
  * Removed Logs



  


When the the user selects "Continue", the Heavy Weight screen is displayed.

  


Data Entry - Heavy Weight:

This screen displays the following data entry field:

  * Heavy Weight



  


This screen also shows the following tally loading summary information as a reference. Each of these displays the corresponding value and a small button to open the corresponding screen:

  * Booking ID
  * Tally ID
  * Removed Logs 
  * Container #



  


When the heavy weight is entered and the user selects "Continue", the Light Weight screen is displayed.

  


Data Entry - Light Weight:

This screen displays the following data entry field:

  * Light Weight



  


This screen also displays the following read-only field:

  * Net Weight (once Light Weight is entered, this displays the difference of Heavy Weight and Light Weight)



  


This screen also shows the following tally loading summary information as a reference. Each of these displays the corresponding value and a small button to open the corresponding screen:

  * Booking ID
  * Tally ID
  * Removed Logs
  * Container #
  * Heavy Weight



  


When the light weight is entered and the user selects "Continue", the Load Pictures screen is displayed.

  


Data Entry - Load Photos:

This screen has the following button that allows the user to take photos (note that there is no longer the option to upload existing files from the device):

  * Choose Files



  


This screen also shows the following tally loading summary information as a reference. Each of these displays the corresponding value and a small button to open the corresponding screen:

  * Booking ID
  * Tally ID
  * Removed Logs
  * Container #
  * Heavy Weight
  * Light Weight
  * Net Weight



  


When the user selects the Choose Files button, a camera screen is opened with options to "Cancel" or take a photo. After a photo has been taken, there are options to "Retake" or to "Use Photo." Selecting "Use Photo" attaches the photo to the Export Tally and returns the user to the Load Photos screen, where a thumbnail of the newly added photo is displayed.  

  


The user can attach multiple photos to the same Tally, and also can delete photos that have been added (via a "Delete Image" button beside each thumbnail). 

  


After one or more files are attached to the tally, the user can select "Continue", and the screen advances to the Seal Number screen.

  


Data Entry - Seal Number:

This screen displays the following data entry field:

  * Serial Number



  


This screen also shows the following tally loading summary information as a reference. Each of these displays the corresponding value and a small button to open the corresponding screen:

  * Booking ID
  * Tally ID
  * Removed Logs
  * Container #
  * Heavy Weight
  * Light Weight
  * Net Weight
  * Photos



  


When a number is entered and the user selects "Continue", the completion screen is displayed.

  


Data Entry - Confirm Tally Loaded:

This screen displays the following read-only field:

  * Tally Loaded On (date; defaults to blank, to display the current date when the "Confirm Loaded" button below is selected) 



  


This screen also shows the following tally loading summary information as a reference. Each of these displays the corresponding value and a small button to open the corresponding screen:

  * Booking ID
  * Tally ID
  * Removed Logs
  * Container #
  * Heavy Weight
  * Light Weight
  * Net Weight
  * Photos
  * Seal #



  


There is the following button:

  * Confirm Loaded



  


When the user selects this button, the status of the Tally is set to "Loaded" and the screen advances to the Tally Complete screen. 

  


Tim Reitz 01/19/2024: Note: As of today, you cannot edit Loaded tallies. If a user wishes to edit one, the Loaded checkbox must be unchecked in the main system first. We need to consider & discuss with the clients if this is a good behavior (see [[[IN9327](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9329&)]] - ZET - Export Tally - Change Validations on the Target BF Fields). 

Ben Reitz 01/26/2024: The client noticed this and we briefly discussed. They said that this behavior is the way that it should be. There is the rare occasion that a container is loaded with the wrong loads but editing a Loaded tally should not be easy to do.

  


Data Entry - Tally Complete: 

This screen displays the tally details for a Loaded tally: 

  * Booking ID
  * Tally ID 
  * Removed Logs
  * Container Number
  * Heavy Weight
  * Light Weight
  * Net Weight
  * Photos
  * Seal #
  * Tally Loaded On



  


It also includes the following buttons: 

  * "Download Bill of Lading" (this opens the Export Tally Bill of Lading printout PDF on the mobile device so the user can then print the document directly to the printer from the device (or save it or share it), then return to the app) 
  * "Done" (this returns to the Tallies List screen)



  


Development Specification

Change Requests: 

  * Tim Reitz 06/10/2024: [[[IN9365](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9367&)]] - ZET - Yard App - Misc items after initial deployment walkthrough 
  * Tim Reitz 08/31/2024: [[[IN10234](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10236&)]] - ZET - Yard App - Export Scaling & Loading - Tally Details Screen - Add Log Details Table


