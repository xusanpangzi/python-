#coding=utf-8

from PIL import Image
import glob
import os

def convertjpg(jpgfile, outdir, width=750, height=1330):
    img = Image.open(jpgfile)
    img = img.convert('RGB')

    new_img = img.resize((width, height), Image.BILINEAR)

    new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
for jpgfile in glob.glob(r"C:\Users\qqq\Pictures\peppa pig\*.jfif"):
    convertjpg(jpgfile, r"C:\Users\qqq\PycharmProjects\untitled\python小项目\five")
