#Данная программа выведет время, которое теряет человек, при выкуренных сигаретах
import math
name = input("Как Вас зовут?")
print("Здравствуйте,",name)
q = int(input('Вы курите? 1 - "да" 2 - "нет"'))
if q <= 1 :
    q2 = int(input('Количество выкуриваемых сигарет в день?'))
    q3 = int(input('Стаж вашего курения:'))
    q5 = q2 * 365 # кол-во сигарет в год
    q6 = q3 * q5 # кол-во сигарет скурено за все время
    q7 = (q6 * 330) # секунд сокращения жизни
    time = q7
    year = (math.floor(time / 31104000))
    month = (math.floor((time - (year * 31104000)) / 2592000))
    day = (math.floor((time - ((month * 2592000) + (year * 31104000))) / 86400))
    hour = (math.floor((time - ((day * 86400) + (month * 2592000) + (year * 31104000))) / 3600))
    minute = (math.floor((time - ((day * 86400) + (month * 2592000) + (year * 31104000) + (hour * 3600))) / 60))
    second = (time - (year * 31104000) - (month * 2592000) - (day * 86400) - (hour * 3600) - (minute * 60))
    print('Американские исследователи подсчитали, что одна выкуренная сигарета\nкрадет у курильщика 5 минут 30 секунд жизнию.\nУважаемый,',name,', ваше курение, заберет от вашей жизни :\n'
          ,year,'год/года/лет',month,'месяц/месяца/месяцев',day,'день/дня/дней',hour,'час/часа/часов',minute,'минуту/минуты/минут',second,'секунду/секунды/секунд')
    x = ('Совет: Бросайте курить!')
elif q >= 2 :
    x = ("Молодец!\nКурить - 'Вредно,опасно,противно'")
print(x)



