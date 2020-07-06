def reorder_log_files(logs):
    digit_logs = []
    letter_logs = []
    letter_logs_dict = {}

    for item in logs:
        if item.split(' ')[1].isdigit():
            digit_logs.append(item)
        else:
            letter_logs_dict[item.split(' ')[0]] = ' '.join(item.split(' ')[1:])

    letter_logs_dict = {k: v for k, v in sorted(letter_logs_dict.items(), key=lambda x: x[1])}

    for k, v in letter_logs_dict.items():
        letter_logs.append(k + ' ' + v)

    return letter_logs + digit_logs


print(reorder_log_files(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
