import streamlit as st

st.markdown("""
    <style>
    /* Background color */
    .stApp { background-color: #f8f9fa; }

    /* Page title */
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 20px;
    }

    /* Container for image and content */
    .paper-container {
        display: flex;
        align-items: center;
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
    }

    /* Image styling */
    .paper-image img {
        width: 150px;
        height: 150px;
        border-radius: 10px;
        object-fit: cover;
    }

    /* Content styling */
    .paper-content {
        flex: 1;
        padding-left: 15px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    /* Paper title */
    .paper-title {
        font-size: 20px;
        font-weight: bold;
        color: #34495e;
        margin-bottom: 10px;
    }

    /* Buttons */
    .paper-button {
        background-color: #2c3e50;
        color: white;
        font-size: 16px;
        padding: 8px;
        border: none;
        cursor: pointer;
        border-radius: 5px;
        width: 150px;
        text-align: center;
        transition: 0.3s;
    }

    .paper-button:hover {
        background-color: #1a252f;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("<div class='title'>Research Paper Recommendation</div>", unsafe_allow_html=True)

if st.button("View Research Papers"):

    papers = [
        {"title": "Deep Learning for NLP", "image": "https://via.placeholder.com/150"},
        {"title": "AI in Healthcare", "image": "https://via.placeholder.com/150"},
        {"title": "Quantum Computing Advances", "image": "https://via.placeholder.com/150"},
        {"title": "Autonomous Vehicles", "image": "https://via.placeholder.com/150"},
        {"title": "Blockchain Security", "image": "https://via.placeholder.com/150"},
        {"title": "Edge Computing", "image": "https://via.placeholder.com/150"}
    ]

    for paper in papers:
        st.markdown(
            f"""
            <div class="paper-container">
                <div class="paper-image">
                    <img src="{paper['image']}" alt="Paper Image">
                </div>
                <div class="paper-content">
                    <div class="paper-title">{paper['title']}</div>
                    <button class="paper-button" onclick="alert('Showing {paper['title']}')">Show Paper</button>
                </div>
            </div>
            """, unsafe_allow_html=True
        )
