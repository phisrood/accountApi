from flask import render_template
import bcrypt
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

def encryptPassword(password):
    return bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt())

def checkPassword(sourcePassword, inputPassword):
    return bcrypt.checkpw(inputPassword.encode("UTF-8"), sourcePassword.encode("UTF-8"))

# 인증메일 보내기
def send_email(account):
    # 메세지 내용
    msg = MIMEBase("multipart", "mixed")
    msg['Subject'] = '제목 테스트'
    htmlBody = render_template('renderMailAuth.html', user_id=account.user_id)

    # htmlFD = open('renderMailAuth.html', 'rb')
    HtmlPart = MIMEText(htmlBody, 'html', _charset='UTF-8')
    # htmlFD.close()

    msg.attach(HtmlPart)

    # 세션 생성
    # smtplib.SMTP(SMTP변수, 포트번호)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # TLS보안 설정
    s.starttls()
    # 로그인 인증
    # s.login('지메일계정','앱비밀번호')
    s.login('kymDev0124@gmail.com', 'qkcnlldrijkkdvqd')
    # 메일 보내기
    # s.sendmail('보내는메일주소','받는메일주소',메세지내용)
    s.sendmail('kymDev0124@gmail.com', account.email, msg.as_string().encode("UTF-8"))
    print('메일보내기 성공')
    # 세션종료
    s.quit()