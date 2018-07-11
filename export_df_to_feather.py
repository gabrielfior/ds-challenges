import pandas as pd
import argparse

def convert_json_to_feather(filename):

	print("filename {}".format(filename))
	df = pd.read_json(filename)
	df.to_feather(filename.split('.')[0]+'.feather')

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('--filename', type=str, help='JSON filename')

	args = parser.parse_args()
	print(args.filename)

	convert_json_to_feather(args.filename)