age = {'Hans':24, 'Prag':23, 'Bunyod':18}

# Display dictionary
print(age)

# Display age of Hans
print(age["Hans"])

# Age Prag by 7 years
age["Prag"] += 7
print(age['Prag'])

# Delete Bunyod
age.pop('Bunyod')
print(age)