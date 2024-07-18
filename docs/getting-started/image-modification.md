---
title: "Image Modification"
---

# Image Modifications

Modify your image data using a variety of image processing functions. These functionality includes
the following.

- [x] [Resize](../examples/resize.md)
- [x] [Crop](../examples/crop.md)
- [x] [Rotate](../examples/rotate.md)
- [x] [Flip](../examples/flip.md)
- [x] [Blur](../examples/blur.md)
- [x] [Pixelate](../examples/pixelate.md)
- [x] [Sharpen](../examples/sharpen.md)
- [x] [Gray Scale](../examples/gray-scale.md)
- [x] [Text Overlay](../examples/text-overlay.md)


### Here are simple examples:

### Resize
=== "Original Image"

    <center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000923288308380000000000000000000815.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/000923288308380000000000000000000815.jpeg)</center>
  
    <center>Original Image </center>

=== "Modified Image"
  
    <center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/i_w_250,i_h_250,i_o_resize_keep/000923288308380000000000000000000815.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_w_250,i_h_250,i_o_resize_keep/000923288308380000000000000000000815.jpeg)</center>

    <center>Real-Time Resize to `250x250px`</center>

### Crop
=== "Original Image"

    <center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000932511633980000000000000000000518.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/000932511633980000000000000000000518.jpeg)</center>
  
    <center>Original Image </center>

=== "Modified Image"
  
    <center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/i_h_300,i_w_300,i_o_crop/000932511633980000000000000000000518.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_h_300,i_w_300,i_o_crop/000932511633980000000000000000000518.jpeg)</center>

    <center>Real-Time Crop to `300x300px`</center>

### Rotate
=== "Original Image"

    <center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000923289401200000000000000000000201.jpeg){ width="300" }]({{ mediaBase }}/media/v1/{{ cloudName }}/000923289401200000000000000000000201.jpeg)</center>
  
    <center>Original Image </center>

=== "Modified Image"
  
    <center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_rotate_180,i_o_format_png_1/000923289401200000000000000000000201.jpeg){ width="300" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_rotate_180,i_o_format_png_1/000923289401200000000000000000000201.jpeg)</center>

    <center>90degree Rotate</center>


### Pixelate
=== "Original Image"

    <center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000931373825510000000000000000000417.jpeg){ width="250" }]({{ mediaBase }}/media/v1/{{ cloudName }}/000931373825510000000000000000000417.jpeg)</center>
  
    <center>Original Image </center>

=== "Modified Image"
  
    <center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_pixelate_10/000931373825510000000000000000000417.jpeg){ width="250" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_pixelate_10/000931373825510000000000000000000417.jpeg)</center>

    <center>Real-Time Pixelate</center>

### Gray Scale
=== "Original Image"

    <center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000923289217250000000000000000000487.jpeg){ width="250" }]({{ mediaBase }}/media/v1/{{ cloudName }}/000923289217250000000000000000000487.jpeg)</center>
  
    <center>Original Image </center>

=== "Modified Image"
  
    <center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_gray/000923289217250000000000000000000487.jpeg){ width="250" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_gray/000923289217250000000000000000000487.jpeg)</center>

    <center>Real-Time Gray Scale</center>

Each operation has [examples](../examples/index.md) and you can also refer to [API reference](../api-reference/index.md) section for complete list of args.

The examples uses inteliver intuitive URL query commands. Please refer to [intuitive query commands](how-inteliver-works.md) for more information on our URL query commands. 

!!! note
    For more information on how to apply these functionalities using our SDKs please refer to [libraries](../libraries/index.md).

## Image Selection

You can apply the operation on different part of image. For selecting the part of image you want to apply
an operation you can use the following different selections.


There are examples of each one in [selection section](../examples/index.md) in examples.

* Window Selection
* Face Selection
* Objects Selection



