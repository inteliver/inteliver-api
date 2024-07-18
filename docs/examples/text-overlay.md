---
title: "Text Overlay"
---

# Textoverlay

Here are some examples to put text overlays on your images on-the-fly.

Using `i_o_text` you can specify the text, scale, font and color of the text you would like to put on the image.

Using `i_c_x` and `i_c_y` you can set the center of the text.

The args are separated using `_` and here is the list of args you can use.

- text: args[0]
- scale: args[1]
- font: args[2]
- red: args[3]
- green: args[4]
- blue: args[5]

!!! warning
    Textoverlay is a new and experimental feature.

```
i_c_y_100,i_c_x_-180,i_o_text_Your-Brand_1.5_4_14_70_160
```
<center>[![Textoverlay]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_y_100,i_c_x_-180,i_o_text_Your-Brand_1.5_4_14_70_160/000932220963390000000000000000000570.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_y_100,i_c_x_-180,i_o_text_Your-Brand_1.5_4_14_70_160/000932220963390000000000000000000570.jpeg)</center>

```
i_c_y_100,i_c_x_-140,i_o_text_inteliver_2.5_1_14_70_160
```
<center>[![Textoverlay]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_y_100,i_c_x_-140,i_o_text_inteliver_2.5_7_14_70_160/000932246193860000000000000000000437.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_y_100,i_c_x_-140,i_o_text_inteliver_2.5_7_14_70_160/000932246193860000000000000000000437.jpeg)</center>

!!! note
    You can refer to the text overlay [API reference](../api-reference/text-overlay.md) to see all the possible values for arguments.
