---
title: "How inteliver Works?"
---

# How inteliver Works?

Inteliver uses **intuitive url query commands** to apply specefic operations on each image.

Using these query commands you can specify what changes you need to apply to your data or which operations
should be applied on your data.

Inteliver delivers the data after processing the query commands and applying the algorithms.

For example for changing the width of the image to `200` pixels you add this command to the image URL:

```
i_w_300,i_o_resize_keep
```

- `i_w_300`: Sets the image width to 200px
- `i_o_resize_keep`: Resize the image while keeping it's ratio

=== "Original Image"

    <center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000923288308380000000000000000000815.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/000923288308380000000000000000000815.jpeg)</center>
  
    `{{ mediaBase }}/media/v1/{{ cloudName }}/000923288308380000000000000000000815.jpeg`

=== "Modified Image"
  
    <center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/i_w_300,i_o_resize_keep/000923288308380000000000000000000815.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_w_300,i_o_resize_keep/000923288308380000000000000000000815.jpeg)</center>

    `{{ mediaBase }}/media/v1/{{ cloudName }}/i_w_300,i_o_resize_keep/000923288308380000000000000000000815.jpeg`


## Data Resource URL

Lets consider the following image URL.

```py title="An image URL on your servers"
"http://your-website/your-storage/image-id.jpg"
```

```py title="An image URL on inteliver storage"
"{{ mediaBase }}/media/v1/{{ cloudName }}/000923288308380000000000000000000815.jpeg"
```

The image can be stored using your own internal storage or inteliver storage. 

The `cloudname` in the above mentioned URL is the cloudname that you use, here it is `{{ cloudName }}`. 

After setting up inteliver self-host or inteliver cloud you will have a cloudname. You can use this cloudname to access your resources.

You can also use your own data storage after enabling your endpoint in inteliver panel.

```
{{ mediaBase }}/media/v1/url/your-path-to-your-data
```

## URL Query Commands

Inteliver query commands are written between the `cloudname` and the `resource pathname`.

The mentioned data resource is the following picture.

<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000923289297500000000000000000000683.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/000923289297500000000000000000000683.jpeg)</center>

Lets say we want to set the focus on these sets of images to face `i_c_face`, and change the size of the image to a `200` by `200` pixels `i_w_200,i_h_200` and crop it `i_o_crop` rounded `i_o_rcrop` and change the image format to png `i_o_format_png`.

The above creates a face focused profile picture.

The final URL with the above mentioned changes will be: 

```py title="Profile Picture Commands"
"{{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_w_200,i_h_200,i_o_crop,i_o_rcrop,i_o_format_png/000923288308380000000000000000000815.jpeg"
```

```py title="Query Commands"
"/i_c_face,i_w_200,i_h_200,i_o_crop,i_o_rcrop,i_o_format_png/"
```

- `i_c_face`: Change the center of modification to detected face
- `i_w_200`, `i_h_200`: Sets the image width to 200 and the image height to 200 pixels
- `i_o_rcrop`: To round crop the image
- `i_o_format_png`: Change the image format to PNG for background transparecy

The result will be a rounded profile picture of the image with focus on face. All done with a minor
url query commands change.

<center>[![Profile Picture]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_w_200,i_h_200,i_o_crop,i_o_rcrop,i_o_format_png/000923289297500000000000000000000683.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_w_200,i_h_200,i_o_crop,i_o_rcrop,i_o_format_png/000923289297500000000000000000000683.jpeg)</center>

!!! success
    Feel free to change and exprience this url commands system in our <a href="https://www.inteliver.com/playground" target="_blank">playground</a>.