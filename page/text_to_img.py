import streamlit as st
import utils.Gen as Gen
import io
st.title("Text to Image")
prompt = st.chat_input("Say something")


if prompt:
    st.text(prompt)
    ImgGen = Gen.ImageGen()
    images = ImgGen.Generate(prompt)

    for nodeid in  images:
        for image_data in images[nodeid]:
            st.image(io.BytesIO(image_data))
            img_down = st.download_button(
                                    label = "Download Image",
                                    data = io.BytesIO(image_data),
                                    file_name = prompt+".png",
                                    mime = "image/png"
                                )
        st.snow()