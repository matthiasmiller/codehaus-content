12.1. Paper Contract Values

Matthias Miller 08/07/2025: TODO_SETH:

  * We need to be very clear between:
    * Value/Terms/Payment that were on the contract
    * VERSUS Value/Terms/Payment that we use internally for calculations
  * We need to store Paper Contract Values for
    * Contract Value
    * Contract Terms
    * Payment Amount
    * NOTE: If Amount * Terms <> Value, then the user MUST override terms. This means someone handwrote the wrong values on the contract. We will always round to 2 decimal places, and the company will always take the shortfall. For example:



Payment Rounding:

  * 7000 / 36 = 194.44444444
  * 6999.84 * 36 = 6999.84


  * Example 2
    * 6000 / 36 = 166.66666667
    * Payment = 166.67
    * 6000 / 166.67 = 35.99928001 "effective" month term



  


  * THEN
    * [ ] Override Checkbox
    * Override Contract Value
    * Effective Terms (Value / Amount)
    * Override Payment Amount
    * Override Reason (string; required)


