#coding=utf-8
#author:u'王健'
#Date: 13-3-4
#Time: 下午9:11
__author__ = u'王健'
import re
html='''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>哈哈.MX——分享所有好笑的事情</title>
        <meta property="qc:admins" content="204766324460101650" />
        <meta name="description" content="哈哈.MX，傲游冷笑话都在这里！冷笑哈，脑筋急转弯，暴汗趣事，经典语录，我们一起分享所有好笑的事情，每天“哈哈”的健康生活~" />
        <meta name="keywords" content="傲游浏览器,遨游冷笑话,傲游冷笑话,遨游,傲游,遨游浏览器,笑话,幽默,冷笑话,笑话网,语录" />
        <meta property="wb:webmaster" content="3fa4a0748acc4f18" />
        <link rel="shortcut icon" href="/favicon.ico" type="/Public/images/x-icon" />
                <link type="text/css" rel="stylesheet" href="http://static.haha.mx/css/page-good.css" />

        <script type="text/javascript">
            var openObj;
            document.domain = 'haha.mx';
            function logined() {
                $("#login").remove();
                location.reload();
            }
            function go_page() {
                var the_url = '/good/day/';

                window.location.href = the_url + $("#go_page").val();
            }
        </script>
    </head>

    <body>
        <!-- header -->
        <div class="header">

                        <div class="account">
                        <!-- 未登录-->
                                      嗨，请 <a href="###" class="highlight" id="btn-login">登录</a> 或<a href="###" class="highlight" id="btn-regist"> 注册</a>  微博登录：<a href="/oauth_api.php?o=sina" target="_blank" class="inline-block btn-bind" id="btn-login-sina"></a><a href="/oauth_api.php?o=qq" target="_blank" class="inline-block btn-bind qq" id="btn-login-qq"></a>

            <!-- //未登录-->
                    </div>


            <!-- top-->
            <div class="top clearfix">
                <h1 class="logo fl">
                    <a href="/"></a>
                </h1>
                <div class="clearfix">
                    <ul class="navigation fl" id="navigation">
                        <li data="good"
                                                        class="current"
                            >
                            <a href="/good" class="icon-dropdown">最哈</a>
                            <!--<ul class="nav-dropdown">
                                <li>
                                    <a href="###">24小时最哈</a>
                                </li>
                                <li>
                                    <a href="###">1周内</a>
                                </li>
                                <li>
                                    <a href="###">1月内</a>
                                </li>
                                <li>
                                    <a href="###">1年内</a>
                                </li>
                                <li>
                                    <a href="###">历史最哈</a>
                                </li>
                            </ul>-->
                        </li>
                        <li >
                            <a href="/new">最新</a>
                        </li>
                        <li data="hot"
                            >
                            <a href="/hot" class="icon-dropdown">热评</a>
                        </li>
                        <li >
                            <a href="/rank">哈友</a>
                        </li>
                        <li >
                            <a href="/pic">趣图</a>
                        </li>
                    </ul>
                    <a href="###" class="btn-primary fl mt-5" id="btn-talk">讲一个</a>
                    <form action="/front_api.php?r=search" method="post" id="search" name="search" class="search fr clearfix mt-5">
                        <input name="s" type="text" class="keywords fl" id="key" value="寻找你的哈哈" />
                        <button class="btn-search fr" type="submit"></button>
                    </form>
                </div>            </div>
            <!-- //top-->
        </div>
        <!-- //header -->


        <!-- container -->
        <div class="container">
            <!-- content -->
            <div id="content" class="content clearfix">
                <!-- content -->
                <div class="main fl">
                    <!-- broadcast-->
                    <div class="block broacast" id="broadcast"><ul><li><a href='http://www.haha.mx/pic' target='_blank'>看图乐哈哈，工作更高效~~~</a></li><li><a href='http://www.haha.mx/joke/760323' target='_blank'>每天看哈哈，生活美如花~~~</a></li><li><a href='http://www.haha.mx/joke/765828' target='_blank'>如果趣图某张图片重复出现~~</a></li><li><a href='http://www.haha.mx/activity/7' target='_blank'>总有一个哈哈，支撑你活到现在~~</a></li></ul></div>                    <!-- //broadcast-->

                    <!-- joke list -->

<div class="list joke">

            		        <a name='765560'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-765560" jid="765560" juid="7187693">
                                                                <p class="text word-wrap">陈光标在接受记者采访时称，计划生育政策应该修改，没有接受过九年义务教育的人不应该生孩子，读过高中的可以生一胎，高中以上学历的生育应该放开。同时，对于一些偏远地区应该特殊对待，保障基本生育权。</p>
                                                                                                <a href="###" data="cp" id="thumbnail-765560" class="thumbnail" path='2013/03/03/' pic_name='765560_8e26172588f2e894b964deda1a9cd1c0_1362317724.jpg'>
                                    <img src="http://image.haha.mx/2013/03/03/small/765560_8e26172588f2e894b964deda1a9cd1c0_1362317724.jpg"/>
                                    <!--<span class="pic-loading"></span>-->
                                </a>
                                <!--<div class="pic-box">
                                    <a class="btn-original" target="_blank" href="http://image.haha.mx/2012/12/10/big/671351_6dca88e6db6cffa2e97769a8957e67ee_1355148283.gif">查看原图</a>
                                    <div class="clear"></div>
                                    <a class="view-default-img"href="###">
                                        <img src="http://image.haha.mx/2012/12/10/middle/671333_246727707911ac1cf00e08af1f8df2b0_1355147713.gif"/>
                                    </a>
                                </div>-->
                                <div class="clear"></div>
                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl">
                                	                                                                                <a href='/label/11355'>趣图 </a>
                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/765560">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/7187693' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/7/187/7187693/1333551375.jpg"/>
                                        </a>
                                        <a href='/user/7187693'>旅行的蜗牛</a>
                                                                                <span> 2013-03-03 21:35:24 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">39</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-765560" data="b">353</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-765560" data="g">252</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='765819'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-765819" jid="765819" juid="16364934">
                                                                <p class="text word-wrap">像不像三分样</p>
                                                                                                <a href="###" data="cp" id="thumbnail-765819" class="thumbnail" path='2013/03/04/' pic_name='765819_64c20eee4bf1085f033555926c913b12_1362362010.gif'>
                                    <img src="http://image.haha.mx/2013/03/04/small/765819_64c20eee4bf1085f033555926c913b12_1362362010.gif"/>
                                    <!--<span class="pic-loading"></span>-->
                                </a>
                                <!--<div class="pic-box">
                                    <a class="btn-original" target="_blank" href="http://image.haha.mx/2012/12/10/big/671351_6dca88e6db6cffa2e97769a8957e67ee_1355148283.gif">查看原图</a>
                                    <div class="clear"></div>
                                    <a class="view-default-img"href="###">
                                        <img src="http://image.haha.mx/2012/12/10/middle/671333_246727707911ac1cf00e08af1f8df2b0_1355147713.gif"/>
                                    </a>
                                </div>-->
                                <div class="clear"></div>
                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl">
                                	                                                                                <a href='/label/11355'>趣图 </a>
                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/765819">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                    <a class="avatar24"><img class="avatar24" src="http://static.haha.mx/images/default.jpg"/></a> <a>匿名</a>
                                                                                <span> 2013-03-04 09:53:30 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">9</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-765819" data="b">4</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-765819" data="g">246</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='766138'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-766138" jid="766138" juid="9613515">
                                                                <p class="text word-wrap">为了大家的提高素质，美女我支持你</p>
                                                                                                <a href="###" data="cp" id="thumbnail-766138" class="thumbnail" path='2013/03/04/' pic_name='766138_c5fb7b56936ab91a839f44b5532486e4_1362369970.jpg'>
                                    <img src="http://image.haha.mx/2013/03/04/small/766138_c5fb7b56936ab91a839f44b5532486e4_1362369970.jpg"/>
                                    <!--<span class="pic-loading"></span>-->
                                </a>
                                <!--<div class="pic-box">
                                    <a class="btn-original" target="_blank" href="http://image.haha.mx/2012/12/10/big/671351_6dca88e6db6cffa2e97769a8957e67ee_1355148283.gif">查看原图</a>
                                    <div class="clear"></div>
                                    <a class="view-default-img"href="###">
                                        <img src="http://image.haha.mx/2012/12/10/middle/671333_246727707911ac1cf00e08af1f8df2b0_1355147713.gif"/>
                                    </a>
                                </div>-->
                                <div class="clear"></div>
                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl">
                                	                                                                                <a href='/label/11355'>趣图 </a>
                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/766138">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/9613515' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/9/613/9613515/1330046844.jpg"/>
                                        </a>
                                        <a href='/user/9613515'>金桥香烟</a>
                                                                                <span> 2013-03-04 12:06:10 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">7</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-766138" data="b">5</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-766138" data="g">245</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='765682'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-765682" jid="765682" juid="3398637">
                                                                <p class="text word-wrap"></p>
                                                                                                <a href="###" data="cp" id="thumbnail-765682" class="thumbnail" path='2013/03/03/' pic_name='765682_8f9f84b9858597e46dddf730b2ff678f_1362324373.jpg'>
                                    <img src="http://image.haha.mx/2013/03/03/small/765682_8f9f84b9858597e46dddf730b2ff678f_1362324373.jpg"/>
                                    <!--<span class="pic-loading"></span>-->
                                </a>
                                <!--<div class="pic-box">
                                    <a class="btn-original" target="_blank" href="http://image.haha.mx/2012/12/10/big/671351_6dca88e6db6cffa2e97769a8957e67ee_1355148283.gif">查看原图</a>
                                    <div class="clear"></div>
                                    <a class="view-default-img"href="###">
                                        <img src="http://image.haha.mx/2012/12/10/middle/671333_246727707911ac1cf00e08af1f8df2b0_1355147713.gif"/>
                                    </a>
                                </div>-->
                                <div class="clear"></div>
                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl">
                                	                                                                                <a href='/label/11355'>趣图 </a>
                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/765682">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                    <a class="avatar24"><img class="avatar24" src="http://static.haha.mx/images/default.jpg"/></a> <a>匿名</a>
                                                                                <span> 2013-03-03 23:26:13 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">6</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-765682" data="b">12</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-765682" data="g">225</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='766217'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-766217" jid="766217" juid="15573166">
                                                                <p class="text word-wrap">花果山坍塌。<br/>唐僧问：死了多少猴子？悟空：26个洞穴都淹了。<br/>唐僧：死了多少猴子？悟空：5000颗桃树被淹。<br/>唐僧：到底死了多少猴子啊？悟空：已经将活的猴子安全转移了。<br/>唐僧急了：你说清楚，到底死了多少猴子？ 悟空忙拭眼泪：16位领导正组织救援&hellip;</p>
                                                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl" style="display: none;">
                                	                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/766217">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/15573166' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/default.png"/>
                                        </a>
                                        <a href='/user/15573166'>栀开栀落</a>
                                                                                <span> 2013-03-04 12:46:01 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">2</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-766217" data="b">7</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-766217" data="g">226</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='765588'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-765588" jid="765588" juid="9613515">
                                                                <p class="text word-wrap">都是手快惹的祸啊</p>
                                                                                                <a href="###" data="cp" id="thumbnail-765588" class="thumbnail" path='2013/03/03/' pic_name='765588_1873f322fbdc6e5a992da38eae4d1325_1362318930.jpg'>
                                    <img src="http://image.haha.mx/2013/03/03/small/765588_1873f322fbdc6e5a992da38eae4d1325_1362318930.jpg"/>
                                    <!--<span class="pic-loading"></span>-->
                                </a>
                                <!--<div class="pic-box">
                                    <a class="btn-original" target="_blank" href="http://image.haha.mx/2012/12/10/big/671351_6dca88e6db6cffa2e97769a8957e67ee_1355148283.gif">查看原图</a>
                                    <div class="clear"></div>
                                    <a class="view-default-img"href="###">
                                        <img src="http://image.haha.mx/2012/12/10/middle/671333_246727707911ac1cf00e08af1f8df2b0_1355147713.gif"/>
                                    </a>
                                </div>-->
                                <div class="clear"></div>
                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl">
                                	                                                                                <a href='/label/11355'>趣图 </a>
                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/765588">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/9613515' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/9/613/9613515/1330046844.jpg"/>
                                        </a>
                                        <a href='/user/9613515'>金桥香烟</a>
                                                                                <span> 2013-03-03 21:55:30 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">7</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-765588" data="b">22</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-765588" data="g">223</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='766063'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-766063" jid="766063" juid="6508672">
                                                                <p class="text word-wrap">老图一张。求出处</p>
                                                                                                <a href="###" data="cp" id="thumbnail-766063" class="thumbnail" path='2013/03/04/' pic_name='766063_657abb489ed78a2ef7979754894261b0_1362367894.gif'>
                                    <img src="http://image.haha.mx/2013/03/04/small/766063_657abb489ed78a2ef7979754894261b0_1362367894.gif"/>
                                    <!--<span class="pic-loading"></span>-->
                                </a>
                                <!--<div class="pic-box">
                                    <a class="btn-original" target="_blank" href="http://image.haha.mx/2012/12/10/big/671351_6dca88e6db6cffa2e97769a8957e67ee_1355148283.gif">查看原图</a>
                                    <div class="clear"></div>
                                    <a class="view-default-img"href="###">
                                        <img src="http://image.haha.mx/2012/12/10/middle/671333_246727707911ac1cf00e08af1f8df2b0_1355147713.gif"/>
                                    </a>
                                </div>-->
                                <div class="clear"></div>
                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl">
                                	                                                                                <a href='/label/11355'>趣图 </a>
                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/766063">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/6508672' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/default.png"/>
                                        </a>
                                        <a href='/user/6508672'>stardanc</a>
                                                                                <span> 2013-03-04 11:31:34 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">4</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-766063" data="b">7</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-766063" data="g">205</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='766055'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-766055" jid="766055" juid="15538184">
                                                                <p class="text word-wrap">同样的一辈子。外出打工和在家乡混的区别！</p>
                                                                                                <a href="###" data="cp" id="thumbnail-766055" class="thumbnail" path='2013/03/04/' pic_name='766055_5628f226b7443b72bb65f9accf85bdc9_1362367697.jpg'>
                                    <img src="http://image.haha.mx/2013/03/04/small/766055_5628f226b7443b72bb65f9accf85bdc9_1362367697.jpg"/>
                                    <!--<span class="pic-loading"></span>-->
                                </a>
                                <!--<div class="pic-box">
                                    <a class="btn-original" target="_blank" href="http://image.haha.mx/2012/12/10/big/671351_6dca88e6db6cffa2e97769a8957e67ee_1355148283.gif">查看原图</a>
                                    <div class="clear"></div>
                                    <a class="view-default-img"href="###">
                                        <img src="http://image.haha.mx/2012/12/10/middle/671333_246727707911ac1cf00e08af1f8df2b0_1355147713.gif"/>
                                    </a>
                                </div>-->
                                <div class="clear"></div>
                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl">
                                	                                                                                <a href='/label/11355'>趣图 </a>
                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/766055">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/15538184' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/15/538/15538184/1352969047.jpg"/>
                                        </a>
                                        <a href='/user/15538184'>woaiaoyo</a>
                                                                                <span> 2013-03-04 11:28:17 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">11</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-766055" data="b">30</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-766055" data="g">203</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='766434'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-766434" jid="766434" juid="12065227">
                                                                <p class="text word-wrap">我暗恋我们公司一个小男生，才22岁，很帅。因为是新员工，上个月手机坏了，我把我以前不用的手机给他用，结果拿过去没到两个小时，充电冲爆了。跟我道歉了好几天。上个礼拜他电脑出问题了，把我笔记本拿去用，没到两个小时，把笔记本电源冲爆了。跟我道歉到现在。其实我想说，你把我拿去用吧，我想体验一下被冲爆的感觉。</p>
                                                                                                <a href="###" data="cp" id="thumbnail-766434" class="thumbnail" path='2013/03/04/' pic_name='766434_a14bfbbe80008ed86ae675dff26f35e7_1362380593.jpg'>
                                    <img src="http://image.haha.mx/2013/03/04/small/766434_a14bfbbe80008ed86ae675dff26f35e7_1362380593.jpg"/>
                                    <!--<span class="pic-loading"></span>-->
                                </a>
                                <!--<div class="pic-box">
                                    <a class="btn-original" target="_blank" href="http://image.haha.mx/2012/12/10/big/671351_6dca88e6db6cffa2e97769a8957e67ee_1355148283.gif">查看原图</a>
                                    <div class="clear"></div>
                                    <a class="view-default-img"href="###">
                                        <img src="http://image.haha.mx/2012/12/10/middle/671333_246727707911ac1cf00e08af1f8df2b0_1355147713.gif"/>
                                    </a>
                                </div>-->
                                <div class="clear"></div>
                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl">
                                	                                                                                <a href='/label/11355'>趣图 </a>
                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/766434">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/12065227' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/12/065/12065227/1327191509.png"/>
                                        </a>
                                        <a href='/user/12065227'>灬心碎而已</a>
                                                                                <span> 2013-03-04 15:03:13 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">10</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-766434" data="b">30</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-766434" data="g">201</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='765602'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-765602" jid="765602" juid="13679954">
                                                                <p class="text word-wrap">今个去肯德基买了个全虾堡，回来把中间的虾给我妈吃了。我弄的豆腐乳夹在中间把汉堡吃了，我妈说我是土鳖&hellip;&hellip;</p>
                                                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl" style="display: none;">
                                	                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/765602">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/13679954' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/13/679/13679954/1358402167.gif"/>
                                        </a>
                                        <a href='/user/13679954'>傲游管理员</a>
                                                                                <span> 2013-03-03 22:07:17 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">4</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-765602" data="b">12</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-765602" data="g">195</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='765989'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-765989" jid="765989" juid="10631133">
                                                                <p class="text word-wrap">地铁上一爷们儿指着电视的歌曲节目说：&ldquo;这老家伙的儿子都轮奸犯了还有脸出来唱歌&rdquo;，哎，我真是替蒋大为感到伤感&hellip;&hellip;</p>
                                                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl" style="display: none;">
                                	                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/765989">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                    <a class="avatar24"><img class="avatar24" src="http://static.haha.mx/images/default.jpg"/></a> <a>匿名</a>
                                                                                <span> 2013-03-04 11:02:35 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">2</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-765989" data="b">5</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-765989" data="g">187</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='765640'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-765640" jid="765640" juid="2725310">
                                                                <p class="text word-wrap">Hussein Chalayan 2013秋冬！一秒变装 好流弊~！<br/><br/>PS：好吧，总算来个惊艳不奇葩的。</p>
                                                                                                <a href="###" data="cp" id="thumbnail-765640" class="thumbnail" path='2013/03/03/' pic_name='765640_50360fe1da3b31b5abd1d1e6e5013958_1362322143.gif'>
                                    <img src="http://image.haha.mx/2013/03/03/small/765640_50360fe1da3b31b5abd1d1e6e5013958_1362322143.gif"/>
                                    <!--<span class="pic-loading"></span>-->
                                </a>
                                <!--<div class="pic-box">
                                    <a class="btn-original" target="_blank" href="http://image.haha.mx/2012/12/10/big/671351_6dca88e6db6cffa2e97769a8957e67ee_1355148283.gif">查看原图</a>
                                    <div class="clear"></div>
                                    <a class="view-default-img"href="###">
                                        <img src="http://image.haha.mx/2012/12/10/middle/671333_246727707911ac1cf00e08af1f8df2b0_1355147713.gif"/>
                                    </a>
                                </div>-->
                                <div class="clear"></div>
                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl">
                                	                                                                                <a href='/label/11355'>趣图 </a>
                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/765640">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/2725310' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/2/725/2725310/1263314805.gif"/>
                                        </a>
                                        <a href='/user/2725310'>恶魔的细语</a>
                                                                                <span> 2013-03-03 22:49:03 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">4</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-765640" data="b">10</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-765640" data="g">173</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='766041'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-766041" jid="766041" juid="15519393">
                                                                <p class="text word-wrap"></p>
                                                                                                <a href="###" data="cp" id="thumbnail-766041" class="thumbnail" path='2013/03/04/' pic_name='766041_0c996ce04f322ba4e888b41d54542e4f_1362367432.gif'>
                                    <img src="http://image.haha.mx/2013/03/04/small/766041_0c996ce04f322ba4e888b41d54542e4f_1362367432.gif"/>
                                    <!--<span class="pic-loading"></span>-->
                                </a>
                                <!--<div class="pic-box">
                                    <a class="btn-original" target="_blank" href="http://image.haha.mx/2012/12/10/big/671351_6dca88e6db6cffa2e97769a8957e67ee_1355148283.gif">查看原图</a>
                                    <div class="clear"></div>
                                    <a class="view-default-img"href="###">
                                        <img src="http://image.haha.mx/2012/12/10/middle/671333_246727707911ac1cf00e08af1f8df2b0_1355147713.gif"/>
                                    </a>
                                </div>-->
                                <div class="clear"></div>
                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl">
                                	                                                                                <a href='/label/11355'>趣图 </a>
                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/766041">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/15519393' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/default.png"/>
                                        </a>
                                        <a href='/user/15519393'>反对派阴谋论专家</a>
                                                                                <span> 2013-03-04 11:23:52 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">15</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-766041" data="b">8</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-766041" data="g">171</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='766119'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-766119" jid="766119" juid="4842348">
                                                                <p class="text word-wrap">比较下老婆和老妈,一比吓一跳<br />
 <br />
1、老婆总想知道自己和婆婆同时落水时，老公会先救哪个，老妈总是嘱咐儿子要与媳妇相亲相爱、百年好合。 <br />
2、老婆会在夜里起来偷偷摸摸老公鞋垫下藏没藏钱，老妈有时会在夜里起来摸摸儿子的鞋垫潮不潮。<br />
3、老婆是把老公累得生病的人，老妈是给儿子生命的人。<br />
4、老婆经常问老公的工资涨没涨，老妈经常问儿子的工作累不累。<br />
5、老婆想吃苹果会把刀子递给老公让他来削给她吃。老妈削个苹果会给儿子先吃，<br />
6、老婆将自己的后半生交给老公，说这是一场赌博，老妈将全部精力花在儿子身上，说这是尽一点母爱。<br />
7、老婆对出差的老公有无数的限令，老妈对出差的儿子有无尽的牵挂。<br />
8、老婆总想让老公把她的生日过得有声有色，老妈不想让儿子为自己过什么生日。<br />
9、老公是老婆的出气筒，老妈是儿子的避难所。<br />
10、老公是老婆的提款机，老妈是儿子的百宝箱。<br />
11、老公是老婆的铁板鱿鱼，老妈是儿子的开心农场...</p>
                                                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl" style="display: none;">
                                	                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/766119">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/4842348' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/default.png"/>
                                        </a>
                                        <a href='/user/4842348'>Rain4842</a>
                                                                                <span> 2013-03-04 11:53:19 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">9</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-766119" data="b">38</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-766119" data="g">162</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='765851'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-765851" jid="765851" juid="15310697">
                                                                <p class="text word-wrap">至今找不到总赞分在哪，发图都没劲。</p>
                                                                                                <a href="###" data="cp" id="thumbnail-765851" class="thumbnail" path='2013/03/04/' pic_name='765851_ce9ce01ef1a15f9d7096fa910c43e4a1_1362363463.gif'>
                                    <img src="http://image.haha.mx/2013/03/04/small/765851_ce9ce01ef1a15f9d7096fa910c43e4a1_1362363463.gif"/>
                                    <!--<span class="pic-loading"></span>-->
                                </a>
                                <!--<div class="pic-box">
                                    <a class="btn-original" target="_blank" href="http://image.haha.mx/2012/12/10/big/671351_6dca88e6db6cffa2e97769a8957e67ee_1355148283.gif">查看原图</a>
                                    <div class="clear"></div>
                                    <a class="view-default-img"href="###">
                                        <img src="http://image.haha.mx/2012/12/10/middle/671333_246727707911ac1cf00e08af1f8df2b0_1355147713.gif"/>
                                    </a>
                                </div>-->
                                <div class="clear"></div>
                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl">
                                	                                                                                <a href='/label/11355'>趣图 </a>
                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/765851">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/15310697' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/15/310/15310697/1361626407.jpg"/>
                                        </a>
                                        <a href='/user/15310697'>xiaorenw</a>
                                                                                <span> 2013-03-04 10:17:43 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">4</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-765851" data="b">15</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-765851" data="g">159</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='765958'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-765958" jid="765958" juid="7827360">
                                                                <p class="text word-wrap">儿子跟我商量：&ldquo;妈妈，春节期间咱家来客人时你别总说我，给我留点儿面子。&rdquo;<br/>我笑道：&ldquo;你也得表现好点儿。&rdquo;<br/>儿子说：&ldquo;我肯定特别乖。&rdquo;<br/>我问：&ldquo;那要有人问你成绩呢？&rdquo;<br/>儿子说：&ldquo;你就赶紧反问他年终奖，也让他哑口无言。&rdquo;</p>
                                                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl">
                                	                                                                                <a href='/label/62920'>哈由心生 </a>
                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/765958">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/7827360' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/7/827/7827360/1353319283.jpg"/>
                                        </a>
                                        <a href='/user/7827360'>语忱</a>
                                                                                <span> 2013-03-04 10:53:47 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">0</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-765958" data="b">6</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-765958" data="g">158</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='765766'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-765766" jid="765766" juid="12838118">
                                                                <p class="text word-wrap">以後我也不愛國了，不愛國的都移民出國享福去了，愛國的都留下來吃苦受累了，以後的歲月裏，千萬別給我機會賣國，我會毫不猶豫的。</p>
                                                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl" style="display: none;">
                                	                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/765766">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/12838118' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/sys/7.png"/>
                                        </a>
                                        <a href='/user/12838118'>南開主任</a>
                                                                                <span> 2013-03-04 09:03:50 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">8</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-765766" data="b">30</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-765766" data="g">153</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='766159'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-766159" jid="766159" juid="13679954">
                                                                <p class="text word-wrap">亲爱的嫂子，求你不要再把你哥介绍给我了好么？万一成了，到底是我喊你嫂子还是你喊我嫂子啊！</p>
                                                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl" style="display: none;">
                                	                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/766159">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/13679954' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/13/679/13679954/1358402167.gif"/>
                                        </a>
                                        <a href='/user/13679954'>傲游管理员</a>
                                                                                <span> 2013-03-04 12:21:03 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">2</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-766159" data="b">5</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-766159" data="g">145</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='766235'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-766235" jid="766235" juid="14020007">
                                                                <p class="text word-wrap">越南阮日慨大战直升飞机</p>
                                                                                                <a href="###" data="cp" id="thumbnail-766235" class="thumbnail" path='2013/03/04/' pic_name='766235_a01e71844ff41cb668ae377532b75d64_1362372909.jpg'>
                                    <img src="http://image.haha.mx/2013/03/04/small/766235_a01e71844ff41cb668ae377532b75d64_1362372909.jpg"/>
                                    <!--<span class="pic-loading"></span>-->
                                </a>
                                <!--<div class="pic-box">
                                    <a class="btn-original" target="_blank" href="http://image.haha.mx/2012/12/10/big/671351_6dca88e6db6cffa2e97769a8957e67ee_1355148283.gif">查看原图</a>
                                    <div class="clear"></div>
                                    <a class="view-default-img"href="###">
                                        <img src="http://image.haha.mx/2012/12/10/middle/671333_246727707911ac1cf00e08af1f8df2b0_1355147713.gif"/>
                                    </a>
                                </div>-->
                                <div class="clear"></div>
                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl">
                                	                                                                                <a href='/label/62920'>哈由心生 </a>
                                                                                <a href='/label/11355'>趣图 </a>
                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/766235">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/14020007' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/default.png"/>
                                        </a>
                                        <a href='/user/14020007'>airvalkk</a>
                                                                                <span> 2013-03-04 12:55:09 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">11</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-766235" data="b">10</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-766235" data="g">145</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                		        <a name='766465'></a>
                            <!-- 单条笑话-->
                            <div class="block joke-item" id="joke-766465" jid="766465" juid="12644417">
                                                                <p class="text word-wrap">我一老同学带着5岁的儿子买了一把高仿ak47,自己。从小缺爱，长大缺钙。那SB拿着枪自己不给儿子玩，自己怀念童年。路过农行的时候，刚好看到运钞车下来几个抬箱子的人。那二货拿起ak,对着运钞车蹦的一枪。现在二货同学还在医院抢救，腹部中弹，2个洞。绝对真事！</p>
                                                                                                <ul class="clearfix mt-15">
                                	                                	<li class="label fl">
                                	                                                                                <a href='/label/62920'>哈由心生 </a>
                                                                            </li>
                                    <li class="toolkit fr">
                                                                                                                    <!--
                                        --><a href="###" data="r">举报</a>|<!--
                                        --><a href="/joke/766465">查看全文</a>
                                    </li>
                                </ul>
                                <ul class="clearfix mt-15">
                                    <li class="info fl">
                                                                                <a href='/user/12644417' class="avatar24">
                                            <img src="http://images1.maxthon.cn/avatar/default.png"/>
                                        </a>
                                        <a href='/user/12644417'>xianglei</a>
                                                                                <span> 2013-03-04 15:23:48 发布</span>
                                    </li>
                                                                        <li class="fr">
                                        <a href="###" title="展开评论" class="fr btn-icon comment" data="c">4</a>
    									    										<a href="###" title="收藏" class="fr btn-icon fav" data="f|0"></a>
    									                                        <a href="###" title="鄙视" class="fr btn-icon bad " id="bad-766465" data="b">9</a>
                                        <a href="###" title="称赞" class="fr btn-icon good " id="good-766465" data="g">145</a>
                                    </li>
                                                                    </ul>
                            </div>
    						                            <!-- //单条笑话 -->
                                                </div>

<div class="pagination mt-15">


    <a href="/good/day/1"><</a>







    <a href="/good/day/1">1</a>






    <a href="/good/day/2" class="current">2</a>






    <a href="/good/day/3">3</a>






    <a href="/good/day/4">4</a>






    <a href="/good/day/5">5</a>





    ...





    <a href="/good/day/62">62</a>







    <a href="/good/day/3">></a>




    <span class="paging-jump">

    跳转<input id="go_page" type="text" class="number" value="" onkeydown="if(event.keyCode == 13){go_page();}"/>页

        <a href="###" onclick ="go_page()" id="btnGo" class="highlight btn-go">GO</a>

    </span>

</div>

                                        <!-- //joke list-->
                </div>
                <!-- //content -->

                <!-- sidebar -->
                <!-- sidebar -->
<div class="sidebar fr">
            <div class="article follow">
    <div class="clearfix pb-10">
        <h3 class="fl">关注收听</h3>
        <a href="###" class="fr highlight" id="btn-add-fav">加入收藏</a>
    </div>

    <ul>
        <li class="inline-block f-sina">
            <a href="http://weibo.com/hahamx" target="_blank">新浪微博</a>
        </li><!--
        --><li class="inline-block f-qq">
            <a href="http://t.qq.com/haha-mx" target="_blank">腾讯微博</a>
        </li><!--
        --><li class="inline-block f-rss">
            <a href="http://feed.feedsky.com/hahamx2" target="_blank">RSS订阅</a>
        </li><!--
        --><li class="inline-block f-feed">
            <a href="http://feed.feedsky.com/hahamx" target="_blank">Feed订阅</a>
        </li>
    </ul>
</div>        <div class="hezuo-google mt-20">
    <script type="text/javascript">
    google_ad_client = "ca-pub-2698861478625135";
    /* 哈哈300&#42;250 */
    google_ad_slot = "4460475721";
    google_alternate_ad_url = '/hezuo/o-300.htm';
    google_ad_width = 300;
    google_ad_height = 250;
    </script>
    <script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js"></script>
</div>
                            <div id="sticky" class="sticky-block">
            <!--<div class="hezuo-tao mt-20">
    <iframe id="hezuo-iframe" width="306" scrolling="no" height="256" frameborder="0" allowtransparency="no" src="/hezuo/t-300.htm"></iframe>
</div>-->

<div id="hezou-tao" class="hezuo-tao mt-20"></div>
<script src="/hezuo/rmif.js"></script>
<script>
var ad1 = SetupAdDiv(300, 250, "", "");
function RefreshAds() {
    ad1.adURL = "http://a.alimama.cn/inf.js";
    ad1.adPage = "/iframe.htm";
    LoadAds();
}
//document.write("<div class='Divider'></div>");
RefreshAds();
</script>            <dl class="article labels">
                        <dt class="clearfix"><h3 class="fl">热门标签</h3><a href="/tag" class="fr highlight">更多</a></dt>
                        <dd class="clearfix"><a href="/label/62920" class="strong">哈由心生</a><a href="/label/7045">世界末日</a><a href="/label/51671">鬼节</a><a href="/label/33286">IT男</a><a href="/label/17299" class="strong">萌物</a><a href="/label/46929">禅师理科生</a><a href="/label/3055">不是笑话</a><a href="/label/17314">搞笑图片</a><a href="/label/7">医生</a><a href="/label/13882">父亲节</a><a href="/label/639">哈哈</a><a href="/label/547">高考</a><a href="/label/13334">六一</a><a href="/label/11650">五道杠</a><a href="/label/906">内涵</a><a href="/label/722">相亲</a><a href="/label/915">haha</a><a href="/label/11355" class="em">趣图</a><a href="/label/704">笑话</a><a href="/label/602">女人</a><a href="/label/564">冷</a><a href="/label/400">冷笑话</a><a href="/label/378">QQ</a><a href="/label/346">美女</a><a href="/label/207">囧</a><a href="/label/9">老师</a></dd></dl>        </div>
    </div>
<!-- //sidebar -->                <!-- //sidebar -->
            </div>
            <!-- //content -->
        </div>
        <!-- //container -->

<!-- footer-->
    <div class="footer">
        <dl class="friendlinks">
            <dt></dt>
            <dd>
                <a href="http://www.2345.com" target="_blank">2345网址导航</a>|<!--
                --><a href="http://www.hao123.com" target="_blank">hao123网址之家</a>|<!--
                --><a href="http://www.tao123.com" target="_blank">淘网址</a>|<!--
                --><a href="http://www.1616.net" target="_blank">1616网址导航</a>|<!--
                --><a href="http://www.114la.com" target="_blank">114啦网址导航</a>|<!--
                --><a href="http://www.1122.com" target="_blank">1122网址导航</a>|<!--
                --><a href="http://www.46.com" target="_blank">46网址导航</a>|<!--
                --><a href="http://www.155.com" target="_blank">155导航</a>|<!--
                --><a href="http://hao.qq.com/" target="_blank">QQ导航</a>|<!--
                --><a href="http://hao.360.cn/" target="_blank">360安全网址导航</a>|<!--
                --><a href="http://yasuo.360.cn" target="_blank">360压缩软件</a>|<!--
                --><a href="http://fun.iqiyi.com/" target="_blank">爱奇艺搞笑视频</a>
            </dd>
        </dl>
        <div class="clearfix">
            <p class="fl">
                版权所有 © 1999-2013 北京傲游天下科技有限公司.  京ICP备08011055号 京公网安备 110108901521
            </p>
            <p class="fr">
                <a href="/about" >关于哈哈.mx</a> | <!--
                --><a href="/statement">免责声明</a> | <!--
                --><a target="_blank" href="http://bbs.maxthon.cn/forum.php?mod=viewthread&tid=745144&extra=page%3D1">反馈</a> | <!--
                --><a target="_blank" href="http://www.maxthon.cn/">傲游主站</a>
            </p>
        </div>
    </div>
    <!-- //footer-->
                <script type="text/javascript" src="http://static.haha.mx/js/lib/require.js" data-main="http://static.haha.mx/js/page-good"></script>
                <script type="text/javascript">
        function maxthonAccountBindHead() {
            if (openObj) {
                addLink('http://static.haha.mx/css/mod.ifrBind.css');
            }
            else {
                return false;
            }
        }
        function maxthonAccountBindSuccee(url) {
            window.location.href = url;
        }
    </script>
    </script>
    <span style="display:none">
    <script src=' http://w.cnzz.com/c.php?id=30035524' language='JavaScript' charset='gb2312'></script>

    </span>
    </body>
</html>


'''

hahaimg=re.findall('(?i)<a [^>]*id=\"thumbnail-(\d+)\"[^>]*>[^<]*?<img src=\"(.*?)\"[^>]*>',html)

for i,img in hahaimg:
    print i,img