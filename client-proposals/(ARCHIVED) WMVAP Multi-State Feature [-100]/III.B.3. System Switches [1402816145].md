3.2.3. System Switches

  


Requirements

*Documentation N/A

  


The following System Switch(es) should be set as following:

  


Development Specification

Ellis Miller 09/04/2024: Nothing to code

  


  


Tim Reitz 08/20/2024: Wrote up this CR for setting these for ZWA/PA: [[[IN10477](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10479&)]] - ZWA - Configure Silverloom Settings & System Switches (post-ZWI development).

  


Ellis Miller 04/24/2025: NOTE: We are typically using readonly system switches for items that we configure as part of development on a per-system basis and that should not be modified. We use Silverloom Settings for any items we expect the client might modify.

  


The main exception is the Resource Menu ID settings which have to be in system switches because menu pages are not allowed to reference database records.

  


Ellis Miller 04/24/2025: _VA: I am proposing that the plan system switches (except for wiki menu) are readonly only defined in the outer catalogs. We list them here for reference but actually define them when we implement a client system.

_VA: Tim Reitz 04/24/2025:

[X] Default all to N/A in the base catalog (main living spec)

[X] Delete all "Default Value" items and replace with "N/A"

[X] Update "Set To" (text pointing to the Deployment / Development sections) with the following approach:

[X] Max Contact Num: Deployment

[X] Resource Menu Configurations: Deployment

[X] All others: Dev 

  


_VA: Tim Reitz 04/24/2025: Make all of these changes in the ZWI proposal as well.
