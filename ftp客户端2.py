import socket,os,json,struct,sys
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))

while 1:
    try:
        username = input('用户名>>:')

        if username:
            username2 = bytes(username, encoding='utf-8')

        else:
            continue

        password = input('密码>>:')
        if password:
            password2 = bytes(password, encoding='utf-8')
            phone.send(username2)
            phone.send(password2)
        else:
            continue

        reply=phone.recv(1024)
        reply2=reply.decode('utf-8')
        print(reply2)           #是否成功


        reply3 = phone.recv(100)
        reply4 = reply3.decode('utf-8')
        print(reply4)           #文件目录

        reply5 = phone.recv(1024)
        reply6 = reply5.decode('utf-8')
        print(reply6)            #文件内容


        func=input('您需要： 1.上传文件'
                   '        2.下载文件\n')
        func2=bytes(func,encoding='utf-8')
        phone.send(func2)

        if func=='1':
            path=input('文件路径：')
            filename=os.path.basename(path)
            size=os.path.getsize(path)
            dic        ={'path':path,'filename':filename,'size':size}
            json_dic   =json.dumps(dic)
            json_dic_b =bytes(json_dic,encoding='utf-8')
            head_len   =struct.pack('i',len(json_dic_b))
            phone.send(head_len)
            phone.send(json_dic_b)

            with open(path,'rb') as f:
                    data=f.read()
                    phone.send(data)


        if func == '2':
            filename=input('下载文件：')
            filename2=bytes(filename,encoding='utf-8')
            phone.send(filename2)

            data1 = phone.recv(4)
            data2 = struct.unpack('i', data1)[0]


            head = phone.recv(data2)
            head2 = head.decode('utf-8')
            head3 = json.loads(head2)


            filepath=input('下载路径：')

            sized = 0

            file=os.path.join(filepath,filename)
            with open(file, 'wb') as f:
                while sized < head3['size']:
                    data = phone.recv(8192)

                    f.write(data)
                    sized += 8192
                    width=70
                    percent=sized/head3['size']
                    show_str = ('[%%-%ds]' % width) % (int(width * percent) * '#')
                    print('\r%s %d%%' % (show_str, int(100 * percent)), file=sys.stdout, flush=True, end='')
    except:
        break
