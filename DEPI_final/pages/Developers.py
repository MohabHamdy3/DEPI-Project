import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
def send_email(name, email, message):
    sender_email = "YOUR_GMAIL@gmail.com"
    app_password = "eirf hmin zwbn psvt"  # من جوجل 16 حرف

    receiver_email = "ahmedsiefeleslam22@gmail.com"  # الإيميل اللي توصله الفيدباك

    subject = "New Feedback Received"
    
    body = f"""
    New feedback from your Streamlit App:

    Name: {name}
    Email: {email}
    
    Message:
    {message}
    """

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        return False
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
            "img": "https://media.licdn.com/dms/image/v2/D4D03AQF43t24jBTPdQ/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1706702711219?e=1766620800&v=beta&t=K7HEMSjkhIcuXXGOOpCN8v0fAEj5neEocpnDBNcCS0A", 
            "linkedin": "https://www.linkedin.com/in/moragab-22nov04/", 
            "github": "#"
        },
        {
            "name": "Youssef ezzat", 
            "role": "Backend Dev", 
            "img": "https://media.licdn.com/dms/image/v2/D4E03AQFR2tal4VhfRQ/profile-displayphoto-scale_200_200/B4EZrD1G1THoAY-/0/1764222071472?e=1766620800&v=beta&t=gS5ZHi4PI1cFAnLRFNqgZaP9n2pKKZmG3rc9rPfwEco", 
            "linkedin": "https://www.linkedin.com/in/youssefezzatb/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app", 
            "github": "#"
        },
        {
            "name": "Omar Mostafa", 
            "role": "Frontend Dev", 
            "img": "https://media.licdn.com/dms/image/v2/D4E35AQHYhmZcYm6aRw/profile-framedphoto-shrink_200_200/B4EZgYEjmaGUAc-/0/1752750504632?e=1765551600&v=beta&t=0hD_T-Gcy9sfvXzjeBkF9fpuSK_46y6qsFHcMdzju5o", 
            "linkedin": "https://www.linkedin.com/in/omar-mostafa-omar/?utm_source=share_via&utm_content=profile&utm_medium=member_android", 
            "github": "#"
        },
        {
            "name": "Osama Abdelrahman", 
            "role": "Researcher", 
            "img": "https://cdn-icons-png.flaticon.com/512/4140/4140040.png", 
            "linkedin": "https://www.linkedin.com/in/osamaabdelrahman1/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app", 
            "github": "#"
        },
        {
            "name": "Mohab Hamdy", 
            "role": "Manager", 
            "img": "https://media.licdn.com/dms/image/v2/D4E03AQH0WeL9l4l1xg/profile-displayphoto-shrink_200_200/B4EZW5QtmvHcAY-/0/1742569921364?e=1766620800&v=beta&t=yKHUOpIplRIYlIE_hmiKmT8O2PBLrAC3dxG7-tnS2KI", 
            "linkedin": "https://www.linkedin.com/in/mohabhamdy/", 
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
            name = st.session_state.get("name_input", "")
            email = st.session_state.get("email_input", "")
            msg = st.session_state.get("feedback_input", "")

            if msg.strip() == "":
                st.error("Please write your feedback first.")
            else:
                ok = send_email(name, email, msg)
                if ok:
                    st.success("Your feedback has been sent successfully!")
                else:
                    st.error("Failed to send the email. Please try again later.")
            
    st.markdown("<div style='text-align: center; color: #666; font-size: 13px; margin-top: 30px;'>&copy; 2025 Deepfake Detection System | All rights reserved</div>", unsafe_allow_html=True)
show_footer()    
