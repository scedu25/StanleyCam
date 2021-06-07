# StanleyCam
This is my final project for CS498: Internet of Things.<br><br>
<img src=https://res.cloudinary.com/dc3kwd5bv/image/upload/v1621225434/qt6lzuh4kemfwbi2tdjx.jpg width=30%>

---

### Introduction
StanleyCam is a pet monitor built using a Raspberry Pi 4 with a camera module. Python and OpenCV are used for cat facial recognition to detect when Stanley gets on the counter. When this happens, the following series of events is triggered:
- A loud vacuum noise (he hates our vacuum) is played through a nearby bluetooth speaker.
- A photo is taken of Stanley and uploaded to Cloudinary for storage.
- An SMS text message is sent to my phone along with the newly uploaded photo URL.

My motivation for this project was the frequency with which our tabby cat must be scolded for jumping on the counter. Stanley has an insatiable appetite. Although we have (for the most part) trained him to avoid the kitchen when we’re at home, we weren't sure how often he'd snoop around with no one there to catch him. So I decided to create a pet monitor that could alert us when we're away from home.

### Specifications
The hardware set up was rather straightforward. I installed Raspberry Pi OS on a Raspberry Pi 4 and connected the Raspberry Pi Camera Module's ribbon cable to the appropriate port. The Raspberry Pi is enclosed in a case and placed on its side, and the camera's ribbon cable loops around and is taped to the front of the case, as pictured below.

<img src='https://lh3.googleusercontent.com/ezjSxPXpc9LUl8ZEKcDhYwohnmJ0moXlg9DfSIudfi37mC4Cyk3NExDU3nWx88oMkoXy_D_ux42nCdKfvhx1NT2stbCAxHly7I3x222u9injo9xLu8V9FLsVwbhmKQHKjO1xXtuIiA_rmg_qJ9fQYsdxfFtEChP3gyt1k8gcQ92fM8aHJTCae7dYRUlFqyDMveGOosBeJvIpuhwlC2qzXjNFQ-h5hGRRAm9gJpTIPMhupshxe8YRbaiREJzjmAbDPOcY_Ft41_6gndsUZSEO-Sa11AWqnh35FUh37ltqolPLSsKAroQRN-yqMQi6C6YEkxOijEQ6rgCsG60Hy5QuG-GrAQqzSk1ox9bD9yF0H7wzeFGzoSkZbsWuVmZtbONw8ZXgZYTxqsVDOAC3RkoU04fnc8TJP3KJue75dpspk0dZqWpmIFyfIeoaRElh1RB3eAStQ208w8hl7JNsOUq1gsL7GGQw0oLx7xE5zybrFmXPIEjXlXMF1l8qC_QovDSc4dVq2okHauQJgQwU-sbSpRwEMcIa9IWYAhI4Mpt65M47s57pFNMZMoYi-o64G2yhupyCJwl9X9Dj_w5uTBCXm5Pp8xfU3JboSGEjt-k4PbKnklChDO8dNhpoeQnhamYLI4IZnmPykvBV4-6vULXqo5zliMjwrej1XoYjzgZ40e4Qkoub5wv0NQD_moLP2zhiVr8Oqf_Ye6cDgSaKaqEE3nw=w1730-h1297-no?authuser=0' width=50%>

---

Pictured below is the camera facing towards Stanley's preferred point of entry to the countertop. The bluetooth speaker is not pictured here but can be seen in the video. It is paired to the Raspberry Pi and chosen as the default audio output.

<img src='https://lh3.googleusercontent.com/4ff06J7HlX3opljG2s51E7yBHsGilw_vyA0o3V1nWPUU68dhq77BYp-Ky7J8eF3RvlIg5Kp4j36Q046rO2aMKUq37vYaJxqsQztZet96EqUfxp2IvgVZr-W4N1s2kz_dscGZTFa2AzuDMX2Duy6VAxn9QMunDI3CAbGG2kLIuSTT9plp9BzTOs_C3YBd4NoMuUgdLFvrEK9Wi2gSDobrjUnZMNfTT87xmrWAygMDicIq7DqD51K0mCn0yLD5ukbwV43nzQ8v0mUqzsSX-npRZEtPnVQeME9zI-MlOXya_AZyxBPRrqyyLLZtAdPRiENe1kl5u74gMsAR9egcW4A4BAHxTqRFuUEjjrBa0eGTKU6jXXj79Y7cLbxl-FNVVXH_AgzLA3stXRDE0XxI6lMrC_zWoTIQLokOS8SpHEVlCz5nZSlX5ozVyIobwR6hWtWzlhmvF1eBvSucZ8_Ht7lyfdNzFFssdv9mtUCNxqVjmae87Ysi5YQOyhkSb4C_3tiO3OUAeWz81JKPDFKRz1RfywShhnXrJc_yfwLMu5Fqmna4MnXQJpE678Q-XyBvb-ZdDooSLMxEQzch1QySfnUqg_2LLzxqW2FFG2Bnv6Vduj944tU7re3_3xRArECOfF2WsANizfc5bYyPHGVElaAg-re8Fa40S0gCJ6Wfs15ZNfpaYX2e1OzQZKneVOQjqk16kMG_eXye7fwfPlyCU_VsZls=w1730-h1297-no?authuser=0' width=50%>

