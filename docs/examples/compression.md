---
title: "Compression"
date: 2019-09-19T06:28:13+04:30
weight: 50
---

## Image Compression Formats

Here are some examples for image compression on-the-fly with size comparison before and after compression.

### JPEG

JPEG is a lossy image compression algorithm, which means that JPEG affects the visual precision of the compressed image. In Inteliver JPEG compression API, you can set the compression level (image quality) from a range of [0, 100]. 

Level zero result in a very small image size while affecting the visual precision alot. Level one hundred will result in the best quality image with biggest size.

=== "Original Image"
    ##### Original Image 

    ```
    No Compression
    ```

    <center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000933034435130000000000000000000473.jpeg){ width="500" }]({{ mediaBase }}/media/v1/{{ cloudName }}/000933034435130000000000000000000473.jpeg)</center>

    <center>Original Image Size: <strong>111 KB</strong></center>

=== "Level: 80"
    ##### JPEG Compression (Quality Level: 80)

    ```
    i_o_format_jpg_80
    ```
    <center>[![Image file format]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_jpg_80/000933034435130000000000000000000473.jpeg){ width="500" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_jpg_80/000933034435130000000000000000000473.jpeg)</center>

    <center>Compressed Image Size: <strong>27.4 KB</strong></center>
    <center>Compression Ratio: <strong>~4x</strong></center>

=== "Level: 40"
    ##### JPEG Compression (Quality Level: 40)

    ```
    i_o_format_jpg_40
    ```
    <center>[![Image file format]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_jpg_40/000933034435130000000000000000000473.jpeg){ width="500" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_jpg_40/000933034435130000000000000000000473.jpeg)</center>

    <center>Compressed Image Size: <strong>14.1 KB</strong></center>
    <center>Compression Ratio: <strong>~8x</strong></center>

=== "Level: 20"
    ##### JPEG Compression (Quality Level: 20)

    ```
    i_o_format_jpg_20
    ```
    <center>[![Image file format]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_jpg_20/000933034435130000000000000000000473.jpeg){ width="500" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_jpg_20/000933034435130000000000000000000473.jpeg)</center>

    <center>Compressed Image Size: <strong>9.3 KB</strong></center>
    <center>Compression Ratio: <strong>~12x</strong></center>


### WEBP

Webp is a lossy image compression algorithm, which means that Webp affects the visual precision of the compressed image. In Inteliver Webp compression API, you can set the compression level (image quality) from a range of [0, 100]. 

Level zero result in a very small image size while affecting the visual precision alot. Level one hundred will result in the best quality image with biggest size.

=== "Original Image"
    ##### Original Image

    ```
    No Compression
    ```

    <center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000933034435130000000000000000000473.jpeg){ width="500" }]({{ mediaBase }}/media/v1/{{ cloudName }}/000933034435130000000000000000000473.jpeg)</center>

    <center>Original Image Size: <strong>111 KB</strong></center>


=== "Level: 80"
    ##### WEBP Compression (Quality Level: 80)

    ```
    i_o_format_webp_80
    ```
    <center>[![Image file format]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_webp_80/000933034435130000000000000000000473.jpeg){ width="500" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_webp_80/000933034435130000000000000000000473.jpeg)</center>

    <center>Compressed Image Size: <strong>20.2 KB</strong></center>
    <center>Compression Ratio: <strong>~5x</strong></center>


=== "Level: 40"
    ##### WEBP Compression (Quality Level: 40)

    ```
    i_o_format_webp_40
    ```
    <center>[![Image file format]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_webp_40/000933034435130000000000000000000473.jpeg){ width="500" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_webp_40/000933034435130000000000000000000473.jpeg)</center>

    <center>Compressed Image Size: <strong>10.6 KB</strong></center>
    <center>Compression Ratio: <strong>~10x</strong></center>

=== "Level: 20"
    ##### WEBP Compression (Quality Level: 20)

    ```
    i_o_format_webp_20
    ```
    <center>[![Image file format]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_webp_20/000933034435130000000000000000000473.jpeg){ width="500" }]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_webp_20/000933034435130000000000000000000473.jpeg)</center>

    <center>Compressed Image Size: <strong>7 KB</strong></center>
    <center>Compression Ratio: <strong>~15x</strong></center>


### PNG

PNG is a lossless image compression algorithm. The PNG compression will not affect the visual precision of the image and after decoding the compressed image is identical to the original one.
Hoewever, the compression level is a trade-off between file size and encoding/decoding speed. 

In Inteliver PNG compression API, you can set the compression level from a range of [1, 9] where level-1 produces the biggest file size and fastest decoding mode and level-9 result in the samllest file size with the slowest decoding time.

=== "Original Image"
    ##### Original Image 

    ```
    No Compression
    ```

    <center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000936971794640000000000000000000399.png)]({{ mediaBase }}/media/v1/{{ cloudName }}/000936971794640000000000000000000399.png)</center>

    <center>Original Image Size: <strong>303 KB</strong></center>

=== "Level: 1"
    ##### PNG Compression Level: 1

    ```
    i_o_format_png_1
    ```
    <center>[![Image file format]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_png_1/000936971794640000000000000000000399.png)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_png_1/000936971794640000000000000000000399.png)</center>

    <center>Compressed Image Size: <strong>303 KB</strong></center>
    <center>Compression Ratio: <strong>1x</strong></center>

=== "Level: 6"
    ##### PNG Compression Level: 6

    ```
    i_o_format_png_6
    ```
    <center>[![Image file format]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_png_6/000936971794640000000000000000000399.png)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_png_6/000936971794640000000000000000000399.png)</center>

    <center>Compressed Image Size: <strong>274 KB</strong></center>
    <center>Compression Ratio: <strong>1.1x</strong></center>

=== "Level: 9"
    ##### PNG Compression Level: 9

    ```
    i_o_format_png_9
    ```
    <center>[![Image file format]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_png_9/000936971794640000000000000000000399.png)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_o_format_png_9/000936971794640000000000000000000399.png)</center>

    <center>Compressed Image Size: <strong>267 KB</strong></center>
    <center>Compression Ratio: <strong>~1.2x</strong></center>
