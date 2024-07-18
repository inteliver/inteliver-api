---
title: "Rotate"
---

# Rotate

Here are some examples for rotate operation on-the-fly.

### Original Image 

<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000932228434370000000000000000000458.jpeg){ width="300" }]({{ mediaBase }}/media/v1/{{ cloudName }}/000932228434370000000000000000000458.jpeg)</center>

### Simple Rotate

Using `i_o_rotate` url command modifier you can rotate the image on-the-fly. The integer after the `i_o_rotate` specify the rotate degree. Here we are rotating our original image by 90 degree and 180 degree.

```
i_o_rotate_90
```
<center>[![Rotate]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_rotate_90/000932228434370000000000000000000458.jpeg){ width="300" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_rotate_90/000932228434370000000000000000000458.jpeg)</center>

```
i_o_rotate_180
```
<center>[![Rotate]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_rotate_180/000932228434370000000000000000000458.jpeg){ width="300" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_rotate_180/000932228434370000000000000000000458.jpeg)</center>


### Scale Rotate

After the rotation degree you can specify a scale. This float value will determine the scale of the image after the rotation.   

```
i_o_rotate_60_1.8
```
<center>[![Rotate]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_rotate_60_1.8/000932228434370000000000000000000458.jpeg){ width="300" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_rotate_60_1.8/000932228434370000000000000000000458.jpeg)</center>


### Rotate Pivot

By default the rotation operation set the pivot of rotation to the center of the image. 

However you can set the rotation pivot either by explicitly using `i_c_x` and `i_c_y` commands or other selecting commands such as `i_c_face` to set the rotation pivot on face.

```
i_c_x_250,i_c_y_250,i_o_rotate_60_2
```
<center>[![Rotate]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_250,i_c_y_250,i_o_rotate_60_2/000932228434370000000000000000000458.jpeg){ width="300" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_250,i_c_y_250,i_o_rotate_60_2/000932228434370000000000000000000458.jpeg)</center>
