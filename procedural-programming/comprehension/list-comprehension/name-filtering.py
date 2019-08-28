names = ['Ana', 'Bruno', 'Andressa', 'Luiz', 'Joao', 'Jose', 'Beatriz', 'Lucia', 'Catarina']

names_beginning_with_the_letter_a = [name for name in names if name[0].lower() == 'a']
names_beginning_with_the_letter_b = [name for name in names if name[0].lower() == 'b']
names_beginning_with_the_letter_c = [name for name in names if name[0].lower() == 'c']
names_beginning_with_the_letter_j = [name for name in names if name[0].lower() == 'j']
names_beginning_with_the_letter_l = [name for name in names if name[0].lower() == 'l']
names_ending_in_letter_a = [name for name in names if name[-1].lower() == 'a']
names_ending_in_letter_o = [name for name in names if name[-1].lower() == 'o']
names_ending_in_letter_z = [name for name in names if name[-1].lower() == 'z']
names_ending_in_letter_e = [name for name in names if name[-1].lower() == 'e']

print(names)
print(names_beginning_with_the_letter_a)
print(names_beginning_with_the_letter_b)
print(names_beginning_with_the_letter_c)
print(names_beginning_with_the_letter_j)
print(names_beginning_with_the_letter_l)
print(names_ending_in_letter_a)
print(names_ending_in_letter_o)
print(names_ending_in_letter_z)
print(names_ending_in_letter_e)
