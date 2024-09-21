a = int(input())
b = int(input())
n = int(input())
m = int(input())

def get_track_time(train_num, train_interval, type):
    if type=='max':
        return 1 * train_num + (train_num + 1) * train_interval
    elif type=='min':
        return 1 * train_num + (train_num - 1) * train_interval

max_ans = min(get_track_time(n, a, 'max'), get_track_time(m, b, 'max'))
min_ans = max(get_track_time(n, a, 'min'), get_track_time(m, b, 'min'))

if max_ans>=min_ans:
    print(min_ans, max_ans)
else:
    print(-1)