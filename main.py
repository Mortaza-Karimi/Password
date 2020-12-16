import stdiomask

count=1
while count<=3:
    pass_ = stdiomask.getpass(prompt="\033[92m"+"Enter a Password (passwors esme to hast. peidash kon): ",mask="●")
    if pass_=="mousavifard":
        print("\nAffarin, password dorost bood \n")
        break
    else:
        if count<3:
            print("\npassword Eshtebahe,dobare emtehan kon \n")
            count+=1
        else:
            break
if count==3 and pass_!="mousavifard":
    print("\nshoma bish az had talash kardid. lotfan badan talash konid")
input("\nPress Enter to Exit ... \n")
print("\033[0m"+"")
