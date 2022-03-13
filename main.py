import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato = "nato_phonetic_alphabet.csv"
ph_alphabets = pandas.read_csv(nato)

#Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
alphabets_dict = {row.letter: row.code for (index, row) in ph_alphabets.iterrows()}


#Create a list of the phonetic code words from a word that the user inputs.
def genaric_phonetic():
    user = input("Enter a word: ").upper()
    try:
        phonetic = [alphabets_dict[n] for n in user.strip()]
    except KeyError:
        print("Please enter only alphabets")
        genaric_phonetic()
    else:
        print(phonetic)

genaric_phonetic()





