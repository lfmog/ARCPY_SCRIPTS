#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy,os,sys, string,re, math
import shutil
from arcpy import env
# RootDir1 = r'D:\CALIBRADAS\CALIBRADA_0'
# TargetFolder = r'D:\CALIBRADAS\CALIBRADA_ENTREGAS'
RootDir1 = r'D:\CALIBRADAS\CALIBRADA_ENTREGAS'
TargetFolder = r'D:\CALIBRADAS\CALIBRADA_0'
for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
    for name in files:
        if name.endswith('.shp') or name.endswith('.cpg') or name.endswith('.cpg') or name.endswith('.dbf') or name.endswith('.prj') or name.endswith('.shx') or name.endswith('.sbx'):
            print "Found"
            SourceFolder = os.path.join(root,name)
            shutil.copy2(SourceFolder, TargetFolder)