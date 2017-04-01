#!/usr/bin/env python

from time import time, sleep, strftime, localtime

prt_0 = ['||||||||', '||    ||', '||    ||', '||    ||', '||||||||']
prt_1 = ['      ||', '      ||', '      ||', '      ||', '      ||']
prt_2 = ['||||||||', '      ||', '||||||||', '||      ', '||||||||']
prt_3 = ['||||||||', '      ||', '||||||||', '      ||', '||||||||']
prt_4 = ['||    ||', '||    ||', '||||||||', '      ||', '      ||']
prt_5 = ['||||||||', '||      ', '||||||||', '      ||', '||||||||']
prt_6 = ['||||||||', '||      ', '||||||||', '||    ||', '||||||||']
prt_7 = ['||||||||', '      ||', '      ||', '      ||', '      ||']
prt_8 = ['||||||||', '||    ||', '||||||||', '||    ||', '||||||||']
prt_9 = ['||||||||', '||    ||', '||||||||', '      ||', '||||||||']
prt_coma = [' ', 'O', ' ', 'O', ' ']
prt_coma1 = [' ', '0', ' ', '0', ' ']

def select_prt(str):
    if str == '0':return prt_0;
    if str == '1':return prt_1;
    if str == '2':return prt_2;
    if str == '3':return prt_3;
    if str == '4':return prt_4;
    if str == '5':return prt_5;
    if str == '6':return prt_6;
    if str == '7':return prt_7;
    if str == '8':return prt_8;
    if str == '9':return prt_9;

def show_time(str_time, blink=1, show_sec=False):
    digit_string=['','','','','']
    digit_bin = [select_prt(c) for c in str_time]
    coma = prt_coma if blink > 0 else prt_coma1

    for i in [0, 1, 2, 3, 4]:
        if show_sec:
            print ' '.join([digit_bin[0][i], digit_bin[1][i], coma[i], \
                            digit_bin[2][i], digit_bin[3][i], coma[i], \
                            digit_bin[4][i], digit_bin[5][i]])
        else:
            print ' '.join([digit_bin[0][i], digit_bin[1][i], coma[i], \
                            digit_bin[2][i], digit_bin[3][i]])
def get_time_formate(hour_sys):
    if hour_sys=='24':
        return "%H%M%S"
    elif hour_sys=='12':
        return "%I%M%S"
    else:
        raise TypeError

def start_clock(hour_sys='24', shiftH=0, shiftM=0, shiftS=0, show_sec=True):
    """
    hour_sys    : Can be either "12" or "24".
    shiftH      : Time adjust of hour.
    shiftM      : Time adjust of minute.
    shiftS      : Time adjust of second.
    show_sec    : Boolean variable to decide either showing second or not.
    """
    # Change hour system between 12/24
    time_formate = get_time_formate(hour_sys)
    # Refresh in second
    refresh_time = 1
    # calculate time shift if system time is not correct
    time_shift = 3600*shiftH + 60*shiftM + 1*shiftS
    # Initial the blink state
    b=1
    while True:
        print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        b *= -1
        time_list = strftime(time_formate, localtime(time()+time_shift))
        show_time(time_list, blink = b, show_sec=show_sec)
        sleep(refresh_time)

if __name__ == '__main__':
    try:
        start_clock(hour_sys="12")
    except:
        print "Exit terminal clock."
