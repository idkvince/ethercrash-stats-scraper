
cash_out = 1.42
total_losing_crash = 0
consecutive_crash = 0
#max_consecutive_crash = 0
line_number = 0
prev_crash = 0
crashed = False

one_crash_count = 0
two_crash_count = 0
three_crash_count = 0
four_crash_count = 0
five_crash_count = 0
six_crash_count = 0
seven_crash_count = 0
eight_crash_count = 0
nine_crash_count = 0
ten_crash_count = 0
##########################

with open('crashpoints', 'r') as f:
    for crash_line in f:
        #print(crash_line)
        line_number += 1

        if float(crash_line) < cash_out:
            print('a')
            print('crash_line: {} cashout {}'.format(crash_line, cash_out))
            total_losing_crash +=1
            crashed = True

        if float(crash_line) >= cash_out:
            print('b')
            print('crash_line: {} cashout {}'.format(crash_line, cash_out))
            consecutive_crash = 0
            crashed = False

        if crashed:
            consecutive_crash += 1

            if consecutive_crash == 1:
                one_crash_count += 1

            if consecutive_crash == 2:
                one_crash_count -= 1
                two_crash_count += 1

            if consecutive_crash == 3:
                one_crash_count -= 1
                two_crash_count -= 1
                three_crash_count += 1

            if consecutive_crash == 4:
                one_crash_count -= 1
                two_crash_count -= 1
                three_crash_count -= 1
                four_crash_count += 1

            if consecutive_crash == 5:
                one_crash_count -= 1
                two_crash_count -= 1
                three_crash_count -= 1
                four_crash_count -= 1                
                five_crash_count += 1

            if consecutive_crash == 6:
                one_crash_count -= 1
                two_crash_count -= 1
                three_crash_count -= 1
                four_crash_count -= 1
                five_crash_count -= 1                
                six_crash_count += 1

            if consecutive_crash == 7:
                one_crash_count -= 1
                two_crash_count -= 1
                three_crash_count -= 1
                four_crash_count -= 1
                five_crash_count -= 1 
                six_crash_count -= 1
                seven_crash_count += 1
            
            if consecutive_crash == 8:
                one_crash_count -= 1
                two_crash_count -= 1
                three_crash_count -= 1
                four_crash_count -= 1
                five_crash_count -= 1                
                six_crash_count -= 1
                seven_crash_count -= 1
                eight_crash_count += 1
           
            if consecutive_crash == 9:
                one_crash_count -= 1
                two_crash_count -= 1
                three_crash_count -= 1
                four_crash_count -= 1
                five_crash_count -= 1
                six_crash_count -= 1
                seven_crash_count -= 1
                eight_crash_count -= 1
                nine_crash_count += 1
          
            if consecutive_crash == 10:
                one_crash_count -= 1
                two_crash_count -= 1
                three_crash_count -= 1
                four_crash_count -= 1
                five_crash_count -= 1
                six_crash_count -= 1
                seven_crash_count -= 1
                eight_crash_count -= 1
                nine_crash_count -= 1
                ten_crash_count += 1

           
print("total games:        {}".format(line_number))
print("total_losing_crash: {}".format(total_losing_crash))

print("crashes at 1:       {} Total crash: {}".format(one_crash_count, one_crash_count))
print("crashes at 2:       {} Total crash: {}".format(two_crash_count,two_crash_count*2))
print("crashes at 3:       {} Total crash: {}".format(three_crash_count,three_crash_count*3))
print("crashes at 4:       {} Total crash: {}".format(four_crash_count,four_crash_count*4))
print("crashes at 5:       {} Total crash: {}".format(five_crash_count,five_crash_count*5))
print("crashes at 6:       {} Total crash: {}".format(six_crash_count,six_crash_count*6))
print("crashes at 7:       {} Total crash: {}".format(seven_crash_count,seven_crash_count*7))
print("crashes at 8:       {} Total crash: {}".format(eight_crash_count,eight_crash_count*8))
print("crashes at 9:       {} Total crash: {}".format(nine_crash_count,nine_crash_count*9))
print("crashes at 10:      {} Total crash: {}".format(ten_crash_count,ten_crash_count*10))
