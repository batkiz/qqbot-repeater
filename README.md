# README

## about
本仓库中代码为仿[噗噗](https://www.robirt.me)的 QQ 机器人，基于 [qqbot](https://github.com/pandolia/qqbot)。

## 基本操作
基本操作大体如下：
输入 ping 可检验机器人是否在线并返回当前时间
输入 !add 触发词=回复 来调♂教复读机
输入 !list 关键词 来查看复读机对该词的所有回应
输入 !list 触发词=回复 来删除这条回复
输入 !help 查看该帮助

## 注意事项
[代码](./repeater.py)中 `file_name` 请改为环境下绝对路径。
由于基于 [qqbot](https://github.com/pandolia/qqbot)，因此 qqbot 中不支持的（图片、语音、XML 卡片消息等）本项目一概不支持。
