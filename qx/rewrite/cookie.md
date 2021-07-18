## task订阅    
https://ghproxy.com/https://raw.githubusercontent.com/wuye999/task-rewrite/main/qx/task/AllinOne.json    

## cookie重写订阅
https://ghproxy.com/https://raw.githubusercontent.com/wuye999/task-rewrite/main/qx/task/AllinOne.json    

## v2p订阅 
https://ghproxy.com/https://raw.githubusercontent.com/wuye999/task-rewrite/main/v2p/task/sngxprov2p.json    

## 快手极速版
赞赏:作者快手邀请码`774010415`,农妇山泉 -> 有点咸，万分感谢;     
本脚本仅适用于快手双版本签到，仅支持正式版获取多Cookie，建议使用正式版获取Cookie，点击视频页悬浮红包，或者进入设置，点击"积分兑好礼"即可;     
本脚本仅在签到成功时通知;     


## 番茄看看前台

番茄看看跳转微信文章真实阅读（疑似鉴权文章不自动返回），云扫码直接倒计时虚假阅读（疑似鉴权文章会跳转微信文章真实阅读，会自动返回（多前台跑云扫码时，鉴权文章标识数据会覆盖，可导致非疑似鉴权的文章也进入文章页面进行真实阅读）    
注意：    
1、ios13、iOS4版本的系统使用qx自测可行，如果是ios12系统的qx用户，老实用单独重写搞定番茄看看和云扫码的真实阅读    

qx：    
[rewrite_local]    
^http://.+/yunonline/v1/task url script-response-body https://raw.githubusercontent.com/age174/-/main/fqkk_auto_read.js    
^http://.+/(reada/jump|v1/jump|task/read)\? url script-response-header https://raw.githubusercontent.com/age174/-/main/fqkk_auto_read.js    
^http://.+/mock/read url script-analyze-echo-response https://raw.githubusercontent.com/age174/-/main/fqkk_auto_read.js    
^https?://mp\.weixin\.qq\.com/s.+?k=feizao url response-body </script> response-body setTimeout(()=>window.history.back(),10000); </script>    

注意：如果微信文章不自动返回，自查是否为ios12的系统，可试试以下重写    
^https?://mp\.weixin\.qq\.com/s.+? url response-body </script> response-body setTimeout(()=>window.history.back(),10000); </script>    
[MITM]    
hostname = mp.weixin.qq.com    

## 百度极速版签到任务     
使用脚本有黑号严重，请谨慎使用‼️     
    
赞赏:作者百度极速邀请码`RW9ZSW 点击链接立得红包，最高100元！https://dwz.cn/Oilv4CJ1`,农妇山泉 -> 有点咸，万分感谢     
    
本脚本默认使用chavyleung大佬和Nobyda的贴吧ck，获取方法请看大佬仓库说明，内置自动提现，提现金额默认30元，当当前时间为早上6点且达到提现金额时仅运行提现任务，提现金额小于设置金额时继续运行其他任务。     
     
增加百度任务开关，Actions中Secrets为BAIDU_TASK，值填true或者false     
     
百度极速获取Cookie:点击"任务"即可      
     
https:\/\/haokan\.baidu\.com\/activity\/h5\/vault\?productid=\d url script-request-header https://raw.githubusercontent.com/Sunert/Scripts/master/Task/baidu_speed.js
         

## 聚看点签到任务
不支持Actions跑阅读任务，其他任务可运行
打开'我的'获取Cookie
可自动提现，提现需填写微信真实姓名，设置提现金额，默认30，此设置可以boxjs内完成，也可本地配置

## 中青阅读极速版，一天撸羊毛大概1.5-2元   

应用版本2.02        
https://github.com/wuye999/task-rewrite/tree/main/itunes           
爱思助手即可导入安装          

 1.重写引用：          
;到配置文件找到[rewrite_remote]贴代码：          

;签到cookie获取         
https://ghproxy.com/https://raw.githubusercontent.com/wuye999/task-rewrite/main/qx/rewrite/zqck.conf, tag=YouthCookie

