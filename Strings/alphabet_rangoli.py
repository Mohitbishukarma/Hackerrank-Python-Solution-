def print_rangoli(size):
    if size ==1:
        print("a")
    else:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        side_alphabet = ""
        for i in range(size):

            side_alphabet_to_use = ""
            for c in side_alphabet:
                if c == side_alphabet[-1]:
                    side_alphabet_to_use += c
                else:
                    side_alphabet_to_use += c+"-"
            print((side_alphabet_to_use+"-"+alphabets[size-(i+1)]+"-"+side_alphabet_to_use[::-1]).center((size*2-1)+(size*2-2),'-'))
            side_alphabet = side_alphabet+alphabets[size-(i+1)]  
        side_alphabet = side_alphabet.replace(side_alphabet[-1],'')   
        for i in range(size-1):
            side_alphabet = side_alphabet.replace(side_alphabet[-1],'')
            side_alphabet_to_use = ""
            for c in side_alphabet:
                if c == side_alphabet[-1]:
                    side_alphabet_to_use += c
                else:
                    side_alphabet_to_use += c+"-"
            print((side_alphabet_to_use+"-"+alphabets[size-(size-(i+1))]+"-"+side_alphabet_to_use[::-1]).center((size*2-1)+(size*2-2),'-'))