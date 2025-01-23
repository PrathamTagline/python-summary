string = "hello my name is pratham, i am a student of btech.my hobby is to read books and play genshin impact , hahahahahaha"

vowel_dicttionary = {}

new_string = string.lower()
new_string = new_string.replace(" ", "") 

count_a = new_string.count("a")
count_e = new_string.count("e")
count_i = new_string.count("i")
count_o = new_string.count("o")
count_u = new_string.count("u")

vowel_dicttionary["a"] = count_a
vowel_dicttionary["e"] = count_e
vowel_dicttionary["i"] = count_i
vowel_dicttionary["o"] = count_o
vowel_dicttionary["u"] = count_u

print(vowel_dicttionary)





