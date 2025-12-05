import streamlit as st

def show_footer():
    st.markdown("---")
    
    st.markdown("<h3 style='text-align: center; color: #fff;'>Meet the Team</h3>", unsafe_allow_html=True)
    
    # ---------------------------------------------------------
    # 1. قائمة الـ 6 أعضاء
    # ---------------------------------------------------------
    team_members = [
        {"name": "Member 1", "role": "AI Engineer", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140048.png", "link": "#"},
        {"name": "Member 2", "role": "Data Scientist", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140037.png", "link": "#"},
        {"name": "Member 3", "role": "Backend Dev", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140047.png", "link": "#"},
        {"name": "Member 4", "role": "Frontend Dev", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140051.png", "link": "#"},
        {"name": "Member 5", "role": "Researcher", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140040.png", "link": "#"},
        {"name": "Member 6", "role": "Manager", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140039.png", "link": "#"},
    ]

    # ---------------------------------------------------------
    # 2. CSS عشان الكروت تيجي جنب بعض (Grid Layout)
    # ---------------------------------------------------------
    st.markdown("""
    <style>
    /* الحاوية الرئيسية للكروت */
    .team-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); /* يوزعهم أوتوماتيك */
        gap: 15px;
        margin-bottom: 20px;
        padding: 10px;
    }
    
    /* تصميم الكارت الواحد */
    .card {
        background-color: #262730;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        transition: transform 0.2s;
        border: 1px solid #444;
    }
    
    .card:hover {
        transform: scale(1.05);
        border-color: #ff4b4b;
    }
    
    .card img {
        border-radius: 50%;
        width: 70px; /* صغرت الصورة شوية عشان الـ 6 يكفوا */
        height: 70px;
        object-fit: cover;
        margin-bottom: 10px;
        border: 2px solid #ff4b4b;
    }
    
    .card h4 {
        margin: 5px 0;
        font-size: 16px;
        color: #fff;
    }
    
    .card p {
        color: #aaa;
        font-size: 12px;
        margin: 0;
    }
    
    .card a {
        display: inline-block;
        margin-top: 10px;
        text-decoration: none;
        color: #ff4b4b;
        font-size: 12px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 3. تكوين الـ HTML
    # ---------------------------------------------------------
    cards_html = '<div class="team-container">'
    for member in team_members:
        cards_html += f"""
        <div class="card">
            <img src="{member['img']}" alt="{member['name']}">
            <h4>{member['name']}</h4>
            <p>{member['role']}</p>
            <a href="{member['link']}" target="_blank">View Profile</a>
        </div>
        """
    cards_html += '</div>'

    st.markdown(cards_html, unsafe_allow_html=True)
    
    # حقوق الملكية في الآخر
    st.markdown("<p style='text-align: center; color: #666; font-size: 12px;'>&copy; 2025 Deepfake Detection System</p>", unsafe_allow_html=True)
