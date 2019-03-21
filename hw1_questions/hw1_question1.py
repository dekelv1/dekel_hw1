def trifeca(word):

    ind = 0
    flag = False

    if(len(word) < 6):
        return False

    for letter in word:
        if ind < len(word)-5:
            if word[ind] == word[ind + 1] and word[ind+2]== word[ind+3] and word[ind+4]==word[ind+5]:
                flag = True
            ind += 1

    return flag

if __name__ == "__main__":
    # Question 1
    param1 = "jiggbbccdxe"
    return_value = trifeca(param1)
    print(f"Question 1 solution: {return_value}")



