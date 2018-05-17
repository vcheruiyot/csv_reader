#!/usr/bin/python3
import csv

class csv_dict_reader:
	def __init__(self, csv_file):
		self.csv_file = csv_file
		
	"""
	pass in the col_1, col_2 for which you 
	want to map the csv file
	"""
	def get_dict(self, col_1, col_2):
		try:
			with open(self.csv_file, 'r') as f:
				reader = csv.reader(f)
				res = {}
				for row in reader:
					try:
						res[row[col_1]] = row[col_2]
					except IndexError:
						print(col_1 + ' and ' + col_2 + 'are out of bounds')
				return res		
		except IOError:
			print("Could not open ", self.csv_file)
				

if __name__ == "__main__":
	csv_file = "../../Downloads/legend.csv"
	csv_reader = csv_dict_reader(csv_file)
	res = csv_reader.get_dict(1, 2)
	print(res)
		
	
		
	