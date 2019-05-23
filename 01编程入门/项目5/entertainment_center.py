#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import media
import fresh_tomatoes
"""creat instances of class Movie"""
hacksaw_ridge = media.Movie(
    "Hacksaw Ridge",
    "根据真实故事改编,以二战时期的冲绳岛战役为背景,讲述基于良知而拒绝持枪上阵的医疗"
    "兵戴斯蒙德·道斯,赤手空拳闯入枪""林弹雨，只身勇救75名战友生命的故事。",
    "http://img5.mtime.cn/mg/2016/11/21/080819.24024286_270X405X4.jpg",  # NOQA
    "https://www.youtube.com/watch?v=s2-1hz1juBI")
Finding_Mr_Right = media.Movie(
     "Finding Mr Right",
     "拜金小三文佳佳怀孕后到美国待产，在这里遇到了月子公司的司机兼护工Frank。文佳佳"
     "的情人在国内出事停了她的信用卡，Frank也正处在离婚危机中。两个失意的人开始慢慢"
     "走近，并最终在帝""国大厦的顶楼定情",
     "http://img31.mtime.cn/mt/2013/02/22/090814.53002276_270X405X4.jpg",  # NOQA
     "https://www.youtube.com/watch?v=CiwmN_2rIT0")
Operation_Red_Sea = media.Movie(
    "Operation Red Sea",
    "索马里海域外，中国商船遭遇劫持，船员全数沦为阶下囚。蛟龙突击队沉着应对，潜入商"
    "船进行突袭，成功解救全部人质。返航途中，非洲北部伊维亚共和国发生政变，恐怖组织"
    "连同叛军攻入首都， 当地华侨面临危险，海军战舰接到上级命令改变",
    "http://img5.mtime.cn/mg/2018/02/17/150051.13993864_270X405X4.jpg",  # NOQA
    "https://www.youtube.com/watch?v=7sOD1Qc0O4M")
n21_Karat = media.Movie(
    "n21 Karat",
    "刘佳音（迪丽热巴 饰）因与富豪男友分手而破产。为了还债，变卖了自己所有的奢侈品。"
    "王继伟（郭京飞""饰）天生爱省，为了省钱无所不用其极。两人因为一场剧场意外相遇，"
    "在一系列机缘巧合下合租在一个屋檐""之下，过起了荒诞爆笑的流浪生活",
    "http://img5.mtime.cn/mg/2018/04/19/171516.84934680_270X405X4.jpg",  # NOQA
    "https://www.youtube.com/watch?v=qZllDNWe2LU")
Annihilation = media.Movie(
    "Annihilation",
    "电影讲述一位女生物学家(娜塔莉·波特曼饰)为调查丈夫的失踪，参加了神秘组织"
    "Southern Reach组织的科学考察。5名女性组队，去研究美国领土内一块被检疫隔离"
    "的生态灾害区域“X地区”。她们发现那里是原生态的荒野，隐藏着神秘的黑暗力量",
    "http://img5.mtime.cn/mg/2018/04/09/120115.76163000_270X405X4.jpg",  # NOQA
    "https://www.youtube.com/watch?v=89OP78l9oF0")
Hindi_Medium = media.Movie(
    "Hindi Medium",
    "一对印度的中产阶级夫妇：服装店老板拉吉（伊尔凡·可汗饰）与太太米塔"
    "（萨巴·卡玛尔饰）为了""让女儿皮娅（蒂希塔·塞加尔饰）接受更好的教育想尽了"
    "各种办法。而当他们费劲心思终于要将女儿送进名校时，事情却又发生了意想不到的变化",
    "http://img5.mtime.cn/mg/2018/03/30/214336.52153599_270X405X4.jpg",  # NOQA
    "https://www.youtube.com/watch?v=GjkFr48jk68")

"""creat a movie object list which contain six instances"""
movie_list = [hacksaw_ridge, Finding_Mr_Right, Operation_Red_Sea,
              n21_Karat, Annihilation, Hindi_Medium]
"""call the function of open_movies_page from fresh_tomatoes.py file
   which make the list of movies  as input and output the HTML file"""
fresh_tomatoes.open_movies_page(movie_list)
