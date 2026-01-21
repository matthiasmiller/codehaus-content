3.3. User Groups

  


Requirements

The Solution will be configured to have the following user groups:

  * Administrator (standard user group): Used for a user who has full access to the Solution. 
  * Batch Processes (standard user group): Used for __



TODO_CH: Tim Reitz 12/27/2023: What is this used for? 

  * Standard User (standard user group): Used for a user who does not have full access to the Solution. 
  * Log Buyer (EZ Tally-specific user group): Used for a user who handles the Yard Tally side of things. 
  * Export Scaler/Loader (EZ Tally-specific user group): Used for a user who handles the Export Tally side of things. 



  


Each group has specific permissions for use of the software. 

  


All user groups other than Administrator are set up and configured within the system. This can be done by CodeCrafters/CodeHaus or an admin user.

  


Note that users must be part of each user group that applies to them. For example: 

  * Full admin: Administrator + Log Buyer + Export Scaler/Loader 
  * Standard log buyer: Standard User + Log Buyer 
  * Etc.



  


Development Specification

Tim Reitz 12/27/2023: Note that the "System" user needs to have full permissions (must be part of each user group).
