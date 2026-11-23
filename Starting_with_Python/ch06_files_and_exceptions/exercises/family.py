def main():
    family = open(r'.\practice_files\familyInfo.txt', 'w')
    family.write('Maya Collins\n')
    family.write('Leo\n')
    family.write('Nora\n')
    family.write('Owen\n')
    family.write('Isla\n')
    family.write('Felix\n')

    family.close()

    infile = open(r'.\practice_files\familyInfo.txt', 'r')

    print(infile.read())





if __name__ == '__main__':
    main()