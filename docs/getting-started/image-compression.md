---
title: "Image Compression"
---

Using different inteliver real-time compressions you can deliver the best quality with lowest size considering the client's bandwidth.


## Image Formats

Currently we supports `WEBP`, `JPEG` and `PNG` compression formats. 

You can specify the format and the compression level. 

Here is an image with Real-Time WEBP compression levels of 80, 50 and 20.

!!! tip
    The compression level is between `0 and 100`. 100 is the best quality and the lower it is it will reduce the size.
    A level of `70 to 85` is usually the best trade off between quality and size.

=== "Original Image"

    ```
    {{ mediaBase }}/media/v1/cloudname/resource.jpeg

    ```

    <center>![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000933034435130000000000000000000473.jpeg "Original Image")</center>

    <center>Original Image Size: <strong>248 KB</strong></center>

=== "WEBP Quality Level: 80"

    ```
    {{ mediaBase }}/media/v1/cloudname/i_o_format_webp_80/resource.jpeg

    ```

    <center>![Compression with ratio: 80]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_webp_80/000933034435130000000000000000000473.jpeg "ratio: 80")</center>

    <center>Compressed Image Size: <strong>20.2 KB</strong></center>
    <center>Compression Ratio: <strong>~12</strong></center>

=== "WEBP Quality Level: 50"

    ```
    {{ mediaBase }}/media/v1/cloudname/i_o_format_webp_50/resource.jpeg
    ```

    <center>![Compression with ratio: 50]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_webp_50/000933034435130000000000000000000473.jpeg "ratio: 50")</center>

    <center>Compressed Image Size: <strong>12.2 KB</strong></center>
    <center>Compression Ratio: <strong>~20</strong></center>

=== "WEBP Quality Level: 20"

    ```
    {{ mediaBase }}/media/v1/cloudname/i_o_format_webp_20/resource.jpeg
    ```

    <center>![Compression with ratio: 20]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_webp_20/000933034435130000000000000000000473.jpeg "ratio: 20")</center>

    <center>Compressed Image Size: <strong>7.1 KB</strong></center>
    <center>Compression Ratio: <strong>~37</strong></center>

you can also refer to [API reference](../api-reference/compression.md) section for complete list of args.