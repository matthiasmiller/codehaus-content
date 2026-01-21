13.2. Building Layout Record

  


Requirements

The building diagram will have:

  * ID
  * Last Version Number
  * Expected Version Number (editable macro used for collision handling)
  * Title
  * Width Feet
  * Length Feet
  * Shapes; RG of:
    * Name
    * Mid X
    * Mid Y
    * Width Feet
    * Length Feet
    * Text
    * Rotation (list of 0. 90. 180, 270)
  * PNG (rendered building diagram as archived document)



  


Development Specification

When copying a building record, save the building diagram in a hidden "Template Building Diagram". This will be used as the starting point for a new building diagram.
