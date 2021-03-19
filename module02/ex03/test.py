#!/usr/bin/python
from csvreader import CsvReader

# if __name__ == "__main__":
# 	with CsvReader('good.csv') as file:
# 		data = file.getdata()
# 		header = file.getheader()
# 		print(data)
# 		print(header)
	
# if __name__ == "__main__":
#     with CsvReader('bad.csv') as file:
#         if file == None:
#             print("File is corrupted")


if __name__ == "__main__":
	with CsvReader('good.csv', ',', True) as file:
		data = file.getdata()
		header = file.getheader()
		print(data)
		print(header)
