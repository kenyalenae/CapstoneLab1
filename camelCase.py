def camelCase(word):
    output = ''.join(x for x in word.title() if x.isalnum())
    return output[0].lower() + output[1:]

print(camelCase('sAN fraNCISCO'))
