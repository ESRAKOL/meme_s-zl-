None
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROLF": "Şakyla karışık cevap",
            "SHEESH": "Onaylamak",
            "CREEPY":"Korkunç",
            "AGGRO": "Agrasifleşmek/sinirlenmek"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")


if word in meme_dict.keys():
    print(meme_dict[word])
   
else:
    print("bu kelime sözlükte yok")
