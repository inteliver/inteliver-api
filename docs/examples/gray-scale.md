---
title: "Gray Scale"
---

# Grayscale

Here are some examples for making an image grayscale on-the-fly.

### Original Image 

<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000932545312870000000000000000000023.jpeg){ width="300" }]({{ mediaBase }}/media/v1/{{ cloudName }}/000932545312870000000000000000000023.jpeg)</center>

### Default Grayscale 

Using the `i_o_gray` url command modifier you can make your images grayscale on-the-fly.

```
i_o_gray
```

<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_gray/000932545312870000000000000000000023.jpeg){ width="300" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_gray/000932545312870000000000000000000023.jpeg)</center>

### Manual Selection Grayscale

The default behaviour of the grayscale effect is to apply the grayscale function on the whole image. However you can select specific region to make it grayscale.

Using `i_c_x` and `i_c_y` you can set the center of the rectangle and using `i_h` and `i_w` you can specify the height and width of the region you want to make grayscale. In this example we set the center of grayscale effect to (100, 300) and the rectangle dimension is (200, 200).

When comparing to the original image you see that the bus ad banner is now grayscaled.

```
i_c_x_100,i_c_y_300,i_h_200,i_w_200,i_o_gray
```
<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_100,i_c_y_300,i_h_200,i_w_200,i_o_gray/000932545312870000000000000000000023.jpeg){ width="300" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_100,i_c_y_300,i_h_200,i_w_200,i_o_gray/000932545312870000000000000000000023.jpeg)</center>

### Objects Grayscale

Using Inteliver A.I. object detection feature you can select different objects in your images and then grayscale them.

In this example, by using object selector `i_c_object_car` we will only make the car in the image grayscale.

```
i_c_object_car,i_o_gray
```
<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_car,i_o_gray/000932545312870000000000000000000023.jpeg){ width="300" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_car,i_o_gray/000932545312870000000000000000000023.jpeg)</center>

You can use variety of selection methods including face selectors to grayscale faces as well.

Using Inteliver command chain you can apply effects multiple times using `/` separator. With the help of this feature you can grayscale multiple regions.

