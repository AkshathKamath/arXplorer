import streamlit as st
import requests

BASE_API_URL = "http://127.0.0.1:4000/"

st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .title { text-align: center; font-size: 40px; font-weight: bold; color: #2c3e50; margin-bottom: 20px; }
    .paper-container { display: flex; align-items: center; background: white; padding: 15px; border-radius: 10px; 
                       box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); margin-bottom: 15px; }
    .paper-title { font-size: 20px; font-weight: bold; color: #34495e; margin-bottom: 10px; }
    .paper-button { background-color: #2c3e50; color: white; font-size: 16px; padding: 8px; border: none;
                    cursor: pointer; border-radius: 5px; width: 150px; text-align: center; transition: 0.3s; }
    .paper-button:hover { background-color: #1a252f; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Research Paper Recommendation</div>", unsafe_allow_html=True)

title = st.text_input("Enter a topic for research papers:", "Deep Learning")

papers = [] 
selected_text = ""

if st.button("View Research Papers"):
    with st.spinner("Fetching research papers..."):
        response = requests.post(f"{BASE_API_URL}search_papers/", json={"title": title})

        if response.status_code == 200:
            papers = response.json().get("papers", [])
        else:
            st.error("Failed to fetch research papers.")
            papers = []

for i, paper in enumerate(papers):
    with st.container():
        st.markdown(
            f"""
            <div class="paper-container">
                <div class="paper-content">
                    <div class="paper-title">{paper['title']}</div>
                    <a href="{paper['link']}" target="_blank">
                        <button class="paper-button">View Paper</button>
                    </a>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )

        if st.button(f"Extract Text {i+1}", key=f"extract_btn_{i}"):
            with st.spinner(f"Extracting text from: {paper['title']}"):
                extract_response = requests.post(f"{BASE_API_URL}extract_pdf_text/", json={"url": paper['link']})

                if extract_response.status_code == 200:
                    selected_text = extract_response.json().get("text", "")
                else:
                    st.error(f"Failed to extract text from {paper['title']}")

if selected_text:
    st.text_area("Extracted Text:", selected_text, height=300)
