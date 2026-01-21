27\. Sales Opp Notes

Ben Reitz 05/14/2024: Glen sent the following email:

  


I understand you do custom software development? 

I am very early in the process of creating a product that will require software development in both cloud server storage and mobile app creation and I was wondering how your process works to review the project?

  


It is going to revolve around large fleets of vehicle speed reporting / tracking and location related statistical reporting as well as vehicle diagnostic info. As noted, it is very early in the design phase and was exploring if you have the capability to assist with this project. 

  


I can provide more details as needed when we can connect.  

  


I asked about internet and employees.

  


Ben Reitz 05/15/2024: Glen replied:

  


This is actually for a churchwide project. So that could involve 2 to 3,000 vehicles potentially lots more. 

Yes, we do have internet access available. 

  


I do have much more detail to share but wasn’t sure how the best format to get that to you? I listed out the concept below. It is open to adjustments and or recommendations. 

  


Each vehicle would have a plug in ODB-II dongle that has cell card connectivity. (An alternative may be waiting till a wifi or Bluetooth data is in range instead)

These would report statistics to a dedicated hosted cloudserver running software such as Traccar provides. 

  


Each dongle or group of dongles would have an account with account specific parameters associated with it. 

                Alerts we are looking to collect and export is overspeed, erratic driving, high rpm, heart beat, etc. These would trigger immediate text message alerts to responsible party. 

  


                Other data reporting would be vehicle engine diagnostics, location, and most other data points that are visible thru dongle. 

  


We also are considering an app of smartphones that would also report much of the same data for coverage when in vehicle with no dongles. 

This app could also have basic level peer group location sharing as an option. 

  


I offered a call with Ellis for May 24th.

  


Ben Reitz 05/16/2024: Call confirmed for the 24th.

  


