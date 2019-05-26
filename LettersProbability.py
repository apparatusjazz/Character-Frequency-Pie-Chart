import operator #for sorting

def letterCount(file):
    '''Counts frequency of all letters and returns a dictionary'''
    text_file = open(file, "r")
    data = text_file.readlines()
    text_file.close()

    letter_freq = {'Symbols': 0}

    for line in data:
        for char in line:
            if char in letter_freq and (char.isalnum() or char.isspace()):
                letter_freq[char] += 1
            elif not char.isalnum() and not char.isspace():
                letter_freq['Symbols'] += 1
            else:
                letter_freq[char] = 1
    
    if letter_freq.get('Symbols') == 0:
        letter_freq.pop('Symbols', None)
    return letter_freq
            

def letterAngles(letters):
    '''Converts probabilities to angles and returns a sorted tuple of the letters and angles'''
    number_letters = sum(letters.values())
    letter_prob = {}
    for i in letters:
        letter_prob[i] = (letters.get(i) / number_letters) * 360

    angles = sorted(letter_prob.items(), key = operator.itemgetter(1), reverse = True)

    return angles


def nAngles(n, angles):
    '''Returns the first n angles as a dictionary, handles different cases for n'''
    n_angles = {}
    sum1 = 0
    if len(angles) < n:
        n = len(angles)
    if n > 54: 
        n = 54
    for i in range(0, n):
        if angles[i][0] == '\n':
            n_angles['\\n'] = angles[i][1]
        elif angles[i][0] == '\t':
            n_angles['\\t'] = angles[i][1]
        elif angles[i][0] == ' ':
            n_angles['Space'] = angles[i][1]
        else:
            n_angles[(angles[i][0])] = angles[i][1]

        sum1 += angles[i][1]
    n_angles['All other'] = 360 - sum1
    return n_angles

