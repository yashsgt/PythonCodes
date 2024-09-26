age=int(input("enter your age"))
citizen=input("are you a citizen?")
voter_id=input("do you have a voter_id card?")

if(age>18):
    if citizen == 'yes':
        print("yes you are a citizen")
    else:
        print("as you are not a citizen you are not allowed to cast your vote")
        if voter_id == 'yes':
            print("yes you can give vote")
        else:
            print("no you can't give a vote")