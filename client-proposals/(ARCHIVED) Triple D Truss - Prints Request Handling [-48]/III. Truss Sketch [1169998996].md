3\. Truss Sketch

  


Requirements

User Details:

  * On a Pending Request, the Sketch Pad will be available through a link called Edit Sketch below the request details.
  * Clicking this link with open the Sketch Pad in a new tab. Here the user can draw with their finger / mouse / trackpad. They can also enter text labels. 
  * When the request is finalized, the "View Sketch" will be added as a link at the bottom of the Truss Print Request.



  


Development Specification

  * We believe that sketches will always be tied to another record. If someone wants to use them generically, they should create a wrapper record type.
    * They will be lookup records named in the format of "SK-RecordType-RecordID-RecordSketchID" where RecordSketchID is some kind of ID within the context of a specific record.
    * This could use a macro using ActivityLevels and LookupTypes.
    * We could still link to these as [[SK0001]] where 1 is the autonumber (absolute value of list number)
    * In the case of truss prints, these would be named "SK-Orders-1234-01" where 1234 is the Sales Order number, and 01 is the Sketch auto-number from the record itself. 
  * Whenever we generate a request, we create a Pending Request Sketch ID that is a numeric auto-number counter.
    * Add a hidden RG field of Sketch ID. This is used for auto-numbering.
    * Disallow editing a sketch if it's on the sales order record. This works because we don't allow saving pending requests. Can Edit Record: Check if Sketch ID is on Sales Order.
  * The link will be generated such as: [https://tripled.apphosting.zone/Reports/Standard/Std_Open_Sketch?Asks=vAskID%32DD1234-01&"](https://tripled.apphosting.zone/Reports/Standard/Std_Open_Sketch?Asks=vAskID%32DD1234-01&"). This will launch the integration, which will auto-create it if needed. We use a report so we don't have to worry about breaking historical links if we move stuff around.
  * When the request is finalized, we append a "[[URL View Sketch]]" at the bottom of the Request Preview memo. Because the memo is read-only, this will look nice. 
  * Underlying "Sketch Record": 
    * Request ID
    * Rendered version of the sketch (either as a data URL or as an archived document attachment)
    * Any required metadata 
  * Interfaced as a full-screen editable sketch pad
  * Be able to type in text on this as well (for measurements). 
  *  See [https://techblog.geekyants.com/building-a-drawing-board-using-javascript](https://techblog.geekyants.com/building-a-drawing-board-using-javascript) for a good possible starting point.



Ellis Miller 10/26/2021: We are assuming that Matthias will do the integration and any fields that are needed on Sketch Record, etc unless specifically requested. We'll provide a simple record with an ID field and a Can Edit expression.

Matthias Miller 10/26/2021: That's good. I'll add anything else I need.
