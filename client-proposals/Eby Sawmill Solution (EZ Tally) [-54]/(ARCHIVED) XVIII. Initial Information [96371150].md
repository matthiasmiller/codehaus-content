18\. Initial Information

DONE_TR - Review and archive

  


Heidi Coblentz 06/16/2022: Received an email from David Musselman asking about software for a sawmill. 

  


Original email: We are looking to develop an app. The basic function would be to create tallies (list of logs) of logs as they come to our mill. And to build tallies to be loaded into containers for export. There are several data points for each log – Species, Grade, Diameter, Length, Price, Tag number, Cost (the diameter and length and price need to run through a formula to calculate this). We would of course want to be able to run a variety of reports on the data in the database. We really like the platform that it looks like you all work from. It would be ideal to us to be able to access the information in the office as soon as it is entered in the log yard. There are other functions that we are thinking about but I wanted to simply reach out to you and see if this sound like something that you all could do for us or not. I would be glad to have a conversation with you about it anytime.

  


I responded with template asking about company size and internet access.

  


Heidi Coblentz 06/17/2022: He responded with this info:

  


Second email:  Sure. That’s understandable. You want to know a better idea of the size of our company and the project.

  * Yes we have excellent internet and we have multiple wireless access points to make it accessible everywhere on our property. (We have an inhouse IT guy and he keeps everything up to speed).
  * We have approx. 50 employees. About 10 of them would be users on the app.



Also we scale approximately 15-20 loads of logs per day and each load has an average of 30-40 logs. (450-800 logs per day)

  


I sent him a scheduler link to schedule a meeting with Ian.

  


  


  


814.767.8060

814.414.9935 cell

[david@ebysawmill.com](mailto:david@ebysawmill.com) 

  


Ian Miller 06/27/2022: 

  


Tell me a little more about your business--what do you do, what services do you provide? 

  * The premise is we're a sawmill
  * Buying logs and sawing board
  * We sell 50% of the logs as logs
  * Our logs are either:
    * Our own logs
    * Logs we bought from someone else
  * We buy 
    * Timber tracts - rights to log land; then we hire loggers to log the land
      * Pay a set cost for the timber tract (eg. $50,000 for the tract); OR
      * Pay a percentage of all logs sold (eg. 40, 50, 60%)
    * Logs from others - they bring it to us, we measure, assess and purchase the logs
  * We make:
    * Wood pellets
    * Mulch
    * Boards, lumber, etc. 
  * We also sell the logs as-is; some we're shipping overseas in shipping containers 
  * Currently using software for buying and selling our logs
    * We started with software built on an old Windows mobile platform; went out of business, not updating
    * We recently started using another software that also has an Android app; they sold it to us saying they are willing to customize it but we had to dump $10-$15,000 to get started; now they're saying they are not able to customize and we need to use it as-is



  


What are the challenges or problems you're facing? What are you looking to solve with custom software? 

  * Log records 
    * As we bring the logs across our log deck, we enter:
      * Wood species
      * Wood grade
      * Diameter and length
        * The diameter and length give us sq. footage, which gives us the total price
      * This calculates the total price for the log based on the variables above
      * Each log record is linked to the vendor, or timber tract owner 



Matthias Miller 08/09/2022: Configuration:

  * BF formula
  * Grade + Species = ??



Tim Reitz 08/08/2022: Log record: 

