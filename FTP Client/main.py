from ftplib import FTP

host="videoftb.test.net"
user="videoftbput"
password="testPw"


with FTP(host)as ftp:
    ftp.login(user=user,passwd=password)
    print(ftp.getwelcome())

    with open('test.txt','wb') as f:
        ftp.retrbinary("RETR"+"myTest.txt",f.write,1024)

    ftp.quit()