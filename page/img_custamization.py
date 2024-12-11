import streamlit as st
import io
import base64
import utils.Edit as Edit

st.title("Image Customization")
uploaded_image = st.file_uploader("Choose a image")

if uploaded_image is not None:
    bytes_data = uploaded_image.getvalue()
    base64_image = base64.b64encode(bytes_data).decode('utf-8')
    st.image(io.BytesIO(bytes_data))
    st.text("Tags:")


    Remove = st.text_input("Remove")
    Replace = st.text_input("Replace ( write as a sentence )")

    submit = st.button("Submit")
    ImageEdit = Edit.ImageEdit()
    images = ImageEdit.Generate(base64_image, Remove, Replace)
    for nodeid in images:
        for image_data in images[nodeid]:
            st.image(io.BytesIO(image_data))
            img_down = st.download_button(
                                    label = "Download Image",
                                    data = io.BytesIO(image_data),
                                    file_name = "Customized image"+".png",
                                    mime = "image/png"
                                )
        st.snow()