import stdiomask
from colorama import Fore

class Password():
    def __init__(self):
        self.count = 1

    def Enter_password(self):

        while self.count<=3:
            
            pass_ = stdiomask.getpass(prompt = "Enter Password: ")

            if pass_ == "password":
                print(Fore.GREEN + "\nAffarin, password dorost bood \n")
                quit()
            else:
                if self.count < 3:
                    print(Fore.YELLOW + "\npassword Eshtebahe,dobare emtehan kon \n")
                    self.count += 1
                    continue
                else:
                    print(Fore.RED +  "\nshoma bish az had talash kardid. lotfan badan talash konid")
                    input("\nPress Enter to Exit ... \n")
                    quit()
    def run_program(self):
        self.Enter_password()
if __name__=="__main__":
    run = Password()
    run.run_program()
        
