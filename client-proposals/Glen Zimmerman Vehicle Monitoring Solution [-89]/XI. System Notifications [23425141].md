11\. System Notifications

HLD notes: 

  


The software will send email and/or text message notifications. 

  


Potential notifications include:

  * Driving Curfew - movement outside time window
  * Absolute Speed - any speed over X mph
  * Over Speed Limit Threshold - any speed of at least X mph over the speed limit (This should be contingent based on practicality. It might be possible share waypoints and calculate the speed limit from Google's API at [https://developers.google.com/maps/documentation/roads/speed-limits](https://developers.google.com/maps/documentation/roads/speed-limits))
  * Rapid Acceleration / Deceleration
  * Sharp Turns
  * Geofencing Notifications (entering or leaving an area)
    * Could also be travel outside of X radius of point



  


It may also include notifications reported by the vehicle or Traccar, such as:

  * Maximum Speed (as reported from the vehicle)
  * Low Tire Pressure (as supported by vehicle)
  * Fuel Level (as supported by vehicle)
  * Oil Life (as supported by vehicle)
  * Any other vehicle error codes



  


This will be sorted as events on the device.

TODO_VA: Tim Reitz 06/12/2025: Some sort of Event / Incident / Notification record to track the details? 

  


The specifics of these notifications will be determined based on the information available from the vehicle and from the OBD.

  


  


TODO_VA: Tim Reitz 10/03/2025: Per conversation with the client today, it would be good to have a high-profile notification for scenarios where a vehicle is stolen and an urgent notification is needed. Notification would go to the Reseller Rep, Group Admin(s), and Master Administrator(s), but not the Account Manager or Driver. Probably all notification channels - SMS, email, in-app. Perhaps a Device Status, or more likely a special checkbox (called "Send Emergency Notification for Any Activity" or something like that).

  


  


TODO_VA: Tim Reitz 11/18/2025: We probably will be having Traccar send the SMS notifications. 

  


TODO_VA: Tim Reitz 11/18/2025: Ellis had a good point: We probably want to have limits on how many alerts go out, so that if something glitches and it appears that a Device is in another part of the world (like we had with Ben's test device today), parents don't get hundreds of bogus alerts.
