
def main():
    outfile = open(r'.\practice_files\contractor_names.txt','w')

    #write the names of new employees in this file

    outfile.write('John\n')
    outfile.write('Sita\n')
    outfile.write('Ashish\n')
    outfile.write('Priya\n')
    outfile.write('Reena\n')
    outfile.write('Aru\n')
    outfile.write('Sonal')
    # we will close the files now
    outfile.close()

main()