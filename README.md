
This project is based on the workings of 
* Dr. Nawar Halabi https://github.com/nawarhalabi/Arabic-Phonetiser
* Dr. Motaz Saad https://github.com/motazsaad/ara-pronunciation-tool
* Dr. Taha Zerrouki


## Dictionary Production

```
python corpus2cmudict.py -i nawar_corpus_tashkeel.txt -p nawar_bw_tashkeel
```
# ara-pronunciation-tool

A python tool that converts Arabic diacritised text to a sequence of phonemes and create a pronunciation dictionary. 

This code  is based on https://github.com/nawarhalabi/Arabic-Phonetiser

Modifications mainly make the code in https://github.com/nawarhalabi/Arabic-Phonetiser compatible with python 3, and provide easy to use cmd tool to build the pronunciation dictionary. 

The pronunciation is generated based on Buckwalter transliteration
see https://en.wikipedia.org/wiki/Buckwalter_transliteration and http://www.qamus.org/transliteration.htm for more information 




