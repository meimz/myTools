import os
import hashlib

def listdir(path, list_name):  # 传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            if not file_path.find('.git')>0:
                list_name.append(file_path)

def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

dbPaths=[]


#修改下面文件路径
listdir(r'D:\wamp64\www\myDiscuz',dbPaths)


md5Strs=''
for p in dbPaths:
    p=p.replace('\\','/')
    passArr=['data/diy/template/default/group/index.htm.bak','config/config_','sendmail.lock','update.lock','source/admincp/discuzfiles.md5','m/index.php','install/images','data/template','data/log','data/cache','install.lock','data/sysdata','install/data','install/include','source/plugin/mobile','source/plugin','uc_server','uc_client']
    passFlg=False
    for passStr in passArr:
        if p.find(passStr)>0:
            passFlg=True
            continue
    if passFlg:
        continue
    file=p.split('/')[-1]
    if file=='index.htm' or file=='index.html':
        continue
    need=p.replace('D:/wamp64/www/myDiscuz/','')
    if need==file:
        need='*./'+need
    else:
        need = '*' + need
    md5Strs=md5Strs+'{} {}'.format(GetFileMd5(p),need)+'\n'
with open('discuzfiles.md5','w',encoding='utf-8') as f:
    f.write(md5Strs)
    f.close()
print(r'将 discuzfiles.md5 复制到 source/admincp/discuzfiles.md5')