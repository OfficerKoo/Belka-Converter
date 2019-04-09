from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser()
    pos_group = parser.add_argument_group()
    pos_group.add_argument('amount', 
     type=float, 
     help='Enter the ammount of currency to convert'
     )
    pos_group.add_argument('currency', default=['BYN', 'RUB'],
     nargs=2, metavar=('CUR1','CUR2'), 
     help='Enter the currencies to convert like so from CUR1 to CUR2, default is BYN to RUB',
     )
    return parser

def main():
     from BelkaConverter import rates

     args = create_parser().parse_args()
     rates = rates.get_rates()
     curs = []
     for obj in rates:
          if obj['Cur_Abbreviation'] in args.currency:
               curs.append(obj)
     if args.currency[0] == 'BYN':
          result = args.amount / curs[0]['Cur_OfficialRate'] * curs[0]['Cur_Scale']
     else:
          result = curs[0]['Cur_OfficialRate'] * args.amount / curs[0]['Cur_Scale']

     print(f"For {args.amount} of {args.currency[0]} you get {result} of {args.currency[1]}")