import pandas
df = pandas.read_csv(r"Day26\NATO-alphabet-start\nato_phonetic_alphabet.csv")
#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():    
    #Access index and row
    #Access row.student or row.score
 #   pass

# Keyword Method with iterrows()
#TODO 1. Create a dictionary in this format:
natoDict={row.letter:row.code for (index, row) in df.iterrows()}
def insert():
    name = input("Please enter a name: ").upper()
    try:
        result={letter:natoDict[letter] for letter in name}
    except KeyError:
        print("Please enter in letters")
        insert()
    else:
        print(result)


insert()


