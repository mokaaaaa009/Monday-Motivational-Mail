#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
letter=""
with open(r"Day24\Mail Merge Project Start\Input\Letters\starting_letter.txt" ) as file:
    letter=file.read()
with open(r"C:\Users\Owner\DaysCode100\Day24\Mail Merge Project Start\Input\Names\invited_names.txt" ) as namesListFile:
    names=namesListFile.readlines()
for name in names:
   
    strippedName=name.strip()
    nLetter = letter.replace("[name]",strippedName)
    with open(f"C:/Users/Owner/DaysCode100/Day24/Mail Merge Project Start/Output/ReadyToSend/{strippedName}.txt","w") as updatedLetter:
        updatedLetter.write(nLetter)