DONE_CH: Tim Reitz 08/16/2022: OR Do we have "Received Load" and "Export Load" records, with RGs for logs?

  * Species
  * Grade
  * Diameter
  * Length
  * ?Board Feet? (calculated)
    * Matthias Miller 08/09/2022: Doyle, Scribner, and International -
    * [https://timbeter.com/help/doyle-log-rule/](https://timbeter.com/help/doyle-log-rule/)
    * Scribner? - [https://timbeter.com/help/scribner-decimal-c/](https://timbeter.com/help/scribner-decimal-c/)
    * International - [https://timbeter.com/help/international-1-4-log-rule/](https://timbeter.com/help/international-1-4-log-rule/)
    * Matthias Miller 08/22/2022: NOTE - They use the Doyle scale
  * Price
  * Tag number
  * Cost (the diameter and length and price need to run through a formula to calculate this)
  * ? Eby's log vs. purchased log?
  * Vendor
  * Timber Tract Owner
  * ?Date entered? 


  * Matthias Miller 08/09/2022: Invoicing?
    *   * Export loads
    * When we are exporting a load of logs we are figuring what's going out 
    * If they get shipped overseas, w may need to have more data on the export such as shipping container seal number and shipping container number 



Tim Reitz 08/08/2022: Export Load record: 

  * ?Logs (
  * Shipping Container #
  * Shipping Container Seal #
  *   * 

  * Timber tract management
    * *Timber tract = a piece of property that we have purchased the rights to log
    * A tool for valuing the timber, and then calculating the percentage we're paying out to the owner
      * Broken down into tiers based on value of the logs
      * The greater the value of the logs, the smaller percentage goes to the owner 
    * A way to track all the dates associated with a timber tract contract
      * When we started logging
      * When we finished
      * When the contract ends
      * When payments are due, if doing a payment plan
    * If we're paying them a percentage, then every log will need to be associated with that timber tract record so that we can calculate the percentage that needs to be paid out to the tract owner
    * A place to track costs related to that tract, so that we can run reports of profit margin (profit or loss) on that specific timber tract



Tim Reitz 08/08/2022: Timber Tract record: 

  * Logging Start Date
  * Logging End Date
  * Contract Start Date? 
  * Contract End Date
  * Payments Due (
  * Percentage due to owner
  * ?Logs from this tract? 
  * Costs (
  * 

  * A record for each log that comes onto our lot
    * Each log has its own data associated with it
      * Wood species
      * Wood grade
      * Diameter and length
    * Each log record is linked to the vendor, or timber tract owner 
  * 3 records
    * Log records
    * Timber tract records
    * Export loads records 



  


Tim Reitz 08/08/2022: Reporting? 

Tim Reitz 08/09/2022: Tally and Reports doc from the client: [https://drive.google.com/drive/folders/1pLG-jotpNbFwpFO1_GhY0F5IcALPjepA](https://drive.google.com/drive/folders/1pLG-jotpNbFwpFO1_GhY0F5IcALPjepA)

DONE_NM: Split this doc into 2: p1 and p2-3, save them in Drive, and link them with the corresponding sections in the proposal.

  


We want our software cloud basedIan Miller 07/05/2022: 

  * Want it stored in the cloud immediately, accessible on the road or in the office or in the yard
    * We have really good internet, 2 sources, very good speeds
    * NOTE: Would be nice to have ability to do calculations off the grid but syncing to the database once coming back online 
      * We are out in the country, our one provider is wireless internet provider; don't want there to be lags 
      * Occasionally we'll go out on the road, it would be great if calculations could happen off the grid 



  


What would success look like to you? How would it make you feel? 

  


  * Clarity, what are our profit margins, or losses 
  * Streamlining our data management



  


Follow up:

[X] Send follow up email with abbreviated call notes and roadmap pdf

[X] Send call notes to "Solutions" group (if client with no internet, send to "Digital Bridge" group)

  


  


Ian Miller 07/05/2022: Call w/ Darrell and David

  


Darrell 

  * They would be very interested in expediting it with the in-person component
  * Whatever we can do to help streamline this and help it move quickly, we're at that point
  * We have a lot of ideas about what works, what doesn't; what's helpful and what's frustrating; would be helpful to have someone there, in-person, seeing all we're doing and using
  * I could see it being beneficial to do in-person in both phases; most impact on phase 1
  * 8-15 hours of phone calls vs. in person, you'll get triple the information
  * I'd be game to start with that
  * 2 hours away
  * I have no hour if there needs to be an adjustment in the fees for the high level design
  * We do business and we understand cost 
  * End of august, early September not available
  * Other than July 15, we're both available for the next 30 days



  


Standard Questions for Each Design: 

  


[X] Offline support

  


[X] What devices do you plan to use?

  


[X] Do you want to use Contact Types? If yes, what should they be?  

  * Vendor contact type
  * Biggest reason for linking to a contact (if we will) is to be able to email the reocnciliation to the land owner



  


[X] Do you want to use the calendar date picker? 

  * Use the number pad



  


[X] Do you want to import data from an existing system or spreadsheet? If yes, what? 

  * No. Soft rollout.



  


[X] What data access restrictions/permissions do you want? 

  * They don't need to access reports
  * Sales prices
  * Administrator
  * Yard Boys who are loading
    * They couldn't create tallies
  * Log Scaling
    * Simply gives you the ability to enter log data, and access



  


  * Edit tract
    * Create tally
    * Delete tally
    * Create vendor
    * Delete vendor
  * Anyone outside of Leo accessing Log Track Analysis reports
    * Restrict all financial fields as well
    * When they're loading the outbound, the only thing is to load the final information for that, with the ability to edit an existing tally, but not create a new tally
    * Hiding menu options is sufficient
  * Matthias Miller 08/29/2022: Moved



  


[X] Do you want to use time tracking for employees? If yes, by hour or by day and hour? 

Matthias Miller 08/22/2022: DONE_TR/DONE_NM: Include a timestamp on a tally

Niccolas Miller 08/29/2022: David said on a call that he sees no point in having a time stamp on report.

  


[X] What about syncing? ie QB

  * None.



  


[X] What do invoices look like?

  * N/A



  


TODO: Create sections & document the answers as needed.

  


  


  


Matthias Miller 08/09/2022: Sketch and Notes

Yard tallies

Vendor| Tract

  


Log

Species

Grade

Diameter

Length

Price

BF

Deduction

Net

Total value

Notes
