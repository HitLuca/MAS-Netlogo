import numpy as np

times = 96
names = ['Amstel', 'Amstelveenseweg', 'Buikslotermeer', 'Centraal', 'Dam', 'Evertsenstraat', 'Floradorp', 'Haarlemmermeerstation', 'Hasseltweg', 'Hendrikkade', 'Leidseplein', 'Lelylaan', 'Muiderpoort', 'Museumplein', 'RAI', 'SciencePark', 'Sloterdijk', 'Surinameplein', 'UvA', 'VU', 'Waterlooplein', 'Weesperplein', 'Wibautstraat', 'Zuid']

passengers = np.zeros((len(names), times))

with open('passengers-location_day1.csv') as f:
    lines = f.readlines()
    for line in lines[2:]:
        line = line.replace('\n', '').split(';')
        # print(line)
        origin = line[1]
        time = line[0].split(':')
        index = int(int(time[0]) * 4 + int(time[1])/15)

        # print(origin)
        # print(index)
        sum = 0
        for t in line[2:]:
            sum += int(t)
        # print(sum)
        passengers[names.index(origin), index] = sum

print(passengers)

with open('passengers.txt', 'w') as f:
    print('[', end='', file=f)
    for line in passengers:
        print(line, file=f)
    print(']', file=f)