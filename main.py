import time
from colorama import init, Fore, Back
from halo import Halo

init()

print( Back.BLUE + Fore.RED + " halo spinner example ")
spinner = Halo(text='What is taking so long..', text_color='cyan', color='green')
spinner.start()
time.sleep(5)
spinner.stop_and_persist(symbol='✔ '.encode('utf-8'), text='Done!')
