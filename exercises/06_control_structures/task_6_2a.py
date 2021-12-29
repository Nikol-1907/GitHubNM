# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Enter IP_address: ')
octet = ip.split(".")
correct_ip = True
if len(octet) != 4:
	correct_ip = False
for octets in octet:
	if not (octets.isdigit() and int(octets) in range(256)):
		correct_ip = False
		break
if not correct_ip:
	print('неправильный ip-адрес')
	
else:
	oct_ip = [int(i) for i in octet]
	if oct_ip[0] in range(1,223):
		print('unicast')
	elif oct_ip[0] in range(224,239):
		print('multicast')
	elif ip == '255.255.255.255':
		print('local broadcast')
	elif ip == '0.0.0.0':
		print('unassigned')
	else:
		print('unused')
 
	
	
