import smtplib
from email.mime.text import MIMEText

# 세션 생성
send_mail = smtplib.SMTP('smtp.gmail.com', 587)
 
# TLS 보안 시작
send_mail.starttls()
 
# 로그인 인증
send_mail.login('bluenote212smart@gmail.com', 'geherkwbgdblqhst')
 
# 보낼 메시지 설정
msg = MIMEText('블라블라블라')
msg['Subject'] = 'test'
 
# 메일 보내기
send_mail.sendmail('bluenote212@telechips.com', ['bluenote212@telechips.com'], msg.as_string())
 
# 세션 종료
send_mail.quit()