# -*- coding: utf-8 -*-
"""Console script for chibi_biologist."""
import yaml
from chibi.file import Chibi_path
from argparse import ArgumentParser
from chibi.config import basic_config
import sys

parser = ArgumentParser(
    description="descargar datos de mangas y animes",
    fromfile_prefix_chars='@'
)

"""
parser.add_argument(
    "sites", nargs='+', metavar="site",
    help="urls de las series que se quieren descargar" )
"""

parser.add_argument(
    "--log_level", dest="log_level", default="INFO",
    help="nivel de log",
)

parser.add_argument(
    "--search", dest="search",
    help="busca en los aminoacidos una coinicdencia y lo imprime",
)


def load_aminoacids():
    file = Chibi_path( 'chibi_biologist/aminoacids.yml' )
    return file.open().read()


def print_aminoacid( aminoacids ):
    # max_size = max( aminoacids, key=lambda x: len( x.es_name ) )
    max_size = max( len( a.es_name ) for a in aminoacids )
    for aminoacid in aminoacids:
        print( f"{aminoacid.es_name : <{max_size}}  {aminoacid.symbol}" )
        # print( aminoacid.es_name, '\t' * 2, aminoacid.symbol )


def main():
    """Console script for chibi_biologist."""
    args = parser.parse_args()
    basic_config( args.log_level )

    aminoacids = load_aminoacids()
    if args.search:
        search = args.search.lower()
        aminoacids = list( filter(
            lambda x: search in x.es_name or search in x.symbol, aminoacids ) )
    print_aminoacid( aminoacids )

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
