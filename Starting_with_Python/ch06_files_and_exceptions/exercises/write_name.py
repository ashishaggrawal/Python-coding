def main():
    print("Enter the names of three friends: ")
    name1 = input("Friend #1: ")
    name2 = input("Friend #2: ")
    name3 = input("Friend #3: ")

    myfile = open(r'.\practice_files\familyInfo.txt','a')

    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    myfile.close()

    print("These names were written to familyInfo.txt")

    file2 = open(r'.\practice_files\familyInfo.txt','r')
    print(file2.read())

if __name__ == '__main__':
    main()
    