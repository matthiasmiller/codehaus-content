5.4.5. Claim - General Release Section

*Done. 

  


  * General Release section:
    * Override Client Name (checkbox)
    * Override Client (plain text; visible and required if "Override Client Name" is checked)
    * Our Insured (auto-set and read-only; with the following details / behaviors:
      * if "Driver" = "Client" (i.e. if the Client was the driver): "<CLIENT NAME>";
      * if "Driver" ≠ "Client" or "(Other/Non-household Driver)": "<CLIENT NAME>, AND THE DRIVER <"DRIVER">";
      * if "Driver" = "(Other/Non-household Driver)": "<CLIENT NAME>, AND THE DRIVER <"NAME">") 
    * Other Party (plain text; required)
    * Accident Date (read-only; in the format: "THE 1ST OF JANUARY 2023")
    * Amount (read-only; the "Total Release" amount; in the format: "ONE HUNDRED DOLLARS AND 0 CENTS ($100.00)")


