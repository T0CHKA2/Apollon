- [En README](#Eng) </br>
- [Ru README](#Ru) </br>

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

Соответственно, за то время работы я конкретно увидел что можно было бы добавить в этого помощника, и как минимум если вы многостаночный сотрудник, то есть, работаете на нескольких станках одновременно, думаю вам обязательно поможет ***Будильник*** которых будет работать как максимум 5, дабы вы могли поставить время на все станки которые у вас работают.

Вы измеряете деталь, а ваша технологическая карта находится в другом краю участка и вам лень за ним идти? Вам в этом поможет така же ***быстрая запись***. Просто произнесите "АПО Запись" и произнесите то что вам будет необходимо. Например "Аполлон Запись Линейный размер хвоста семьдесят-пять миллиметров плюс минус одна десятая" и в нужный момент вы можете его спросить, какой линейный размер хвоста. Или того что вы записали

Так же имеются мысли применить 4-х бальную систему опасности которая будет работать от различных датчиков. Например вы вошли на участок на котором большое загрязнение воздуха и вам лучше для соблюдения Техники Безопасности использовать респиратор? Получите предупреждение от Аполлона которое выставит 1 балл опасности и уведомит вас о загрязнении и напомнит об респираторе. Вошли в зону где очень высокая температура воздуха? Получите ещё 1 балл опасности и уведомление о обезвоживании в жарких условиях и возможности получить ожог или солнечный удар летом. В зависимости от того сколько будет баллов опасности, цвет на корпусе будет меняться от Жёлтого (Незначительная опасность) до Красного (Значимая опасность).

Вам выдали новый чертёж, вы поставили первую заготовку и получили из неё первую деталь которую вам необходимо замерить, и замерив вы обнаружили что это исправимый брак, но как вам посчитать, на сколько вам нужно повернуть деталь? Или вы ставите новую оснаску на станок, но вы не знаете на сколько вам нужно повернуть её? Вам поможет ***продвинутый калькулятор*** который работает, не удивительно, голосом. Просто скажите необходимую информацию Аполлону и вы получите результат. Пример: "Аполлон Тангенс угла 320" на что он вам даст ответ.

Прошлого сотрудника уволили, и на вашем устройстве нет места? Не беда, в корпусе имеется окно для SD карт для повышения объёма памяти, которое в основном для этого и используется.

П.С. Всегда можно переспросить АПО про некоторую информацию, например если вы поставили будильник через 40 минут, вы можете спросить сколько осталось до конца будильника.
___
## Компоненты

Для сборки необходимо: </br>
[ESP32]() </br>
[DHT22]() </br>
[RTC DS1307]() </br>
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

Пока неизвестно


###### Work in progress...
