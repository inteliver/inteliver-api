---
title: "Integration"
---

# Integration


### Intuitive URLs

Without any change in your codes, you can modify your image resources using our intuitive url modifiers.

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

### SDK Integration

Inteliver tries to minimize the integration process by providing SDKs in different programming languages.
Please visit our [libraries](../libraries/index.md) section for integrating using an SDK.

Inteliver currently provides [Python](../libraries/python.md), [Javascript](../libraries/javascript.md), and [React](../libraries/react.md) SDKs.

!!! note
    We are updating SDKs to be compatibale with our latest changes. Meanwhile we are more focused on Intuitive URL integration mode.

### DNS Integration

!!! note
    This feature will be available soon.

You can integrate with inteliver by only changing your DNS nameservers to ours and use our intuitive 
URL commands query system.