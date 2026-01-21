32\. Phase 2 - Tracking by App

  


Requirements

The second phase will be tracking drivers with the Traccar Client app.

  


Rather than build a second app, the easiest way to enforce this is to require the Traccar Client service to be enabled for a user to log into their personal Driver portal in the main app.

  


This will also allow us to monitor app versions and force upgrades if there is a breaking item.

  


When implementing this, we will implement a way for users to share locations with each other. (Requests and shares are sent via text messages to the other individual. If they do not have the app installed, they are invited to sign up.)

  


This has potential benefits to end users:

  * Parents have the ability to track their teens, no matter what vehicle they're driving.
  * Employers are (ideally) able to match drivers to their individual trips.
  * Friends can share their location with each other. For example, Bill can ask Bob to share his location, or Bob can initiate sharing his location to Bill.
  * Account Administrators can submit explanations when the device gets unplugged.
  * It provides redundancy if the OBD is not tracking correctly.



  


Development Specification

TODO_VA: When we get to Phase 2, we will need to add a "Phone" device type. We will also need to show phones in the app.
