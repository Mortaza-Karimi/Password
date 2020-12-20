import stdiomask

class Password():
    def __init__(self):
        self.count = 1
    def Enter_password(self,pass_):
        while count<=3:
            if pass_=="password":
                print("\nAffarin, password dorost bood \n")
                break
            else:
                if count<3:
                    print("\npassword Eshtebahe,dobare emtehan kon \n")
                    count+=1
                else:
                    break
        if count==3 and pass_!="password":
            print("\nshoma bish az had talash kardid. lotfan badan talash konid")
        input("\nPress Enter to Exit ... \n")
        print("\033[0m"+"")
    def run_program(self):
        self.Enter_password()
if __name__=="__main__":
    run = Password()
    run.run_program()
        
