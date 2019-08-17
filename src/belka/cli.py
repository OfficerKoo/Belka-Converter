from argparse import ArgumentParser, FileType
from sys import exit
from os import path, mkdir

"""
Default path variables to save rates to
"""
FILENAME = 'belka_rates.json'
DIRNAME = '.belka'
FILEPATH = path.join(path.expanduser('~'), DIRNAME, FILENAME)

def create_parser():
    parser = ArgumentParser()
    pos_group = parser.add_argument_group()
    pos_group.add_argument('amount', 
     type=float, 
     help='Enter the ammount of currency to convert (REQUIRED)'
     )
    pos_group.add_argument('currency', default=['BYN', 'RUB'],
     nargs='*', metavar=('CUR1','CUR2'),
     type=str.upper, action='store',
     help='Enter the currencies to convert like so from CUR1 to CUR2, default is BYN to RUB',
     )
    key_group = parser.add_argument_group()
    key_group.add_argument('-f', '--file', default=FILEPATH,
     help='Select the file to save daily rates default is rates.json')
    key_group.add_argument('-u', '--update', action='store_true',
     help='Update rates from web')
    return parser

def main():
     from belka import rates

     args = create_parser().parse_args()
     #check for variables
     if len(args.currency) > 2:
          print("Too many arguments")
          exit(1)
     """
     this block works like this, it checks for existance of directory in FILEPATH variable, if it's not, than it creates it
     than it check for belka_rates.json(default) if it's not exist, it creates it
     TODO: Make it check for file date, if it older that a day, force update
     """
     if not path.exists(path.dirname(FILEPATH)):
          mkdir(path.dirname(FILEPATH))
     if args.update == False:
          if not path.isfile(args.file):
               currates = rates.get_rates()
               rates.save_rates(args.file, currates)
          else:
               currates = rates.load_rates(args.file)
     else:
          currates = rates.get_rates()
          rates.save_rates(args.file, currates)
     curs = [obj for obj in currates if obj['Cur_Abbreviation'] in args.currency]
     if args.currency[0] == 'BYN':
          result = round(args.amount / curs[0]['Cur_OfficialRate'] * curs[0]['Cur_Scale'], ndigits=2)
     elif 'BYN' not in args.currency:
          print(f"Sorry, this is Belka Converter for belarusian rubles")
          exit(1)
     else:
          result = round(curs[0]['Cur_OfficialRate'] * args.amount / curs[0]['Cur_Scale'], ndigits=2)

     print(f"For {args.amount} of {args.currency[0]} you get {result} of {args.currency[1]}")
     exit(0)