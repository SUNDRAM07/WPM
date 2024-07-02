import curses
import random
import time
from curses import wrapper


def display_text(TARGET,stdscr,current_text,wpm):
    stdscr.addstr(TARGET)
    stdscr.addstr(1,0, f"WPM: {wpm}")
    for i,char in enumerate(current_text):
        if char==TARGET[i]:
            stdscr.addstr(0 , i , char,curses.color_pair(2))       
        else:
            stdscr.addstr(0,i, char,curses.color_pair(3))
    stdscr.refresh()
def target_text():
    global y
    with open("wordperminute.txt","r") as f:
        read=f.read()
        x=read.split("|")
        y=random.choice(x)

def init_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("---------------------------------------")
    stdscr.addstr("WELCOME TO THE WORD PER MINUTE GAME..")
    stdscr.addstr("----------------------------------------")
    stdscr.addstr("\nPress enter to continue..")
    stdscr.refresh()
    stdscr.getkey()
    target_text()
    wpm_text(stdscr,y)
    while True:
        stdscr.addstr(2,0,"You completed the quiz ..press esc to quit to play again press any key other than esc.. ")
        key=stdscr.getkey()
        if ord(key)==27:
            quit()
        else:
            init_screen(stdscr)

def wpm_text(stdscr,y):
    wpm=0
    TARGET=y
    current_text=[]
    start_Time=time.time()
    stdscr.nodelay(True)
    while True:
        time_elapsed= max(time.time()-start_Time,1)
        wpm=(len(current_text)/(time_elapsed/60)/5)
        stdscr.clear()
        display_text(TARGET,stdscr,current_text,wpm)
        try:
            key=stdscr.getkey()
        except:
            continue
        if "".join(current_text) ==TARGET:
            stdscr.nodelay(False)
            break
        
        if ord(key)==27:
            quit()
        if key in ('KEY_BACKSPACE','\b','\x7f' ):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text)<len(TARGET):
            current_text.append(key)
        
        
        


def main(stdscr):
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLACK )
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_RED,curses.COLOR_BLACK)
    init_screen(stdscr)
    

play_or_not= input("Would you like to play the typing test game?(Y or N)").lower()
if play_or_not=="y":
    wrapper(main)
    
elif play_or_not=="n":
    quit()
else:
    print("input a valid input....")
        