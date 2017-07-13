import re, time, json, hashlib, base64, asyncio
import logging; logging.basicConfig(level=logging.INFO)
import markdown2, orm

from aiohttp import web

from coroweb import get, post
from apis import APIValueError, APIResourceNotFoundError

from models import User, Comment, Blog, next_id
from config import configs

loop = asyncio.get_event_loop()

'''
 #插入
async def insert():
     await orm.create_pool(loop,user='root', password='password', db='awesome')
     uid = next_id()
    sha1_passwd = '%s:%s' % (uid, passwd)
    user = User(id=uid, name=name.strip(), email=email, passwd=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest(), image='http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email.encode('utf-8')).hexdigest())

     await u.save()

     r = await User.findAll()
     print(r)

#删除
async def remove():
    await orm.create_pool(loop, user='root', password='password', db='awesome')
    r = await User.find('001492757565916ec72f6eeb731405ab07ee37911a3ae79000')
    await r.remove()
    print('remove',r)
    await orm.destory_pool()
'''
#更新
async def update():
    await orm.create_pool(loop, user='root', password='password', db='awesome')
    rs = await User.findAll('email=?', 'admin@admin.com')
    r=rs[0]
    sha1 = hashlib.sha1()
    sha1.update(r.id.encode('utf-8'))
    sha1.update(b':')
    sha1.update('admin@admin'.encode('utf-8'))
    sha1.update(b':')
    sha1.update('072916'.encode('utf-8'))
    r.passwd = sha1.hexdigest()
    print(sha1.hexdigest())
    await r.update()
    print('update',r)
    await orm.destory_pool()


#async def find():
#    all = await User.findAll()
#    print(all)
#    pk = await User.find('00149276202953187d8d3176f894f1fa82d9caa7d36775a000')
#    print(pk)
#    num = await User.findNumber('email')
#    print(num)
#    await orm.destory_pool()

loop.run_until_complete(update())
loop.close()