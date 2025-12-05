import streamlit as st

def show_footer():
    st.markdown("---")
    
    # عنوان قسم الفريق
    st.markdown("<h3 style='text-align: center; color: #fff;'>Meet the Team</h3>", unsafe_allow_html=True)
    
    # ---------------------------------------------------------
    # 1. بيانات أعضاء الفريق (عدل الأسماء والصور واللينكات هنا)
    # ---------------------------------------------------------
    team_members = [
        {"name": "Ahmed Sief Eleslam", "role": "AI Engineer", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140048.png", "link": "#"},
        {"name": "Member 2", "role": "Data Scientist", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140037.png", "link": "#"},
        {"name": "Member 3", "role": "Backend Dev", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140047.png", "link": "#"},
        {"name": "Member 4", "role": "Frontend Dev", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140051.png", "link": "#"},
        {"name": "Member 5", "role": "Researcher", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140040.png", "link": "#"},
        {"name": "Member 6", "role": "Manager", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140039.png", "link": "#"},
    ]

    # ---------------------------------------------------------
    # 2. CSS (التصميم عشان يجوا جنب بعض)
    # ---------------------------------------------------------
    st.markdown("""
    <style>
    .team-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 20px;
        margin-bottom: 40px;
        padding: 10px;
    }
    
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
        transform: translateY(-5px);
        border-color: #ff4b4b;
    }
    
    .card img {
        border-radius: 50%;
        width: 80px;
        height: 80px;
        object-fit: cover;
        margin-bottom: 10px;
        border: 2px solid #ff4b4b;
    }
    
    .card h4 {
        margin: 5px 0;
        font-size: 16px;
        color: #fff;
        font-weight: 600;
    }
    
    .card p {
        color: #aaa;
        font-size: 13px;
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
    # 3. تحويل البيانات لـ HTML وعرضها
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

    # السطر ده هو اللي بيخلي الكود يظهر كشكل مش كنص
    st.markdown(cards_html, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 4. قسم الفيدباك (Feedback Form) - رجعناه تاني
    # ---------------------------------------------------------
    st.write("---")
    st.subheader("📩 Send Feedback")
    
    with st.form("feedback_form"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Name (Optional)")
        with c2:
            email = st.text_input("Email (Optional)")
            
        feedback = st.text_area("Your Feedback", placeholder="Tell us what you think or report a bug...")
        
        submitted = st.form_submit_button("Submit Feedback")
        
        if submitted:
            st.success("Thank you for your feedback!")

    # حقوق الملكية في النهاية
    st.markdown("<br><p style='text-align: center; color: #666; font-size: 12px;'>&copy; 2025 Deepfake Detection System</p>", unsafe_allow_html=True)
