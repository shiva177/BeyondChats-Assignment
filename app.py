# import streamlit as st
# from scraper.reddit_api import get_user_data
# from cleaner.clean_reddit_data import clean_reddit_data
# from llm.persona_llm import build_user_persona_llm
# from utils.file_saver import save_to_file

# def extract_username_from_url(url: str) -> str:
#     parts = url.strip("/").split("/")
#     if "user" in parts:
#         index = parts.index("user")
#         return parts[index + 1] if index + 1 < len(parts) else None
#     return None

# # Streamlit UI Config
# st.set_page_config(page_title="Reddit Persona Builder", layout="wide")
# st.title("🤖 Reddit User Persona Generator")

# profile_url = st.text_input("Enter Reddit Profile URL", "https://www.reddit.com/user/kojied/")

# if st.button("Generate Persona"):
#     username = extract_username_from_url(profile_url)

#     if not username:
#         st.error("❌ Invalid Reddit profile URL")
#     else:
#         st.info(f"📥 Fetching data for u/{username}...")

#         try:
#             content = get_user_data(username)
#             st.success(f"✅ Raw data fetched successfully! Total: {len(content)} items")

#             cleaned = clean_reddit_data(content)
#             st.info(f"🧽 Cleaned {len(cleaned)} items")

#             if len(cleaned) == 0:
#                 st.warning("⚠️ No meaningful content to analyze.")
#             else:
#                 st.subheader("🔎 Cleaned Posts & Comments")
#                 for item in cleaned[:5]:
#                     st.code(str(item), language='json')

#                 st.subheader("🧠 Generated Persona")
#                 trimmed_data = cleaned[:30]
#                 persona = build_user_persona_llm(trimmed_data, username)  # ✅ FIXED: passed both arguments
#                 st.markdown(persona)

#                 save_to_file(username, cleaned)

#                 st.download_button(
#                     label="📄 Download Persona",
#                     data=persona,
#                     file_name=f"{username}_persona.txt",
#                     mime="text/plain"
#                 )

#         except Exception as e:
#             st.error(f"❌ Error occurred: {str(e)}")



import streamlit as st
from scraper.reddit_api import get_user_data
from cleaner.clean_reddit_data import clean_reddit_data
from llm.persona_llm import build_user_persona_llm
from utils.file_saver import save_to_file

def extract_username_from_url(url: str) -> str:
    parts = url.strip("/").split("/")
    if "user" in parts:
        index = parts.index("user")
        return parts[index + 1] if index + 1 < len(parts) else None
    return None

# ✅ Initialize theme state
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True  # Default to dark mode

# ✅ Theme toggle
with st.sidebar:
    st.title("🧰 Settings")
    if st.toggle("🌗 Toggle Light/Dark Mode", value=st.session_state.dark_mode):
        st.session_state.dark_mode = True
    else:
        st.session_state.dark_mode = False

# ✅ Apply dynamic theme styling
if st.session_state.dark_mode:
    st.markdown("""
        <style>
        body, .stApp {
            background-color: #0e1117;
            color: #fafafa;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #fafafa;
        }
        input, .stTextInput input {
            color: white;
            background-color: #262730;
        }
        .stButton>button {
            background-color: #262730;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        body, .stApp {
            background-color: #ffffff;
            color: #000000;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #000000;
        }
        input, .stTextInput input {
            color: black;
            background-color: #f0f2f6;
        }
        .stButton>button {
            background-color: #e0e0e0;
            color: black;
        }
        </style>
    """, unsafe_allow_html=True)


# ✅ App Layout
st.set_page_config(page_title="Reddit Persona Builder", layout="wide")
st.title("🤖 Reddit User Persona Generator")

profile_url = st.text_input("Enter Reddit Profile URL", "https://www.reddit.com/user/kojied/")

if st.button("Generate Persona"):
    username = extract_username_from_url(profile_url)

    if not username:
        st.error("❌ Invalid Reddit profile URL")
    else:
        st.info(f"📥 Fetching data for u/{username}...")

        try:
            content = get_user_data(username)
            st.success(f"✅ Raw data fetched successfully! Total: {len(content)} items")

            cleaned = clean_reddit_data(content)
            st.info(f"🧽 Cleaned {len(cleaned)} items")

            if len(cleaned) == 0:
                st.warning("No meaningful content to analyze")
            else:
                st.subheader("🔎 Cleaned Posts & Comments")
                for item in cleaned[:5]:
                    st.code(str(item), language='json')

                st.subheader("🧠 Generated Persona")

                # ✅ Limit to 30 to avoid token overflow
                trimmed = cleaned[:30]
                persona = build_user_persona_llm(trimmed, username)
                st.markdown(persona)

                save_to_file(username, cleaned)
                st.download_button("📄 Download Persona", persona, file_name=f"{username}_persona.txt")

        except Exception as e:
            st.error(f"❌ Error occurred: {str(e)}")

