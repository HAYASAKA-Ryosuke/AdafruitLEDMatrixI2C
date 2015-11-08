#!coding:utf-8
import serial
import time


def smile():
    res = [
        0, 0, 1, 1, 1, 1, 0, 0,
        0, 1, 0, 0, 0, 0, 1, 0,
        1, 0, 1, 0, 0, 1, 0, 1,
        1, 0, 0, 0, 0, 0, 0, 1,
        1, 0, 1, 0, 0, 1, 0, 1,
        1, 0, 0, 1, 1, 0, 0, 1,
        0, 1, 0, 0, 0, 0, 1, 0,
        0, 0, 1, 1, 1, 1, 0, 0,
    ]
    return res


def clear_window():
    res = [
        0, 0, 1, 1, 1, 1, 0, 0,
        0, 1, 0, 0, 0, 0, 1, 0,
        1, 0, 0, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 0, 0, 1,
        0, 1, 0, 0, 0, 0, 1, 0,
        0, 0, 1, 1, 1, 1, 0, 0,
    ]
    return res


if __name__ == '__main__':
    ser = serial.Serial(
        port='/dev/tty.usbmodem1411',
        baudrate=38400,
    )
    print("smile")
    ser.write(smile())
    ser.close()
    time.sleep(2)
    ser = serial.Serial(
        port='/dev/tty.usbmodem1411',
        baudrate=38400,
    )
    ser.write(clear_window())
    ser.close()
    print("clear")