阅读body获取            
https://ghproxy.com/https://raw.githubusercontent.com/wuye999/task-rewrite/main/qx/rewrite/zqbody.conf, tag=YouthGetBody, update-interval=86400, opt-parser=false, enabled=true

中青看看赚&浏览赚           
https://ghproxy.com/https://raw.githubusercontent.com/wuye999/task-rewrite/main/qx/rewrite/zqkkz.conf, tag=中青看看赚&浏览赚cookie


 2.食用方法：         
1.到[重写]-[引用],启动YouthCookie禁用YouthGetBody,先获取cookie            

签到cookie:         
进入app，进入任务中心或者签到一次          

阅读请求body&阅读时长:      
阅读一篇文章或者视频到获取金币奖励            

惊喜红包:          
在阅读文章拉下面有个惊喜红包，点击获取             

2.手动执行一次定时脚本-”中青看点极速版”,看签到是不是正常           

3.到[重写]-[引用],启动YouthGetBody禁用YouthCookie,获取文章body           

阅读请求body:阅读一篇文章或者视频到获取金币奖励,通知提示body1

4.手动执行一次定时脚本-”中青阅读”,是不是运行正常

5.获取更多的body,一天一般上限7200金币,建议获取200个body      
5.9 启用中青看看赚&浏览赚cookie，关闭YouthGetBody    

6. 浏览赚：任务中心-》看看赚-》顶部的浏览赚-》点任务开始抓到任务数据包即可，所有任务都要点    

7. 看看赚：任务中心-》看看赚-》点看看赚任务抓到任务数据包即可，所有任务都要点    
8. 任务中心尝试添加看看赚入口
9. 已有阅读时长数据时，只保存大于1分钟的时长数据

## 较全的库
https://github.com/SallyU/fuidvsfjkd/tree/master/app_gift

## OK语音
10W分兑换100K币,可提现
每日任务具体多少没算,反正都是挂着脚本,10w分可兑换100K币
打开任务界面抓包 auth
提现必须人脸实名,玩不玩随意阿。
export okAuth=""
export oksource ="android" //或ios
也可以邀请人 ,A邀请B,A得三块,B邀请C,B得三块,(一个号一次),都发红包转给A然后凑100提现


## 腾讯自选股
BOXJS：https://raw.githubusercontent.com/CenBoMin/GithubSync/main/cenbomin.box.json    
运行脚本前请先下载app,登录。。。手动完成成长任务,有钱    
8.8打卡任务也手动做,建议只打卡4个成功即可,第5个基本拿不到    
微信小程序-腾讯自选股和app的日常任务是分开的,毛比较少,手动做吧！    
食用方法    
到[重写]-[引用],加入重写引用,根据以下提示获取cookie    
重写引用    
IOS APP：https://raw.githubusercontent.com/CenBoMin/GithubSync/main/TXSTOCK/txs_cookie.conf    
微信小程序：https://raw.githubusercontent.com/CenBoMin/GithubSync/main/TXSTOCK/txs_wxcookie.conf    
**** IOS APP ****    
taskheader：打开app-立即获取    
taskkey：点击左上头像-我的福利-点击获取    
userheader：点击左上头像-进入即获取    
userkey：点击左上头像-进入即获取    

提现cookie(cashheader):禁用获取cookie重写,重新打开app,点击左上头像-进入,等待我的福利下面活动加载成功,启用获取cookie重写,然后再点击第一个猜涨跌活动的页面就能够获取到了。。。    

签到cookie(signheader)：禁用获取cookie重写,重新打开app,点击左上头像-进入,等待右上角的金币数加载成功（进入提现页面）,启用获取cookie重写,点击进入提现的页面,会卡住加载几秒...过一会就能够获取到了    

