import uuid 
import socket
import smtplib
msg=""
EMAIL_ADDRESS='username@gmail.com'#sender mail
PASSWORD='password'#seder pass
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
msg=msg+(f"Hostname: {hostname}")
msg=msg+(f"IP Address: {ip_address}") 
msg=msg+(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
for ele in range(0,8*6,8)][::-1])) 
print(msg)
##############################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

a=0
receivers=["recipent@gmail.com"]#recipent mail
def send_email(subject,msg):
	try:
		server=smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		#print("1")
		server.starttls()
		server.login(EMAIL_ADDRESS, PASSWORD)
		#print('3')
		message='subject:{}\n {}'.format(subject, msg)
		#print('4')
		for words in receivers:
			server.sendmail(EMAIL_ADDRESS,words,message)#sender,recier,email
		#print('5')
		server.quit()
		#i=len.receivers()
		print(receivers)
		#print("EMail sent")
		a=1
	except:
		#print("email failed")
		a=2
subject='software launched'

send_email(subject,msg)