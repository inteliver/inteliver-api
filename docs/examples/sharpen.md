---
title: "Sharpen"
---

# Sharpen

Here are some examples for sharpening operation on-the-fly.

### Original Image 

<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000932511633980000000000000000000518.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/000932511633980000000000000000000518.jpeg)</center>


### Default Sharpen 

Using the `i_o_sharpen` url command modifier you can sharpen your images on-the-fly.

```
i_o_sharpen
```
<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_sharpen/000932511633980000000000000000000518.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_sharpen/000932511633980000000000000000000518.jpeg)</center>


### Manual Selection Sharpen

The default behaviour of the sharpening image effect is to apply the sharpen function on the whole image. However you can select specific region to apply sharpen effect.

Using `i_c_x` and `i_c_y` you can set the center of the rectangle and using `i_h` and `i_w` you can specify the height and width of the region you want to apply sharpen effect. In this example we set the center of sharpen effect to (275, 300) and the rectangle dimension is (100, 100).

Using sharpen effect we made the car plate in this example much more clearer. Compare the car plate in this image with the original image.

```
i_c_x_275,i_c_y_300,i_h_100,i_w_100,i_o_sharpen
```
<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_275,i_c_y_300,i_h_100,i_w_100,i_o_sharpen/000932511633980000000000000000000518.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_275,i_c_y_300,i_h_100,i_w_100,i_o_sharpen/000932511633980000000000000000000518.jpeg)</center>

### Objects Sharpen

Using Inteliver A.I. object detection feature you can select different objects in your images and then sharpen them.

In this example, by using object selector `i_c_object_car` we will only sharpen the car in the image.

```
i_c_object_car,i_o_sharpen
```
<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_car,i_o_sharpen/000932511633980000000000000000000518.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_car,i_o_sharpen/000932511633980000000000000000000518.jpeg)</center>

!!! note
    You can lookup the object detection [API reference](../api-reference/object-detection.md) to see all the objects we detect in images.


### Face Sharpen

You can sharpen faces in your images using face selector and sharpen operation command. This will both make blured faces in your image more clearer and also can be used for better face recognition.

#### Original Image 

<center>[![Pixelate]({{ mediaBase }}/media/v1/{{ cloudName }}/000931439336620000000000000000000556.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/000931439336620000000000000000000556.jpeg)</center>

#### Face Sharpen

```
i_c_face,i_o_sharpen
```

<center>[![Pixelate]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_o_sharpen/000931439336620000000000000000000556.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_o_sharpen/000931439336620000000000000000000556.jpeg)</center>


Using Inteliver command chain you can apply effects multiple times using `/` separator. With the help of this feature you can sharpen multiple regions.

<!-- ### Multi-Selection Sharpen
```
i_c_x_180,i_c_y_300,i_h_100,i_w_100,i_o_sharpen/i_c_face,i_o_sharpen
```
<center>[![Sharpen]({{ mediaBase }}/media/v1/inteliver/i_c_x_180,i_c_y_300,i_h_100,i_w_100,i_o_sharpen/i_c_face,i_o_sharpen/i_h_200,i_o_resize/000837226335640000000000000000000912.jpg)]({{ mediaBase }}/media/v1/inteliver/i_c_x_180,i_c_y_300,i_h_100,i_w_100,i_o_sharpen/i_c_face,i_o_sharpen/000837226335640000000000000000000912.jpg)</center> -->
