13\. Mobile Support (App)

  


Requirements

_VA: Tim Reitz 07/24/2025: From conversation with Ellis: this would be a web app with PWA like ZET

[ ] Find out what the client wants to see / be able to do; 

[ ] can ask Jonathan for visuals from FB portal; 

[ ] VA can put together rough mockups in Excel, 

[ ] then Ellis has a contact through InvTools; 

  


TODO_VA: Tim Reitz 08/25/2025: At this point, we're actually planning on not building our own app / PWA for this (planning to user the Traccar apps). 

  


Install Traccar App Screen

  * When installing the app, the user will encounter the following instruction screen:
    * "To continue, please install and enable the Traccar Client app."
    * Install App (link to iPhone / Android app)
    * In the Traccar app, enter your Device ID 
    * <Device ID> <option to copy ID for easy entry in the app>
    * In the Traccar app, enter the Server URL
    * <URL for Traccar / Silverloom> <option to copy URL for easy entry>
    * In the Traccar app, toggle the Service Status to turn it on
    * "This page will automatically continue after the above steps have been done."



TODO_VA: Tim Reitz 12/10/2025: Let's make sure to have instructions like these somewhere, probably in the welcome email for new users 

[ ] Traccar Manager App (for all users)

[ ] Traccar Client App (when needed) 

  


Inviting New Users

  * Account Admins can invite new drivers to their account via phone number. The process will be as follows:
    * Send Invite (prompts for a phone number)
    * New driver gets a text saying that someone invited them to join an account, with a link to the app.
    * If the new driver does not have a profile yet, they will be prompted to follow the instructions in the "Install Traccar App Screen" section above.
    * If the new driver already has a profile, there will be a list of any unanswered invitations. The driver will have the ability to either accept or decline the invite. If they accept, they will be added to the list of drivers for the account.



  


  


Login Screen

  * To log in, the user will see the following:
    * Logo
    * Enter phone number (text field)
    * Send code (button; sends numeric code to entered phone number)
    * Please enter your login code (text field)
    * Login (button)



  


  


Master Administrator

  * When an Administrator logs in, they will see 3 menu options:
    * Impersonate Account Group Admin (allows to choose from a list of account groups)
    * Impersonate Account Reseller (allows to choose from a list of Resellers)
    * View All Accounts



  


  


Master Administrator / Account Group Admin / Account Reseller

  * When any of these individuals log in, they will see:
    * Group icon (allows them to search the database, filtered according to User Permissions)
    * Personal icon (takes them to their own account)
    * Search People (drop list; filters as they type; visible with the Group icon)
    * VIN / Driver's License (drop list; filters as they type)
  * When they select a person, the screen will display "<Name of current user> as <Role of selected person>" at the top
    * The screen will the display what the selected person would be able to see



  


  


Account Manager

  * When an Account Manger logs in, they will see the same as the individuals above. However, they will have the following additional items on their screen:
    * Search Vehicles (drop list of vehicles linked to their account)
    * View Map (button that brings up pings on a map that corresponds with the location of their vehicles)



  


  


Vehicle Details Screen

  * When a Vehicle is selected from the above list, it will open a new screen with various details for that vehicle, such as VIN, License Plate #, etc. It will also show a map with that vehicle's last known location.



  


  


Driver Details Screen

  * When a Driver is selected from the list on the first screen, it will open a new screen with various details for that Driver such as Vehicles, Last Known Location, Last Known Speed, etc.



  


  


Settings Screen

  * The app will have a Settings screen that will provide the options to:
    * Change phone number. NOTE: This will require a special confirmation process.
    * Change email address. NOTE: This will require a special confirmation process.



  


Development Specification

Mockup - [[File:Glen Zimmerman.pdf]]
