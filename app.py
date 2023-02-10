import time

import streamlit as st
from PIL import Image

from helpers import remove_black_border

# Set page config
st.set_page_config(
    page_title="Detect and Remove Black Border from Screenshots Images",
    page_icon="◾️",
)


# Main page
st.title("Detect and Remove Black Border from Screenshots Images")
st.write(
    """
      Detecting and removing black borders from screenshot images is a computer vision task that involves processing images to identify and eliminate the black borders that sometimes appear in screenshots. This process is commonly performed to improve the visual quality of the images, reduce their size, or prepare them for further processing. The detection of the black border can be achieved through image processing techniques, such as thresholding, edge detection, or contour detection. Once the border has been detected, it can be removed using image cropping, resizing, or inpainting algorithms. The final result is an image with only the content of interest, without the distracting black borders. This technique can be applied to various types of screenshots, including those taken from computer screens, mobile devices, or videos.
"""
)
st.markdown("  ")

# Run load model
uploaded_file = st.file_uploader(
    "Upload image file", type=["jpg", "jpeg", "png", "bmp", "tiff"]
)
if uploaded_file is not None:
    uploaded_file = Image.open(uploaded_file).convert("RGB")
    st.markdown("  ")
    st.write("Source Image")
    st.image(uploaded_file)

    predict_button = st.button("Remove background")
    st.markdown("  ")

    if predict_button:
        with st.spinner("Wait for it..."):
            start_time = time.perf_counter()
            crop_image = remove_black_border(uploaded_file)
            st.write(
                f"Inference time: {(time.perf_counter() - start_time):.3f} seconds"
            )
            st.image(crop_image)