Ben Reitz 05/24/2024: Ellis and I had our call with Glen today. Here are the call notes: [https://docs.google.com/document/d/1n_UsPeo5-xiCCOE2JLvwOUp8k6ZwgGqb_ceSsLo_adA/edit](https://docs.google.com/document/d/1n_UsPeo5-xiCCOE2JLvwOUp8k6ZwgGqb_ceSsLo_adA/edit)

  


Overview:

Call Summary:

  * Located in New Holland, PA
  * Looking for a software that can help parents teach their children responsible driving
  * Part of the Weaverland Mennonite Conference (knows Bruce)
  * This software would be indirectly tied with the brotherhood aid plan
  * Tracar ([https://tracar.de/en/](https://tracar.de/en/) ) has an open source software that can be used for entire fleet management, as well as ODB-II devices
  * Glen thought Tracar looks intriguing but realizes that it would need a management interface to manage the accounts, etc.
  * Having it tie into the Aid plan would be a possibility in the future
  * Privacy permissions are going to have to be very well thought through
  * In the long run, it would be nice to have it available both in the app store and via website



  


Thoughts from Ellis:

  * This looks very doable
  * Maybe we could integrate with Tracar so that Tracar looks at it as one entire fleet. Then our software would be the connector between the users and Tracar. Our software would then be where parents, etc., would go in and review data
    * This would also be ideal in case Tracar goes away or something. Then they don’t have to rebuild everything, just simply integrate with a new fleet management software
  * Ellis somewhat offered a HLD but said he’d like to talk with the others before giving a HLD price, since this is a complex project



  


Next Steps:

  * Ellis will talk with Matthias and Josh to talk through the model and see what questions and comments they have
  * Ben will send Project Design Overview and System Screenshots
  * Ellis thinks he can be in touch next week with a proposal for a HLD



  


Ellis Miller 06/06/2024: We think this is possible. We'd like to offer a HLD for $3500. 

  


Ellis Miller 06/06/2024: Verbally offered Glen a HLD at 3500. This will be a standard HLD. We will do some some preliminary research to see if we can tie into the API's. As HLD progresses, we may offer additional R&D for a proof of concept at T&M with an estimate of costs. 

  


Glen has confirmed and I'm asking Ben to send him our standard documents and connect with him for the downpayment and to get scheduling started.

  


Ben Reitz 06/06/2024:  I sent over the documents and reached out to Matthias to find out when works best for him to do the HLD.

  


  


Matthias Miller 07/26/2024: 

  *   * New angles where fleets and employers might want to tap into it and use it as well.



  


  


  * Tested various other devices that are commercially available
  * This particular one is part of the exploration is the one that has the server - Traccar 
    * Some vehicles pipe everything out
    * Traccar can do different levels of data integration on the backend



  


Two Kinds of Tracking:

  * Vehicle
  * Mobile (could use the Traccar app)



  


On certain models of dongles they have deduplication.

It runs independently

Traccar used a dongle device and a bluetooth to your app...

  


  


User Levels:

  * Master Administrator Access - full access everywhere
  * Reseller Administrator - Account / Accounts (i.e. tech support companies who do work for cell phone controls, etc and could be dealer)
  * Head of Household / Head of Business - administrative access to devices on their account
  * Actual User / Dongle User



  


Back of Napkin:

  * Autocreate user accounts in the backend traccar system
  * Being able to push a serial number / IMEI to the back end + also bring in the VIN of the vehicle



  


  * Pulling in vehicle + phone data
  * Storing that appropriately & figuring out what kind on reporting
  * Alerts
    * exceeded distance from X
    * exceeded speed threshhold
    * exceeded acceleration / deceleration



  


  * Use latitutude and latitutde
    * If you want a visual, you need to tie it into a map



  


  * Make it appealing for people to get in on the app -- that's a - to cover when the vehicle doesn't have a tracker & as a secondary reference point



  


  * Had looked into an accountability portal & user base -- they looked at it, because they're doing Internet Filtering, etc -- and this would just be looked
    * This is like Teen Driving Safety
    * Administrative Portal App



  


Statistical Information - err on the side of transparency, that what the parent can see

  


  


PRIORITY:

  * PHASE 1 - DONGLE first
    * Contact Type
      * Master Administrator
      * Account Group Administrator
      * Reseller Administrator
      * Account Administrator
      * Driver



  


  * Account Group
    * i.e. Weaverland PA, Weaverland by state
    * For each account type, specify the administrators for that account type



  


  * Account
    * Account Group (required)
    * Reseller
    * Administrators
    * Members
    * Which alerts to who for which vehicle? Do you break it down by class? Email & Text Message



  


  * Account Administrator
    * Church Name
    * Reseller Name
    * Members
    * Which alerts do they want to get?
      * 


  


  * Vehicles
    * Account Administrator
    * automatically tie back to the reseller
    * Desc (from OBD)
      * VIN (UID for the vehicle)
      * Color
      * Year
      * Make
      * Model
      * These can be pulled OBD
    * License Plate



  


  * Date / Time / Latitutde / Longitude
  * One of two ways to track driving events:
    * Either going to report it with the position, or store separate driving events. This depends on the device, traccar, and how it gets report.
    * [https://freematics.com/store/index.php?route=product/product&product_id=98&tracking=5fbca3beebc8d](https://freematics.com/store/index.php?route=product/product&product_id=98&tracking=5fbca3beebc8d)



  


  * Error Codes
    * Different classes of alerts (critical, informational, mildly annoying)



  


  * Alerts
    * Driving Curfew - Movement outside time window
    * Absolute Speed Threshold
    * Over Speed Limit Threshold -- is there any 
      * [https://developers.google.com/maps/documentation/roads/speed-limits](https://developers.google.com/maps/documentation/roads/speed-limits)
      * What is the practicality of that?
    * Rapid Acceleration / Deceleration
    * Sharp Turns
    * Will Record Maximum Speed of the vehicle -- you can pull this out of the vehicle, and if the vehicle reports a new maximum speed, and it changes
      * i.e. what information is available & when it resets
    * Travel outside of X radius of point
    * Low Tire Pressure alert
    * Fuel Level (?)
    * Oil Life
    * Any other vehicle error codes (air filter clogged) - could be others that are available



  


  


  * The dongle is the shipped part of it -- what they plug it into, they don't care, except for reporting information. And would be surprised at a grassroots level, they will automatically report what vehicle they're plugged into
  * In their database, how they want to track it, so that this vehicle has a clean record, and this one doesn't, 
    * Always, report data based on VIN not on dongle



  


  * associated administrative portal + user portal to see statistical tracking information



  


  * show vehicle information on map



  


  * HELP
    * LOCATE - shoot back reverse geocode, current speed, for all vehicles (max out on 5-10 vehicles)
    * % of users w/ only text message access - 30-40% on that, and depending on groups it could be higher, and could be the only method



  


  


  * App Experience -- russian nesting dolls
    * Master Administrator Levels



  


  * Reseller Logins
    * List of Account Administrators



  


  * Account Login
    * List of Driver



  


  


  * PHASE 2 - APP second
    * communications back and forth with circle groups of friends -- allow or disallow your friends to see your location & where you're at
    * One of the things that a lot of them use that quite a bit -- one of the things that's annoying -- i..e legitimate times when you don't care to let them know
      * if they make a request to letyou know where you're at, and if you don't opt in at any time
      * but if you're the parent, you don't have the privilege at that
    * App to explain why it was unplugged



  


  


"Freematics ONE+"
