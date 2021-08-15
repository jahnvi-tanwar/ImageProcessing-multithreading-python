import os

outputFolder = 'Compare'

try:
    os.mkdir(outputFolder)
except:
    pass

report_multithreading = 'report_multithreading'
report_no_multithreading = 'report_no_multithreading'


os.system('python gray_scale_multithreading.py > compare/{}'.format(report_multithreading))
os.system('python gray_scale.py > compare/{}'.format(report_no_multithreading))