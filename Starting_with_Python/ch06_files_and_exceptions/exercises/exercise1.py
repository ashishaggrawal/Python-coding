
def main():
    outfile = open(r'.\practice_files\contractor_names.txt','w')

    #write the names of new employees in this file

    outfile.write('Tom\n')
    outfile.write('Ava\n')
    outfile.write('Ben\n')
    outfile.write('Zoe\n')
    outfile.write('Sam\n')
    outfile.write('Mia\n')
    outfile.write('Eli')
    # we will close the files now
    outfile.close()

main()