def check_plate(plate):
	if (len(plate) == 13):
		if( 'A' <= plate[0] <= 'Z' and 'A' <= plate[1] <= 'Z'and plate[2] ==' ' and '0' <= plate[3] <= '9' and '0' <= plate[4] <= '9' and plate[5] ==' ' and 'A' <= plate[6] <= 'Z' and 'A' <= plate[7] <= 'Z' and plate[8] ==' 'and '0' <= plate[9] <= '9' and '0' <= plate[10] <= '9' and '0' <= plate[11] <= '9' and '0' <= plate[12] <= '9' ):
			return True
	else:
		return False

import csv
my_dict = {'1': 'aaa', '2': 'bbb', '3': 'ccc'}
with open('test.csv', 'w') as f:
    for key in my_dict.keys():
        f.write("%s,%s\n"%(key,my_dict[key]))
