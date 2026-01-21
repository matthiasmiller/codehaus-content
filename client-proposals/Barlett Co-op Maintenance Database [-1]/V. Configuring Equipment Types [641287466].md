5\. Configuring Equipment Types

  


Requirements

Bartlett Co-op will define types of equipment (e.g. Loader, Fork Lift, Truck, Bulk Tank, Anhydrous Tank) and specify deadlines for each type of equipment.

  


Equipment Types Report

In the Advanced | Configuration Menu, there will be a link to an "Equipment Types" report. 

  * This report will list all equipment types 
  * The report will columns for Type, # Active, # Inactive
  * It will have a button to create a new type
  * Clicking on a type will let you view/edit the record
  * There will be an option to view the equipment for that type



  


Equipment Type Record

The Equipment Type record will contain:

  * Type name (e.g. Bulk Tank)
  * Active checkbox 
  * Track - options for Hours, Miles, or blank. 
  * List of Deadlines -- multiple deadlines can be defined for each equipment type. Each deadline will contain:
    * Deadline Label (e.g. Replace Hose)
    * Deadline Frequency (Months) -- optional frequency of the deadline in months since the last occurrence.
    * Instructions -- optional text instructions to be displayed on the equipment record (e.g. "When replacing the hose....")



  


If there is any equipment with this type, the type cannot be deleted.

  


If there is any active equipment for this type, then the type cannot be made inactive.

  


Equipment types can be edited by users with the "Manage equipment list" permission.

  


Development Specification

Equipment Types Report

  * Grouped by Active and Inactive (show in gray)
  * Sorted by EquipTypeName
  * New button
  * Column for Equipment Type (name)
  * Hyperlink both the # Active and # Inactive to run the equipment scan report, filtered by equipment type, grouped by location, and Active vs Inactive



  


Equipment Type Record

  * This is a lookup record with EquipmentTypeName as the list field in the EquipmentTypes list
  * EquipTypeActive checkbox is used for an ActiveEquipmentTypes list (ConcatLookups)
  * Deadlines RG:
    * Deadline ID. This is a numeric ID OnInit set it to one higher than the max RG. Non-editable.
    * Deadline Label: Text. Required
    * Frequency (Months): Number. Optional.
    * Deadline Explanation: Wider Text column, optional.
  * Can't delete if any equipment exists for this



  


Uses some form of generated ID for each deadline (e.g. D101).
