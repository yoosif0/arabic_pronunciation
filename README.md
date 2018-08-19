
## Arabic Pronunciation

This project is based on the workings of 
* Dr. Nawar Halabi https://github.com/nawarhalabi/Arabic-Phonetiser
* Dr. Motaz Saad https://github.com/motazsaad/ara-pronunciation-tool
* Dr. Taha Zerrouki

I just refactored the code and added an api wrapper for it to be used easily through installing a package

## Usage
```python
from arabic_pronunciation import phonetise_Arabic

phonetise_Arabic.phonetise_word("بِمُسْتَطِيل")
>>> ['b i0 m u0 s t A T ii0 l']

phonetise_Arabic.phonetise_word("نُتَابِعُهَا")
>>> ['n u0 t aa b i0 E u0 h aa', 'n u0 t aa b i0 E u0 h a']

```


## Tests
* `python -m pytest`

## Static Dictionary Production

* Add your corpus to the root of this project
* `python arabic_pronunciation/corpus2cmudict.py -i {corpus_name}.txt -p {corpus_name}`
* It might take long time to for large corpuses and the command line might not show that the process is going on but it is.




