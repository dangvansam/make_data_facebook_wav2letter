'''
script create data for facebook wav2letter
by dangvansam98 MTA VN
email: dangvansam98@gmail.com
github: dangvansam98
21/05/2019
'''
import os
import shutil
import json
from speaker_id import map_spk_gen #dict of speaker -> gender, ex:{'10': 'F', '38': 'F', '16': 'F', '41': 'F', '42': 'F'}

#create folder data_wav2letter, and create 3 foler: train, test, valid in data_wav2letter for output file
#folder train,test, valid include wav file
#file train.json, test.json, valid.json store key(path to wav file), text( transcript of wav file), duration (lenght wav file)
#ex: {"duration": 3.3125, "key": "D:\\ASR\\dataset ASR\\vivos2\\train\\VIVOSSPK01_R008.wav", "text": "có đêm gặp phải heo nọc nó rượt"}
#dataset___data_wav2letter ___train(.wav, .tkn, .wrd, .id)\
#       |                 |___test(.wav, .tkn, .wrd, .id) \  data for facebook wav2letter
#       |                 |___valid(.wav, .tkn, .wrd, .id)\
#       |_______train(.wav files)
#       |_______test(.wav files)
#       |_______valid(.wav files)
#       |_______train.json
#       |_______test.json
#       |_______valid.json 


phar = 'train'    #train, test, valid data folder
data_1 = phar + '/'
data_2 = 'facebook_data_wav2letter/'+data_1
for i,file in enumerate(os.listdir(data_1)):
    print(i+1,file)
    shutil.copyfile(data_1+file,data_2 +'{:09d}.wav'.format(i))
def tkn_conv(words):
    tkn = []
    for c in words:
        if c== ' ':
            tkn.append('|')
        else:
            tkn.append(c)
    tkn2 = ' '.join(tkn)
    return tkn2+' '

#words = 'sam sam'
#print(tkn_conv(words))
data = []
train_json = open(phar+".json",encoding = "UTF-8")
for line in train_json:
    data.append(json.loads(line))
print(data[1]['key'].split('\\')[-1][8:10])

for i,data_1 in enumerate(data):
    tkl = open(data_2+'{:09d}.tkn'.format(i),'w',encoding = "UTF-8")
    print('tkn:',tkn_conv(data_1['text']))
    tkl.write(tkn_conv(data_1['text']))

    print('wrd:',data_1['text'])
    wrd = open(data_2+'{:09d}.wrd'.format(i),'w',encoding = "UTF-8")
    wrd.write(data_1['text'])

    idd = open(data_2+'{:09d}.id'.format(i),'w')
    idd.write('file_id'+'\t'+str(i)+'\n')
    print('file_id'+'\t'+str(i))
    spk = data_1['key'].split('\\')[-1][8:10]
    idd.write('gender'+'\t'+ map_spk_gen[spk]+'\n')
    print('gender'+'\t'+ map_spk_gen[spk])
    spk_id = spk
    if spk_id[0] == '0':
        spk_id = spk_id[1]
    idd.write('speaker_id'+'\t'+spk_id)
    print('speaker_id'+'\t'+spk_id)

