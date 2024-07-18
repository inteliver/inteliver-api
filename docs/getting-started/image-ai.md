---
title: "Image A.I. Algorithms"
---

Inteliver currently supports out-of-the-box `Object Detection` and `Face Detection`. 

!!! info
    Background Removal is our next feature in A.I. algorithms.

## Object Detection

Using Inteliver you can detect the objects in each image. You can either use this metadata or you can select
based on each object and apply the desired operation.

Here is the returend result after using object detection command.

!!! tip
    Object detection can be used to automatically fill image tags or search images semantically in a large dataset of images.

=== "Original Image"

    ```
    {{ mediaBase }}/media/v1/cloudname/resource.jpeg

    ```

    <center>![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000932453002500000000000000000000097.jpeg "Original Image"){ width="300" }</center>


=== "Object Detection"

    ```
    {{ mediaBase }}/media/v1/cloudname/i_o_detect/resource.jpeg
    ```

    <center>![Object Detection]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_detect/000932453002500000000000000000000097.jpeg "Object Detection"){ width="300" }</center>


### Operation on Objects
Using object detection feature of inteliver you can modify images semantically.

Lets say we want to crop the cars in a set of images:

=== "Original Image"

    ```
    {{ mediaBase }}/media/v1/cloudname/resource.jpeg

    ```

    <center>![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000923288812730000000000000000000687.jpeg "Original Image"){ width="300" }</center>


=== "Object Operation"

    ```
    {{ mediaBase }}/media/v1/cloudname/i_c_object_truck,i_o_crop/resource.jpeg
    ```

    <center>![Object Detection]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_object_truck,i_o_crop/000923288812730000000000000000000687.jpeg "Object Detection"){ width="300" }</center>

!!! note
    Here we first select car's object by `i_c_object_truck` and then crop it using `i_o_crop` operation.

There are also more examples in [object detection examples](../examples/object-detection.md).

!!! info
    you can also refer to [API reference](../api-reference/object-detection.md) section for complete list of args.


## Face Detection

Using A.I. algorithms and deep learning face detection neural networks, Inteliver enables you to detect all the faces present in your image data.

Using Inteliver you can detect the faces in each image. You can either use this metadata or you can select
based on each face and apply the desired operation.

### Profile Picture
Here is an example to extract a profile picture out of the user image.

=== "Original Image"

    ```
    {{ mediaBase }}/media/v1/cloudname/resource.jpg
    ```

    <center>![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000923289297500000000000000000000683.jpeg "Original Image"){ width="500" }</center>


=== "Profile Picture"

    ```
    {{ mediaBase }}/media/v1/cloudname/i_c_face,i_h_200,i_w_200,i_o_crop,i_o_rcrop,i_o_format_png/resource.jpg
    ```

    <center>![Profile Picture]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_200,i_w_200,i_o_crop,i_o_rcrop,i_o_format_png/000923289297500000000000000000000683.jpeg "Profile Picture")</center>


!!! tip
    If the image containes more than one face, the faces will be numbered and accessible through each face numbers.
    The face number automatically asigned according to the focusness of that specefic face.

### Multiple Faces

Here is an image with a two faces.

=== "Original Image"

    ```
    {{ mediaBase }}/media/v1/cloudname/resource.jpg
    ```

    <center>![Two of faces]({{ mediaBase }}/media/v1/{{ cloudName }}/000931404155200000000000000000000353.jpeg "Two of faces"){ width="500" }</center>

=== "Choose First Face"

    ```
    {{ mediaBase }}/media/v1/cloudname/i_c_face_0,i_h_250,i_w_250,i_o_crop,i_o_rcrop,i_o_format_png/resource.jpeg
    ```

    <center>![Apply on first face]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face_0,i_h_250,i_w_250,i_o_crop,i_o_rcrop,i_o_format_png/000931404155200000000000000000000353.jpeg "Apply on first face")</center>

=== "Choose Second Face"

    ```
    {{ mediaBase }}/media/v1/cloudname/i_c_face_2,i_h_250,i_w_250,i_o_crop,i_o_rcrop,i_o_format_png/resource.jpg
    ```

    <center>![Apply on second face]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face_2,i_h_250,i_w_250,i_o_crop,i_o_rcrop,i_o_format_png/000931404155200000000000000000000353.jpeg "Apply on second face")</center>


## Background Removal

Using background removal A.I. feature you can remove the background of your images.

!!! info

    This feature is under development and upon release the docs will get completed.