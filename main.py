import argparse
import os
import datetime

import Preprocess

def main(args):
    print('Reading parameters...')
    source = args.get('source')
    destiny = args.get('destiny')
    if source and destiny:
        p = Preprocess.Preprocess(source, destiny)
        #I'm calling all the algotims to test
        p.equalizeHistory()
        p.adaptiveThreshold()
        p.claheEqualization()
        p.claheColor()
    else:
        print('Check the parameters....')

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Preprocess utility.....\n")
    defaultSource = os.getcwd()
    defaultDestiny = os.path.join(defaultSource, 'Results {0}'.format(str(datetime.datetime.now().day)))
    parser.add_argument('-source', type=str, help='Source folder', default=defaultSource)
    parser.add_argument('-destiny', type=str, help='Destiny folder', default=defaultDestiny)
    args = vars(parser.parse_args())
    main(args)