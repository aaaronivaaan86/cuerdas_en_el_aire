def files_into_strings(filename):
    strings = []
    # open the file
    with open(f'texts/Echeverria{filename}.txt', mode = "r",  encoding="utf-8") as f:
        # get strings
        strings.append(f.read())
    return '\n'.join(strings)