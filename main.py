#!/usr/bin/env python3

from scripts.populatemarkdown import ReactPopulateMarkdown
from scripts.populateconfluence import ReactPopulateConfluence
from scripts.thehive_templates import RPTheHive
from scripts.reactutils import REACTutils
from scripts.generate_mkdocs_config import GenerateMkdocs
from scripts.react2stix import GenerateSTIX
from scripts.react_navigator import GenerateNavigator
from scripts.update_attack_mapping import UpdateAttackMapping

# For confluence
from requests.auth import HTTPBasicAuth

# Others
import getpass
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="""Main function of ATC RE&CT.

    You can not only choose to export analytics but also to use different
    modules.
""")

    # Mutually exclusive group for chosing the output of the script
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-ALL', '--all', action='store_true',
                        help='Build all the analytics')
    group.add_argument('-M', '--markdown', action='store_true',
                       help='Export analytics to Markdown repository')
    group.add_argument('-C', '--confluence', action='store_true',
                       help='Export analytics to Confluence')
    group.add_argument('-T', '--thehive', action='store_true',
                       help='Generate TheHive Case templates')
    group.add_argument('-MK', '--mkdocs', action='store_true',
                       help='Generate mkdofc navigation file')
    group.add_argument('-STIX', '--stix', action='store_true',
                       help='Generate STIX objects')
    group.add_argument('-NAV', '--navigator', action='store_true',
                       help='Generate RE&CT Navigator profile')

    # Mutually exclusive group for chosing type of data
    group2 = parser.add_mutually_exclusive_group(required=False)

    group2.add_argument('-A', '--auto', action='store_true',
                        help='Build full repository')
    group2.add_argument('-RA', '--responseactions', action='store_true',
                        help='Build response action part')
    group2.add_argument('-RP', '--responseplaybook', action='store_true',
                        help='Build response playbook part')
    group2.add_argument('-RS', '--responsestage', action='store_true',
                        help='Build response stage part')

    # Init capabilities
    parser.add_argument('-i', '--init', action='store_true',
                        help="Build initial pages or directories " +
                             "depending on the export type")

    args = parser.parse_args()

    if args.markdown:
        UpdateAttackMapping()
        ReactPopulateMarkdown(auto=args.auto, ra=args.responseactions,
                              rp=args.responseplaybook, rs=args.responsestage,
                              init=args.init)
    
    elif args.confluence:
        print("Provide Confluence credentials\n")

        mail = input("Login: ")
        password = getpass.getpass(prompt='Password: ', stream=None)

        auth = HTTPBasicAuth(mail, password)
        UpdateAttackMapping()
        ReactPopulateConfluence(auth=auth, auto=args.auto, 
                                ra=args.responseactions, rp=args.responseplaybook,
                                rs=args.responsestage, init=args.init)

    elif args.all:
        UpdateAttackMapping()
        ReactPopulateMarkdown(auto=args.auto, ra=args.responseactions,
                              rp=args.responseplaybook, rs=args.responsestage,
                              init=args.init)
        GenerateMkdocs()
        GenerateSTIX()
        GenerateNavigator()
    elif args.mkdocs:
        GenerateMkdocs()
    elif args.stix:
        GenerateSTIX()
    elif args.navigator:
        GenerateNavigator()
    elif args.thehive:
        UpdateAttackMapping()
        REACTConfig = REACTutils.read_yaml_file("config.yml")
        REACTConfig2 = REACTutils.read_yaml_file("scripts/config.default.yml")
        #print("HINT: Make sure proper directories are " +
        #      "configured in the scripts/config.yml")
        
        if REACTConfig.get(
                'response_playbooks_dir',
                REACTConfig2.get('response_playbooks_dir')) and \
                REACTConfig.get(
                    'response_actions_dir',
                    REACTConfig2.get('response_actions_dir')) and \
                REACTConfig.get(
                    'thehive_templates_dir',
                    REACTConfig2.get('thehive_templates_dir')):
            RPTheHive(
                inputRP=REACTConfig.get(
                    'response_playbooks_dir',
                    REACTConfig2.get('response_playbooks_dir')),
                inputRA=REACTConfig.get(
                    'response_actions_dir',
                    REACTConfig2.get('response_actions_dir')),
                output=REACTConfig.get(
                    'thehive_templates_dir',
                    REACTConfig2.get('thehive_templates_dir'))
            )
            print("[+] TheHive Templates generated!")
        else:
            print("[!] Failed to populateTheHive Templates. Directories were not provided in the config")
