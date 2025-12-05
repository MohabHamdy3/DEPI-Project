import streamlit as st

def show_footer():
    st.markdown("---")
    
    # ---------------------------------------------------------
    # 1. TEAM SECTION (Interactive Cards)
    # ---------------------------------------------------------
    st.markdown("<h3 style='text-align: center;'>Meet the Team</h3>", unsafe_allow_html=True)
    
    # قائمة بأسماء الفريق وبياناتهم (تقدر تعدل الصور واللينكات من هنا)
    team_members = [
        {
            "name": "Ahmed Sief Eleslam",
            "role": "AI Engineer & Developer",
            "img": "https://cdn-icons-png.flaticon.com/512/4140/4140048.png", # استبدلها بصورتك الحقيقية لو حابب
            "linkedin": "#",
            "github": "#"
        },
        {
            "name": "Team Member 2",
            "role": "Data Scientist",
            "img": "https://cdn-icons-png.flaticon.com/512/4140/4140037.png",
            "linkedin": "#",
            "github": "#"
        },
        # تقدر تزود أعضاء تانيين هنا
    ]

    # تصميم الـ CSS عشان الكروت تكون تفاعلية وشكلها حلو
    st.markdown("""
    <style>
    .team-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 20px;
        margin-bottom: 30px;
    }
    .card {
        background-color: #262730; /* لون الكارت (يتماشى مع الدارك مود) */
        border-radius: 15px;
        padding: 20px;
        width: 250px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        transition: transform 0.3s, box-shadow 0.3s;
        border: 1px solid #444;
    }
    .card:hover {
        transform: translateY(-10px); /* حركة الرفع لفوق */
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
        border-color: #ff4b4b; /* لون حدود أحمر عند الوقوف عليه */
    }
    .card img {
        border-radius: 50%;
        width: 100px;
        height: 100px;
        object-fit: cover;
        margin-bottom: 15px;
        border: 3px solid #ff4b4b;
    }
    .card h4 {
        margin: 10px 0 5px 0;
        color: #fff;
    }
    .card p {
        color: #aaa;
        font-size: 14px;
        margin-bottom: 15px;
    }
    .social-links a {
        text-decoration: none;
        margin: 0 10px;
        font-size: 20px;
        color: #fff;
        transition: color 0.3s;
    }
    .social-links a:hover {
        color: #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

    # تكوين كود الـ HTML للكروت
    cards_html = '<div class="team-container">'
    for member in team_members:
        cards_html += f"""
        <div class="card">
            <img src="{member['img']}" alt="{member['name']}">
            <h4>{member['name']}</h4>
            <p>{member['role']}</p>
            <div class="social-links">
                <a href="{member['linkedin']}" target="_blank">LinkedIn</a>
                <a href="{member['github']}" target="_blank">GitHub</a>
            </div>
        </div>
        """
    cards_html += '</div>'

    st.markdown(cards_html, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 2. FEEDBACK SECTION
    # ---------------------------------------------------------
    st.write("---")
    st.subheader("📩 Send Feedback")
    
    with st.form("feedback_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name (Optional)")
        with col2:
            email = st.text_input("Email (Optional)")
            
        feedback = st.text_area("Your Feedback", placeholder="Tell us what you think or report a bug...")
        
        submitted = st.form_submit_button("Submit Feedback")
        
        if submitted:
            if feedback:
                # هنا ممكن تضيف كود يبعت الإيميل ليك أو يسيف الداتا في فايل
                # كمثال بسيط هنعرض رسالة شكر
                st.success("Thank you for your feedback! We appreciate it.")
            else:
                st.warning("Please write some feedback before submitting.")
