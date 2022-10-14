#!/usr/bin/env python3

#write a script to download file, open and read the contents, uppercase each line andprint each line to the STDOUT



#print the contents to the screen
file=open("/Users/student/prbproblemsets/pyth3/txt_files/lyric.txt","r")
contents=file.read()
print(contents)
file.close()

#uppercase each line
contents_upper=contents.upper()
fileupper=open("/Users/student/prbproblemsets/pyth3/txt_files/lyricupper.txt","w")
fileupper.write(contents_upper)


