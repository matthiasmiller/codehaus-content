1\. Overview

  


Requirements

Business Goals

The goal of this project is to streamline the ordering and cut process for the production of poly furniture.

  


By our estimation, this project should measurably increase profitability of your business by:

  


  * Freeing 1 hour each day for you as the owner (totaling 20 hours each month, or six weeks per year) by streamlining the cut lists



  


  * Freeing at least 2 hours/week for your staff and 1 hour/week for yourself (totaling nearly four weeks per year) by eliminating the need to re-cut during the day



  


  * Reducing material costs by eliminating the need to re-cut pieces.



  


  * Increasing efficiency by consolidating orders to create the same types of furniture on the same day.



  


This section describes how you will use the system in your day-to-day workflow.

  


Entering Orders

Whenever you receive an order, you will enter it into the software. This will include:

  * Dealer Name (which you can select from a list or add another dealer)
  * Order Date
  * Order Deadline
  * QuickBooks Invoice #
  * Customer PO



  


In the order, you will list each of the pieces of furniture:

  * Quantity (# of pieces of furniture)
  * Code (with option to choose from a list)
  * Primary Color (choice from a list)
  * Secondary Color (choice from a list)
  * Cut Date (this will be blank when you create the order)
  * Assembly Date (this will be blank when you create the order)



  


It will then give you an option to calculate the cuts required for this order. This will generate a list of the number of boards (broken down by color) required to fulfill the order.

  


Once you've entered the order into the software, you'll be able to create cut lists for each day.

  


Creating Cut Lists

Every afternoon, you will open the software to view all furniture that needs to be cut.

  


This will list all pieces of furniture, grouped by the deadline and sorted by the furniture type, making it easy to combine similar furniture pieces. It will also show:

  * Quantity
  * Primary / Secondary Colors
  * Dealer Name



  


You will check off the pieces of furniture that you'd like to cut, and click "Add to Cut List". It will prompt for a date, defaulting to the following business day. This will then add those pieces to that day's cut list.

  


Because we prompt for a date, you could schedule your cut list for an entire week if you choose.

  


Printing Cut Lists

Once you're done setting up the Cut List, you will click "View Cut List".

  


Once you open the cut list, you will be able to enter the scraps that you have on hand. Any 16' pieces of lumber will be entered as scrap. Then, you will have an option to calculate the cuts for that day.

  


Then, you click Print to print a summary that includes:

  


  * Overview. A summary of all pieces of furniture to be created, including quantity, description, and colors.
  * Cuts. A list of all cuts for all of the pieces of furniture. These should be listed from longest to shortest, grouped by color.
  * Parts. A list of all parts for all pieces of furniture. These should be listed in alphabetical order, then sorted by color.



  


If you need to edit cut lists, you can open the original order and remove or edit the cut date. You will also have an option to view and print prior cut lists.

  


Creating and Printing Assembly List

Once a piece of furniture has been cut, you will be able to create an Assembly List. This will show a list of all cut but unassembled pieces of furniture.

  


Just like the "Creating Cut Lists" section, this will list all pieces of furniture, grouped by the deadline and sorted by the furniture type, making it easy to combine similar furniture pieces. It will also show:

  * Quantity
  * Primary / Secondary Colors
  * Dealer Name



  


You will check off the pieces of furniture that you'd like to cut, and click "Add to Assembly List". It will prompt for a date, defaulting to the following business day. This will then add those pieces to that day's assembly list.

  


Because we prompt for a date, you could schedule your assembly list for an entire week if you choose.

  


Once you've set up the Assembly List, you will click "View Assembly List", which will print a report with a summary of all pieces of furniture to be created, including quantity, description, and colors

  


Reports

Every year (or more frequently if you wish), you will be able to run a report showing the total quantity of furniture, along with a breakdown of all types and color combinations.

  


The color breakdown is especially important, because QuickBooks does not allow this breakdown.

  


You will be able to specify a date range, based on the order date.

  


How Cuts Get Calculated

The software will determine the most efficient way to cut the board by minimizing waste. This means that it may use additional boards if it can save end pieces for future use.

  


Development Specification

Matthias Miller 04/03/2018: Joe's Phone # (719) 849-3996

  


  * Use a ghost row for all RGs
  * The Cut List report should show things scheduled to be cut today, as well as unscheduled pieces.
  * The Cut List will be a lookup type, based on the date YYYY-MM-DD. This will link specific pieces of furniture to the cut list.
  * Need to validate that a part can't exceed the board length



  


His price sheet - [[File:2018-04-09 16-40.pdf]]