signkey：禁用获取cookie重写,重新打开app,点击左上头像-进入,等待我的福利下面活动加载成功,启用获取cookie重写,然后再点击第一个猜涨跌活动的页面就能够获取到了。。。    
**** 微信小程序 ****    
！！！！！微信和app重写有冲突,不能两个同时开    
！！！！！必须先关闭app重写,在加入微信小程序重写https://raw.githubusercontent.com/CenBoMin/GithubSync/main/TXSTOCK/txs_wxcookie.conf,启用之后就可以去微信小程序做任务获取cookie     

微信任务cookie(wxtaskkey):进入微信小程序,点击资讯页面或者股票页面获取    

！！！！！获取完cookie,务必关闭重写引用    
脚本一天尽量运行1-3次,本脚本虽然加了防呆机制,但是还是尽量避免运行多次哦...    
且用且珍惜,更新无限期。    

手动做部分:    
 模拟炒股周赛奖励：星期天登录模拟炒股(微信/app)    
 周一抢牛活动：周一登录抢牛活动页面（app）    

## 软件名：拼拼猪 （iOS/安卓都有）别充钱就行了 
注册地址：必须要微信扫码，然后授权微信登入 
  获取CK ： 打开软件 → 养猪场 → 喂养  
   每天1元 秒到！ 秒到支付宝！ 不需要实名！！！！支付宝多的上才艺吧 
每个账号好像可以提现6次  

## 软件名：开心点点消（安卓）      微信授权登入
亲测 我提了两个0.3+0.5  目前提现还是秒到的  上车前问一下还能不能玩 
获取CK ： 打开软件 → 转盘抽奖 → 看一次视频即可   
下载地址更改为蓝奏云https://wwr.lanzoui.com/itpS4qej5va
密码:977p

## 软件名：乐享广告（安卓）      微信、支付宝授权
每天看15个广告，0.02币一个广告，根据得到的乐币进行分红
下载地址：https://www.teq0gh.cn/register?pid=16421
食用方法：需要下载小黄鸟(工具自行百度) ⇨ 设置 ⇨ 其它选项 ⇨ 安装平行空间(某些手机可能需要额外安装64位补丁) ⇨ 打开平行空间 ⇨ 添加乐享广告 ⇨ 登入绑定微信/支付宝
需要获取两条数据
一 ：登入 ⇨ 平台任务
二 ：平台任务 ⇨ 任意一个任务 ⇨ 等待10s点左下角 领取即可


## 软件名：炎兔
下载地址：https://github.com/xl2101200/-/blob/main/tom/yt.png   需要邀请码：1085099
填写身份证及上传微信（支付宝）收款码即可
每天签到得到20兔钻，1兔钻=0.3元   兔钻可直接卖！兔钻石越多分红越多，提现秒到
食用方法：注册好后使用微信登入  签到一次获取ck   
v2p好像不能直接获取ck  解决方法：使用锤子抓一下签到的包，然后挂v2p的代理，重放一次获取ck即可！

## 软件名：魔力消消乐（安卓）      微信授权登入  
ps：黑号的话用一键新机获取ck
下载地址：https://wwr.lanzoui.com/ilu7Mr7cqfc  密码:5ig8
获取CK ： 打开软件 → 转盘抽奖 → 看一次视频即可    

## 小程序：玩物志好物商店 网页:https://coolbuy.com
task: https://raw.githubusercontent.com/Wenmoux/monster/main/coolbuy/coolbuy.js    
需要的参数    
只能node跑   
```
{    
    "type": "wx或者web 小程序就是wx",    
    "authorization": "只有小程序才需要这个",    
    "cookie": "这里面是你的cookie"    
}  
```    
填完之后去这里压缩并转义 https://m.sojson.com/yasuoyihang.html 结果如下     
export coolBuyStr='{"type":"wx或者web 小程序就是wx","authorization":"只有小程序才需要这个","cookie":"这里面是你的cookie"}'       
签到一个月要么抽奖换6.66微信红包,要么兑换100-50券或者一个手机壳       

    
## 10s阅读
微信打开立即参与 -> http://h5.qzsjfc.xyz/j/h?upuid=136513&ch=xmy&type=1
备用链接 -> http://h5.saibangkaile.xyz/j/h?upuid=136513&ch=xmy&type=1
每小时有0.3 一天5轮 一天1.5
进不去关注10秒读书极速版公众号用官方链接
使用方法:点击开始阅读 成功阅读一次即可抓到包
脚本没写过盾的
每次运行都要手动验证一次(也就是一天5次)
点立即阅读,等文章出来后关闭页面(注意 千万不要返回)
拉一人头提现0.3奖励0.5 0.8再奖励0.5
https://t.me/wenmou_car

