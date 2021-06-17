def swapFile():
    file1=open("C:/Users/sango/Downloads/whiteHatJr/python/file1Swap.txt","r+")
    text1=file1.read()
    
    file2=open("C:/Users/sango/Downloads/whiteHatJr/python/file2Swap.txt","r+")
    text2=file2.read()
    
    text1=text1.replace(text2,"")
    text2=text2.replace(text1,"")
    
    file1.write(text2)
    file2.write(text1)
    
    
swapFile()    