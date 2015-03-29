# Calculates running median of number of words in lines of text files
import os
import numpy as np

def running_median():
        pathname=input("Path to files: ")
        listfiles=[file for file in os.listdir(pathname) if file.lower().endswith('.txt')]

        numwords=[]
        midian=[]
        # get list of text files in directory
        for s in listfiles:

                # separate text into lines
            lines=[line.strip() for line in open(os.path.join(pathname,s),'r')]

            #count number of words per line, put into array and get median
            for t in range(len(lines)):
                counts={}
                text=lines[t]
                for weird_characters in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
                    text = text.replace(weird_characters, '')
                txx=text.split()
                for w in txx:
                    counts[w]=counts.get(w,0)+1
                numwords.append(sum(counts.values()))
                mdian=np.median(numwords)
                midian.append(mdian)
                #print mdian

        # Write computed running medians to text file
        enter_output_dir=input("Enter path to wc_output directory: ")
        write_to = open(os.path.join(enter_output_dir,'med_result.txt'),'w')
        
        for i in midian:
                write_to.write("%s\n" % i)

        write_to.close()
