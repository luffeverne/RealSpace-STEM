#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

class SI:
    MainWidget: None
    frame_Mode3D: None
    frame_SAED: None
    frame_Simulation: None
    frame_UserGuide: None
    frame_Contact: None

    dbconn = pymysql.connect(
        host="localhost",
        database="mydb",
        user="root",
        password="123456",
        port=3306,
        charset='utf8'
    )
    # dbconn = pymysql.connect(
    #     host="39.98.146.215",
    #     database="mydb",
    #     user="fei",
    #     password="fei",
    #     port=23306,
    #     charset='utf8'
    # )
    cursor = dbconn.cursor()

    name = "luffe"
