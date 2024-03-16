from AvitoParser.config import Token_words


# this function return bool value if Token_word in ads_info:
def check_sector(info_string):
    flag = []
    for word in Token_words:
        if word in info_string:
            flag.append(1)
        else:
            flag.append(0)

    if sum(flag) == 0:
        return True
    else:
        return False

