def num_to_words(num):
    units = ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"]
    teens = ["ده", "یازده", "دوازده", "سیزده", "چهارده", "پانزده", "شانزده", "هفده", "هجده", "نوزده"]
    tens = ["", "ده", "بیست", "سی", "چهل", "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"]
    hundreds = ["", "صد", "دویست", "سیصد", "چهارصد", "پانصد", "ششصد", "هفتصد", "هشتصد", "نهصد"]
    thousands = ["", "هزار", "میلیون", "میلیارد"]

    def get_segment_words(n):
        if n == 0:
            return ""
        elif n < 10:
            return units[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + (" و " + units[n % 10] if (n % 10) != 0 else "")
        else:
            return hundreds[n // 100] + (" و " + get_segment_words(n % 100) if (n % 100) != 0 else "")

    def split_by_thousands(n):
        segments = []
        while n > 0:
            segments.append(n % 1000)
            n //= 1000
        return segments

    segments = split_by_thousands(num)
    words = []
    for i, segment in enumerate(segments):
        if segment != 0:
            words.append(get_segment_words(segment) + (" " + thousands[i] if thousands[i] != "" else ""))

    return ' و '.join(reversed(words))


# دریافت مبلغ از کاربر
amount = int(input("مبلغ را وارد کنید: "))
print(num_to_words(amount))
