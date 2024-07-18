---
title: "Crop"
---

# Crop

Here are some examples for crop operation on-the-fly.

#### Original Image 

<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000931783192390000000000000000000704.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/000931783192390000000000000000000704.jpeg)</center>

#### Simple Crop

Let's say we want to crop the image to 300 pixels by 300 pixels. Here is the url command to do that. The center of the image will be used as the center for crop operation in this example.

Using `i_h_300` and `i_w_300` will set the requested size and `i_o_crop` will specify the crop operation.

```
i_h_300,i_w_300,i_o_crop
```
<center>[![Crop]({{ mediaBase }}/media/v1/{{ cloudName }}/i_h_300,i_w_300,i_o_crop/000931783192390000000000000000000704.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_h_300,i_w_300,i_o_crop/000931783192390000000000000000000704.jpeg)</center>

#### Change Center

As mentioned in the previous example, the default crop operation will crop the image based on the center of the image.

Using center selectors you can change this default. `i_c_x` and `i_c_y` will set the X and Y of the desired center for crop operation. Top left corner of the image is (0, 0). In this example we set the center of the image to be (400, 250).

```
i_c_x_400,i_c_y_250,i_h_300,i_w_300,i_o_crop
```

<center>[![Crop]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_400,i_c_y_250,i_h_300,i_w_300,i_o_crop
/000931783192390000000000000000000704.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_x_400,i_c_y_250,i_h_300,i_w_300,i_o_crop
/000931783192390000000000000000000704.jpeg)</center>

#### Center on Objects

Using our A.I. object detection features you can set the center of crop operation on objects presents in your image. Using `i_c_object` and the name of the object we can set the center on a specific object.

In this example lets say we want to crop the truck image. We are using center selector `i_c_object_truck` to achive this.

```
i_c_object_truck,i_h_250,i_w_250,i_o_crop
```

<center>[![Crop]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_truck,i_h_250,i_w_250,i_o_crop
/000931783192390000000000000000000704.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_truck,i_h_250,i_w_250,i_o_crop
/000931783192390000000000000000000704.jpeg)</center>

We can also crop the image based on the person in it. Using center selector `i_c_object_person` will do the trick.

```
i_c_object_person,i_h_200,i_w_200,i_o_crop
```

<center>[![Crop]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_person,i_h_200,i_w_200,i_o_crop
/000931783192390000000000000000000704.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_person,i_h_200,i_w_200,i_o_crop
/000931783192390000000000000000000704.jpeg)</center>

!!! info
    You can lookup the object detection [API reference](../api-reference/object-detection.md) to see all the objects we detect in images.


#### Round Crop

It is also possible to crop the image in a round style. Using `i_o_rcrop` operator will crop the image in a round style. Here are some of the examples with round crop.

```
i_h_300,i_w_300,i_o_crop,i_o_rcrop
```

<center>[![Crop]({{ mediaBase }}/media/v1/{{ cloudName }}/i_h_300,i_w_300,i_o_crop,i_o_rcrop/000931783192390000000000000000000704.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_h_300,i_w_300,i_o_crop,i_o_rcrop
/000931783192390000000000000000000704.jpeg)</center>

Adding a PNG format conversion will transparent the corners for better desing.

```
i_h_300,i_w_300,i_o_crop,i_o_rcrop,i_o_format_png
```

<center>[![Crop]({{ mediaBase }}/media/v1/{{ cloudName }}/i_h_300,i_w_300,i_o_crop,i_o_rcrop,i_o_format_png/000931783192390000000000000000000704.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_h_300,i_w_300,i_o_crop,i_o_rcrop,i_o_format_png/000931783192390000000000000000000704.jpeg)</center>

!!! note
    Please note if you are specifying args for crop operation you have to first crop the image using `i_o_crop` operation and then style it with a round crop using `i_o_rcrop`.

And here is the result of setting the center of the image on the truck and round crop it with PNG format. 

```
i_c_object_truck,i_h_250,i_w_250,i_o_crop,i_o_rcrop,i_o_format_png
```

<center>[![Crop]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_truck,i_h_250,i_w_250,i_o_crop,i_o_rcrop,i_o_format_png/000931783192390000000000000000000704.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_truck,i_h_250,i_w_250,i_o_crop,i_o_rcrop,i_o_format_png/000931783192390000000000000000000704.jpeg)</center>


### Face Crop

Using Inteliver A.I. face detection feature, you can also set the center of the crop on the faces detected in the image.

#### Original Image

<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000932170183830000000000000000000848.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/000932170183830000000000000000000848.jpeg)</center>

#### Simple Face Crop

Using `i_c_face` selector you can set the center of the crop on the face.

```
i_c_face,i_h_200,i_w_200,i_o_crop
```

<center>[![Face Crop]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_200,i_w_200,i_o_crop/i_h_200,i_o_resize/000932170183830000000000000000000848.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_200,i_w_200,i_o_crop/000932170183830000000000000000000848.jpeg)</center>

#### Rounded Face Crop

Combining round crop and PNG format conversion with centering the crop operation on face will result in an automatic profile picture.

```
i_c_face,i_h_200,i_w_200,i_o_crop,i_o_rcrop,i_o_format_png
```
<center>[![Face Crop]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_200,i_w_200,i_o_crop,i_o_rcrop,i_o_format_png/000932170183830000000000000000000848.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_200,i_w_200,i_o_crop,i_o_rcrop,i_o_format_png/000932170183830000000000000000000848.jpeg)</center>

<!-- ### Face Crop
```
i_c_face,i_h_200,i_w_200,i_o_crop
```
<center>[![Face Crop]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_200,i_w_200,i_o_crop/i_h_200,i_o_resize/000931751163850000000000000000000800.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_200,i_w_200,i_o_crop/000931751163850000000000000000000800.jpeg)</center>

### Face Crop with Rounded Crop
```
i_c_face,i_h_200,i_w_200,i_o_crop,i_o_rcrop
```
<center>[![Face Crop]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_200,i_w_200,i_o_crop,i_o_rcrop/000931751163850000000000000000000800.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_200,i_w_200,i_o_crop,i_o_rcrop/000931751163850000000000000000000800.jpeg)</center>

```
i_c_face,i_h_200,i_w_200,i_o_crop,i_o_rcrop,i_o_format_png
```
<center>[![Face Crop]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_200,i_w_200,i_o_crop,i_o_rcrop,i_o_format_png/000931751163850000000000000000000800.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_200,i_w_200,i_o_crop,i_o_rcrop,i_o_format_png/000931751163850000000000000000000800.jpeg)</center>

```
i_c_face_1,i_h_150,i_w_150,i_o_crop,i_o_rcrop,i_o_format_png
```
<center>[![Face Crop]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face_1,i_h_150,i_w_150,i_o_crop,i_o_rcrop,i_o_format_png/000931751163850000000000000000000800.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face_1,i_h_150,i_w_150,i_o_crop,i_o_rcrop,i_o_format_png/000931751163850000000000000000000800.jpeg)</center>

```
i_c_face_2,i_h_150,i_w_150,i_o_crop,i_o_rcrop,i_o_format_png
```
<center>[![Face Crop]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face_2,i_h_150,i_w_150,i_o_crop,i_o_rcrop,i_o_format_png/000931751163850000000000000000000800.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face_2,i_h_150,i_w_150,i_o_crop,i_o_rcrop,i_o_format_png/000931751163850000000000000000000800.jpeg)</center> -->
