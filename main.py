from SolitaireCipher import SolitaireCipher

def read_from_file(name_file):
    f = open(name_file, 'r')
    return f.read()


if __name__ == '__main__':
    strInput = ''
    option = input('Welcome! do you want to enter text or import a file? \n')
    if option == 'enter':
        strInput = input("enter text \n")
    elif option == 'import':
        name_file = input("enter name of file \n")
        strInput = read_from_file(name_file)
    solitaire = SolitaireCipher(message=strInput)
    solitaire.encrypt()
    print(solitaire.get_encryption())
    solitaire.decrypt()
    print(solitaire.get_decryption())
    print(solitaire.get_stream())

