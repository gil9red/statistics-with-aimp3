#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from collections import defaultdict
import os
import traceback
import sys


if __name__ == '__main__':
    disabled_audio = defaultdict(int)
    enabled_audio = defaultdict(int)

    disabled_artist = defaultdict(int)
    enabled_artist = defaultdict(int)

    black_list = set()

    total = 0
    genre = None
    aimppl_path = r'C:\Users\ipetrash\AppData\Roaming\AIMP3\PLS\Popular vk.aimppl'

    with open(aimppl_path, encoding='UTF-16LE') as f:
        for line in f.readlines():
            if '#Track' not in line and '#Group' not in line:
                continue

            if '#Group' in line:
                try:
                    group = line.split(':', maxsplit=1)[-1]
                    group = group[:group.rindex('|')]
                    genre = os.path.split(group)[-1]
                    continue

                except Exception:
                    traceback.print_exception(*sys.exc_info())
                    exit()

            path = line.split('|')[1]
            file_name = os.path.split(path)[-1]

            try:
                # Удаление '.mp3' с правого края
                index = file_name.rindex('.mp3')
                file_name = file_name[:index]

                artist, title = file_name.split(' - ', maxsplit=1)

            except ValueError:
                print('Странный текст: ', path, file_name, sep='\n')
                traceback.print_exception(*sys.exc_info())
                continue

            if '#Track:0' in line:
                black_list.add(path)

                disabled_audio[genre] += 1
                disabled_artist[artist] += 1
            else:
                enabled_audio[genre] += 1
                enabled_artist[artist] += 1

            total += 1

    print('Всего: {}, отключено: {} ({}%)'.format(total, sum(disabled_audio.values()),
                                                  int(sum(disabled_audio.values()) / total * 100)))

    print()
    print('Отключенные песни:')
    print('  Жанры:')
    for k, v in sorted(disabled_audio.items(), key=lambda x: x[1], reverse=True):
        count_audio = disabled_audio[k] + enabled_audio[k]

        # Выведим процент отключенных песен по жанрам
        print('    {}: {} ({:.2f}%)'.format(k, v, v / count_audio * 100))

    print()
    top_count = 5
    print('  Исполнители (топ {}):'.format(top_count))
    for k, v in sorted(disabled_artist.items(), key=lambda x: x[1], reverse=True)[:top_count]:
        count_audio = disabled_artist[k] + enabled_artist[k]

        # Выведим процент отключенных песен по исполнителям
        print('    {}: {} ({:.2f}%)'.format(k, v, v / count_audio * 100))

    print()
    print('Черный список ({}):'.format(len(black_list)))
    # Сортируем по имени файла
    for i, audio in enumerate(sorted(black_list, key=lambda x: os.path.split(x)[-1]), 1):
        print('{}. {}: {}'.format(i, os.path.split(audio)[-1], audio))
