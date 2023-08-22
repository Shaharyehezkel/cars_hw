
def user():
    name = input("Enter your name: ")
    lastName = input("Enter your last name: ")
    # print(name)
    # print(lastName)
    thisdict  = {
    "name": name,
    "last name": lastName,
    } 
    return(thisdict)

def main():
    print(user())


# if __name__ == '__main__':
main()



