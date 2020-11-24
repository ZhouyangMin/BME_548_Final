# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Reference:
#/***************************************************************************************
#*    Title: <BME590_ML_Final_Project/BME590_Final_Project_keras.ipynb>
#*    Author: <Huisi Cai, Zhen Lin>
#*    Date: <2019>
#*    Code version: <N/A>
#*    Availability: <https://github.com/SylviaCHS/BME590_ML_Final_Project>
#*
#***************************************************************************************/
import xml.etree.ElementTree as ET
import json


def create_json(filename):
    path = 'C:\\Users\\Soya\\Documents\\BME548L\\FinalGithub\\plasmodium-phonecamera\\' + str(filename)
    tree = ET.parse(path)
    root = tree.getroot()
    
    xmin = []
    xmax = []
    ymin = []
    ymax = []
    
    for x1 in root.iter('xmin'):
        xmin1 = int(float(x1.text))
        xmin.append(xmin1)

    for x2 in root.iter('xmax'):
        xmax1 = int(float(x2.text))
        xmax.append(xmax1)

    for y1 in root.iter('ymin'):
        ymin1 = int(float(y1.text))
        ymin.append(ymin1)

    for y2 in root.iter('ymax'):
        ymax1 = int(float(y2.text))
        ymax.append(ymax1)

    loc = {'xmin': xmin,
           'xmax': xmax,
           'ymin': ymin,
           'ymax': ymax
           }
    
    name, _ = str(filename).split('.')
    output_name = str(name) + '.json'
    out_file = open(output_name, "w")
    json.dump(loc, out_file)
    out_file.close()
    
    
for i in range(1182):
    num = str(i+1).zfill(4)
    filename = 'plasmodium-phone-' + str(num) + '.xml'
    create_json(filename)




