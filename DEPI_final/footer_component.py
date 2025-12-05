import streamlit as st

def show_footer():
    st.write("---")
    
    # 1. العنوان
    st.markdown("<h3 style='text-align: center; color: #fff;'>Meet the Team</h3>", unsafe_allow_html=True)
    
    # 2. البيانات
    team_members = [
        {"name": "Ahmed Sief", "role": "AI Engineer", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140048.png", "link": "#"},
        {"name": "Member 2", "role": "Data Scientist", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140037.png", "link": "#"},
        {"name": "Member 3", "role": "Backend Dev", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140047.png", "link": "#"},
        {"name": "Member 4", "role": "Frontend Dev", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140051.png", "link": "#"},
        {"name": "Member 5", "role": "Researcher", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140040.png", "link": "#"},
        {"name": "Member 6", "role": "Manager", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140039.png", "link": "#"},
    ]

    # 3. الـ CSS (الاستايل)
    st.markdown("""
    <style>
    .team-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 15px;
        margin-bottom: 30px;
    }
    .team-card {
        background-color: #262730;
        border: 1px solid #444;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        transition: transform 0.2s;
    }
    .team-card:hover {
        transform: translateY(-5px);
        border-color: #ff4b4b;
    }
    .team-card img {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        margin-bottom: 10px;
        border: 2px solid #ff4b4b;
    }
    .team-card h4 {
        margin: 0;
        font-size: 16px;
        color: #fff;
    }
    .team-card p {
        margin: 5px 0 10px 0;
        font-size: 12px;
        color: #aaa;
    }
    .team-card a {
        text-decoration: none;
        color: #ff4b4b;
        font-size: 12px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    # 4. تجميع الـ HTML (بدون مسافات Indentation عشان المارك داون ميبوظش)
    cards_html = '<div class="team-grid">'
    for member in team_members:
        cards_html += (
            f'<div class="team-card">'
            f'<img src="{member["img"]}" alt="{member["name"]}">'
            f'<h4>{member["name"]}</h4>'
            f'<p>{member["role"]}</p>'
            f'<a href="{member["link"]}" target="_blank">View Profile</a>'
            f'</div>'
        )
    cards_html += '</div>'

    # عرض الكروت
    st.markdown(cards_html, unsafe_allow_html=True)

    # 5. الفيدباك
    st.write("---")
    st.subheader("📩 Send Feedback")
    
    with st.form("feedback_form"):
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Name (Optional)")
        with c2:
            st.text_input("Email (Optional)")
        st.text_area("Your Feedback")
        
        if st.form_submit_button("Submit"):
            st.success("Thanks!")
            
    st.markdown("<div style='text-align: center; color: #666; font-size: 12px; margin-top: 20px;'>&copy; 2025 Deepfake Detection System</div>", unsafe_allow_html=True)
