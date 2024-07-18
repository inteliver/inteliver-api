---
title: "Selection"
date: 2019-09-19T06:31:45+04:30
weight: 1
---

## Image Selection

You can apply Inteliver operations on different part of image. For selecting the part of image you want to apply
an operation you can use the following different selections.

* Window Selection
* Face Selection
* Objects Selection

### Window Selection

By default the image processing operations are applied to the whole image. However you can manually select a window and then apply the operation. 

Using `i_c_x` and `i_c_y` you can set the center of your window and using `i_h` and `i_w` you can set the width and height of the window respectively.

### Face Selection

Using Inteliver A.I. face detection you can choose to apply an operation on only faces.
For example you can crop the image based on the faces or blur or pixelate a face to provide privacy. 

Using `i_c_face` you can select to apply the operation on the faces present in your images.

### Objects Selection

Using Inteliver A.I. object detection you can apply different operations on images. For example you can crop the objects in the image or sharpen a specific object.

We detect many object in the images. Using `i_c_object` and the desired object as arg to this command you can automatically apply the operations on the specific objects.

Using A.I. features possibilities are simply endless.

### Text Selection

!!! info
    This feature will be released soon.


Using Inteliver A.I. text detection you can apply image processing functions only on texts. For example pixelating a car plate or applying faster OCR on texts in an image.

!!! info
    In the following examples for each operation we show you how to exploit the full potential of these selection methods.
