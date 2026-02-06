3\. Org Chart

  


Requirements

We need to be able to define an org chart with role name, job descriptions, training manual, and up-lines.

  


Certain roles need to be available across multiple divisions. For example, "thrift store manager" applies to each of the thrift store locations. "House parent" applies to each of the child care homes.

  


The org chart needs to be visible to all users. We will have a report that shows the org chart. If individuals fill multiple roles, they will be displayed multiple times.

  


Each job role will define:

  * Available time off policies (explained separately)
  * Business holidays (New Years, New Years Eve, Christmas, Christmas Eve, Good Friday, Thanksgiving, Memorial Day, Labor Day, Independence Day, etc)



  


Most of these will be scheduled by Month+Day, except for Good Friday, Thanksgiving, Black Friday, Memorial Day, and Labor Day.

  


We will also define Employment Type, which will include "Salaried", "Full-Time", and "Part-Time". This type, in combination with the role, will determine the vacation policy available to each individual.

  


USER SPECIFICATION

Each role can also have multiple divisions. For example, the houseparent role can define divisions for “Central” and “Hannah’s House”.

  


To avoid complications, once you define divisions for a role, none of the child roles can specify divisions. For example, once you divide the houseparent role into divisions, you can’t create a different set of divisions for nannies.

  


Development Specification

  * Are we going to run into issues if we restrict information from other records? I think we plan to only restrict certain pieces, not entire records.


