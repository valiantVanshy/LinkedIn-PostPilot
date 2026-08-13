import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at 10% 20%, rgba(79, 70, 229, 0.22), transparent 28%),
            radial-gradient(circle at 90% 15%, rgba(14, 165, 233, 0.20), transparent 28%),
            radial-gradient(circle at 70% 85%, rgba(168, 85, 247, 0.18), transparent 30%),
            linear-gradient(135deg, #070b17 0%, #0d1224 45%, #111827 100%);
        background-attachment: fixed;
        color: white;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 4rem;
        padding-bottom: 4rem;
    }

    .main-card {
        padding: 42px;
        border-radius: 28px;
        background: rgba(255, 255, 255, 0.055);
        border: 1px solid rgba(255, 255, 255, 0.12);
        box-shadow:
            0 25px 80px rgba(0, 0, 0, 0.45),
            inset 0 1px 0 rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        animation: fadeIn 0.8s ease;
    }

    .title {
        font-size: 42px;
        font-weight: 800;
        line-height: 1.15;
        margin-bottom: 10px;
        background: linear-gradient(90deg, #60a5fa, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .subtitle {
        color: #aab4c8;
        font-size: 17px;
        margin-bottom: 35px;
    }

    .section-label {
        font-size: 13px;
        font-weight: 700;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 8px;
    }

    div[data-baseweb="select"] > div {
        background: rgba(255, 255, 255, 0.07) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 14px !important;
        min-height: 48px;
        transition: all 0.25s ease;
    }

    div[data-baseweb="select"] > div:hover {
        border-color: rgba(96, 165, 250, 0.8) !important;
        box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.08);
    }

    div[data-baseweb="select"] span {
        color: #f8fafc !important;
    }

    div.stButton > button {
        width: 100%;
        min-height: 52px;
        border: none;
        border-radius: 14px;
        color: white;
        font-size: 16px;
        font-weight: 700;
        background: linear-gradient(90deg, #2563eb, #7c3aed);
        box-shadow: 0 10px 30px rgba(79, 70, 229, 0.35);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 40px rgba(99, 102, 241, 0.5);
        border: none;
        color: white;
    }

    div.stButton > button:active {
        transform: translateY(0);
    }

    .output-title {
        margin-top: 35px;
        font-size: 14px;
        font-weight: 700;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1.5px;
    }

    .post-output {
        margin-top: 12px;
        padding: 28px;
        border-radius: 20px;
        background: linear-gradient(
            135deg,
            rgba(37, 99, 235, 0.12),
            rgba(124, 58, 237, 0.10)
        );
        border: 1px solid rgba(255, 255, 255, 0.12);
        color: #e5e7eb;
        font-size: 16px;
        line-height: 1.8;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.25);
        animation: slideUp 0.5s ease;
    }

    .footer {
        text-align: center;
        margin-top: 30px;
        color: #64748b;
        font-size: 13px;
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(15px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(15px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @media (max-width: 768px) {
        .block-container {
            padding-top: 2rem;
        }

        .main-card {
            padding: 25px;
        }

        .title {
            font-size: 32px;
        }

        .subtitle {
            font-size: 15px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

length_options = ["Short", "Medium", "Long"]
language_options = ["English"]

def main():
    st.markdown(
        """
        <div class="main-card">
            <div class="title">
                💼 LinkedIn Post Generator
            </div>
            <div class="subtitle">
                Create professional, engaging LinkedIn posts powered by AI.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    fs = FewShotPosts()
    tags = fs.get_tags()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            '<div class="section-label">🎯 Topic</div>',
            unsafe_allow_html=True
        )
        selected_tag = st.selectbox(
            "Topic",
            options=tags,
            label_visibility="collapsed"
        )

    with col2:
        st.markdown(
            '<div class="section-label">📏 Length</div>',
            unsafe_allow_html=True
        )
        selected_length = st.selectbox(
            "Length",
            options=length_options,
            label_visibility="collapsed"
        )

    with col3:
        st.markdown(
            '<div class="section-label">🌐 Language</div>',
            unsafe_allow_html=True
        )
        selected_language = st.selectbox(
            "Language",
            options=language_options,
            label_visibility="collapsed"
        )

    st.write("")

    generate = st.button("✨ Generate LinkedIn Post")

    if generate:
        with st.spinner("✨ Crafting your LinkedIn post..."):
            post = generate_post(
                selected_length,
                selected_language,
                selected_tag
            )

        st.markdown(
            '<div class="output-title">Generated Post</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="post-output">
                {post}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success("Your LinkedIn post is ready!")

    st.markdown(
        """
        <div class="footer">
            Powered by LangChain + Groq + Streamlit
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()