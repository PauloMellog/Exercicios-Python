#Conversões em python!

from calendar import day_name

medida = int(input('Coloque a distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {}m corresponde a:'.format(medida))
print('{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{}dm \n{}cm \n{}mm'.format(km, hm, dam, dm, cm, mm))