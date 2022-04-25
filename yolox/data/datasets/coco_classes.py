#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.
import json
import os

filePath = os.path.dirname(__file__)
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
path = os.path.join(fileNamePath, 'datasets/COCO/annotations/instances_train2017.json')


with open('../datasets\\COCO\\annotations\\instances_train2017.json', 'r', encoding='utf-8') as f:
    dataset = json.load(f)

COCO_CLASSES = []
for i in dataset['categories']:
    COCO_CLASSES.append(i['name'])



