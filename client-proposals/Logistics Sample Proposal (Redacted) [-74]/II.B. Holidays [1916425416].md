2.2. Holidays

  


Requirements

We will provide settings to control the list of holidays for the entire Pickup & Delivery system. The holidays would be a list of holidays defined in the system.

  


Development Specification

Holiday Refactoring

[ ] Move Holidays and HolidayTypes (list, fields, and detail screens) along with the HolidayDate macro, reports, etc. to the AppHosting Base catalog.

  


Holiday Enhancements

[ ] Hide the Month and Type fields for Good Friday.

[ ] Add two checkboxes to the Holiday (not visible for Good Friday; only if the type is for a specific date):

[ ] Observe on Friday if it falls on Saturday

[ ] Observe on Monday if it falls on Sunday

[ ] Update HolidayDate to respect these checkboxes.

[ ] Add Current Year and Next Year dates to the detail screen (same as the report)

  


Global Route Settings

[ ] Add a child screen to the AppHosting.zone settings for Routes setting.

[ ] Add an auto-push report called "Configure Route Settings" that directly opens the Routes child screen on AppHosting settings.

[ ] In the AppHosting.zone settings, add a Holidays section . It should be an RG of Holidays (list field). Add read-only columns for Current Year and Next Year dates. Include Move Up/Move Down buttons.
