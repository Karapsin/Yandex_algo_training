n = int(input())
sound = [float(input())]
dist = [None]

count = 1
while count < n:
    input_list = input().strip().split()
    sound.append(float(input_list[0]))
    dist.append(input_list[1])

    count = count + 1

lower = 30
upper = 4000

for i in range(len(sound)-1):
    if abs(sound[i+1]-sound[i])<10**(-6):
        continue

    if sound[i+1]>=sound[i] and dist[i+1]=='closer':
        lower = max((sound[i] + sound[i + 1]) / 2, lower)
    if sound[i+1]>=sound[i] and dist[i+1]=='further':
        upper = min((sound[i] + sound[i + 1]) / 2, upper)

    if sound[i+1]<sound[i] and dist[i+1]=='closer':
        upper = min((sound[i] + sound[i + 1]) / 2, upper)
    if sound[i+1]<sound[i] and dist[i+1]=='further':
        lower = max((sound[i] + sound[i + 1]) / 2, lower)

print(lower, upper)