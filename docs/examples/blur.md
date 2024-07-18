---
title: "Blur"
---

# Blur

Here are some examples for blur operation on-the-fly.

### Original Image 

<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000932268822640000000000000000000521.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/000932268822640000000000000000000521.jpeg)</center>


### Simple Blur

Using the `i_o_blur` url command modifier you can blur your images on-the-fly. The args value to this modifier will specify the intensiveness of the blur operation.

Here are the original image with blur modification with 10 and 40 as intensiveness values. 

```
i_o_blur_10
```
<center>[![Blur]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_blur_10/000932268822640000000000000000000521.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_blur_10/000932268822640000000000000000000521.jpeg)</center>

```
i_o_blur_40
```
<center>[![Blur]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_blur_40/000932268822640000000000000000000521.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_blur_40/000932268822640000000000000000000521.jpeg)</center>

### Manual Selection Blur

The default behaviour of the blur image effect is to apply the blur function on the whole image. However you can select specific region to apply blur effect.

Using `i_c_x` and `i_c_y` you can set the center of the rectangle and using `i_h` and `i_w` you can specify the height and width of the region you want to apply blur effect. In this example we set the center of blur effect to (275, 275) and the rectangle dimension is (75, 75).


```
i_c_x_275,i_c_y_275,i_h_75,i_w_75,i_o_blur_25
```
<center>[![Blur]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_275,i_c_y_275,i_h_75,i_w_75,i_o_blur_25/000932268822640000000000000000000521.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_275,i_c_y_275,i_h_75,i_w_75,i_o_blur_25/000932268822640000000000000000000521.jpeg)</center>


### Multi-Selection Blur

#### Original Image 

<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000932433646790000000000000000001018.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/000932433646790000000000000000001018.jpeg)</center>

#### Multi-Selection

Using Inteliver command chain you can apply effects multiple times using `/` separator. With the help of this feature you can blur multiple regions.

Here, in the first part of the command chain we will blur a rectangle and in the second part we blur the face.

```
i_c_x_280,i_c_y_50,i_h_100,i_w_100,i_o_blur_25/i_c_face,i_o_blur_21
```
<center>[![Blur]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_280,i_c_y_50,i_h_100,i_w_100,i_o_blur_25/i_c_face,i_o_blur_21
/000932433646790000000000000000001018.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_280,i_c_y_50,i_h_100,i_w_100,i_o_blur_25/i_c_face,i_o_blur_21/000932433646790000000000000000001018.jpeg)</center>

### Face Blur

You can blur faces in your images using face selector and blur operation command.


```
i_c_face,i_o_blur_20
```
<center>[![Face Blur 1]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_o_blur_20/000932433646790000000000000000001018.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_o_blur_19/000932433646790000000000000000001018.jpeg)</center>


### Objects Blur

Using Inteliver A.I. object detection feature you can select different objects in your images and then blur them out.

In this example, by using object selector `i_c_object_person` we will blur the person in the image.

```
i_c_object_person,i_o_blur_20
```
<center>[![Face Blur 1]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_person,i_o_blur_20/000932433646790000000000000000001018.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_person,i_o_blur_20
/000932433646790000000000000000001018.jpeg)</center>

And we can also blur the car in the image.

```
i_c_object_truck,i_o_blur_20
```
<center>[![Face Blur 1]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_truck,i_o_blur_20/000932433646790000000000000000001018.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_truck,i_o_blur_20
/000932433646790000000000000000001018.jpeg)</center>

Or by using the command chain feature we can blur out the persons and cars in the image.

```
i_c_object_truck,i_o_blur_20/i_c_object_person,i_o_blur_20
```

<center>[![Face Blur 1]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_car,i_o_blur_20/i_c_object_person,i_o_blur_20/000932433646790000000000000000001018.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_car,i_o_blur_20/i_c_object_person,i_o_blur_20/000932433646790000000000000000001018.jpeg)</center>



!!! info
    You can lookup the object detection [API reference](../api-reference/object-detection.md) to see all the objects we detect in images.
