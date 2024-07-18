---
title: "Selection"
---


### Window Selection
<table>
  <tr>
    <th>Command</th>
    <th>Details</th>
  </tr>
  <tr>
    <td>i_c_x_{value}</td>
    <td>Set the value of X-dimension for the center point of the selection rectangle. e.g. i_c_x_100 will set the center point X-value to 100. Value can be an integer and in pixels or it can be in [0, 1] range float number which is interpreted as percentage of the original image size.</td>
  </tr>
  <tr>
    <td>i_c_y_{value}</td>
    <td>Set the value of Y-dimension for the center point of the selection rectangle. e.g. i_c_y_100 will set the center point Y-value to 100. Value can be an integer and in pixels or it can be in [0, 1] range float number which is interpreted as percentage of the original image size.</td>
  </tr>
  <tr>
    <td>i_h_{value}</td>
    <td>Set the height of the selection rectangle. e.g. i_h_200 will set the selection rectangle height to 200 pixels. Value can be an integer and in pixels or it can be in [0, 1] range float number which is interpreted as percentage of the original image size. 
    </td>
  </tr>
  <tr>
    <td>i_w_{value}</td>
    <td>Set the width of the selection rectangle. e.g. i_w_200 will set the selection rectangle width to 200 pixels. Value can be an integer and in pixels or it can be in [0, 1] range float number which is interpreted as percentage of the original image size.
    </td>
  </tr>
  <tr>
    <td>i_h_ih</td>
    <td>Set the height of the selection rectangle to image height.
    </td>
  </tr>
  <tr>
    <td>i_w_iw</td>
    <td>Set the width of the selection rectangle to image width.
    </td>
  </tr>
</table>

### Face Selection

<table>
  <tr>
    <th>Command</th>
    <th>Details</th>
  </tr>
  <tr>
    <td>i_c_face</td>
    <td>Set the selection rectangle to the most focused face.</td>
  </tr>
  <tr>
    <td>i_c_face_{value}</td>
    <td>Set the selection rectangle to the n`th face present in the image. The face number automatically asigned according to the focusness of that specefic face and starting from zero. e.g. i_c_face_2 will select the third face in the image.
    </td>
  </tr>
</table>

### Object Selection

<table>
  <tr>
    <th>Command</th>
    <th>Details</th>
  </tr>
  <tr>
    <td>i_c_object_{value}</td>
    <td>Set the selection rectangle to the object specified by the value. e.g. i_c_object_car will set the selection rectangle around the car objects in the image.</td>
  </tr>
</table>

???+ info

      The list of objects we detect are documented in object detection [API reference](object-detection.md).

