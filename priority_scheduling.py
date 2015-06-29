__author__ = 'Ahmad Al-Sajid'


def priority_scheduling():
    process_number = int(input())

    list_of_process = []
    for i in range(process_number):
        a,b = input().split(" ")
        data = {
            'name': "Process {}".format(i+1),
            'time': int(a),
            'priority': int(b),
        }
        list_of_process.append(data.copy())

    sorted_list_of_process = sorted(list_of_process, key=lambda k: k['priority'])

    waiting_time = [0, ]
    turnaround_time = [sorted_list_of_process[0]['time'], ]
    response_time = [0, ]
    for i in range(1, process_number):
        waiting_time.append(waiting_time[i-1]+sorted_list_of_process[i-1]['time'])
        turnaround_time.append(turnaround_time[i-1] + sorted_list_of_process[i]['time'])
        response_time.append(waiting_time[i-1]+sorted_list_of_process[i-1]['time'])


    average_waiting_time = sum(waiting_time)/process_number
    average_turnaround_time = sum(turnaround_time)/process_number
    average_response_time = sum(response_time)/process_number
    names = ["Process name", "Waiting time", "Turnaround time", "Response time"]
    print("{:<20} {:<20} {:<20} {:<20}".format(names[0], names[1], names[2], names[3]))
    for i in range(len(sorted_list_of_process)):
        print("{:<20} {:<20.2f} {:<20.2f} {:<20.2f}".format(sorted_list_of_process[i]['name'], waiting_time[i], turnaround_time[i], response_time[i]))
    avg_names = ["Average waiting time", "Average turnaround time", "Average response time"]
    print("{:<30} {:<30} {:<30}".format(avg_names[0], avg_names[1], avg_names[2]))
    print("{:<30.2f} {:<30.2f} {:<30.2f}".format(average_waiting_time, average_turnaround_time, average_response_time))


if __name__ == '__main__':
    priority_scheduling()
