---
title: "Python"
---

# Python

## Inteliver Python SDK

!!! warning
    We are updating SDKs to be compatibale with our latest changes.

!!! note
    Please visit our <a href="https://github.com/inteliver/pyinteliver" target="_blank">Github page</a> for more information.

-------------

## PyInteliver

Using our python sdk you can **upload**, set **configs** and **retrieve** your data.


### Installation

This python package is available at **PyPI**.
simply run the following command to be able to use our python API.

``` bash
    pip install pyinteliver
```

You can also pull our repository and use the API **without any requirements** to install. 

``` bash
    git pull https://github.com/inteliver/pyinteliver.git
```

### Inteliver Configs
After registering in  <a href="https://www.inteliver.com" target="_blank">Inteliver</a> you will have a **cloud-name** and **token**. This pair will be used to authenticate you for uploading data or using intelligent service. 
To set this in your code simply:

```py title="Create InteliverConfig"
from InteliverConfig import InteliverConfig

config = InteliverConfig(cloudname="your-cloudname", token="your-token")
```


### Upload

To upload your data first set your **config** object.
Then use the following lines:

```py title="Upload"
from Uploader import Uploader

uploader = Uploader(config)
file_key = uploader.upload('logo.jpg')
```

If uploaded successfully you will receive a **json** file with following format.
```json
{
    'success': True, 
    'message': 'Successfully uploaded.', 
    'resource_key': RETURNED_RESOURCE_KEY
}
```

`resource_key` is a unique key which able you to receive your data later. 


### Retrieve Data

Using `#!python InteliverRetrieve` class you can **build the URL** of the data you need to get from Inteliver.

To retrieve your data first set your **config** object. After setting your config object, build an `InteliverRetrieve` object.

```py title="Set Config Object"
from InteliverConfig import InteliverConfig
from InteliverRetrieve import InteliverRetrieve

config = InteliverConfig(cloudname="your-cloudname")
rt = InteliverRetrieve(config)
```

!!! tip
    Note that for retrieving data you only need your **cloudname** to be set.

All the image modifications are sequentional. 

for example lets say you want to **select the main face** in picture **resize** it to 200 and 200 and keep the original ratio and to **crop** the image in a rounded shape and change the **format** to png and build the url. 

let say your resource image is this one:

<center>[![Original Image]({{ mediaBase }}/media/v1/{{ cloudName }}/000931373825510000000000000000000417.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/000931373825510000000000000000000417.jpeg)</center>

```py title="Retrieve Rounded Face Image"
    rt.select_face()
    rt.select('height', 200)
    rt.select('width', 200)
    rt.image_crop(round_crop=True)
    rt.image_change_format('PNG')
    url_to_get = rt.build_url(your_resource_key)
```

This will build a url like this:

```py
"{{ mediaBase }}/media/v1/yourcloudname/i_c_face,i_w_200,i_h_200,i_o_crop,i_o_rcrop,i_o_format_png/resourcekey.jpg"
```

The image you receive after modification is : 

<center>[![Modified Image]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_w_200,i_h_200,i_o_crop,i_o_rcrop,i_o_format_png/000931373825510000000000000000000417.jpeg)]({{ mediaBase }}/media/v1/{{ cloudName }}/i_c_face,i_w_200,i_h_200,i_o_crop,i_o_rcrop,i_o_format_png/000931373825510000000000000000000417.jpeg)</center>


!!! info
    You can find out about the image modification examples at [inteliver Examples](../examples/index.md).