def main():
    family = open(r'.\practice_files\familyInfo.txt', 'w')
    family.write('Reena Patel\n')
    family.write('Ashish\n')
    family.write('Ram\n')
    family.write('Gita\n')
    family.write('Veer\n')
    family.write('Shyam\n')

    family.close()

    infile = open(r'.\practice_files\familyInfo.txt', 'r')

    print(infile.read())





if __name__ == '__main__':
    main()