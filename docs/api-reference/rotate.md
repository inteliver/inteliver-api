---
title: "Rotate"
---

### Rotate Operation

<table>
  <tr>
    <th>Command</th>
    <th>Details</th>
  </tr>
  <tr>
    <td>i_o_rotate_{degree}</td>
    <td>Rotate the image with respect to the degree which is the degree of rotation. degree is an integer between 0 and 360. Positive values mean counter-clockwise rotation (the coordinate origin is assumed to be the top-left corner).</td>
  </tr>
  <tr>
    <td>i_o_rotate_{degree}_{scale}</td>
    <td>Rotate the image with the specified degree and also apply the isotropic scale factor to the rotation. Rotation scale is an integer between 0 and 10.</td>
  </tr>
</table>

!!! tip
      Default pivot point is the center of the image.


!!! tip
      Setting the center before the rotation operation will rotate the image with respect to the new center as pivot point.
