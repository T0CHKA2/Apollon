- [En README](#Eng) </br>
- [Ru README](#Ru) </br>
- [Changelog](#changelog) </br>

# Eng
___
<h1 align="center"> Apollon - Helper of CNC operators </h1> </br>

![APOLLON WATERMARK](https://i.ibb.co/5Bt1rSY/Apollon.png)
![GitHub](https://img.shields.io/github/license/T0CHKA2/Apollon?style=for-the-badge)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/T0CHKA2/Apollon/dev?style=for-the-badge)
___
## Intro

So, a few years later, I decided to continue my development on the voice assistant, changed the programming language, and managed to get a job (i.e., get at least some money to buy components and start a project), as well as enter practice from a technical school. And since I went to work as a CNC machine operator, I found that it is possible to speed up and simplify the work process by creating a special voice assistant. I decided to take my last [project](https://github.com/T0CHKA2/I.S.A.C) for the design so far, also adding a few cool things that are not in the usual voice assistant, and a little sorting out those necessary things that are needed to create this project. I also decided that using phrases from Tom Clancy's The Division is not convenient due to the fact that there are no necessary replicas for some functions, for which it will be replaced with a regular robotic voice. </br>

I decided to name the project simply and concisely, A.P.O.-llon </br>
APO stands for ***Autonomous Helper of Operators*** of CNC machines </br>
In the future, all commands will be activated with his name </br>

The demo version can be viewed [here](https://wokwi.com/projects/354477939926235137) </br>

![Demo Version](https://i.ibb.co/WPyDdTW/442.png)
___
## Сapability

⚒️ - Accordingly, during that time of work, I specifically saw what could be added to this assistant, and at least if you are a multi-machine employee, that is, you work on several machines at the same time, I think you will definitely be helped by ***Alarm clock*** which will be at least 5, so that you can set an alarm clock  on all the machines are working.

❌ - You are measuring a part, and your technological map is located at the other end of the site and you are too lazy to follow it? The same ***quick recording*** will help you with this. Just say "Apollo Recording" and say what you will need. For example, "Apollo Records the linear size of the tail seventy-five millimeters plus minus one tenth" and at the right moment you can ask him what the linear size of the tail is. Or what you wrote down

✅ - There are also thoughts to apply a 4-point hazard system that will work from various sensors. For example, you entered an area where there is a lot of air pollution and it is better for you to use a respirator to comply with Safety Regulations? Get a warning from Apollo that will set 1 danger point and notify you of contamination and remind you of the respirator. Have you entered an area where the air temperature is very high? Get another 1 hazard score and notification of dehydration in hot conditions and the possibility of getting burned or sunstroke in summer. Depending on how many danger points there will be, the color on the case will change from Yellow (Minor danger) to Red (Significant danger).

❌ - You were given a new drawing, you put the first blank and received from it the first part that you need to measure, and after measuring you found that this is a fixable defect, but how do you calculate how much you need to rotate the part? Or do you put a new rig on the machine, but you don't know how much you need to turn it? *** An advanced calculator*** that works, not surprisingly, by voice will help you. Just tell the necessary information to Apollo and you will get the result. Example: "Apollo tangent of angle 320" to which he will give you an answer.

⚒️ - The last employee was fired, and there is no space on your device? It doesn't matter, the case has a window for SD cards to increase the amount of memory, which is mainly used for this.

PS You can always ask Apollo about some information, for example, if you set the alarm after 40 minutes, you can ask how much is left until the end of the alarm.

___
## Components

For assembling requiring: </br>
[ESP32]() </br>
[RTC DS1307]() </br>
[DHT22]() </br>
[Two buttons]() </br>
[Neopixel Ring LEDs]() </br>
[SD module]() </br>
[Speakers (2 at least)]() </br>
[Microphone]()  </br>

And 3D Printer, [link to the data for printer are here]()

___
## Assembling

In state of assembling
___
## Efficiency

In state of testing
___
## Further project support

Still unknown

___
</br>

# Ru
___
<h1 align="center"> АПОллон - Помощник операторов станков с ПУ </h1> </br>

![APOLLON WATERMARK](https://i.ibb.co/5Bt1rSY/Apollon.png)
![GitHub](https://img.shields.io/github/license/T0CHKA2/Apollon?style=for-the-badge)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/T0CHKA2/Apollon/dev?style=for-the-badge)
___
## Оглавления

- [Вступление](#Вступление)
- [Возможности](#Возможности)
- [Компоненты](#Компоненты)
- [Программирование](#программирование)
- [Сборка](#Сборка)
- [Работоспособность](#Работоспособность)
- [Дальнейшая поддержка проекта](#Дальнейшая-поддержка-проекта)
___
## Вступление

Итак, спустя несколько лет я решил продолжить свою разработку над голосовым помощником, сменил язык программирования, и успел устроиться на работу (т.е. получить какие то хоть деньги для покупки компонентов и начала проекта), так же как и выйти на практику от техникума. А поскольку я вышел на работу Оператором станков с ПУ, я обнаружил что можно ускорить и упростить процесс работы с помощью создания специального голосового помощника. Решил за дизайн взять пока что свой прошлый [проект](https://github.com/T0CHKA2/I.S.A.C), так же добавив несколько прикольных штук которых нет в обычном голосовом помощнике, и немного перебрав те необходимые вещи которые нужны для создания этого проекта. Так же я решил что использовать фразы из Tom Clancy's The Division не удобно в связи того что нет необходимых реплик на некоторые функции, за что это будет заменено на обычный роботический голос. </br>

Проект решил назвать просто и лаконично, А.П.О.-ллон </br>
АПО расшифровывается как ***Автономный Помощник Оператора*** станков с Программным Управлением </br>
В дальнейшем все команды будут активироваться с его имени. </br>

Так же было принято решение создать отдельную ветку для тех кто просто хочет косплеить. [Ссылка здесь на эту ветку здесь](https://github.com/T0CHKA2/Apollon/tree/cosplay)

Демо-версию можно посмотреть [здесь](https://wokwi.com/projects/354477939926235137) </br>

![Demo Version](https://i.ibb.co/WPyDdTW/442.png)
___
## Возможности

⚒️ - Соответственно, за то время работы я конкретно увидел что можно было бы добавить в этого помощника, и как минимум если вы многостаночный сотрудник, то есть, работаете на нескольких станках одновременно, думаю вам обязательно поможет ***Будильник*** которых будет работать как максимум 5, дабы вы могли поставить время на все станки которые у вас работают.

❌ - Вы измеряете деталь, а ваша технологическая карта находится в другом краю участка и вам лень за ним идти? Вам в этом поможет така же ***быстрая запись***. Просто произнесите "АПО Запись" и произнесите то что вам будет необходимо. Например "Аполлон Запись Линейный размер хвоста семьдесят-пять миллиметров плюс минус одна десятая" и в нужный момент вы можете его спросить, какой линейный размер хвоста. Или того что вы записали

✅ - Так же имеются мысли применить 4-х бальную систему опасности которая будет работать от различных датчиков. Например вы вошли на участок на котором большое загрязнение воздуха и вам лучше для соблюдения Техники Безопасности использовать респиратор? Получите предупреждение от Аполлона которое выставит 1 балл опасности и уведомит вас о загрязнении и напомнит об респираторе. Вошли в зону где очень высокая температура воздуха? Получите ещё 1 балл опасности и уведомление о обезвоживании в жарких условиях и возможности получить ожог или солнечный удар летом. В зависимости от того сколько будет баллов опасности, цвет на корпусе будет меняться от Жёлтого (Незначительная опасность) до Красного (Значимая опасность).

❌ - Вам выдали новый чертёж, вы поставили первую заготовку и получили из неё первую деталь которую вам необходимо замерить, и замерив вы обнаружили что это исправимый брак, но как вам посчитать, на сколько вам нужно повернуть деталь? Или вы ставите новую оснаску на станок, но вы не знаете на сколько вам нужно повернуть её? Вам поможет ***продвинутый калькулятор*** который работает, не удивительно, голосом. Просто скажите необходимую информацию Аполлону и вы получите результат. Пример: "Аполлон Тангенс угла 320" на что он вам даст ответ.

⚒️ - Прошлого сотрудника уволили, и на вашем устройстве нет места? Не беда, в корпусе имеется окно для SD карт для повышения объёма памяти, которое в основном для этого и используется.

П.С. Всегда можно переспросить АПО про некоторую информацию, например если вы поставили будильник через 40 минут, вы можете спросить сколько осталось до конца будильника.
___
## Компоненты

Для сборки необходимо: </br>
[ESP32](https://www.ozon.ru/product/modul-esp32-devkit-v1-wroom-32-bluetooth-i-wi-fi-380180322/?asb=rOfyN3pWgTReXEpKFnMtyGkLqxxX8g9OuVy82rRl4oA%253D&asb2=UO7eahulf8SJAf1mRKEHXEazoJlrXSzJJ8S3dO21ZPI2HYp2m2fx5SG5XBgBiuvs&avtc=1&avte=2&avts=1674982710&keywords=ESP32&sh=jiTmkT38Ng) </br>
[DHT22](https://www.ozon.ru/product/datchik-temperatury-i-vlazhnosti-tsifrovoy-dht22-am2302-336621891/?asb=bXy5ib%252FbzQIpiKID9KgLxW38pNFD61PmuLLmlS01S18%253D&asb2=_q_ao_cZ_nQiLhORWsSoIyMu7iNJjnmxVbM78L9Rdbbd865N-1UhdKBcUegMiBpk&avtc=1&avte=2&avts=1674982742&keywords=DHT22&sh=jiTmkc8ztQ) </br>
[RTC DS1307](https://www.ozon.ru/product/rtc-modul-chasov-realnogo-vremeni-ds1307-614402200/?advert=zXt_JcSb_x2cqNiTEdigoDI1TSpSnantFgHHGmvnTTWSpa13X3y-5tJp4iWIepgxAwDgsUOmlAdXqNuiWmsaowsDG6OoxtQFVrWkkU_-9rVGCLFvZWEI9hs70nHCaz9lDcFDOnMMjipiSwplCOhKLDZVZLbgbMFcF36e2tgwdCWjl84PzTBWvtRlsQhyU7XzJ4iB3sGI2jcdO4pi2wDmNeKbVzxXqIbL6ZlzpjGb3lTJmtQlX-3OLw29pw6w5gGmp17hpOmFMrQbi4MqsewMvFV5g1TVavisavRMQafDNUoKiITbQi3GP1tU-R9tbEjhRaEk2b_uT6XBhyrwOdMGDlsZzCPvN663VKB2uh_hBrjhr1r-3HmwDyuvLy7DqZBdXS4Z8xK1QZDqeq5TK72hOdO55LrO25-5IlZFnM2ScHH87xuNVKcOqUfO8P9XQXuZQuB8Co3MCOt3MFy9YddftC_1gvz7hRvKR4eHgbl2AyKSDk_iK5gikzEd8YocepvZOKAOkPSu5Ny9ItUB18bFdZNUrKzbNWXvtbrHEfhRfJp8mqc5olpo00Vh9gnUZnqh1VDJZvstvPnF_fHbEYFb7S51fJl-EWF6eF57itE0XMuPvc87uLy7JpQ1eI9Bn4L3w_WZ-NNZU2GruNHKBgyvoPycwKvao6iHWNvjvrX0IgyG2Paw1o5a5iraiXqvmnsKpUN-mGOSDZpe_36n5d1e22lK6b0y5g2Lf0BSkqRgoFkPlJJhBK2JcWtwsWjkriJECyuWwWxjUmAyVtucIJxdLllNVtnFB_84alwvCDpUb6pL0TijJeqzLQy8IyMBrjiOg_rblm-U18Zp1xQSwbegsw&avtc=1&avte=2&avts=1674982785&keywords=RTC+ds1307&sh=jiTmkV0TnA) </br>
[Две кнопки]() </br>
[Светодиоды](https://amperkot.ru/products/svetodiodnoe_koltso_cjmcu_16_ws2812_5050_rgb_led/24260776.html) </br>
[SD модуль]() </br>
[Динамик (хотя бы два)]() </br>
[Микрофон]() </br>

И 3D принтер для печати корпуса, [тык сюда для ссылки на данные для 3D принтера]()
___
## Программирование

В процессе работы
___
## Сборка

В процессе изготовления
___
## Работоспособность

В процессе проверки
___
## Дальнейшая поддержка проекта

Скорее всего будет. Но пока проект не завершён ответа точного сказать не могу.

# Changelog
 - [[04.02.2023] all: GitHub page update, code commentary, main merge]()
 - [[04.02.2023] Advanced Events update, 4-point danger status]()
 - [[01.02.2023] Events update]()
 - [[30.01.2023] Events rework, Unit-tests LED and README.md update](https://github.com/T0CHKA2/Apollon/commit/e3c72a21be7cfd7387e9e1370653f3b2235f0e6a)
 - [[28.01.2023] GitHub page upgrade, bug fixes, Eng translation for README.md, Events update](https://github.com/T0CHKA2/Apollon/commit/718430fa31d6bd200d37f67e45772c25dcb3a3dc)
 - [[28.01.2023] Unit-Tests, Cosplay branch, code improvement](https://github.com/T0CHKA2/Apollon/commit/5ad87c2af36c2dac0817a0e9ba654eaed916c6f6)
 - [[27.01.2023] GitHub page upgrade](https://github.com/T0CHKA2/Apollon/commit/5f53b319a82b1f54227076f0d856d56985d973d4)
 - [[24.01.2023] Code upgrade, RTC and Alarms](https://github.com/T0CHKA2/Apollon/commit/14e936d86b7f239b0a8549241f0af31b5aa5e60a)
 - [[23.01.2023] Event Handling](https://github.com/T0CHKA2/Apollon/commit/73517a1ccc67d092cbfc4f26255338cef65d6742)
 - [[21.01.2023] DHT22 and Async](https://github.com/T0CHKA2/Apollon/commit/b9ebb92e417f117cd9647a0a16df47002a8c48b6)
 - [[21.01.2023] NeoPixel LED Ring module support](https://github.com/T0CHKA2/Apollon/commit/e8ef0dabc6a360f021455f1c35787cc60a30ec99)

###### Work in progress...
