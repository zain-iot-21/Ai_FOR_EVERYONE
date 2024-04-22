import streamlit as st
from PIL import Image
from remove_bg import remove_background

# Function to remove background
def remove_bg(image):
    api_key = ''  # YOUR_API_KEY here
    return remove_background(api_key, image)


def main():
    st.title("Background Remover App")


    uploaded_file = st.file_uploader("Upload a JPEG image", type=["jpg", "jpeg", "PNG"])

    if uploaded_file is not None:
        try:
            # Display original image
            st.subheader("Original Image")
            original_image = Image.open(uploaded_file)
            st.image(original_image, caption='Original Image', use_column_width=True)

            # Remove background
            st.subheader("Background Removed Image")
            removed_bg_image = remove_bg(uploaded_file)
            if removed_bg_image is not None:
                st.image(removed_bg_image, caption='Background Removed Image', use_column_width=True)
            else:
                st.error("Failed to remove background. Please try again.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()