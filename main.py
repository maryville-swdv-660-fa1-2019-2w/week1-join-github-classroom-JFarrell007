#######################################################################
#Class: SWDV-660
#Assignment: Week 1 Package Managed Projects
#Name: Jim Farrell
#Description: Create a spinning / to demonstrate halo spinner.
#######################################################################
import time
from colorama import init, Fore, Back
from halo import Halo

def main():
    init() #initialize colorama
    print( Back.BLUE + Fore.RED + " halo spinner example ")
    #create the Halo spinner
    spinner = Halo(text='What is taking so long..', text_color='cyan', color='green')
    #start the spin simulation
    spinner.start()
    #sleep
    time.sleep(5)
    #stop and print the final message
    spinner.stop_and_persist(symbol='✔ '.encode('utf-8'), text='Done!')

main()
