import websocket, json, time, datetime,requests
from datetime import datetime

import time, requests, random
sandi = input('Masukan password : ')
if sandi == 'rizal':
	print('Jangan nyesal gunakan aku ya? /n karena aku lagi pms')
else:
	ws.close()
xz = 1
status = 'tidur'
nama = 'xyx'
judul = 'xyz'
timeh = datetime.today()
response3 = '{"div":"hai"}'
createdl = datetime.today()
z = 0
namal = 'xyz'
judull = 'xwx'
timehl2 = datetime.today()

txtid = input('Masukan Link Live : ')
response = requests.get(txtid)
urlo = response.url
slink = urlo[34:-59]
socketstring = ("wss://id-heimdallr.spooncast.net/" + slink)
print(socketstring)
botauthtoken2 = 'e2f85e476d5d560b388236c42fecabba40bf82dd' #token lu disini
mypesan = '{"live_id":'+slink+',"token":"'+botauthtoken2+'","event":"live_join"}'###### end


def on_message(ws, message):
        global judul
        global nama
        global response3
        global status
        global timeh
        global timehl2
        global xz
        global z
        chat = json.loads(message)
        uid = chat['data']['author']['id']
        nick = chat['data']['author']['nickname']
        evn = chat['event']
        kesurupan = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"Hallo Kamu Fans Ku Wellcome !! 😳 "}'
        if 1 == 1:
            if z == 0:
                ws.send(kesurupan)
                z = 1
        if evn == 'live_message':
            psn = chat['data']['message']
            tag = chat['data']['author']['tag']
            print(chat['data']['author']['tag'])
        emot = ['🤭🤭🤭', '🙄🙄🙄', '😝😝😝', '😇😇😇', '😌😌😌', '😔😔😔', '🥺🥺🥺']
        ya = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"' + nick + 'Sokap Ih !!' + random.choice(emot) + '"}'
        tidak = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"' + nick + ' Lau Bicik Ih ' + random.choice(emot) + '"}'
        bisajadi = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"' + nick + 'Bodo Amat Ya ' + random.choice(emot) + '"}'
        bodoamat = '{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"' + nick + ' IYA ' + random.choice(emot) + '"}'
        listjawaban = [
         ya, tidak, bisajadi, bodoamat]
        if evn == 'live_message' and psn[:1].lower() == 't' and psn[-1:] == '?':
            kambeng = random.choice(listjawaban)
            print(kambeng)
            ws.send(kambeng)
        lsjoin = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"Hayo ' + nick + 'ghost huu"}'
        sapa = [' Long Time No See😊 ',' Gimana Kabar Kamu😳  ',' Bahagia Terus Ya🙂 ',' Kak Kangen Aku Ya🤗 ',' Jangan Lupa Makan Kak?😳 ','  Semoga Music Nya Membuat Kamu Nyaman😊 ',' Hai Kak Welcome😇 ',' Salken Kak Ya😅 ','  Jangan Lupa Bahagia Kak🙃  ','  Enjoy Yan Kak🤗 ','  Awas Kangen Kak Kesini Mulu😂 ',' Hai Kak Imut😉 ',' Jangan Lupa TabLove😍 ',' Hai Kak Cute?😁 ']
        ljoin = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":" ' + nick + random.choice(sapa) + ' '+ '"}'
        likee = [' Thanks Cinta Palsunya ',' Love Nya palsu Ah ','  Love Sungguhan Dong ',' Lovenya Palsu Terus Sabar Hmm ']
        llike = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":" ' + nick + random.choice(likee) + '❤️' + '"}'
        tidur = '{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":" Tara Bucin Dulu Ya Gais Bye 😳"}'
        kalem = '{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":" HAHAHAHAHAHAHAHAH !! 😆😆"}'
        bangun = '{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":" Tara Kembali Maaf Abis Bucin 😒"}'
        bangun2 = '{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":" HALLO JUGA KAK ' + nick + ' JANGAN LUPA KADONYA YA KAK DI POJOK KIRI BAWAH 🎁🤭"}'
        ping = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"' + nick + ' Jangan Pernah Terlalu Berharap Karena Disuatu Saat Akan Sakit😌"}'
        fans = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"' + nick + ' Pagi Juga Kamu, Jangan Lupa Sarapan Ya !! 😊"}'
        promot = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"Lau Siapa Si' + nick + ' So Kenal Manggil² Jelek !! 😏"}'
        ig = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"Hai ' + nick + ' Malam Juga Kamu, Jangan bergadang kak !! 😊"}'
        makasih = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":"' + nick + ' Waalaikuksalam Wr. Wb. 😊😇"}'
        jawab = '{"appversion":"4.1.0","event":"live_message","token":"","useragent":"Web","message":" Tara Kasih Tau Ya Akak  ' + nick + ' Kazal Sayang Anggrak😳  "}'
        rank = '{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":" Punya tangankan? pencet sana panteq 😒"}'
        if evn == 'live_message' and (psn == '#status' or psn == '#durasi' or psn == '#info'):
        	headers2 = {'User-Agent': 'Mozilla/5.0'}
        	response2 = requests.get(('https://id-api.spooncast.net/lives/' + slink + ''), headers=headers2)
        	createdl = response2.json()['results'][0]['created']
        	tanggal = datetime.today()
        	cre = createdl[:-17]
        	crea = createdl[11:-8]
        	creat = cre + ' ' + crea
        	creatdt = datetime.strptime(creat, '%Y-%m-%d %H:%M:%S')
        	selisih = tanggal - creatdt
        	s1 = '07:00:00'
        	s2 = str(selisih)[:-7]
        	formatss = '%H:%M:%S'
        	timehl2 = datetime.strptime(s2, formatss) - datetime.strptime(s1, formatss)
        	ws.send('{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"Durasi Room: 🔥🔥 '+ str(timehl2) +' 🔥🔥"}')
        if evn == 'live_join':
            if status == 'bangun':
                ws.send(ljoin)
            if evn == 'live_shodowjoin':
                ws.send(lsjoin)
        if evn == 'live_like' and status == 'bangun':
            ws.send(llike)
        if evn == 'live_message' and psn == '#off‏�1�7��1�7�1�7  1�7' and status == 'bangun':
            status = 'tidur'
            ws.send(tidur)
        if evn == 'live_message' and psn == '#rank':
            headers3 = {'User-Agent': 'Mozilla/5.0'}
            response3 = requests.get('https://id-api.spooncast.net/lives/popular/', headers=headers3)
            ws.send(rank)
        if evn == 'live_message' and psn[:-3] == '#rank':
            zz = psn[6:]
            xz = int(zz) - 1
            tanggal = datetime.today()
            nama = response3.json()['results'][xz]['author']['nickname']
            judul = response3.json()['results'][xz]['title']
            created = response3.json()['results'][int(xz)]['created']
            cre = created[:-17]
            crea = created[11:-8]
            creat = cre + ' ' + crea
            creatdt = datetime.strptime(creat, '%Y-%m-%d %H:%M:%S')
            selisih = tanggal - creatdt
            s1 = '07:00:00'
            s2 = str(selisih)[:-7]
            formatss = '%H:%M:%S'
            timeh = datetime.strptime(s2, formatss) - datetime.strptime(s1, formatss)
            ws.send('{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"Info rank ' + str(xz + 1) + '  nama: ' + nama + ' judul: ' + judul + '  durasi -> ' + str(timeh) + ' "}')
        if evn == 'live_message' and psn[:-2] == '#rank':
            zz = psn[6:]
            xz = int(zz) - 1
            tanggal = datetime.today()
            nama = response3.json()['results'][xz]['author']['nickname']
            judul = response3.json()['results'][xz]['title']
            created = response3.json()['results'][int(xz)]['created']
            cre = created[:-17]
            crea = created[11:-8]
            creat = cre + ' ' + crea
            creatdt = datetime.strptime(creat, '%Y-%m-%d %H:%M:%S')
            selisih = tanggal - creatdt
            s1 = '07:00:00'
            s2 = str(selisih)[:-7]
            formatss = '%H:%M:%S'
            timeh = datetime.strptime(s2, formatss) - datetime.strptime(s1, formatss)
            ws.send('{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"Info rank ' + str(xz + 1) + '  nama: ' + nama + ' judul: ' + judul + '  durasi -> ' + str(timeh) + ' "}')
        if evn == 'live_message' and psn == '#me':
            print('sjqjajsajajhshsajsjjsjwjwa')
            cid = tag
            headers4 = {'User-Agent': 'Mozilla/5.0'}
            response4 = requests.get(('https://id-api.spooncast.net/search/user/?keyword=' + cid + ''), headers=headers4)
            idd = response4.json()['results'][0]['id']
            headers5 = {'User-Agent': 'Mozilla/5.0'}
            response5 = requests.get(('https://id-api.spooncast.net/users/' + str(idd) + '/notice/'), headers=headers5)
            nn = response5.json()['results'][0]['bj']['nickname']
            tg = str(response5.json()['results'][0]['bj']['date_joined'])
            tan = tg[:-17]
            tang = tg[11:-8]
            tangg = tan + ' ' + tang
            tangga = datetime.strptime(tangg, '%Y-%m-%d %H:%M:%S')
            ws.send('{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"Info username ' + nn + ' tanggal akun dibuat -> ' + str(tangga) + ' GMT +0 "}')
        if evn == 'live_message' and psn[:4] == '#cek':
            print('sjqjajsajajhshsajsjjsjwjwa')
            cid = psn[5:]
            headers4 = {'User-Agent': 'Mozilla/5.0'}
            response4 = requests.get(('https://id-api.spooncast.net/search/user/?keyword=' + cid + ''), headers=headers4)
            idd = response4.json()['results'][0]['id']
            headers5 = {'User-Agent': 'Mozilla/5.0'}
            response5 = requests.get(('https://id-api.spooncast.net/users/' + str(idd) + '/notice/'), headers=headers5)
            nn = response5.json()['results'][0]['bj']['nickname']
            tg = str(response5.json()['results'][0]['bj']['date_joined'])
            tan = tg[:-17]
            tang = tg[11:-8]
            tangg = tan + ' ' + tang
            tangga = datetime.strptime(tangg, '%Y-%m-%d %H:%M:%S')
            ws.send('{"appversion":"4.1.0","event":"live_message","token":" ","useragent":"Web","message":"Info username ' + nn + ' tanggal akun dibuat -> ' + str(tangga) + ' GMT +0 "}')
        if evn == 'live_message' and psn == '#on‏�1�7��1�7�1�7  1�7' and status == 'tidur':
            status = 'bangun'
            ws.send(bangun)
        if evn == 'live_message' and psn == 'wkwkwk':
                ws.send(kalem)
        if evn == 'live_message' and psn == 'hallo':
                ws.send(bangun2)
        if evn == 'live_message' and psn == 'qoutes':
            ws.send(ping)
        if evn == 'live_message' and psn == 'pagi':
            ws.send(fans)
            if evn == 'live_message' and psn == 'tara':
            ws.send(promot)
        if evn == 'live_message' and psn == 'malam':
            ws.send(ig)
        if evn == 'live_message' and (psn == 'ass' or ps == 'Ass' or ps == 'ASS'):
                ws.send(makasih)
        if evn == 'live_message' and psn == 'tara‏�1�7��1�7�1�7  1�7':
            ws.send(jawab)
        if evn == 'live_message':
            if psn == 'keluar' and uid == '210900010':
                ws.close()
def on_close(ws): #on close of the bot.
    print ("### closed ###")
    
def on_open(ws): #when the bot initially connects.
 print ("open")
 time.sleep(1)
 ws.send(mypesan)
 time.sleep(1)
 gblk = """
 Connected
 """
 print(gblk)
 time.sleep(1)

if __name__ == "__main__":
 
 websocket.enableTrace(True)
 ws = websocket.WebSocketApp("wss://id-heimdallr.spooncast.net/"+slink,                                           
                              on_message = on_message,
                              on_close = on_close)
ws.on_open = on_open
ws.run_forever()
