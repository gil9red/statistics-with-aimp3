statistics-with-aimp3
===========

Сбор статистики с плейлиста AIMP3 (#python #python3 #aimp3 #aimppl)


Версия AIMP3: 3.60, build 1470


### Этот скрипт работает вместе с [audio.getPopular downloads.py](https://github.com/gil9red/SimplePyScripts/blob/master/vk_api/audio.getPopular%20downloads.py). ###

[audio.getPopular downloads.py](https://github.com/gil9red/SimplePyScripts/blob/master/vk_api/audio.getPopular%20downloads.py) скачивает музыку по жанрам в
отдельные папки -- для каждого жанра своя. После эти папки добавляются в один плейлист AIMP3. Скрипт парсит файл плейлиста aimppl и выясняет процент отключенных
песен и их жанр (смотрит в папку).


### Лог работы: ###

```
C:\Python34\pythonw.exe C:/Users/ipetrash/Desktop/PyScripts/statistics-with-aimp3/main.py
Всего: 633, отключено: 221 (34%)

Отключенные песни:
  Жанры:
    rock: 79 (50.64%)
    dubstep: 79 (48.17%)
    alternative: 40 (27.97%)
    metal: 23 (13.53%)

  Исполнители (топ 5):
    Король И Шут (Киш): 5 (83.33%)
    Король И Шут: 5 (83.33%)
    Океан Ельзи: 5 (100.00%)
    Linkin Park: 5 (41.67%)
    Scorpions: 4 (100.00%)

Черный список (221):
1. 30 Seconds To Mars - City of the angels.mp3: D:\Users\Music\Popular vk\alternative\30 Seconds To Mars - City of the angels.mp3
2. 501 - Kill your boss (barely alive remix).mp3: D:\Users\Music\Popular vk\dubstep\501 - Kill your boss (barely alive remix).mp3
3. A$Ap Rocky & Skrillex Feat. Birdy Nam Nam - Wild for the night.mp3: D:\Users\Music\Popular vk\dubstep\A$Ap Rocky & Skrillex Feat. Birdy Nam Nam - Wild for the night.mp3
...
221. Фиксики - Помогатор (house trap remix).mp3: D:\Users\Music\Popular vk\dubstep\Фиксики - Помогатор (house trap remix).mp3

Process finished with exit code 0

```