---

The cat facial recognition was done using OpenCV and a [pre-trained classification model](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalcatface.xml). Start the Python script with:<br>
`$ python3 catFaceDetection.py`<br>
This enables the video feed from the Raspberry Pi Camera Module, and each frame is individually processed by the program for facial recognition. When a cat face is detected, the vacuum noise plays through the Bluetooth speaker to ward the cat away, and a photo is captured. A rectangle is drawn around the cat's face, and the photo is saved locally then uploaded to Cloud storage provider Cloudinary. Using the Vonage API, an SMS text message is then sent to my phone with the newly uploaded photo's URL.

---

<img src='https://lh3.googleusercontent.com/Xwx_rxzCX0OdDtP9T-KysZMe_qXVW6iWou27yMIqrE_jOl7nE6arJ4nAqZpeK2IX0TyDX2qFwr5Pui9A9_BMQInyWGJd6OsgqQUASs-UhRFyjeObUdcIZr5PqMdjA_B5bAg33RpVEZBO-W_ygWZp-_ZjJwtZB4jhwqSyQenPCFW0uwTHwdeXPbXHoGijh7VFYlhSu1R-DS-z7I9qAwUyX_eDHdYTP3DRiUJDjtuLap0wC0Hc1x2aw3TaKevtHb58qGOnKaTM_t97KbzVW0sAHJ1Wt-WOAoQ6nnIkvACbsG8EfRfITvaDFqVIkD_IN_4vxdpVFcjLFIIF9UQqELjkUBl-FFneWk6mRwab2T2P857GsOALcEF3WP0Ws6mte6ivgnuBEhUL5cFX-aNeSwS2_Ly7RcdUCCTZFhCX9bRwZQJeRgEi0YQ5GsW_Of7NyeJ8bReBu_SFUHKFBMtLl2ccvS0LO7EIIiPqfMXLQiQV8EHI3BaLQ1HDwuTGbeSQQD5Cxh8igfMkEWKByPIpwtviIpEgWwDehrnjm3ssElSHvOyYaJWc1hPDQYVUpsjtQZdpJdiK7unM9QQcErzs55DABODDGFNkbR_Pwye4i-jIkXBeo1Kdo860Z624QE54lpYcdUcgND-ad2XpvtIfGtafcdI3rrEgaUVLkXoMg9tx6QOM-E5cXqCNqleuk1w4DvrFX4sSJZfNqDQGHmV0R0M9Rtg=w480-h640-no?authuser=0' height=600> <img src='https://lh3.googleusercontent.com/AuHepBbo_GFOOPRqZ7ZDWTGlMlw6o6OTZi85Lij55riaWe-0pLuCZ1aReE5I4khK7G1jMmaM_wRSFcHt7k_eJBxBu_ev5OMh6bQIXo_FSfjxGcKvin0IE1ZotnfUn5ODDx4gFZMh0B54h35bZyqq6p8-ziMHxr52pT6UBa_KhUWC4sl82ryqm6jGDdxkazjBd6vntjTxaI8xtWo4z0BNFTTnawZ6CcafUUyDbzlbiuGpBnKFMADTBhe1pXFb18grBwD1Hiudr8prUnE8OMpIq9qIe2-kLWJ8fLuI-ytFpjBCpDget0kAjWnVODA6FCfM3KZ1Toue45s6HNlFmKr9tCJw_xya66_L_Xu3TS-MuEBV8-U5ZA1CjIxtW0K0ejhM8s5Mrm7pL7_hzxEGt98wjihqrRv7raQUAskti1reQFWOIG_2WZj79D4StTJvQu-l1kH-eDiAbB4g9cwz1g1OPOP-8BN12Fy9kGGXrFgvLN0Yq40VD3hmgoe05jImkvfakUVbF-ld95dFfoIi-BsHewkhvqncpH4dyJ9uo03UFVivuZsO-d9JGsFTf16AX7wodPsWxEHa5vukJ_gY2IpOMEHJSly756FKwViCUNarbdMByldEPitNnEIo3ahxfEsW7Vsg4Ba5yd2cH3dIMOOBzTphMjY2Idl9X_qliNeIq-dSC8YA68ZgIY4TNpZAb_e1xJcTCXJ9sf1bS9m-Xrzuaxo=w599-h1297-no?authuser=0' height=600>
