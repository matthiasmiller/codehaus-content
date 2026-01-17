
# Strasburg Pallet - Settings

## Records

### SPC Settings Record

Sections and Fields:

* Lumber Price section:
  * Lumber Est. $/BF (currency; 2 decimals)
* Labor Target section:
  * Labor Target % (percentage; 2 decimals)
  * Labor $/Man-Hr (currency; 2 decimals)
* Sawing Pricing section:
  * Sawing BF/Man-Hr (number; 0 decimals)
  * Sawing Base O/H $/BF (currency; 2 decimals)
  * Sawing Spec. O/H $/BF (currency; 2 decimals)
* Assembly Pricing section:
  * Machine BF Per Man-Hr (number; 0 decimals)
  * Machine Overhead $ / BF (currency; 2 decimals)
* Score Weights section:
  * Board Feet Weight (number; 2 decimals)
  * Fastener Weight (number; 2 decimals)
  * Parts Weight (number; 2 decimals)
* Sizer Waste section:
  * Sizer Default Waste % (percentage; 0 decimals)
  * Sizer Default Addl. Count (number; 0 decimals)
* Assembly Setup Time section:
  * Setup Time Base (Mins) (number; 0 decimals)
  * Setup Time by Outer Dimensions; embedded spreadsheet of:
    * Outer Dim. (Ft) (number; 0 decimals; required)
    * Addl. Mins (number; 0 decimals; required)
  * Setup Time by Parts; embedded spreadsheet of:
    * # Parts (number; 0 decimals; required)
    * Addl. Mins (number; 0 decimals; required)
  * Setup Time by Fastener Types; embedded spreadsheet of:
    * # of Fastener Types (number; 0 decimals; required)
    * Addl. Mins (number; 0 decimals; required)
* Assembly Time Coefficients section:
  * Assembly Time Coefficients; embedded spreadsheet of:
    * Type (drop list of Coefficient Types; required)
    * Feature (drop list of Coefficient Features; required)
    * Assembly Method (drop list of Assembly Methods; required)
    * Fastener (drop list of Raw Materials; required)
    * Item Category (drop list of Item Categories; required)
    * Method (drop list of Coefficient Methods; required)
    * Value (number; 9 decimals; required)
    * Mean (number; 9 decimals; required)
    * Std Dev (number; 9 decimals; required)
* Settings section:
  * Name (string)