## 葱花视频
【任务中心请求】：首页-右下角-点击现金红包-弹出任务中心

【视频奖励请求】：看视频到获取金币奖励,通知提示“添加🥦阅读请求，当前共有X个”,获取50个body请求左右

【时段奖励请求】：每天领金币任务,倒计时结束之后,点击"领取"

【分享请求】：首页任一个视频,点击视频右下角微信分享,跳转微信等待下,通知提示
!备注：没有跳转,换别的视频试试...警告必须只获取2-3个即可,超出根据提示重新获取）

【分享奖励请求】：分享过后,回到app跳出红包,点击分享任务-领取

【助力奖励请求】：随便分享一个视频到微信（建议发到文件传输助手）,成功之后点击加载视频,观看并且等待通知弹出助力奖励通知

【提现奖励请求】：账户金额满5元,打开重写提现5元...弹出提现请求。


## 今日头条极速版
#右上角签到即可获取签到cookie
#进一次农场即可获取农场cookie
#读文章弹出金币获取读文章cookie

## 抖音火山版
#看一个视频弹出金币获取ck

## 抖音极速版
#签到获取signheader and signcookie（已签到获取不到应该）
#走路修改步数，提前之前需要重新获取ck，不然提交失败，进一次任务界面就可
#看一个视频弹出金币获取readheader and readkey

## 书旗
1.一般版本,请添加重写获取cookie：https://raw.githubusercontent.com/CenBoMin/GithubSync/main/SHUQI/cookie.conf    

✅【一键收取】:登录App-点击下方中间【福利】- 有气泡可以收取，点击招财猫中间图标【做任务赚金币】,即可获取成功     
✅【一般-签到打卡】:登录App-点击下方中间【福利】- 点击【每日签到】 - 立即签到,即可获取成功     
⭐️【一般-阅读金币】:登录App-点击下方中间【福利】- 点击【30秒计时奖励】 - 找一本书点进去 -往右滑动看书 - 右上角会出现一个圈圈 -持续看书到获取金币,即可获取成功     
✅【一般-看视频金币】:登录App-点击下方中间【福利】- 点击【看视频领金币】- 看完一篇视频广告,即可获取成功     
⭐️【一般-邀请书友】:登录App-点击下方中间【福利】- 点击【邀请书友】,分享到微信朋友圈 - 分享完成返回app,如果提示网路错误或者没有获取到，就继续分享朋友圈返回，大约三次奖励成功就可以获取到了     

2.极速版本,请添加重写获取cookie：https://raw.githubusercontent.com/CenBoMin/GithubSync/main/SHUQI/spcookie.conf     

✅【极速-签到打卡】:登录App-点击下方中间【福利】-点击右侧图标【每日签到】- 立即签到,即可获取成功      
✅【极速-阅读小说金币】:登录App-点击下方中间【福利】-点击左侧图标【赚金币】- 点击【30秒计时奖励】 - 找一本书点进去 -往右滑动看书 - 右上角会出现一个圈圈 -持续看书到获取金币,即可获取成功      
⭐️【极速-看视频金币】:登录App-点击下方中间【福利】-点击左侧图标【赚金币】-点击【看视频领金币】- 看完一篇视频广告,即可获取成功     
✅【极速-邀请书友】:登录App-点击下方中间【福利】-点击左侧图标【赚金币】-点击【邀请书友】,分享到微信朋友圈 - 分享完成返回app,即可获取成功     

