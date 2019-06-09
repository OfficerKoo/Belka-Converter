from argparse import ArgumentParser
from sys import exit

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
    return parser

def main():
     from belka import rates

     args = create_parser().parse_args()
     if len(args.currency) > 2:
          print("Too many arguments")
          exit(1)
     rates = rates.get_rates()
     curs = [obj for obj in rates if obj['Cur_Abbreviation'] in args.currency]
     if args.currency[0] == 'BYN':
          result = round(args.amount / curs[0]['Cur_OfficialRate'] * curs[0]['Cur_Scale'], ndigits=2)
     elif 'BYN' not in args.currency:
          print(f"Sorry, this is Belka Converter for belarusian rubles")
          exit(1)
     else:
          result = round(curs[0]['Cur_OfficialRate'] * args.amount / curs[0]['Cur_Scale'], ndigits=2)

     print(f"For {args.amount} of {args.currency[0]} you get {result} of {args.currency[1]}")
     exit(0)