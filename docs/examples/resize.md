---
title: "Resize"
date: 2019-09-19T06:22:01+04:30
weight: 5
---

# Resize

Here are some examples for resize operation on-the-fly.

### Original Image 

<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000931751163850000000000000000000800.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/000931751163850000000000000000000800.jpeg)</center>

### Simple Resize

Let's say we want to resize the image to 200 pixels by 200 pixels. Here is the url command to do that.

```
i_h_200,i_w_200,i_o_resize
```

`i_h_200` will set height to 200 and `i_w_200` also set the width to 200. `i_o_resize` is the operation command.

<center>[![Resize]({{ mediaBase }}/media/v1/{{ cloudName }}/i_h_200,i_w_200,i_o_resize/000931751163850000000000000000000800.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_h_200,i_w_200,i_o_resize/000931751163850000000000000000000800.jpeg)</center>

### Keep Ratio

As obvious in the modified image, ratio is not preserved. If you would like to keep the original image ratio when resizing you can use `i_o_resize_keep` instead.

```
i_h_200,i_w_200,i_o_resize_keep
```

<center>[![Resize]({{ mediaBase }}/media/v1/{{ cloudName }}/i_h_200,i_w_200,i_o_resize_keep/000931751163850000000000000000000800.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_h_200,i_w_200,i_o_resize_keep/000931751163850000000000000000000800.jpeg)</center>

### Face Center

You can use face selector `i_c_face` to resize the image centered on the face. 

```
i_c_face,i_h_200,i_w_200,i_o_resize_keep
```

<center>[![Resize]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_200,i_w_200,i_o_resize_keep/000931751163850000000000000000000800.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_200,i_w_200,i_o_resize_keep/000931751163850000000000000000000800.jpeg)</center>


### Combining Operations

Using face selector plus a round crop `i_o_rcrop` you can create an automatic round profile picture. Using `i_o_format_png` will change the image format to PNG to be transparent in the corners.

```
i_c_face,i_h_200,i_w_200,i_o_resize_keep,i_o_rcrop,i_o_format_png
```
<center>[![Resize]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_200,i_w_200,i_o_resize_keep,i_o_rcrop,i_o_format_png/000931751163850000000000000000000800.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_200,i_w_200,i_o_resize_keep,i_o_rcrop,i_o_format_png/000931751163850000000000000000000800.jpeg)</center>

### One Dimension Resize

You can resize an image by specifying only height or width. The other dimension will be calculated according to the original image ratio.

The following image is resized to have a height of 200 pixels.

```
i_h_200,i_o_resize
```
<center>[![Resize]({{ mediaBase }}/media/v1/{{ cloudName }}/i_h_200,i_o_resize/000931751163850000000000000000000800.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_h_200,i_o_resize/000931751163850000000000000000000800.jpeg)</center>


The following image is resized to have a width of 200 pixels.

```
i_w_200,i_o_resize
```
<center>[![Resize]({{ mediaBase }}/media/v1/{{ cloudName }}/i_w_200,i_o_resize/000931751163850000000000000000000800.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_w_200,i_o_resize/000931751163850000000000000000000800.jpeg)</center>
