map1 = open('map_spk_gen.txt','r')
i = 1
map_spk_gen = {}
for line in map1:
    line = line.strip('\n')
   #print(line)
    speaker = line.split(' ')[0][8:10]
    gender = line.split(' ')[1]
    i+=1
    map_spk_gen[speaker] = gender.upper()
print(map_spk_gen)