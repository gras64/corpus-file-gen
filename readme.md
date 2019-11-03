# This is a Corpus File Generator

It extract sentence for mycroft-mimic-studio on https://github.com/MycroftAI/mimic-recording-studio.git.
The data is processed by https://github.com/MycroftAI/lingua-franca.git and all numbers are replaced by letters.


## Installation
* `pip install -r requirements.txt`


### Test Files

For now, we have an English corpus, `english_corpus.csv` made available which
can be found in `backend/prompt/`. To use your own corpus follow these steps.

1. Create a csv file in the same format as `english_corpus.csv` using tabs
   (`\t`) as the delimiter.
2. Add your corpus to the `backend/prompt` directory.
3. Change the `CORPUS` environment variable in `docker-compose.yml` to your
   corpus name.

### use the generator

there is a file generator that generates any sentences from wikipedia. just call the command.
* 'python3 corpus_file_gen.py'
to run. you are always asked about the wiki language 'en'.

if you have only a simple text file without line length and tab you can only check the file.
* python3 corpus_file_gen.py --prepare_file 3 --file english_corpus.csv
if you have already started a file, the generator will expand the file 35K.
* python3 corpus_file_gen.py --prepare_file 1 --file english_corpus.csv
or --help for help.

This is a very simple generator.
You should always check the file and delite false records. We are working on a solution to change numbers into words

## operation

this is a bad tool vor get sentence from mycroft translate,mozilla voice and wiki. It make 35k sentence it use mycroft tools to make numbers in sentence.

# Contributions
by gras64
