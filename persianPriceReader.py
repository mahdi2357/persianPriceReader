persianNumberPronunciation = {
    0: "صفر",
    1: "یک",
    2: "دو",
    3: "سه",
    4: "چهار",
    5: "پنج",
    6: "شش",
    7: "هفت",
    8: "هشت",
    9: "نه",
    10: "ده",
    11: "یازده",
    12: "دوازده",
    13: "سیزده",
    14: "چهارده",
    15: "پانزده",
    16: "شانزده",
    17: "هفده",
    18: "هجده",
    19: "نوزده",
    20: "بیست",
    30: "سی",
    40: "چهل",
    50: "پنجاه",
    60: "شصت",
    70: "هفتاد",
    80: "هششتاد",
    90: "نود",
    100: "صد",
    200: "دویست",
    300: "سیصد",
    500: "پانصد",
    1000: "هزار"
}


def two_digits(prc2):
    if prc2 in persianNumberPronunciation:
        rs = persianNumberPronunciation[prc2]
    else:
        b = int(prc2 / 10) * 10
        r = prc2 % 10
        rs = persianNumberPronunciation[b] + ' و ' + persianNumberPronunciation[r]
    return rs


def three_digits(prc3):
    if str(prc3)[1:3] == "00":
        if prc3 in persianNumberPronunciation:
            return persianNumberPronunciation[prc3]
        else:
            return persianNumberPronunciation[prc3 / 100] + " صد"
    else:
        first_digit = int(prc3 / 100) * 100
        if first_digit in persianNumberPronunciation:
            return persianNumberPronunciation[first_digit] + ' و ' + two_digits(prc3 % 100)
        else:
            return persianNumberPronunciation[first_digit / 100] + 'صد و ' + two_digits(prc3 % 100)


def six_digits(prc6):
    prc6_length = len(str(prc6))
    first_three_digits = int(prc6 / 1000)
    second_three_digits = prc6 % 1000
    if prc6_length == 6:
        result = three_digits(first_three_digits)
    elif prc6_length == 5:
        result = two_digits(first_three_digits)
    else:
        result = persianNumberPronunciation[first_three_digits]

    if second_three_digits != 0:
        return result + " هزار و " + three_digits(second_three_digits) + " تومان"
    else:
        return result + " هزار تومان "


def nine_digits(prc9):
    prc9_length = len(str(prc9))
    milion9 = int(prc9 / 1000000)
    hezar = prc9 - milion9 * 1000000
    if prc9_length == 9:
        res9 = three_digits(milion9)
    elif prc9_length == 8:
        res9 = two_digits(milion9)
    else:
        res9 = persianNumberPronunciation[milion9]

    return res9 + " میلیون و " + six_digits(hezar)


def twelve_digits(prc12):
    prc12_length = len(str(prc12))
    miliard = int(prc12 / 1000000000)
    milion12 = prc12 - miliard * 1000000000

    if prc12_length == 12:
        res9 = three_digits(miliard)
    elif prc12_length == 11:
        res9 = two_digits(miliard)
    else:
        res9 = persianNumberPronunciation[miliard]

    return res9 + " میلیارد و " + nine_digits(milion12)


price = 1

while price != 0:
    try:
        price = int(input("لطفا مبلغ مورد نظر را وارد کنید : \n"))
    except:
        print("مقدار وارد شده معتبر نمی باشد")
        break

    if not isinstance(price, int):
        break
    else:
        priceLength = len(str(price))
        try:
            if price in persianNumberPronunciation:
                print(persianNumberPronunciation[price] + " تومان ")
            else:
                if price < 100:
                    print(two_digits(price) + " تومان")
                elif price < 1000:
                    print(three_digits(price) + " تومان")
                elif price < 1000000:
                    print(six_digits(price))
                elif price < 1000000000:
                    print(nine_digits(price))
                elif price < 1000000000000:
                    print(twelve_digits(price))
                else:
                    print("برنامه توانایی خواندن عدد مورد نظر را ندارد")
        except:
            print("برنامه توانایی خواندن عدد مورد نظر را ندارد")

# bugs:  2000001
# 456000000
# چهارصد و پنجاه و شش میلیون و صفر هزار تومان 