3.一般版本-福利转转转，极速版本-浏览书城，极速版本-签到页面看视频,请添加重写获取cookie：        
https://ghproxy.com/https://raw.githubusercontent.com/wuye999/task-rewrite/main/qx/rewrite/SqLottery.conf     
✅【一般-转盘机会】:登录App-点击下方中间【福利】-点击左侧图标【福利转转转】-点击下方【看视频抽奖】- 看完一篇视频广告,即可获取成功       
⭐️【一般-转盘抽奖】:登录App-点击下方中间【福利】-点击左侧图标【福利转转转】-点击下方【金币抽奖】- 即可获取成功,如果，没有获取到，多试几次就可以    
✅【极速-浏览书城15秒】:登录App-点击下方中间【福利】-点击左侧【赚金币】-点击【浏览书城】-右下角有计时-滑动或者停止会倒数计时,直到归零获取奖励,即可获取成功     

4.极速版-刷时长，请添加重写获取cookie：https://raw.githubusercontent.com/CenBoMin/GithubSync/main/SHUQI/everday.conf     
✅【极速-获取阅读时长】:登录App - 找一本书点进去 -往右滑动看书 - 右上角会出现一个圈圈 -持续看书至少6圈，保证看书三分钟，点击中间，左上角退出,即可获取成功      
⭐️【极速-签到页面看视频】:登录App-点击下方中间【福利】-点击右侧图标【每日签到】，如果签到完成会弹出看【视频拿金币】，看完一篇视频广告,即可获取成功    

## 悬赏喵喵
使用方法:
打开悬赏喵喵小程序，获得悬赏喵喵的数据，


## 芝嫲视频
点击夺宝获取body


## 朗果英语
打开朗果英语，首页右上角点击红包获得数据

## 西梅
打开西梅，首页推荐下拉刷新获得数据


## 生活圈
使用方法:首页找到评论有奖,点进去即获取数据成功

## 招招试药
进入招招，点击我的，点击每日任务，获得数据。

## 百事乐元
扫码进入主页授权即可获取数据
二维码地址 : https://ae01.alicdn.com/kf/Ud69446ceaf974ebfbdbc642d1f21b201q.jpg

## 幸福养鸡场
进入游戏点击领饲料获得数据。
十分钟一次吧。cron自己改。

## 考状元娶老婆
两个游戏的抓包都是一样的，进入游戏玩一关领取金币就可以获取数据了，记得绑定一下微信，后面应该会加入自动提现。所以别忘记绑定微信。否则无法自动提现

## 特仑苏
进入微信小程序特仑苏》我的奖品 获取·

## 富豪小镇
进入app获取

## 开心大丰收
进入app获取

## 笑谱Ariszy
天天领现金-每日签到领现金-点击随便一个任务，获取ck

## 京东金融领豆
进入app获取

## 先下载芒果TV登录
然后浏览器打开地址即可跳芒果APP即可获取数据
签到三天得汽水
https://h5.mgtv.com/2021/h5/60a608f6726e3f50c2942730/?inv=d75f73f2de2b47b2bd913a02510fa7f8&tc=FzJN9gmzJgCu#/


## 云云赚呗A
搜索公众号：云云赚呗A    邀请码：26716  感谢大佬们填写
关注后⇨领取会员卡⇨即可获取ck  可多号撸！

## 青椒音乐
安卓小黄鸟抓包


## 软件名：赚多多
下载地址：读书少找不到邀请连接，自己百度下载！
设置好代理打开软件，点击赚钱即可获取ck


## 软件名：草根时代
下载地址：  读书少找不到邀请连接，自己百度下载！
每天看视频领低保1.2元稳如老狗，一天1200+积分，5000=5元！提现需要完成一次高佣任务或试玩，建议选择微信点赞任务
不秒到，审核需要一天


## 软件名：红包多多    
看一次视频获取CK 
 一机一号！！！
抓包后运行脚本，脚本运行结束后在打开APP提现！



















































