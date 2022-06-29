import string


def password_check(passwd):
    specialSymb=['$','@','#','%']
    val=True
    if len (passwd)<6:
        print('the length of the password should be greater than 6')
        val=False
    if len (passwd)>20:
        print('the length should not be greater than 20')
        val= False
    if not any (char.isdigit() for char in passwd):
        print('passwd should have atleast one numeric value')
        val= False
    if not any (char.isupper() for char in passwd):
        print('pasword should have atleast 1 upper case ')
        val=False
    if not any (char.islower() for char in passwd):
        print('pasword should have atleast 1 lower case ')
        val=False

    if not any(char in specialSymb for char in passwd):
        print('passwd must have special symbol')
        val=False

    if val:
        return val
def main():
    passwd = input("enter thePassword: ")
    

    if (password_check(passwd)):
        print('Password is valid ')
    else:
        print('pasword is invalid')

main()