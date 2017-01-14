#!/usr/local/bin/python3
# import modules used here -- sys is a very standard one
import sys, argparse, logging
import json
import urllib.request
def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    
    endpoint = 'http://endpoint'
    print ("Welcome to toccata. Toccata is a cromulent tool which embiggens your productivity.")
    logging.info("You passed in the token")
    logging.debug("Your Token: %s" % args.token)

    data = {}
    data['subject'] = args.subject
    data['body'] = args.body
    data['command'] = args.command
    json_data = json.dumps(data)

    rawbody = {}
    rawbody['data'] = data
    tokens = []
    tokens.append(args.token)
    rawbody['tokens'] = tokens
    json_rawbody = json.dumps(rawbody)
    print(json_rawbody)

    params = json.dumps(rawbody).encode('utf8')
    req = urllib.request.Request(endpoint, data=params, headers={'Content-Type': 'application/json', 'Authorization': 'key='})
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf8'))
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser( 
        description = "./toccata.py --token @inputs.txt --subject TestSubj --body TestBody --command hello",
        epilog = "As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @inputs.txt'.",
        fromfile_prefix_chars = '@' )

    #parser.add_argument(
    #    "argument",
    #    help = "pass ARG to the program",
    #    metavar = "ARG")
    parser.add_argument(
        "-v",
        "--verbose",
        help="increase output verbosity",
        action="store_true")
    parser.add_argument('-t', '--token',
                    default='token',
                    required=False,
                    help='token') 
    parser.add_argument('-s', '--subject',
                    default='Hello',
                    required=False,
                    help='subject')
    parser.add_argument('-b', '--body',
                    default='Hello',
                    required=False,
                    help='body')
    parser.add_argument('-c', '--command',
                    default='testcommand',
                    required=False,
                    help='command')
    args = parser.parse_args()
    
    # Setup logging
    if args.verbose:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
    
    main(args, loglevel)
