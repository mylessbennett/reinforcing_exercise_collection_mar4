digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']

dict = {}

for digit in range(1, len(digits)+1):
    dict[digit] = {'french': fr[(digit-1)], 'english': en[(digit-1)]}

print(dict)
