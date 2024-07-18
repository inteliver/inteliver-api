---
title: "Pixelate"
---

# Pixelate
Here are some examples for pixelate operation on-the-fly.

### Original Image 

<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000932453002500000000000000000000097.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/000932453002500000000000000000000097.jpeg)</center>

### Default Pixelate 

Using the `i_o_pixelate` url command modifier you can pixelate your images on-the-fly. The args value to this modifier will specify the intensiveness of the pixelate operation.

Here are the original image with pixelate modification with 5 and 20 as intensiveness values.

```
i_o_pixelate_5
```
<center>[![Pixelate]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_pixelate_5/000932453002500000000000000000000097.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_pixelate_5/000932453002500000000000000000000097.jpeg)</center>

```
i_o_pixelate_20
```
<center>[![Pixelate]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_pixelate_20/000932453002500000000000000000000097.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_pixelate_20/000932453002500000000000000000000097.jpeg)</center>

### Manual Selection Pixelate

The default behaviour of the pixelate image effect is to apply the pixelate function on the whole image. However you can select specific region to apply pixelate effect.

Using `i_c_x` and `i_c_y` you can set the center of the rectangle and using `i_h` and `i_w` you can specify the height and width of the region you want to apply pixelate effect. In this example we set the center of pixelate effect to (150, 100) and the rectangle dimension is (200, 200).

```
i_c_x_150,i_c_y_100,i_h_200,i_w_200,i_o_pixelate_10
```
<center>[![Pixelate]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_150,i_c_y_100,i_h_200,i_w_200,i_o_pixelate_10/000932453002500000000000000000000097.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_150,i_c_y_100,i_h_200,i_w_200,i_o_pixelate_10/000932453002500000000000000000000097.jpeg)</center>

### Multi-Selection Pixelate

Using Inteliver command chain you can apply effects multiple times using `/` separator. With the help of this feature you can pixelate multiple regions.

Here, in the first part of the command chain we will pixelate a rectangle and in the second part we blur the face.

```
i_c_x_150,i_c_y_100,i_h_200,i_w_200,i_o_pixelate_10/i_c_face,i_o_pixelate_10
```

<center>[![Pixelate]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_150,i_c_y_100,i_h_200,i_w_200,i_o_pixelate_10/i_c_face,i_o_pixelate_10/000932453002500000000000000000000097.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_150,i_c_y_100,i_h_200,i_w_200,i_o_pixelate_10/i_c_face,i_o_pixelate_10/000932453002500000000000000000000097.jpeg)</center>



### Face Pixelate

You can pixelate faces in your images using face selector and pixelate operation command.

```
i_c_face,i_o_pixelate_10
```

<center>[![Pixelate]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_o_pixelate_10/000932453002500000000000000000000097.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_o_pixelate_10/000932453002500000000000000000000097.jpeg)</center>


### Objects Pixelate

Using Inteliver A.I. object detection feature you can select different objects in your images and then pixelate them.

In this example, by using object selector `i_c_object_person` we will pixelate the person in the image.

```
i_c_object_person,i_o_pixelate_10
```

<center>[![Pixelate]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_person,i_o_pixelate_10/000932453002500000000000000000000097.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_person,i_o_pixelate_10/000932453002500000000000000000000097.jpeg)</center>

And we can also pixelate the dog in the image.

```
i_c_object_dog,i_o_pixelate_10
```

<center>[![Pixelate]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_dog,i_o_pixelate_10/000932453002500000000000000000000097.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_dog,i_o_pixelate_10/000932453002500000000000000000000097.jpeg)</center>

!!! note
    You can lookup the object detection [API reference](../api-reference/object-detection.md) to see all the objects we detect in images.
