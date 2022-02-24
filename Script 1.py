
f = open("script1.txt", "w+")
value = input("please enter data: \n")

f.write(f'{value}\r\n')

f.close()

import zipfile

with zipfile.ZipFile('script1.zip', 'w') as script1_zip:
    script1_zip.write('script1.txt','w', compress_type=zipfile.ZIP_DEFLATED)
