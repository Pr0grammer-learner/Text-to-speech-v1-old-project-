from tqdm import tqdm
from time import sleep
import win32com.client
speaker = win32com.client.Dispatch('Sapi.SpVoice')

file_path = input( 'Введите путь к файлу: ')

file = open( file_path, 'r' )
print('Текст преобразуется подождите!')
theText = file.read()
for i in tqdm( range( 100 ) ):
    sleep( 0.01 )
speaker.Speak( theText )

file.close()
