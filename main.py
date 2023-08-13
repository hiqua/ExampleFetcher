#!/usr/bin/env python3
import logging
import requests
import argparse

URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def print_examples(resp):
    no_example = True
    for subresp in resp:
        for meaning in subresp['meanings']:
            for definition in meaning['definitions']:
                if 'example' in definition:
                    print(definition['example'])
                    no_example = False
    if no_example:
        logging.warning('Could not find example.')
def main():
    parser = argparse.ArgumentParser(
                    prog='ExampleFetcher',
                    description='Fetch dictionary examples for the given word.',
                    epilog='')
    parser.add_argument('word')
    args = parser.parse_args()
    word = args.word
    response = requests.get(URL + word).json()
    print_examples(response)


if __name__ == '__main__':
    main()



