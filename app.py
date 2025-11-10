import io
import streamlit as st
from PIL import Image
from ollama import chat


st.set_page_config(page_title="Paveikslėlio aprašymas (Ollama + Streamlit)", layout="centered")

st.title("Paveikslėlio apibūdinimas")
st.write("Įkelkite paveikslėlį, o dirbtinis intelektas (modelis gemma3:4b) apibūdins jo turinį.")


def describe_image(image_bytes: bytes) -> str:
    """Send the image bytes to Ollama's gemma3:4b model and return the description.

    Returns a short Lithuanian description or raises an exception on failure.
    """
    # The docs show you can pass raw bytes in the 'images' field.
    messages = [{
        'role': 'user',
        'content': 'Apibūdink trumpai, aiškiai ir lietuviškai, kas yra šiame paveikslėlyje. Paminėk svarbiausius objektus, veiksmus ir spalvas.',
        'images': [image_bytes]
    }]

    response = chat(
        model='gemma3:4b',
        messages=messages,
        options={'temperature': 0.2}
    )

    # response.message.content per docs
    return response.message.content


uploaded_file = st.file_uploader("Įkelkite paveikslėlį (jpg, png, gif)", type=["jpg", "jpeg", "png", "gif", "bmp"])

if uploaded_file is not None:
    # Read bytes early so we can both display and send to the model
    image_bytes = uploaded_file.read()
    try:
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption="Įkeltas paveikslėlis", use_column_width=True)
    except Exception:
        st.warning("Nepavyko atidaryti paveikslėlio peržiūrai, bet bandysiu apibūdinti jį pagal turimus baitus.")

    if st.button("Apibūdinti paveikslėlį"):
        with st.spinner("Kreipiamasi į modelį gemma3:4b..."):
            try:
                description = describe_image(image_bytes)
                st.markdown("### Modelio aprašymas")
                st.write(description)
            except Exception as e:
                st.error(f"Klaida kviečiant modelį: {e}")
                st.info("Įsitikinkite, kad Ollama veikia lokaliai ir kad modelis `gemma3:4b` yra įrašytas/užkrautas.")

else:
    st.info("Įkelkite paveikslėlį, kad pradėtumėte.")
