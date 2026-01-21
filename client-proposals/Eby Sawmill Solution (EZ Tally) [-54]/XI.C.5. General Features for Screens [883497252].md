11.3.5. General Features for Screens

The following items are displayed on all screens:

  


TODO_US: Tim Reitz 01/17/2024: Merge these (previously from the "Yard App Screens" row)) with the Footer items below:

All screens other than the startup screens will have the following: 

  * Home (opens the Home screen; visible for all users)
  * Yard Scaling (begins the yard tally scaling process; visible for Administrator & Log Buyer users)
  * Export Scaling (begins the export tally scaling process; visible for Administrators & Export Scaler/Loader users)
  * Export Loading (begins the export tally loading process; visible for Administrators & Export Scaler/Loader users)



  


  * Footer / toolbar at the bottom of the screen, with the following button options: 
    * Home (selecting this takes the user to the Home screen; if there are unsaved changes there first is a warning that entered data will be lost) 
    * Yard Scaling (selecting this takes the user to the Yard Scaling - Yard Tallies List screen; if there are unsaved changes there first is a warning that entered data will be lost)
    * Export Scaling (selecting this takes the user to the Export Scaling - Booking List screen; if there are unsaved changes there first is a warning that entered data will be lost)
    * Export Loading (selecting this takes the user to the Export Loading - Bookings screen; if there are unsaved changes there first is a warning that entered data will be lost)
    * Log Out (selecting this gives a warning prompt: "Are you sure that you want to log out?" if there are no unsaved changes, or a warning that entered data will be lost if there are unsaved changes; if the user chooses to continue, they are logged out of the Yard App) 



  


The following items are displayed on all screens, except for the login screen:

  


  * Unsaved Changes icon: When there are unsaved changes (for example, when the device is not connected to the internet), a red/orange circle appears in the heading bar, displaying the number of unsaved changes. When the device is able to save the changes (i.e. reconnects to the internet), the icon disappears and is replaced by the green refresh icon. Note that unsaved changes icon might not update until the user navigates to a different part of the app - this might be improved in a future update. 



  


  * Refresh icon: There is a green refresh icon in the top right corner of each screen, on the heading bar. Selecting this manually syncs the Yard App with the main AppHosting database. Note that the screen might not actually refresh right away, or the user might have to navigate to a different screen, then back to the original screen to see the refreshed data - this might be improved in a future update. 



  


  * Sync error message: If a sync error has occurred and no data is able to be saved, a message is displayed in the top left corner of the screen: "Unable to save data.", in bold red text. This is a hard error, and no changes will be saved until the connection is reset. If a user encounters this error message while using the Yard App, they should log out and log back in to reset the connection, and reach out to CodeCrafters support to diagnose the error.


