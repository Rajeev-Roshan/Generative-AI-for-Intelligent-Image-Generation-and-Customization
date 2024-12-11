import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = ["User"]

def login():

    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()

role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

request_1 = st.Page(
    "page/Explaination.py",
    title="Project Explanation",
    icon=":material/help:",
    default=True
)

request_2 = st.Page(
    "page/text_to_img.py",
    title="text to img",
    icon=":material/help:",
)

request_3 = st.Page(
    "page/img_custamization.py", title="image custamization ", icon=":material/bug_report:"
)
if st.session_state.role not in ROLES:

    st.title("Generative AI for Intelligent Image Generation and Custamization")

pages = [request_1, request_2, request_3]
account_pages = [logout_page]
page_dict = {}
if st.session_state.role in ["User"]:
    page_dict["Options"] = pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages }| page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()