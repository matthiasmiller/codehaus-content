3\. *System-wide Configuration

  


Requirements

We will provide the following settings as system-wide configuration options:

  


  * # of Days Until Member Payment Due - This will be configured to 20 days from the SPE application approval date.
  * # of Days Until SPE Payment Due - This will be configured to 60 days from the SPE application approval date.
  * # of Days Until SPE Receipt Due - This will be configured to 90 days from the SPE application approval date.



  


We will also provide a setting for the Default Tax Year End Date. It will default to December 31.

  


Development Specification

My proposal for the default tax year end date--precision doesn't matter *that* much, since it's an overridable default. My vote is that we add a month drop list and day field, then simply make sure that it's a valid date for a non-leap year.

  


(The alternative is allowing leap day, then using YearInc to move from a leap year to the current year--but that's overengineered.)

  


Tim Reitz 01/22/2021: The clients do not want the calendar date picker.

  


Ellis Miller 02/08/2021: 

AppHosting settings:

[ ] 3 numbers

[ ] Month drop list / Day droplist -- with a CalcTaxYearEndDate(vYear) macro.

  


Target: 2 hrs
