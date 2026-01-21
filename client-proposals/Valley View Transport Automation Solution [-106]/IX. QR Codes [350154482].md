9\. QR Codes

  


Requirements

The Solution uses QR codes instead of traditional barcodes to track individual furniture pieces through the warehouse workflow. Each QR code links to a unique URL (formatted like [https://vvt.wsgi.silverloom.io/qr/12345/ABCD](https://vvt.wsgi.silverloom.io/qr/12345/ABCD)) that can be scanned using standard smartphones—eliminating the need for specialized barcode scanning hardware. When warehouse staff scan a code, they're prompted to authenticate, then taken to a mobile-responsive interface tailored to their role and the piece's current status.

  


The scanning interface is organized into three sections for optimal workflow:

  


1\. The top of the screen displays the current Bill of Lading number, drop number, and left/right navigation buttons to move between stops, along with a high-level summary of the scanned item.

2\. The middle section contains action buttons that change based on the user's role—pullers see "Mark as Pulled," loaders see "Mark as Loaded," and delivery drivers see "Mark as Delivered"—with buttons only appearing when appropriate based on the order's current status.

3\. The bottom section shows a scrollable list of all orders for the current customer, with the just-scanned item highlighted, allowing staff to see what else needs attention for that stop.

  


Pullers are required to work through customers sequentially, though warehouse managers can override or defer items with explanatory notes when exceptions arise. This design ensures that all pieces of an order (like the 9 components of a bedroom set) get accounted for before the truck leaves, preventing the "wrong truck" mistakes that currently cost VVT time and customer satisfaction.

  


Development Specification

  * $5-10K
    * >> Raspberry Pi connected to a printer, watching for print requests (?)
    * OR - printer connected to the tablet ??
    * >> QR Code PDF Generation to print
  * Page View for Order
    * Expect:
      * 1-2 x30s
      * 1-2 r20s
      * 1-2 WSGI templates
    * Login
    * Conditionally showing different buttons based on Status + User Permissions
    * View of all items



  


  


Authentication Ideas:

  * User Name / Password
    * Replicate Invest logic
  * User Name / Password
    * Flask Session
    * Redirect to Silverloom login page
    * SL login page redirects to r20
    * r20 redirects back to WSGI w/ HMAC + User ID
    * NOTE - use a macro with ComponentWebURL for the r20 to know the redirect link from WSGI land)



  


  * Logout
    * Clear session
    * Redirect to silverloom logout page
    * Could homepage report redirect out to the WSGI, taking care to avoid infinite redirects?


  * Code via Email
  * Code via SMS (requires $1500-3k setup + $20/mo + Twilio account)


