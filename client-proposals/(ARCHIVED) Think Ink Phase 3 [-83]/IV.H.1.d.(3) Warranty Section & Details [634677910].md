4.8.1.4.3. Warranty Section & Details

  


Requirements

Overview: Think Ink sells various extended warranties as sales items; they register it with the manufacturer and link it with the Device's Serial #. These are to be tracked on Sales Item records with a Category of "Warranty".

  


Accessed via: 

  * Configure Warranties Report (see the corresponding section of this proposal) 



  


Custom Fields (visible for Warranty SKU type): 

  * Warranty Details section
    * Terms (required; number field with no decimals; includes a "months" label after the field, like this: "[___] months")  



  


Data Access: All users can view and edit

  


Validations: 

  * Warning on save if a Warranty-type Sales Item is deactivated while being used by one or more active Devices: "This Warranty currently is being used by one or more active Devices." 



  


Other Notes: 

  * There should be one or more "Custom Warranty" items set up by Think Ink, to allow for handling edge cases. The number of months would be determined on the warranty record, but there could be multiple ones, such as "Custom Warranty - 3 months", "Custom Warranty - 6 months", etc.
  * Note that this record should have a name, date, and time stamp for Created and Last Modified, as well as a link to access Modification History (standard).



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=336746928](https://docs.google.com/spreadsheets/d/1XpXzA29sECIbqfYOQC6VPagvOEh1uuhErBS-LsAFhV8/edit#gid=336746928)
