7.2.1. Exceptions

  


Requirements

The Production and Payroll Verification Report will include an Exceptions section that highlights potential issues or concerns in the payroll and production numbers. These are generated automatically.

  


Specifically:

  


  * All buildings that were completed that week, with one or more missing stations. For example, "Invoice #______ was completed on ______ without any time recorded for station _______."



  


  * All employees with time tracking enabled but without submitted hours (including PTO for hourly employees). For example, "John Troyer is a (hourly employed or salaried employee using time tracking) but does not have any hours specified on the time card."



  


  * If work orders exceed production bonus. "The work orders were $450.44, but the production bonus was $0.00."



  


Development Specification

I propose using a macro with multiple child macros. This makes it easy to re-use for the exception email that gets sent to Duane every Monday morning.
