3.32. Delivery Scheduling - Auto-Print Sale Tags

  


Requirements

We will provide an application you can install on one of your computers to automatically print out Sale Tags. You will be able to select a printer to print to, and it will automatically print to that printer whenever a sold tag is created.

  


This can be installed on the POS or on another computer at the store. You will need to install O&K Print Router, which you are currently using on the POS. It is a simple program that allows one print command to go to multiple locations.

  


Development Specification

Matthias Miller 09/14/2020: Windows App....print via PDF

  * Qt Tray Icon w/ Browser Config
  * Background pulling
  * Start on startup
  * Send PDF to Qt PDF
  * Ghostscript to convert to PCL and then to print -- [https://stackoverflow.com/questions/27195594/python-silent-print-pdf-to-specific-printer](https://stackoverflow.com/questions/27195594/python-silent-print-pdf-to-specific-printer)


