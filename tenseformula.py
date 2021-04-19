def cetakverb(subject, verb, object, sentence):
    lv = ["s", "o", "z", "h", "y", "x"]
    vocal = ["a", "i", "u", "e", "o"]
    gender = ["He", "She", "It"]
    n = len(verb)
    if subject in gender:
        if verb[-1:] == "y" and verb[-2 : n - 1] not in vocal:
            verbs = verb[: n - 1]
            verb = verbs + "ies"
        elif verb[-1:] in lv:
            verb = verb + "s"
        else:
            print("Error Verb")
        sentence = f"{subject} {verb} {object}"
        return sentence


def Simple_Tense(tense):
    subject = input("Masukkan Subject : ")
    verb = input("Masukkan verb : ")
    object = input("Masukkan object : ")
    if tense == 1:
        sentence = f"{subject} {verb} {object}"
        cetakverb(subject, verb, object, sentence)
    if tense == 2:
        sentence = f"{subject} {verb}ed {object}"
        cetakverb(subject, verb, object, sentence)
    if tense == 3:
        sentence = f"{subject} will {verb} {object}"
    cetakverb(subject, verb, object, sentence)
    print(sentence)


def Progressive_Tense(tense):
    gender = ["You", "It", "We", "They"]
    subject = input("Masukkan Subject : ")
    verb = input("Masukkan verb : ")
    object = input("Masukkan object : ")
    if tense == 1:
        sentence = f"{subject} {verb}ing {object}"
        cetakverb(subject, verb, object, sentence)
    if tense == 2:
        sentence = f"{subject} was {verb}ing {object}"
        cetakverb(subject, verb, object, sentence)
        if subject in gender:
            sentence = sentence.replace("was", "were")
    if tense == 3:
        sentence = f"{subject} will be {verb}ing {object}"
        cetakverb(subject, verb, object, sentence)
    print(sentence)


def Perfect_Tense(tense):
    gender = ["He", "She", "It"]
    subject = input("Masukkan Subject : ")
    verb = input("Masukkan verb : ")
    object = input("Masukkan object : ")
    if tense == 1:
        sentence = f"{subject} have {verb}ed {object}"
        cetakverb(subject, verb, object, sentence)
        if subject in gender:
            sentence = sentence.replace("have", "has")
    if tense == 2:
        sentence = f"{subject} had {verb}ed {object}"
        cetakverb(subject, verb, object, sentence)
    if tense == 3:
        sentence = f"{subject} will have {verb}ed {object}"
        cetakverb(subject, verb, object, sentence)
    print(sentence)


def Perfect_progressive(tense):

    gender = ["He", "She", "It"]
    subject = input("Masukkan Subject : ")
    verb = input("Masukkan verb : ")
    object = input("Masukkan object : ")
    if tense == 1:
        sentence = f"{subject} have been {verb}ing {object}"
        cetakverb(subject, verb, object, sentence)
        if subject in gender:
            sentence = sentence.replace("have", "has")
    if tense == 2:
        sentence = f"{subject} had been {verb}ing {object}"
        cetakverb(subject, verb, object, sentence)
    if tense == 3:
        sentence = f"{subject} will have been {verb}ing {object}"
        cetakverb(subject, verb, object, sentence)
    print(sentence)


def pastTense():
    print("========= Past Tense =========")
    print("1.Simple Past Tense")
    print("2.Past Progressive Tense")
    print("3.Past Perfect Tense")
    print("4.Past Perfect Progressive")
    pil = input("Pilih : ")
    if pil in ["1", "2", "3", "4"]:
        if pil == "1":
            Simple_Tense(2)
        if pil == "2":
            Progressive_Tense(2)
        if pil == "3":
            Perfect_Tense(2)
        if pil == "4":
            Perfect_progressive(2)


def futureTense():
    print("========= Future Tense =========")
    print("1.Simple Past Tense")
    print("2.Past Progressive Tense")
    print("3.Past Perfect Tense")
    print("4.Past Perfect Progressive")
    pil = input("Pilih : ")
    if pil in ["1", "2", "3", "4"]:
        if pil == "1":
            Simple_Tense(3)
        if pil == "2":
            Progressive_Tense(3)
        if pil == "3":
            Perfect_Tense(3)
        if pil == "4":
            Perfect_progressive(3)


def tampilandepan():
    print("Membuat kalimat bahasa inggris dalam bentuk")
    print("1.Present Tense")
    print("2.Past Tense")
    print("3.Future Tense")
    pil = input("Pilih : ")
    if pil in ["1", "2", "3"]:
        if pil == "1":
            presentTense()
        if pil == "2":
            pastTense()
        if pil == "3":
            futureTense()


def presentTense():
    print("======== Present Tense ========")
    print("1.Simple Present Tense")
    print("2.Present Progressive Tense")
    print("3.Present Perfect Tense")
    print("4.Present Perfect Progressive")
    pil = input("Pilih : ")
    if pil in ["1", "2", "3", "4"]:
        if pil == "1":
            Simple_Tense(1)
        if pil == "2":
            Progressive_Tense(1)
        if pil == "3":
            Perfect_Tense(1)
        if pil == "4":
            Perfect_progressive(1)


tampilandepan()


# Apbila sudah ada kata kerja bantu (Modal) dalam kalimat, maka tidak perlu ditambah S/ES

# Kata benda yang berakhiran F atau EF jika akan di buat jamak (plural), maka diganti dengan V kemudian ditambah dengan ES
