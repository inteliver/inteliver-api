---
title: "Usecases"
---


## End-To-End Image Assets Management

Inteliver offers a comprehensive solution for managing your organization's digital assets:

### Upload and Store

- [x] Easily upload images with intuitive APIs or user-friendly interfaces.
- [x] Store images in various formats (JPG, PNG, WEBP) and resolutions, organized for easy access.

### Transform and Customize

- [x] Use real-time programmable media to resize, crop, rotate, and apply filters to images.
- [x] Perform bulk transformations for consistency across large image sets.

### Monitor and Analyze

- [x] Track usage patterns and performance metrics.
- [x] Manage different versions of images for change tracking and reversion.

### Optimize and Deliver

- [x] Use Inteliver’s CDN integration to cache images closer to users, reducing latency.
- [x] Convert images to mobile-friendly formats and dynamically adjust compression for faster load times.
- [x] Implement lazy loading to defer image loading until needed, improving initial page load times.

Inteliver’s end-to-end image asset management ensures your digital assets are organized, optimized, and securely managed, enhancing productivity and collaboration within your organization.

## E-commerce Optimization

E-commerce platforms need to balance image quality with page speed. Inteliver allows you to:

- [x] Dynamically resize and crop product images.
- [x] Apply compression to reduce file sizes without sacrificing quality.
- [x] Use lazy loading to defer offscreen images, enhancing page performance.

## Mobile Delivery Optimization

Delivering high-quality images to mobile devices efficiently is crucial for providing a seamless user experience. 

Inteliver's mobile delivery optimization ensures that images are resized and compressed to enhance loading times, offering up to a **20x** speed improvement. Here’s how you can achieve this:

### Resizing for Mobile Screens

- [x] **Dynamic Resizing:** Automatically resize images to fit various mobile screen sizes, ensuring optimal display without compromising quality.
- [x] **Adaptive Delivery:** Use responsive design principles to deliver appropriately sized images based on the device type and resolution.

### Compression Techniques

- [x] Format Conversion: Convert images to mobile-friendly formats like WEBP, which provide better compression and faster load times compared to traditional formats like JPG and PNG.
- [x] Quality Adjustment: Adjust the compression quality dynamically to balance image clarity and file size, ensuring quick delivery without noticeable degradation.

### CDN Integration:

- [x] Edge Caching: Leverage Content Delivery Networks (CDN) to cache images closer to mobile users, reducing latency and speeding up delivery times.
- [x] Global Distribution: Distribute images across multiple CDN nodes worldwide, ensuring fast access regardless of the user’s location.

Using Inteliver’s mobile delivery optimization improves the speed and performance of mobile services, enhancing user satisfaction and boosting engagement and conversion rates.

## User-Generated Content

Managing user-uploaded images can be challenging. Inteliver helps by:

- [x] Automatically applying transformations to uploaded images.
- [x] Ensuring consistent quality and appearance.
- [x] Reducing the need for manual intervention and processing.

## Profile Picture

A usefull usecase is to extract profile picture automatically from user picture.

=== "Original Image"

    ```
    {{ mediaBase }}/media/v1/cloudname/resource.jpg
    ```

    <center>![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000932170183830000000000000000000848.jpeg "Original Image"){ width="350" }</center>

=== "Profile Picture on-the-fly"

    ```
    {{ mediaBase }}/media/v1/cloudname/i_c_face,i_h_200,i_w_200,i_o_crop,i_o_rcrop,i_o_format_png/resource.jpg
    ```

    <center>![Profile Picture]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_h_250,i_w_250,i_o_crop,i_o_rcrop,i_o_format_png/000932170183830000000000000000000848.jpeg "Profile Picture")</center>


## Face Blur

Another usecase is to blur faces in image to protect the privacy of public shared image data.

=== "Original Image"

    ```
    {{ mediaBase }}/media/v1/cloudname/resouce.jpg
    ```

    <center>![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000931373825510000000000000000000417.jpeg "Original Image"){ width="250" }</center>

=== "Face Blur on-the-fly"

    ```
    {{ mediaBase }}/media/v1/cloudname/i_c_face,i_o_blur_30/resource.jpg
    ```

    <center>![Face Blur]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_o_blur_30/000931373825510000000000000000000417.jpeg "Face Blur"){ width="250" }</center>

!!! note
    Please visit our <a href="https://www.inteliver.com/playground" target="_blank">playground</a> for more predefined usecases.
