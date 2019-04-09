from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser()
    pos_group = parser.add_argument_group()
    pos_group.add_argument('amount', type=float, help='Enter the ammount of currency to convert')
    pos_group.add_argument('currency',
     nargs=2, metavar=('CUR1','CUR2'), 
     help='Enter the currencies to convert like so from CUR1 to CUR2',
     )
    return parser