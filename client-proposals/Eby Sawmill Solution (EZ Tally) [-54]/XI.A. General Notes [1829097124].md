11.1. General Notes

  


Requirements

Data Entry:

  * Log information will be entered as a series of numbers for as much of the data entry process as possible. Note the quick entry process, of being able to use numbers to enter data quickly without needing to press anything in between.



  


  


Saving Data: Entered data is saved at the following points in the Yard App: 

  * "Save New Vendor" button in the New Yard Tally workflow
  * "Enter New Log" button on the following screens: 
    * Yard Tally Details 
    * Yard Tally Log Entry
    * Export Tally Details 
    * Export Tally Log Entry 
  * "Delete Log" button on the following screens: 
    * Yard Tally Log Entry 
    * Export Tally Log Entry 
  * The "Save & Return" buttons (as previously)
  * "Finish Scaling" button on the following screens: 
    * Yard Tally Log Entry 
    * Export Tally Log Entry 
  * With each log deletion on Export Loading
  * "Confirm Loaded" button on the Export Loading screen



  


  


Secondary Saves / Safety Net: 

The Yard App includes a "secondary save" feature that can serve as a safety net if a sync error occurs during offline user. This saves information on the server where a senior developer can access it in an emergency or for diagnostics. 

  


Other Notes: 

  * This safety net only applies to data that the app attempted to save, and does not apply to changes that a user discards via the warning buttons. 
  * When working in offline mode, the app retains data even if the user closes the app, and then syncs to the main system when the app regains connection.



  


  


Offline Use: The yard app will allow loading the app on an Internet connection, going offline to enter the logs, then going back online to save the logs.

  


Note that offline use is only needed for the Yard Tally Scaling portion of the yard app. 

  


  


Automatic Data Refresh: The Yard App automatically refreshes its view of the data in the main database every 5 minutes, to bring in any changes made in the interim. This reduces (but doesn't completely eliminate) the chance of users overwriting or canceling out each others' entered data. 

  


  


Misc. Functions:

  * The app will allow leaving an open tally, switching to another load, then returning to the first open tally and finishing it.
  * The app will also allow opening confirmed tallies, editing, and re-confirming.
  * After a Yard Tally has been confirmed, the Yard Tally Summary Email can be sent to the vendor.



  


  


Browser "Back" Function Disabled: At its core, the Yard App was built differently from the ground up to handle the offline use. As part of this the browser back navigation (back button / back swipe) does not work as normally would be expected. For that reason, the browser back button / back swipe feature has been disabled. If a user attempts to use the back button / back swipe, they may experience the screen changing back momentarily, but this quickly auto-corrects and brings the user back to the same screen.

  


If at some point in the future the browser's back navigation functionality is desired, it could be considered (it would need some thought to properly handle the workflow to avoid losing partially-saved data, etc.).

  


  


"Live" vs. "Test" Versions: There are two versions of the Yard App:

  * Live Version: This is the main version of the Yard App that is connected to the live main database.
  * Test Version: This version of the Yard App is connected to the test database, and has clear visual markings to distinguish it from the live version (red "EZ TALLY TEST" heading at the top of the screen; red menu indicators, etc.).



  


  


Warning Messages: The Yard App displays various warnings when navigating away from the current screen. Since this is a web app that runs via the browser and can be used across platforms (Android, iOS, Windows), it uses the browser's prompting framework for these warning messages. Therefore the message may display somewhat differently on different platforms. 

  


The wording of the warning messages themselves can be changed fairly easily, along with basic formatting (putting them in all caps, etc.), but since the browser's framework is in use here, we don't have control over the wording for the buttons or the workflow (i.e. a special save & continue). It would be an option to consider coding for a custom warning and prompt feature with its own messages/buttons and workflows (rather than using the browser's framework), but that would require additional design work prior to coding, and would be a somewhat significant change. 

  


Following is a list of current warning messages: 

Yard Scaling: 

  * Yard Scaling - Log Entry - when clicking the Tally ID navigation link: 



Message: "🛑 REMOVE THE CURRENT LOG?" 

Yard Scaling - Log Entry - when clicking the "Yard Scaling" navigation link or one of the menu buttons at the bottom: 

Message: "🛑 YOU WILL LOSE YOUR CHANGES. CONTINUE?" 

 

Export Scaling: 

  * Export Scaling - Log Entry - when clicking the Booking ID navigation link: 



Message: "🛑 YOU WILL LOSE YOUR CHANGES. CONTINUE?" 

  * Export Scaling - Log Entry - when clicking the "Export Scaling" navigation link or one of the menu buttons at the bottom: 



Message: "🛑 YOU WILL LOSE YOUR CHANGES. CONTINUE?" 

 

Export Loading: 

  * Export Loading - when clicking the Booking ID navigation link: 



Message: "🛑 YOU WILL LOSE YOUR CHANGES. CONTINUE?"

Export Loading - when clicking the "Export Scaling" navigation link or one of the menu buttons at the bottom: 

Message: "🛑 YOU WILL LOSE YOUR CHANGES. CONTINUE?" 

 

General: 

  * Delete Log: 



Message: "🛑 REMOVE THE CURRENT LOG?" 

  * Log Out (any time): 



Message: "Are you sure that you want to log out?"

  


Development Specification

This would use an API call to send the email.

  


Note that offline work might happen 1-2 times/week

  


Change Requests: 

  * [[[IN8952](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8954&)]] - ZET - Yard App - Support Intermediate Saves
  * [[[IN9455](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9457&)]] - ZET - Yard App - Support Secondary Saves
  * Tim Reitz 06/11/2024: [[[IN9385](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9387&)]] - ZET - Yard App - Back Swipe / Back Button - Disable
  * Tim Reitz 06/11/2024: [[[IN9354](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9356&)]] - ZET - Yard App - Distinguish Test App from Live App
  * Tim Reitz 06/11/2024: [[[IN9436](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9438&)]] - ZET - Yard App - Change Wording for Warning Messages
  * Tim Reitz 06/20/2024: [[[IN9883](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9885&)]] - ZET - Extra log deletion


