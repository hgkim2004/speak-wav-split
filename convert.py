# -*- coding: utf-8 -*-
"""
    kss 데이터에 대해서
    https://www.kaggle.com/bryanpark/korean-single-speaker-speech-dataset

    transcript.v.1.3.txt 파일을
    alignment.json 형태로 바꿔주는 프로그램
"""
out = open("alignment.json", "wt", encoding="utf-8")
out.write("{\n")

# http://raccoonyy.github.io/working-with-unicode-streams-in-python-korean/
with open("transcript.v.1.3.txt", encoding="utf-8") as f:
    while True:
    #for i in range(1000):
        line = f.readline()
        if len(line) <= 0: break
        strArray = line.split('|')
        #text = '    ".\\datasets\kss/audio\\{}" : "{}",\n'.format(strArray[0].replace('/', '\\'), strArray[1])
        cText = strArray[1].replace(",", "")
        cText = cText.replace('"', '')
        text = '    "./datasets/kss/audio/{}" : "{}",\n'.format(strArray[0], cText)
        #print(text)
        out.write(text)
        #break


out.write("}\n")
out.close()
