import streamlit as st

def show_footer():
    st.write("---")
    
    # 1. العنوان
    st.markdown("<h3 style='text-align: center; color: #fff; margin-bottom: 30px;'>Meet the Team</h3>", unsafe_allow_html=True)
    
    # 2. البيانات (تقدر تعدل اللينكات هنا)
    team_members = [
        {
            "name": "Ahmed Sief Eleslam", 
            "role": "AI Engineer", 
            "img": "https://media.licdn.com/dms/image/v2/D4D03AQE4AQyY8K67nA/profile-displayphoto-scale_200_200/B4DZf4ftipGsAc-/0/1752220753755?e=1766620800&v=beta&t=uYgHHsyOaoOkzIoPcwUKWf2zBD0osVRpSTpXBK-yJ4Y", 
            "linkedin": "https://www.linkedin.com/in/ahmed-sief-eleslam-124b4a249/", 
            "github": "https://github.com/ahmedsief0"
        },
        {
            "name": "Mohamed Ragab", 
            "role": "Data Scientist", 
            "img": "https://cdn-icons-png.flaticon.com/512/4140/4140037.png", 
            "linkedin": "#", 
            "github": "#"
        },
        {
            "name": "Youssef ezzat", 
            "role": "Backend Dev", 
            "img": "https://cdn-icons-png.flaticon.com/512/4140/4140047.png", 
            "linkedin": "#", 
            "github": "#"
        },
        {
            "name": "Omar Mostafa", 
            "role": "Frontend Dev", 
            "img": "https://cdn-icons-png.flaticon.com/512/4140/4140051.png", 
            "linkedin": "#", 
            "github": "#"
        },
        {
            "name": "Osama Abdelrahman", 
            "role": "Researcher", 
            "img": "https://cdn-icons-png.flaticon.com/512/4140/4140040.png", 
            "linkedin": "#", 
            "github": "#"
        },
        {
            "name": "Mohab Hamdy", 
            "role": "Manager", 
            "img": "https://cdn-icons-png.flaticon.com/512/4140/4140039.png", 
            "linkedin": "#", 
            "github": "#"
        },
    ]

    # 3. CSS (التعديلات هنا: كبرنا المقاسات وظبطنا الـ Grid ليكون 3)
    st.markdown("""
    <style>
    .team-grid {
        display: grid;
        /* الرقم 250px ده هو اللي بيتحكم انهم يبقوا 3 جنب بعض على الشاشات العادية */
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 25px; /* مسافة أوسع بين الكروت */
        margin-bottom: 50px;
    }
    .team-card {
        background-color: #262730;
        border: 1px solid #444;
        border-radius: 15px; /* زوايا أنعم */
        padding: 25px; /* مساحة داخلية أكبر */
        text-align: center;
        transition: transform 0.3s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .team-card:hover {
        transform: translateY(-8px);
        border-color: #ff4b4b;
        box-shadow: 0 8px 15px rgba(255, 75, 75, 0.2);
    }
    .team-card img {
        width: 110px; /* كبرنا الصورة */
        height: 110px;
        border-radius: 50%;
        margin-bottom: 15px;
        border: 3px solid #ff4b4b;
    }
    .team-card h4 {
        margin: 0;
        font-size: 22px; /* كبرنا اسم الشخص */
        color: #fff;
        font-weight: 700;
    }
    .team-card p {
        margin: 8px 0 20px 0;
        font-size: 15px; /* كبرنا المسمى الوظيفي */
        color: #bbb;
    }
    /* تنسيق أزرار لينكدإن وجيت هاب */
    .social-box {
        display: flex;
        justify-content: center;
        gap: 15px;
    }
    .social-box a {
        text-decoration: none;
        color: #fff;
        font-size: 14px;
        font-weight: bold;
        background-color: #ff4b4b;
        padding: 8px 16px; /* زرار أكبر */
        border-radius: 6px;
        transition: background-color 0.3s, transform 0.2s;
    }
    .social-box a:hover {
        background-color: #d43b3b;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

    # 4. تجميع HTML (بدون مسافات عشان المشكلة السابقة)
    cards_html = '<div class="team-grid">'
    for member in team_members:
        cards_html += (
            f'<div class="team-card">'
            f'<img src="{member["img"]}" alt="{member["name"]}">'
            f'<h4>{member["name"]}</h4>'
            f'<p>{member["role"]}</p>'
            f'<div class="social-box">'
            f'<a href="{member["linkedin"]}" target="_blank">LinkedIn</a>'
            f'<a href="{member["github"]}" target="_blank">GitHub</a>'
            f'</div>'
            f'</div>'
        )
    cards_html += '</div>'

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
        st.text_area("Your Feedback", height=100)
        
        if st.form_submit_button("Submit"):
            st.success("Thank you for your feedback!")
            
    st.markdown("<div style='text-align: center; color: #666; font-size: 13px; margin-top: 30px;'>&copy; 2025 Deepfake Detection System | All rights reserved</div>", unsafe_allow_html=True)
show_footer()    
