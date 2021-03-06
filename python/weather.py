#!coding:utf-8
import serial
import time
import requests

def sunny():
    res = [
        1, 1, 0, 1, 1, 0, 0, 1,
        0, 1, 1, 1, 1, 0, 1, 1,
        0, 0, 1, 1, 1, 1, 1, 0,
        0, 0, 0, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 0, 1, 1, 0, 1, 1,
        1, 0, 0, 1, 1, 0, 0, 1,
    ]
    return res

def rain():
    res = [
        0, 0, 0, 1, 1, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 0, 1, 1, 0, 1, 0,
        1, 0, 0, 1, 1, 0, 0, 1,
        1, 0, 0, 1, 1, 0, 0, 1,
        0, 0, 0, 1, 1, 0, 0, 0,
        0, 0, 0, 1, 1, 0, 0, 0,
        0, 0, 0, 1, 1, 0, 0, 0,
    ]

def snow():
    res = [
        0, 0, 0, 1, 1, 0, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        1, 0, 0, 1, 1, 0, 0, 1,
        0, 1, 0, 1, 1, 0, 1, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 0, 0, 1, 0, 0,
        0, 0, 1, 1, 1, 1, 0, 0,
    ]

def crowd():
    res = [
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 1, 1, 1, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 1, 1, 1, 1, 0, 0,
        0, 0, 1, 0, 1, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
    ]
