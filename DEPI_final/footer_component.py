import streamlit as st

def show_footer():
    st.markdown("---")
    
    # 1. عنوان الفريق
    st.markdown("<h3 style='text-align: center; color: #fff; margin-bottom: 20px;'>Meet the Team</h3>", unsafe_allow_html=True)
    
    # 2. بيانات الـ 6 أعضاء (تقدر تغير الصور والأسماء براحتك)
    team_members = [
        {"name": "Ahmed Sief", "role": "AI Engineer", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140048.png", "link": "#"},
        {"name": "Member 2", "role": "Data Scientist", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140037.png", "link": "#"},
        {"name": "Member 3", "role": "Backend Dev", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140047.png", "link": "#"},
        {"name": "Member 4", "role": "Frontend Dev", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140051.png", "link": "#"},
        {"name": "Member 5", "role": "Researcher", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140040.png", "link": "#"},
        {"name": "Member 6", "role": "Manager", "img": "https://cdn-icons-png.flaticon.com/512/4140/4140039.png", "link": "#"},
    ]

    # 3. تصميم CSS يضمن ظهور الكروت بجانب بعضها
    st.markdown("""
    <style>
    .team-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 15px;
        justify-items: center;
        margin-bottom: 40px;
    }
    .team-card {
        background-color: #262730;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 15px;
        width: 100%;
        text-align: center;
        transition: transform 0.3s ease;
    }
    .team-card:hover {
        transform: translateY(-5px);
        border-color: #ff4b4b;
    }
    .team-card img {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        object-fit: cover;
        margin-bottom: 10px;
        border: 2px solid #ff4b4b;
    }
    .team-card h4 {
        margin: 5px 0;
        font-size: 16px;
        color: #fff;
    }
    .team-card p {
        font-size: 12px;
        color: #aaa;
        margin-bottom: 10px;
    }
    .team-card a {
        text-decoration: none;
        color: #ff4b4b;
        font-weight: bold;
        font-size: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

    # 4. بناء كود HTML للكروت
    html_code = '<div class="team-grid">'
    for member in team_members:
        html_code += f"""
        <div class="team-card">
            <img src="{member['img']}">
            <h4>{member['name']}</h4>
            <p>{member['role']}</p>
            <a href="{member['link']}" target="_blank">View Profile</a>
        </div>
        """
    html_code += '</div>'

    # عرض الكروت (هنا السر: استخدام markdown مرة واحدة للكل)
    st.markdown(html_code, unsafe_allow_html=True)

    # 5. صندوق الفيدباك (زي ما طلبت يكون موجود تحت)
    st.write("---")
    st.subheader("📩 Send Feedback")
    
    with st.form("feedback_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Name (Optional)")
        with col2:
            st.text_input("Email (Optional)")
            
        st.text_area("Your Feedback", placeholder="Tell us what you think...")
        
        if st.form_submit_button("Submit Feedback"):
            st.success("Thank you for your feedback!")
            
    # الحقوق
    st.markdown("<div style='text-align: center; color: #666; font-size: 12px; margin-top: 20px;'>&copy; 2025 Deepfake Detection System</div>", unsafe_allow_html=True)
