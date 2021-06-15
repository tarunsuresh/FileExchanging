
def CountWordsFromFile():
    with open("File2.txt","r")as b:
        file2=b.read()
    with open("File1.txt","r")as a:
        file1=a.read()

    with open("File2.txt","w")as b:
        b.write(file1)
    with open("File1.txt","w")as a:
        a.write(file2)


CountWordsFromFile()
