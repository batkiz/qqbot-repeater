# -*- coding: utf-8 -*-
import time
import re
import random
import json

file_name = r'~\.qqbot-tmp\plugins\custom.json'
'''关键词 key-value 数据存放文件'''

with open(file_name) as file_obj:
    custom = json.loads(file_obj.read())


def CommandAdd(bot, contact, member, content, custom):
    '''添加 key-val'''
    key = ''
    val = ''
    count = content.find('=')
    key = content[5:count]
    val = content[count + 1:]
    if key not in custom:
        custom[key] = []
    custom[key].append(val)
    bot.SendTo(contact, "你说" + key + "，我说" + val)


def CommandDel(bot, contact, member, content, custom):
    '''删除'''
    count = content.find('=')
    key = content[5:count]
    val = content[count + 1:]
    if key in custom:
        custom[key].remove(val)
    bot.SendTo(contact, "已删除 " + key + "=" + val, resendOn1202=True)


def CommandList(bot, contact, member, content, custom):
    d = content[6:]
    ResList = ""
    for val in custom[d]:
        ResList += (val + '\n')
    bot.SendTo(contact, ResList, resendOn1202=False)


def onQQMessage(bot, contact, member, content):
    if bot.isMe(contact, member):
        pass
    else:
        if content == '!help':
            bot.SendTo(contact, "输入 !add 触发词=回复 来调♂教复读机\n"
                                + "输入 !list 关键词 来查看复读机对该词的所有回应\n"
                                + "输入 !list 触发词=回复 来删除这条回复\n"
                                + "输入 !help 查看该帮助")
        """
        if random.randint(0, 6) == 1:
            bot.SendTo(contact, content, resendOn1202=False)
        """
        '''1/6 的几率复读'''
        if 'ping' in content:
            bot.SendTo(contact, "pong！现在是 " +
                       time.strftime("%H:%M", time.localtime()))
        """
        if '@ME' in content:
            bot.SendTo(contact, member.name+'艾特我干嘛呢')
        """
        if re.match(r'!add*=*', content):
            CommandAdd(bot, contact, member, content, custom)
        elif re.match(r'!list *', content):
            CommandList(bot, contact, member, content, custom)
        elif re.match(r'!del *', content):
            CommandDel(bot, contact, member, content, custom)
        else:
            for item in custom:
                if item in content:
                    bot.SendTo(contact, random.choice(
                        custom[item]), resendOn1202=False)
                    break
            '''从字典中随机选取一个回复'''

        with open(file_name, 'w') as file_obj:
            json.dump(custom, file_obj)
    time.sleep(1)
    '''设置 cd 时间为 1s'''
