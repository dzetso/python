# Getting names list
names = open("mail_merge/Input/Names/invited_names.txt")
raw_names_list = names.readlines()
names_list = []
for number in range(0, len(raw_names_list)):
    names_list.append(raw_names_list[number].replace("\n", ""))

# Writing letters for every name in the names list
for name in names_list:
    with open("mail_merge/Input/Letters/starting_letter.txt") as example:
        example_text = example.read()
        with open(f"mail_merge/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
            letter.write(example_text.replace("[name]", name.strip()))