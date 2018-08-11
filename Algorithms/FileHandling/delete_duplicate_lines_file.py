# Author: Sami Ahmad Khan
# File_overview: Delete duplicate lines in a file.
#  **
#   Follow up: If the file is very large, general hash map takes too much spaces,
#   come up with a better solution.
#  **

import os
import glob

def read_files():
    directory = './splits/'
    for i, f in enumerate(os.listdir(directory)):
        with open(directory+f) as fin:
            content = fin.read().splitlines()
        content = set(content)

        fout = open("./splits/split-%d"%i,"wb")
        for line in content:
            fout.write(line)

        fout.close()


def delete_duplicates(lines):
    new_content = set()
    for line in lines:
        new_content.add(line)

    return new_content

def split_chunks(File):
    NUM_OF_LINES = 1000
    file_size = os.stat(File).st_size

    with open(File) as fin:
        if not os.path.exists('./splits'):
            os.makedirs('./splits')

        fout = open("./splits/split-0","wb")

        for i, line in enumerate(fin):
            fout.write(line)
            if (i+1)%NUM_OF_LINES == 0:
                fout.close()
                fout = open("./splits/split-%d"%(i/NUM_OF_LINES+1),"wb")
        fout.close()



if __name__ == "__main__":
    # read_file('dummy_file')
    split_chunks('dummy_file')
    read_files()
