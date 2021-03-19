# Wingspan Translator
This small Python script will try to generate translations of all the birds in the [Wingspan game](https://stonemaiergames.com/games/wingspan/) into any language of choice, by browsing Wikipedia articles in different languages. It uses the [Wikipedia-API](https://pypi.org/project/Wikipedia-API/) Python package to accomplish this.

As long as the bird page exists in your language, this script should be able to handle the translation, as well as to get the scientific name for most of the birds.

The result is a csv list with the english, scientific and translated name of each bird. Here is a (slightly polished) list of [Swedish translations](./swedish_translations.pdf) converted into pdf format.


## Requirements

* Python 3

## Setup
(Optional) Create a virtual Python environment and activate it:

    python3 -m venv tutorial-env

    source bin/activate

Install dependencies:

    pip install -r requirements.txt

## Usage
When your virtual environment is activated (see above), simply run:

    python wingspan.py

The translations will be written to the file `translations.csv`.

To change the translation language, simply change the `language_code` varaible to any valid 2-letter language code.

## Contribution
You are very welcome to contribute to this repository by simply opening a pull request!

If you add any new Python dependencies, remember to run:

    pip freeze > requirements.txt

### Future improvements

* Take language code as an argument.