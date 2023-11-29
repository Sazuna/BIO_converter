#!/bin/python3
import sys
import regex
import tokeniser as tk
import argparse

def main(in_file, out_file, granularity="all"):
	with open(in_file) as f:
		tokens = tk.tokenise(f.read(), granularity)

	print(tokens)
	opened = None
	inside = False
	result = []
	for token in tokens:
		if regex.match(r"</\w+>", token):
			closed = token[2:-1]
			if closed != opened:
				print(f"Les balises <{opened}> et </{closed}> ne correspondent pas.")
				sys.exit(1)
			opened = None
			inside = False
		elif regex.match("<\w+>", token):
			if opened:
				print(f"La balise <{opened}> n'a pas été fermée.")
				sys.exit(1)
			opened = token[1:-1]
		else:
			if opened and inside:
				result.append((token, str(len(token)), 'I-'+opened))
			elif opened:
				result.append((token, str(len(token)), 'B-'+opened))
				inside = True
			else:
				result.append((token, str(len(token)), 'O'))

	with open (out_file, 'w') as f:
		for token in result:
			f.write('\t'.join(token) + '\n')

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', required=True)
	parser.add_argument('-o', '--output', required=False)
	parser.add_argument('-t', '--tokenizer', required=False, choices=['all', 'apostrophe', 'hashtag_apostrophe'], default='hashtag_apostrophe')
	args = parser.parse_args()
	if args.output == None:
		args.output = args.input + '.tab' # ou .tsv ou .bio
	main(args.input, args.output, args.tokenizer)
