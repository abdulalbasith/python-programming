#read a file
text_file = open ('lines.txt', 'r')

lines = text_file.read()
text_file.close()

print (lines)

#write to a file

text_file = open ('lines.txt', 'a')
text_file.write("\nHere is a third line")
text_file.close()