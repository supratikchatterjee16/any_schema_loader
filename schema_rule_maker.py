# Syntax
# [[ ]] This will be for headers
# [ ] this will be for mentioning a field. Can be used to work with RegEx
# [?pattern] or [[?pattern]] if this field exists verify pattern and store the following row or column based on it
# [! ] field may or may not exist
# [[! ]] Column name may or may not exist
# [[#type ]] provide a number at # and the datatype for it to be parsed as such
# These can be grouped together
# 'extension' should be provided, when the rule being provided only needs to be loaded with the provided mechanism
# 'type' is mandatory 
# 'name' is mandatory
# 'delimiter' is mandatory it may be single character a string, or a set of characters or none
# reading of format starts after 2 NEWLINE characters

# Some considerations
# It is easy for a person to cause blockages in the system using this, if it isn't provisioned against
# To prevent a DDOS attack, through this, it has to be limited to what it acccepts and what it doesn't

import os
import sys
import json

RULE_FILE = 'rules.json'
ENVIRONMENT = 'LINUX'
LOADING_PROGRAM = 'python3'
HEADER_LINE_LIMIT = 30
ACCEPT_LIMIT = 2000000

ACCEPTED_PARAMETERS = ['##extension', '##type']

def read_rules_file():
	rules = {}
	if os.path.isfile(RULE_FILE):
		with open(RULE_FILE, 'r') as rules_store:
			try:
				rules = json.load(rules_store)
			except ValueError as err:
				print(RULE_FILE, ' is empty')
	return rules

def write_rules_file(rules):
	with open(RULE_FILE, 'w') as rules_store:
		json.dump(rules, rules_store, indent = 4)

def get_rules(content):
	

def read_parsing_data(filename):
	rules = read_rules_file()
	try:
		size = os.path.getsize(filename)
		if size > ACCEPT_LIMIT:
			print('\nFile too big.\nDescriptors are usually never too large.')
			return 1
		rule = get_rules(with open(filename) as f : s = f.read())
	except Exception as e:
		print(e)
	write_rules_file(rules)
	return 0

read_parsing_data('col_major_schema.fd')