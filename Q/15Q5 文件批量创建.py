import random as rd
from pathlib import Path 

def pp():
    return chr(rd.randint(32,126))

n=int(input('文件数'))

dr = Path('test')
dr.mkdir(exist_ok = True)

for i in range(n):
    f_path = dr/f'f{i+1}.txt'
    m=(int(input(f'文件{i+1}行数')))
    line=[]
    for _ in range(m):
        line.append(''.join(pp() for _ in range(rd.randint(1,10))))
    f_path.write_text('\n'.join(line),encoding='ascii')
    
#改名字
address = Path('test')
files = list(address.glob('*.txt'))
for i in files:
    
    with open(i,'r',encoding='ascii') as f:
        content=f.read().splitlines()
        content_new = [qwq+'-python' for qwq in content]
    with open(i,'w',encoding='ascii') as f:
        f.write('\n'.join(content_new))
        
    name = i.stem
    suffix = i.suffix
    new_name = f'{name}-python{suffix}'
    new_path = dr/new_name
    i.rename(new_path)
    
print('over')