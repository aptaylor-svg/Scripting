import zipfile

with zipfile.ZipFile('script1.zip') as script1_zip:
    script1_zip.extractall('Script1')