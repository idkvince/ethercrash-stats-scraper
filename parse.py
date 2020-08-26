import csv

sanitized_stats = open('santized_ethcrash_stats.csv', 'a')
with open('ethcrash_stats.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    list_of_rows = list(csv_reader)
    print(len(list_of_rows))
    
for i in range(len(list_of_rows)):
    split_date = list_of_rows[i][1].split(" ")
    date_list = split_date[0] + " " + split_date[1] + " " + split_date[2] + " " + split_date[3] + " " + split_date[4]

    space_date_list = date_list.split(" ")
    #print(space_date_list)
    #time_list = space_date_list[4].split(":")

    day = True
    if 'Jan' in space_date_list[1]:
        time_list = space_date_list[4].split(":")
        month = 1
        day = True

    elif 'Jan' in space_date_list[0]:
        time_list = space_date_list[3].split(":")
        month = 1 
        day = False

    if 'Feb' in space_date_list[1]:
        time_list = space_date_list[4].split(":")
        month = 2
        day = True

    elif 'Feb' in space_date_list[0]:
        time_list = space_date_list[3].split(":")
        month = 2 
        day = False

    if 'Mar' in space_date_list[1]:
        time_list = space_date_list[4].split(":")
        month = 3
        day = True

    elif 'Mar' in space_date_list[0]:
        time_list = space_date_list[3].split(":")
        month = 3
        day = False

    if 'Apr' in space_date_list[1]:
        time_list = space_date_list[4].split(":")
        month = 4
        day = True

    elif 'Apr' in space_date_list[0]:
        time_list = space_date_list[3].split(":")
        month = 4
        day = False

    if 'May' in space_date_list[1]:
        time_list = space_date_list[4].split(":")
        month = 5
        day = True

    elif 'May' in space_date_list[0]:
        time_list = space_date_list[3].split(":")
        month = 5
        day = False

    if 'Jun' in space_date_list[1]:
        time_list = space_date_list[4].split(":")
        month = 6
        day = True 

    elif 'Jun' in space_date_list[0]:
        time_list = space_date_list[3].split(":")
        month = 6
        day = False

    if 'Jul' in space_date_list[1]:
        time_list = space_date_list[4].split(":")
        month = 7
        day = True

    elif 'Jul' in space_date_list[0]:
        time_list = space_date_list[3].split(":")
        month = 7
        day = False

    if 'Aug' in space_date_list[1]:
        time_list = space_date_list[4].split(":")
        month = 8 
        day = True

    elif 'Aug' in space_date_list[0]:
        time_list = space_date_list[3].split(":")
        month = 8
        day = False

    if 'Sep' in space_date_list[1]:
        time_list = space_date_list[4].split(":")
        month = 9
        day = True

    elif 'Sep' in space_date_list[0]:
        time_list = space_date_list[3].split(":")
        month = 9
        day = False

    if 'Oct' in space_date_list[1]:
        time_list = space_date_list[4].split(":")
        month = 10
        day = True

    elif 'Oct' in space_date_list[0]:
        time_list = space_date_list[3].split(":")
        month = 10
        day = False

    if 'Nov' in space_date_list[1]:
        time_list = space_date_list[4].split(":")
        month = 11
        day = True

    elif 'Nov' in space_date_list[0]:
        time_list = space_date_list[3].split(":")
        month = 11
        day = False

    if 'Dec' in space_date_list[1]:
        time_list = space_date_list[4].split(":")
        month = 12
        day = True

    elif 'Dec' in space_date_list[0]:
        time_list = space_date_list[3].split(":")
        month = 12
        day = False
    
    #print('day: {}'.format(day))
    #print('space_date_list: {}'.format(space_date_list))

    no_x_list = list_of_rows[i][2].split("x")
    #print("line number: {}".format(i))
    #print(str(month) + "," + space_date_list[2] + "," + space_date_list[3] + "," + time_list[0] + "," + time_list[1] + "," + time_list[2] + "," + no_x_list[0])

    if day is True:
        recombine_list = (str(month) + "," + space_date_list[2] + "," + space_date_list[3] + "," + time_list[0] + "," + time_list[1] + "," + time_list[2] + "," + no_x_list[0])

    if day is False:
        recombine_list = (str(month) + "," + space_date_list[1] + "," + space_date_list[2] + "," + time_list[0] + "," + time_list[1] + "," + time_list[2] + "," + no_x_list[0])

    print(recombine_list)
    sanitized_stats.writelines(recombine_list + '\n')

sanitized_stats.close()



