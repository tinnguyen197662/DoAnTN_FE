import streamlit as st
from flask import Flask, jsonify, request
from langdetect import detect
import requests
from IPython.display import HTML
# Set favicon
st.set_page_config(page_title="Streamlit App", page_icon="static/res/favicon.png")

st.markdown(
    '''
    <style>
        .center-image {
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .header-image {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .header-image img {
            max-width: 80%;
            height: auto;
        }
        
        .container {
            display: grid;
            grid-template-columns: 8fr 2fr; /* Tỉ lệ 8:2 */
            align-items: center;
            text-align: center;
        }
        a:visited {
            color: blue;
        }
    </style>
    <a href="https://hcmut.edu.vn">
    <div class="header-image">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/HCMUT_official_logo.png/200px-HCMUT_official_logo.png" alt="Header image" style="max-width: 100%; max-height: 100%;">
    </div>
    </a>
    <p></p>
    <p></p>
    <body>
        <header>
            <div class="container">
                <h1>Question Answering System</h1>
                <div class="center-image">
                    <img src="https://rksemitronics.com/image/bot.png" style="max-width: 80%; max-height: 80%;">
                </div>
            </div>
        </header>
        <br/>
    </body>
    ''',
    unsafe_allow_html=True
)

# Load the question answering model and tokenizer
# User input
question_input = st.text_input("**Question:**")

if question_input:
    language = detect(question_input)
    
    if language == 'en':
        no_answer = 'No answer found for this question'
        content_detail = 'See more detail at'
        more_info = 'You can check out more information here'
    else:
        no_answer = 'Không tìm thấy câu trả lời phù hợp với câu hỏi'
        content_detail = 'Nội dung chi tiết'
        more_info = 'Ngoài ra, bạn có thể tham khảo một số bài viết liên quan đến câu hỏi bạn đang tìm kiếm'
        
    QA_input = {
        'question': question_input
    }
    api_url = 'http://127.0.0.1:8080/questions'
    
    # res = requests.post(api_url, json=QA_input)
    # res = res.json()
    res = {
        "context": [
            [
                "Trường xét và công nhận tốt nghiệp trong các học kỳ chính, vào khoảng cuối mỗi tháng. Sinh viên được xét và công nhận tốt nghiệp khi có đủ các điều kiện sau: ",
                "Truy cập văn bản <b>2933_Quyết định ban hành Quy định học vụ và đào tạo bậc Đại học</b> nằm trong thư mục <a href='https://drive.google.com/drive/u/1/folders/1cL0f1uaKJ7hF3QXuyZZAiOlzytj6fTbE'>quy chế</a>",
                "Trong tốt nghiệp , Với nội dung về công nhận tốt nghiệp:  Sinh viên được xét và công nhận tốt nghiệp khi có đủ các điều kiện sau: \na) Tích lũy đủ học phần, số tín chỉ của chương trình đào tạo, đạt chuẩn đầu ra của chương trình đào tạo; b) Hoàn thành chương trình Giáo dục Quốc phòng - An ninh và chương trình Giáo dục Thể chất; c) Hoàn thành chương trình rèn luyện sinh viên theo quy định của nhà trường; d) Đạt chuẩn ngoại ngữ tốt nghiệp và các chuẩn khác của nhà trường; e) Điểm trung bình tích lũy của toàn khóa học đạt từ trung bình trở lên; f) Tại thời điểm xét tốt nghiệp không bị truy cứu trách nhiệm hình sự hoặc không đang trong thời gian bị kỷ luật ở mức đình chỉ học tập. \nTrường xét và công nhận tốt nghiệp trong các học kỳ chính, vào khoảng cuối mỗi tháng."
            ],
            [
                [
                    "Giấy này không thay thế cho bằng tốt nghiệp. trong thời hạn 03 tháng tính từ thời điểm sinh viên đáp ứng đầy đủ điều kiện tốt nghiệp và hoàn thành nghĩa vụ với nhà trường ",
                    "Truy cập văn bản <b>2933_Quyết định ban hành Quy định học vụ và đào tạo bậc Đại học</b> nằm trong thư mục <a href='https://drive.google.com/drive/u/1/folders/1cL0f1uaKJ7hF3QXuyZZAiOlzytj6fTbE'>quy chế</a>"
                ],
                [
                    "Giấy này không thay thế cho bằng tốt nghiệp. 21 trong thời hạn 03 tháng tính từ thời điểm sinh viên đáp ứng đầy đủ điều kiện tốt nghiệp và hoàn thành nghĩa vụ với nhà trường ",
                    "Truy cập văn bản <b>Quy định về học vụ và đào tạo bậc đại học - phiên bản hợp nhất</b> nằm trong thư mục <a href='https://drive.google.com/drive/u/1/folders/1cL0f1uaKJ7hF3QXuyZZAiOlzytj6fTbE'>quy chế</a>"
                ]
            ]
        ],
        "link": "Truy cập vào bài viết <a href='https://mybk.hcmut.edu.vn/bksi/public/vi/blog/lch-trnh-ng-k-tt-nghipv-cp-bng-t-thng-042023'>LỊCH TRÌNH ĐĂNG KÝ TỐT NGHIỆP VÀ CẤP BẰNG ĐỢT THÁNG /</a> để xem thông tin chi tiết"
    }
    if res == {}:
        html_string = f"""
        <div> <b>Answer: </b>
            {no_answer}
            <br/>
        </div>
        """
    else:
        best_answer = res['context'][0]
        another_answers = res['context'][1]
        if best_answer ==-1:
            # best_answer = [no_answer]
            html_string = f"""
                <div> <b>Answer: </b>
                    {no_answer}
                    <br/>
                </div>
                """
        else:
            html_string = f"""
                <div> <b>Answer: </b>
                    {best_answer[0]}
                    <br/><br/>
                    <i> <b>{content_detail}:</b>  {best_answer[1]}</i>
                </div>
                <div>
                <br/>
            """
        # Display the answer
        # Khởi tạo chuỗi HTML với phần thông tin cố định
        
        if res['link'] != -1:
            html_content = f"<b>{more_info}:</b><br/><i>-{res['link']}</i>"
        else:
            if len(another_answers) ==0:
                html_content = ""
            else:
                html_content = f"<b>{more_info}:</b>"
        html_string += html_content
        # Thêm các phần tử từ danh sách another_answers vào chuỗi HTML
        for answer in another_answers:
            html_string += f"""
            <br/>
            <i>-{answer}</i> 
            """

        # Kết thúc chuỗi HTML
        html_string += "</div>"

    # Hiển thị chuỗi HTML
    st.html(html_string)
