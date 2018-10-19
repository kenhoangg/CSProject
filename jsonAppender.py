import os
from os import listdir
from os.path import isfile, join

'''
Appends one .json file to another .json file
for use in congregating the annotated .json files together
'''

def cat_json(output_filename, input_filenames):
    with open(output_filename, "w") as outfile:
        firstFile = True
        for infile_name in input_filenames:
            with open(infile_name) as infile:
                if firstFile:
                    outfile.write('[')
                    firstFile = False
                else:
                    outfile.write(',')
                outfile.write(mangle(infile.read()))
        outfile.write(']')

def mangle(s):
    return s.strip()[1:-1] #start:end possibly need to change

def main():
    #create new file name 'annotations_group.json' to append the file data
    output_file = open('annotations_group.json', 'w+')
    mypath = os.getcwd()
    input_files = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
    cat_json('annotations_group.json', input_files)

if __name__ == '__main__':
    main()