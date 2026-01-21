3\. Detail Screens: Building

  


Requirements

Add the following fields to the end of the building's Location RG:

  * Hauler (list of haulers; read-only if complete)
  * Hauler Load # (number; no decimals; required if Hauler is specified, default to 1; read-only if complete)
  * Scheduled Date (read-only if complete)
  * Scheduling Notes
  * Damaged? (checkbox)



  


Add an RG of pictures:

  * Date
  * S3 ID
  * Upload Picture (link)
  * View Picture (link)



  


Development Specification

Matthias Miller 08/26/2021: This whole thing goes to Josh.

  


NOTE: Ideally, the Scheduling Notes column in the RG is about the same width as the column in the report.

  


TODO_WSGI: Pictures
