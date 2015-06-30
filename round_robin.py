__author__ = 'Ahmad Al-Sajid'


def round_robin():

    #input n
    process_number = int(input())
    # input n number of burst times
    temp_list_of_process = [int(x) for x in input().split(" ")]
    #input quantum
    quantum = int(input())
    #total burst time of all processes
    total_execution_time = sum(temp_list_of_process)
    #print("total burst time {}".format(total_execution_time))                              #debug
    #assign id with process
    list_of_process = []
    for i in range(len(temp_list_of_process)):
        data = {
            'id': int(i+1),
            'time': temp_list_of_process[i],
        }
        list_of_process.append(data.copy())

    ##########################################################################################
    #grant chart
    i = 0 #counter
    counter =0                                                                              # debug
    vector_of_grant_chart =[]
    temp_execution_time = 0
    while(True):
        if(total_execution_time == temp_execution_time): break
        if i == process_number : i = 0
        if temp_list_of_process[i] > 0:
            if temp_list_of_process[i] >= quantum :
                data = {
                    'id' : list_of_process[i]['id'],
                    'time' : quantum,
                }
                temp_list_of_process[i] = temp_list_of_process[i] - quantum
            else:
                data = {
                    'id' : list_of_process[i]['id'],
                    'time' :temp_list_of_process[i] % quantum,
                }
                temp_list_of_process[i] = 0
            vector_of_grant_chart.append(data.copy())
            temp_execution_time = temp_execution_time+ data['time']
            #print("process {} burst time {} remaining time {}".format(i+1,data['time'],temp_list_of_process[i]))    #debug
        i = i+1                 # increment counter

    #for vector in vector_of_grant_chart:                                               #debug
    #    print("process {}-----> time {}".format(vector['id'],vector['time']))

    #######################################################################################
    waiting_time = []
    turnaround_time = []
    response_time = []
    for process in range(1,process_number+1):
        last_index =0
        temp_time = 0
        #print("length  of vector {}".format(len(vector_of_grant_chart)))                            #debug
        #print("process {}".format(process))                                                               #debug
        for i in range(len(vector_of_grant_chart)):
            if vector_of_grant_chart[i]['id'] == process:
                last_index = i
        #print("last index of {} is {}".format(process,last_index))                             #debug
        for i in range(last_index+1):
            temp_time = temp_time + vector_of_grant_chart[i]['time']
        waiting_time.append(temp_time - list_of_process[process-1]['time'])
        turnaround_time.append(temp_time)
        ############################# response time   #####################
        temp_time =0
        for i in range(len(vector_of_grant_chart)):
            if vector_of_grant_chart[i]['id'] == process:
                last_index = i
                break
        for i in range(last_index):
            temp_time = temp_time + vector_of_grant_chart[i]['time']
        response_time.append(temp_time)
        ###################################################################


    average_waiting_time = sum(waiting_time)/process_number
    average_turnaround_time = sum(turnaround_time)/process_number
    average_response_time = sum(response_time)/process_number

    names = ["Process name", "Waiting time", "Turnaround time", "Response time"]
    print("{:<20} {:<20} {:<20} {:<20}".format(names[0], names[1], names[2], names[3]))
    for i in range(process_number):
        print("Process {:<12} {:<20.2f} {:<20.2f} {:<20.2f}".format(i+1, waiting_time[i], turnaround_time[i], response_time[i]))

    avg_names = ["Average waiting time", "Average turnaround time", "Average response time"]
    print("{:<30} {:<30} {:<30}".format(avg_names[0], avg_names[1], avg_names[2]))
    print("{:<30.2f} {:<30.2f} {:<30.2f}".format(average_waiting_time, average_turnaround_time, average_response_time))



if __name__ == '__main__':
    round_robin()
