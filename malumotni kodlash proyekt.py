from work15 import nomlock_dict as nd

"""
tavsif: belgilarni kodlash va shu koddagi belgilarni chiqarish
sana: 16-mart 2021
tuzuvchi: Haydarov Akbar
"""

user_kod = input("ma'lumot kiriting: ")
kod = int(input("kod qanaqa bulsin "
                "1-agar malumot shifrlamoqchi bulsangiz "
                "0-shifrni yechmoqchi bulsangiz"))


def qushib_ber_listni(list):
    """bu funksiya orqali listdagi malumotlarni qushishimiz mumkin"""
    s = " ".join(list)
    return s


def user_tekshiruv(user):
    """bu funksiya orqali matindagi har bir suzni kichik harflarda qilinadi"""
    listalr0 = []
    satrlar = user.split(" ")
    for ji in satrlar:
        if ji.isalpha():
            listalr0.append(ji.lower())
        else:
            listalr0.append(ji)
    return qushib_ber_listni(listalr0)


def nomlock_qiber(numss):
    """bu funksiya orqali harfni belgiga aylantiradi"""
    try:
        return nd.get(numss, numss)
    except:
        print("soryy!")


def nomlockdan_yechber(numss):
    """bu funksiya orqali belgini harf yoki songa utkariladi"""
    try:
        if numss in nd.values():
            for keys, values in nd.items():
                if values == numss:
                    return keys
        else:
            return numss
    except:
        print("Sorry!!!")


def capitalize_func(satr1):
    """bu funksiya orqali satrdagi suzlarni olib bosh harf qilib qaytaradi"""
    ss = satr1.split(" ")
    ss_list = []
    for k in ss:
        if k.isalpha():
            ss_list.append(k.capitalize())
        else:
            ss_list.append(k)
    return qushib_ber_listni(ss_list)


def nomlock_func_yechish(numsu):
    """bu funcksiya kodlashni yechishda har bir belgini tekshiradi"""
    result_satr1 = ""
    for item in numsu:
        result_satrok = (nomlockdan_yechber(item))
        if result_satrok != " ":
            result_satr1 += str(nomlockdan_yechber(item))
        else:
            result_satr1 += " "
    return capitalize_func(result_satr1)


def nomlock_func(nums):
    """bu funksiya kodlashda har bir harfni tekshiradi"""
    result_satr = ""
    for item in nums:
        if item.isdigit():
            item = int(item)
            result_satr += nomlock_qiber(item)
        else:
            result_satr += nomlock_qiber(item)
    return result_satr


# bu yerda biz kodni birinchi tekshirishimiz kerak
if kod == 1:

    user_kod = user_tekshiruv(user_kod)
    nom = nomlock_func(user_kod)

else:
    nom = nomlock_func_yechish(user_kod)

print(nom)
# tugadi