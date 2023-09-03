import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="1821BEATs Page", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images\IMG_20210924_140917_538.webp")
img_lottie_animation = Image.open("images\PicsArt_11-27-06.21.07.jpg")
img_lottie_letme = Image.open("images\letme.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am 1821BEATs :wave:")
    st.title("A Music Producer From South Africa")
    st.write(
        "I am passionate about making beats, making music and dropping my own music."
    )
    st.write("[Learn More About 1821 >](https://www.google.com/search?client=firefox-b-d&q=1821beats)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Work")
        st.write("##")
        st.write(
            """
            Google 1821BEATs for more
            """
        )
        st.write("[More about 1821 >](https://www.google.com/search?client=firefox-b-d&q=1821beats)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("1821BEATs - Unlocked EP")
        st.write(
            """
            My first Solo project that I dropped in 2021 and has over 20 000 streams
            """
        )
        st.markdown("[Apple Music...](https://music.apple.com/za/album/unlocked-single/1545625798)")
        st.markdown("[Spotify...](https://open.spotify.com/album/6neVETZSE4nohtzYaQ7ENS?si=T6KXqAtjSnCwKUB95Vd_jg)")
        st.markdown("[YouTube...](https://www.youtube.com/watch?v=QXzZYHZMh_4&list=OLAK5uy_mby2IEXfp2tuZ2RPovtwGE_rSxztzqk40)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("1821BEATs & Senator Jei - Rags To Racks")
        st.write(
            """
            This is the second project that I released with Jei.
            """
        )
        st.markdown("[Apple Music...](https://music.apple.com/za/album/rags-to-racks-ep/1586769045)")
        st.markdown("[Spotify...](https://open.spotify.com/album/2KMZvexgRznJLVYOCxDpOh?si=as1OANzeSruH6MUyJewh3Q)")
        st.markdown("[YouTube...](https://www.youtube.com/watch?v=LKwdgWGLfls&list=OLAK5uy_lRQY07BTJlBCbKgLengD8aSi4j0uT2fwg)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_letme)
    with text_column:
        st.subheader("1821BEATs & Sasky Mali - Let Me")
        st.write(
            """
            This is a single Track I drop with Sasky.
            """
        )
        st.markdown("[Apple Music...](https://music.apple.com/za/album/str8-up-single/1570291422)")
        st.markdown("[Spotify...](https://open.spotify.com/album/0e8be9xlSrkHQGZMPDMKH8?si=CkyedfYESKyxW3thlpYFpg)")
        st.markdown("[YouTube...](https://youtu.be/deJ8QWoCt7k)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Book A Session or Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/musicdis411@gmail.com.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
