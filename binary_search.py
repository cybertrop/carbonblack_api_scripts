# This is a standard CB API Script used to query the CB API.
# Specifically this script is to query the API for a given binary(s).
# The object 'Original Document' provides the most relevant data. 
# Feel free to play around! 

# Please remember to have saved your CB API key accordingly

# binary_search.py will be invoked by query_cb_api_for_md5_list.sh
# E.G. ./query_cb_api_for_md5_list.sh <list_of_hashes.txt> 
# For individual binary queries use "python binary_search.py --query <hash>"



import sys
from cbapi.response.models import Binary
from cbapi.example_helpers import build_cli_parser, get_cb_response_object


def main():
    parser = build_cli_parser()
    parser.add_argument("--query", help="binary query", default='')
    args = parser.parse_args()

    cb = get_cb_response_object(args)
    binary_query = cb.select(Binary).where(args.query)

    # for each result
    for binary in binary_query:
        print(binary.md5sum)
        print("-" * 80)
        print("%-20s : %s" % ('Observed Filenames', binary.observed_filenames))
        print("%-20s : %s" % ('Original Document', binary.original_document))


        for fn in binary.observed_filenames:
            print("%-20s : %s" % ('On-Disk Filename', fn.split('\\')[-1]))

        print('\n')

if __name__ == "__main__":
    sys.exit(main())
