def solution(s):
    new_str = []
    print(s.split(" "))
    for word in s.split(" "):
        if word != "":
            if word[0].isalpha():
                new_str.append(word.capitalize())
            else:
                new_str.append(word)
        else:
            new_str.append(word)
    return " ".join(new_str)
