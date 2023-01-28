- [En README](#Eng) </br>
- [Ru README](#Ru) </br>

# Eng
___
<h1 align="center"> Cosplay version ISAC</h1>

![ApollonCosplay](https://i.ibb.co/WGKRjRT/Apollon-Cosplay.png)
![GitHub](https://img.shields.io/github/license/T0CHKA2/Apollon?style=for-the-badge)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/T0CHKA2/Apollon/cosplay?style=for-the-badge)

While working, I was thinking about the fact that there are people who star in Tom Clancy's "The Division" cosplays. And to ease their burden, I decided that a separate branch could be created for this. The assembly will continue to be carried out on ESP32 and MicroPython with the subsequent possibility of modifying the project.

Demo version is [here](https://wokwi.com/projects/355118489164064769)
___
# Assembling

First you need to connect everything you need together. Since this is the cosplay version, only three wires need to be connected here. These are:</br>
GND - GND</br>
VCC - 3V3</br>
DIN - <Any open pin></br>

The main thing is to remember the pin number where you attached the VIN, in my case it was 27 pin.</br>
Connected? Well done. Now everything is ready to work.
___
# Programming

So we collected everything and attached it. Now it's programming time. Go to main.py from notepad or any other editor that supports files .py </br>
There we will see the following line: </br>
```python
# ...
pin = Pin(<Your Pin here>)
led_pixels(<Your pixels length here>)
# ...
```
</br>
In the fields marked <>, you must fill in the appropriate data. </br>
Download to ESP32 and enable. </br>
Voila, you have a working ISAC block </br>
___

# Ru
___
<h1 align="center">Косплей версия ISAC</h1>

![ApollonCosplay](https://i.ibb.co/WGKRjRT/Apollon-Cosplay.png)
![GitHub](https://img.shields.io/github/license/T0CHKA2/Apollon?style=for-the-badge)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/T0CHKA2/Apollon/cosplay?style=for-the-badge)

Во время работы я подзадумался над тем что есть люди которые делают косплеи по Tom Clancy's The Division. И дабы облегчить им ношу я решил что можно создать отдельную ветку для этого. Сборка всё так же будет вестись на ESP32 и MicroPython с последующей возможностью модифицирования проекта.</br>

Демо версию можно увидеть [здесь](https://wokwi.com/projects/355118489164064769)
___
# Сборка

Для начала необходимо соединить всё необходимое вместе. Поскольку это косплей версия, здесь необходимо соединить только три провода. Это:</br>
GND - GND</br>
VCC - 3V3</br>
DIN - <Любой открытый пин></br>

Главное запомнить номер пина куда вы присоединили VIN, в моём случае это был 27 пин.</br>
Соединили? Молодцы. Теперь всё готово работать.
___
# Программирование

Итак мы собрали всё и присоединили. Теперь время программирования. Заходите в main.py с блокнота или любого другого редактора который поддерживает файлы .py </br>
Там мы увидем следующую строку: </br>
```python
# ...
pin = Pin(<Your Pin here>)
led_pixels(<Your pixels length here>)
# ...
```
</br>
В поля отмеченные <> необходимо заполнить соответствующие данные. </br>
Загрузить на ESP32 и включить. </br>
Вуаля, у вас есть работающий блок ISAC </br>