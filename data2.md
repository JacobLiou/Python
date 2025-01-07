## 点位列说明
| 序号 | 列字母标识 | 列名称 | 备注说明 |
| --- | --- | --- | --- |
| 1 | A | 块说明 | 解析时忽略本列数据 |
| 2 | B | 寄存器地址 | 点位Modbus数据存储地址，十六进制值表示，分3类：\n1.单寄存器格式，例如：“0404”，表示0x0404寄存器地址；\n2.多寄存器格式，例如：“0427 -- 0428”，表示从0x0427,0x0428两个连续的寄存器地址；\n3.标题说明，例如：“二、实时数据区”，纯文本数据，无HEX格式字符，解析时忽略本行数据； |
| 3 | C | 字段 | 解析时忽略本列数据 |
| 4 | D | 区域说明 | 解析时忽略本列数据 |
| 5 | E | 类型 | 存储地址的数据类型，注意包括以下几类：\n1）I16 表示有符文16位数据；\n2）U16 表示无符合16位数据；\n3）I32 表示有符合32位数据；\n4）U32 表示无符号32位数据；\n3）I64 表示有符合64位数据；\n4）U64 表示无符号64位数据；\n5）ASCII 表示可视ASCII码字符；\n6）BCD16 表示16比特值的BCD码； |
| 6 | F | 精度 | 存储数据的精度值 |
| 7 | G | 单位 | 存储数据代表数据所使用的单位符合，若未填充数据则表示无单位 |
| 8 | H | 最小值 | 解析时忽略本列数据 |
| 9 | I | 最大值 | 解析时忽略本列数据 |
| 10 | J | 读写属性 | 存储寄存器地址的操作属性，主要包括以下几类：\n1）R 表示只读属性；\n2）W 表示只写属性；\n3）RW 表示可读可写属性；\n4）WV 表示可写易变属性；\n5）RWV 表示可读可写且易变属性； |
| 11 | K | 说明 | 寄存器存储内容的简要说明,解析时忽略本列数据 |
| 12 | L | 机密等级 | 解析时忽略本列数据 |
| 13 | M | 备注 | 解析时忽略本列数据 |

## 点位信息表
| 块说明 | 寄存器地址 | 字段 | 区域说明 | 类型 | 精度 | 单位 | 最小值 | 最大值 | 读写属性 | 说明 | 机密等级 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NaN | 二、实时数据区 | (0x0400-0x07FF) | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 2.1系统信息 | (0x0400-0x047F) | 运行状态，故障信息表，并网等待时间，温度值，系统和发电时间，机器序列号，状态信息，软件版本信息等 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 0400 -- 0403 | AddressMask\_Realtime\_SysInfo1 | NaN | U64 | NaN | NaN | NaN | NaN | R | 本地址开始的64个寄存器地址字的掩码区。\n参看地址0x0040的说明 | 终端用户 | NaN |
| 运行状态 | 0404 | SysState | NaN | U16 | NaN | NaN | NaN | NaN | R | 运行状态。\n0：等待状态\n1：检测状态\n2：并网状态\n3：应急供电状态\n4：可恢复故障状态\n5：永久性故障状态\n6：升级状态\n7：自充电状态\n8：SVG状态\n9：PID状态\n10：限载状态 | 终端用户 | 逆变器的运行状态，3、6-9的状态区分机型\n例：0x0004表示逆变器处于可恢复故障状态 |
| 故障信息表\n2-1 | 0405 | Fault1 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息表1\n记录逆变器的故障信息，还有扩展的19-30地址在0x0432-043D | 终端用户 | 对应故障信息查看此表格的另外一张工作表“故障位域说明”\n例：从0x0405读取值为0x0002表示逆变器有电网欠压的故障 |
| NaN | 0406 | Fault2 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息2 | 终端用户 | NaN |
| NaN | 0407 | Fault3 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息3 | 终端用户 | NaN |
| NaN | 0408 | Fault4 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息4 | 终端用户 | NaN |
| NaN | 0409 | Fault5 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息5 | 终端用户 | NaN |
| NaN | 040A | Fault6 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息6 | 终端用户 | NaN |
| NaN | 040B | Fault7 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息7 | 终端用户 | NaN |
| NaN | 040C | Fault8 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息8 | 终端用户 | NaN |
| NaN | 040D | Fault9 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息9 | 终端用户 | NaN |
| NaN | 040E | Fault10 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息10 | 终端用户 | NaN |
| NaN | 040F | Fault11 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息11 | 终端用户 | NaN |
| NaN | 0410 | Fault12 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息12 | 终端用户 | NaN |
| NaN | 0411 | Fault13 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息13 | 终端用户 | NaN |
| NaN | 0412 | Fault14 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息14 | 终端用户 | NaN |
| NaN | 0413 | Fault15 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息15 | 终端用户 | NaN |
| NaN | 0414 | Fault16 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息16 | 终端用户 | NaN |
| NaN | 0415 | Fault17 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息17 | 终端用户 | NaN |
| NaN | 0416 | Fault18 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息18 | 终端用户 | NaN |
| 并网等待时间 | 0417 | Countdown | NaN | U16 | 1 | 秒 | NaN | NaN | R | 并网等待时间(开机倒计时) | 终端用户 | 并网等待时间，可供查看的开机倒计时\n例：0x003C指开机时间为60秒 |
| 温度 | 0418 | Temperature\_Env1 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 环境温度1 | 终端用户 | 例：0x0001指环境温度1为1℃ |
| NaN | 0419 | Temperature\_Env2 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 环境温度2 | 终端用户 | NaN |
| NaN | 041A | Temperature\_HeatSink1 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 散热器温度1 | 终端用户 | 是否具备此功能与机型相关，可根据掩码查看是否使用对应寄存器\n案例请查看0x0418地址说明 |
| NaN | 041B | Temperature\_HeatSink2 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 散热器温度2 | 终端用户 | NaN |
| NaN | 041C | Temperature\_HeatSink3 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 散热器温度3 | 终端用户 | NaN |
| NaN | 041D | Temperature\_HeatSink4 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 散热器温度4 | 终端用户 | NaN |
| NaN | 041E | Temperature\_HeatSink5 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 散热器温度5 | 终端用户 | NaN |
| NaN | 041F | Temperature\_HeatSink6 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 散热器温度6 | 终端用户 | NaN |
| NaN | 0420 | Temperature\_Inv1 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 模块温度1 | 终端用户 | NaN |
| NaN | 0421 | Temperature\_Inv2 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 模块温度2 | 终端用户 | NaN |
| NaN | 0422 | Temperature\_Inv3 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 模块温度3 | 终端用户 | NaN |
| NaN | 0423 | Temperature\_Inv4 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 模块温度4 | 终端用户 | NaN |
| NaN | 0424 | Temperature\_Inv5 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 模块温度5 | 终端用户 | NaN |
| NaN | 0425 | Temperature\_Inv6 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 模块温度6 | 终端用户 | NaN |
| 发电、运行时间 | 0426 | GenerationTime\_Today | NaN | U16 | 1 | 分钟 | NaN | NaN | R | 当日发电时间 | 终端用户 | 逆变器今日的发电时间，并网后开始计时\n例：0x0001指当日发电1分钟 |
| NaN | 0427 -- 0428 | GenerationTime\_Total | NaN | U32 | 1 | 分钟 | NaN | NaN | R | 总发电时间 | 终端用户 | 逆变器并网后开始计时，占用两个寄存器，例：0x0000 0x087E指总发电时间为2174分钟 |
| NaN | 0429 -- 042A | ServiceTime\_Total | NaN | U32 | 1 | 分钟 | NaN | NaN | R | 总运行时间 | 终端用户 | 逆变器上电开始计时，占用两个寄存器，例：0x0000 0x09C5指总运行时间为2501分钟 |
| 绝缘阻抗 | 042B | InsulationResistance | NaN | U16 | 1 | kΩ | NaN | NaN | R | 绝缘阻抗 | 终端用户 | 绝缘阻抗大小，逆变器在检测状态检测 |
| 系统时间\n2-1 | 042C | SysTime\_Year | NaN | U16 | NaN | NaN | NaN | NaN | R | 系统时间-年 | 终端用户 | 实际年份用2000年加上读出来的数据\n例：0x0016指2022年 |
| NaN | 042D | SysTime\_Month | NaN | U16 | NaN | NaN | NaN | NaN | R | 系统时间-月 | 终端用户 | 例：0x0005指5月 |
| NaN | 042E | SysTime\_Date | NaN | U16 | NaN | NaN | NaN | NaN | R | 系统时间-日 | 终端用户 | 例：0x000F指15日 |
| NaN | 042F | SysTime\_Hour | NaN | U16 | NaN | NaN | NaN | NaN | R | 系统时间-时 | 终端用户 | 例：0x0010指16时 |
| NaN | 0430 | SysTime\_Minute | NaN | U16 | NaN | NaN | NaN | NaN | R | 系统时间-分 | 终端用户 | 例：0x0020指32分 |
| NaN | 0431 | SysTime\_Second | NaN | U16 | NaN | NaN | NaN | NaN | R | 系统时间-秒 | 终端用户 | 例：0x0030指48秒 |
| 故障信息表\n2-2 | 0432 | Fault19 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息19\n记录逆变器的故障信息，前18个在0x0418地址 | 终端用户 | 对应故障信息查看此表格的另外一张工作表“故障位域说明”，案例请查看0x0405地址备注 |
| NaN | 0433 | Fault20 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息20 | 终端用户 | NaN |
| NaN | 0434 | Fault21 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息21 | 终端用户 | NaN |
| NaN | 0435 | Fault22 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息22 | 终端用户 | NaN |
| NaN | 0436 | Fault23 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息23 | 终端用户 | NaN |
| NaN | 0437 | Fault24 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息24 | 终端用户 | NaN |
| NaN | 0438 | Fault25 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息25 | 终端用户 | NaN |
| NaN | 0439 | Fault26 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息26 | 终端用户 | NaN |
| NaN | 043A | Fault27 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息27 | 终端用户 | NaN |
| NaN | 043B | Fault28 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息28 | 终端用户 | NaN |
| NaN | 043C | Fault29 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息29 | 终端用户 | NaN |
| NaN | 043D | Fault30 | NaN | U16 | NaN | NaN | NaN | NaN | R | 故障信息30 | 终端用户 | NaN |
| 风扇转速 | 043E | SpeedFan | NaN | U16 | NaN | r/min | NaN | NaN | R | 风扇转速 | 终端用户 | NaN |
| NaN | 043F | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 预留 | NaN | 与地址0x1070定义是否冲突？ |
| NaN | 0440 -- 0443 | AddressMask\_Realtime\_SysInfo2 | NaN | U64 | NaN | NaN | NaN | NaN | R | 本地址开始的64个寄存器地址字的掩码区。\n参看地址0x0040的说明 | 终端用户 | NaN |
| NaN | 0444 | Production\_Code | NaN | U16 | NaN | NaN | NaN | NaN | NaN | 预留 | NaN | NaN |
| 机器序列号\n2-1 | 0445 -- 044C | Serial\_Number0 -- 7 | NaN | ASCII | NaN | NaN | NaN | NaN | R | 机器序列号Serial\_Number0-7（8个，表示序列号第1-16位），第17-20位在寄存器地址0x0470和0x0471 | 终端用户 | 解析需要查看DCC的条码规则定义文档\nSerial\_Number0是序列号第1、2位，其他依次类推，\n寄存器高8位存放序列号第1位；\n寄存器低8位存放序列号第2位。\n例：0x5353指"SS" |
| 硬件版本号 | 044D -- 044E | Hardware\_Version0 -- 1 | NaN | ASCII | NaN | NaN | NaN | NaN | R | 硬件版本号0-2（2个，4个ASCII位） | 终端用户 | 地址0x044D表示第1、2位。依次类推。\n寄存器高8位存放序列号第1位；\n寄存器低8位存放序列号第2位。\n例：0x5630指"V0",0x3033指"03"，实测：V003 |
| 通讯芯片\n软件版本号 | 044F | Software\_Version\_Stage\_COM | NaN | ASCII | NaN | NaN | NaN | NaN | R | 通讯芯片软件版本号阶段定义位。\n寄存器低8位存放ASCII码。正式版本的默认值为'V'。\n | 终端用户 | 地址0x044F有'V'、'G'、'I'等版本，均为正式版\n0G100003即表示通讯芯片软件版本号为G100003\n例1：地址0x044F读取的0x3047表示"0G"\n例2：地址0x0450读取的0x3130表示"10"\n例3：地址0x0451读取的0x3030表示"00" |
| NaN | 0450 | Software\_Version\_Major\_COM | NaN | ASCII | NaN | NaN | NaN | NaN | R | 通讯芯片软件主版本号。\n同一个系统中所有芯片主版本号必须一致，否则视为系统故障。\n寄存器高8位存放高位数字；\n寄存器低8位存放低位数字。 | 终端用户 | NaN |
| NaN | 0451 | Software\_Version\_Custom\_COM | NaN | ASCII | NaN | NaN | NaN | NaN | R | 通讯芯片软件非标定制版本号。\n正标软件此版本号为"00"。同一个系统中所有芯片非标定制版本号必须一致，否则视为系统故障。\n寄存器高8位存放高位数字；\n寄存器低8位存放低位数字。 | 终端用户 | NaN |
| NaN | 0452 | Software\_Version\_Minor\_COM | NaN | ASCII | NaN | NaN | NaN | NaN | R | 通讯芯片软件子版本号。\n寄存器高8位存放高位数字；\n寄存器低8位存放低位数字。\n例：0x3033指"03" | 终端用户 | NaN |
| 主控制器芯片\n软件版本号 | 0453 | Software\_Version\_Stage\_Master | NaN | ASCII | NaN | NaN | NaN | NaN | R | 主控制器芯片软件版本号阶段定义位。\n寄存器低8位存放ASCII码。正式版本的默认值为'V'。\n寄存器高8位存放高位数字；\n寄存器低8位存放低位数字。 | 终端用户 | 地址0x0453可能有其他字符\n案例分析请查看通讯芯片软件版本号说明\n0V100002即表示主控制器芯片软件版本号为V100002 |
| NaN | 0454 | Software\_Version\_Major\_Master | NaN | ASCII | NaN | NaN | NaN | NaN | R | 主控制器芯片软件主版本号。\n同一个系统中所有芯片主版本号必须一致，否则视为系统故障。\n寄存器高8位存放高位数字；\n寄存器低8位存放低位数字。 | 终端用户 | NaN |
| NaN | 0455 | Software\_Version\_Custom\_Master | NaN | ASCII | NaN | NaN | NaN | NaN | R | 主控制器芯片软件非标定制版本号。\n正标软件此版本号为"00"。同一个系统中所有芯片非标定制版本号必须一致，否则视为系统故障。\n寄存器高8位存放高位数字；\n寄存器低8位存放低位数字。 | 终端用户 | NaN |
| NaN | 0456 | Software\_Version\_Minor\_Master | NaN | ASCII | NaN | NaN | NaN | NaN | R | 主控制器芯片软件子版本号。\n寄存器高8位存放高位数字；\n寄存器低8位存放低位数字。 | 终端用户 | NaN |
| 副控制器芯片\n软件版本号 | 0457 | Software\_Version\_Stage\_Slave | NaN | ASCII | NaN | NaN | NaN | NaN | R | 副控制器芯片软件版本号阶段定义位。\n寄存器低8位存放ASCII码。正式版本的默认值为'V'。\n寄存器高8位存放高位数字；\n寄存器低8位存放低位数字。 | 终端用户 | 地址0x0457可能有其他字符\n案例分析请查看通讯芯片软件版本号说明\n0L100000即表示副控制器芯片软件版本号为L100000 |
| NaN | 0458 | Software\_Version\_Major\_Slave | NaN | ASCII | NaN | NaN | NaN | NaN | R | 副控制器芯片软件主版本号。\n同一个系统中所有芯片主版本号必须一致，否则视为系统故障。\n寄存器高8位存放高位数字；\n寄存器低8位存放低位数字。 | 终端用户 | NaN |
| NaN | 0459 | Software\_Version\_Custom\_Slave | NaN | ASCII | NaN | NaN | NaN | NaN | R | 副控制器芯片软件非标定制版本号。\n正标软件此版本号为"00"。同一个系统中所有芯片非标定制版本号必须一致，否则视为系统故障。\n寄存器高8位存放高位数字；\n寄存器低8位存放低位数字。 | 终端用户 | NaN |
| NaN | 045A | Software\_Version\_Minor\_Slave | NaN | ASCII | NaN | NaN | NaN | NaN | R | 副控制器芯片软件子版本号。\n寄存器高8位存放高位数字；\n寄存器低8位存放低位数字。 | 终端用户 | NaN |
| 安规库\n版本号 | 045B | Safety\_Version\_Major | NaN | ASCII | NaN | NaN | NaN | NaN | R | 安规库主版本号\n例：0x3036指06主版本 | 终端用户 | NaN |
| NaN | 045C | Safety\_version\_Minor | NaN | ASCII | NaN | NaN | NaN | NaN | R | 安规库子版本号\n例：0x3038指08子版本 | 终端用户 | NaN |
| BOOT版本号 | 045D | Boot\_Version\_COM | NaN | U16 | NaN | NaN | NaN | NaN | R | 通讯板的BOOT版本号 | 终端用户 | NaN |
| NaN | 045E | Boot\_Version\_Master | NaN | U16 | NaN | NaN | NaN | NaN | R | 主DSP的BOOT版本号 | 终端用户 | NaN |
| NaN | 045F | Boot\_Version\_Slave | NaN | U16 | NaN | NaN | NaN | NaN | R | 副DSP的BOOT版本号 | 终端用户 | NaN |
| 安规认证\n相关版本号 | 0460 | Safety\_Firmware\_Version\_Stage | NaN | ASCII | NaN | NaN | NaN | NaN | R | 安规认证软件版本号阶段定义位。\n寄存器低8位存放ASCII码。正式版本的默认值为'V'。\n寄存器高8位存放高位数字；\n寄存器低8位存放低位数字。 | 终端用户 | 案例分析请查看通讯芯片软件版本号说明\n0V000001即表示安规软件认证版本号为V000001 |
| NaN | 0461 | Safety\_Firmware\_Version\_Major | NaN | ASCII | NaN | NaN | NaN | NaN | R | 安规认证软件主版本号。\n同一个系统中所有芯片主版本号必须一致，否则视为系统故障。\n寄存器高8位存放高位数字；\n寄存器低8位存放低位数字。 | 终端用户 | NaN |
| NaN | 0462 | Safety\_Firmware\_Version\_Custom | NaN | ASCII | NaN | NaN | NaN | NaN | R | 安规认证软件非标定制版本号。\n正标软件此版本号为"00"。同一个系统中所有芯片非标定制版本号必须一致，否则视为系统故障。\n寄存器高8位存放高位数字；\n寄存器低8位存放低位数字。 | 终端用户 | NaN |
| NaN | 0463 | Safety\_Firmware\_Version\_Minor | NaN | ASCII | NaN | NaN | NaN | NaN | R | 安规认证软件子版本号。\n寄存器高8位存放高位数字；\n寄存器低8位存放低位数字。 | 终端用户 | NaN |
| NaN | 0464 | Safety\_Hardware\_Version0 | NaN | ASCII | NaN | NaN | NaN | NaN | R | 安规认证硬件版本号第1、2位。\n寄存器高8位存放序列号第1位；\n寄存器低8位存放序列号第2位。 | 终端用户 | 案例分析请查看硬件版本号说明\n实测：安规硬件认证版本号为V201 |
| NaN | 0465 | Safety\_Hardware\_Version1 | NaN | ASCII | NaN | NaN | NaN | NaN | R | 安规认证硬件版本号第3、4位。\n寄存器高8位存放序列号第3位；\n寄存器低8位存放序列号第4位。 | 终端用户 | NaN |
| AFCI版本号 | 0466 | Afci\_Ver\_Firmware | NaN | ASCII | NaN | NaN | NaN | NaN | R | afci固件版本号'V'。\n高8位保留；\n低8位存放版本号。 | NaN | 案例分析请查看通讯芯片软件版本号说明\n请对照ASCII码翻译查看 |
| NaN | 0467 | Afci\_Ver\_Sft | NaN | ASCII | NaN | NaN | NaN | NaN | R | afci软件版本。\n高8位存放第1位；\n低8位存放第2位。 | NaN | NaN |
| NaN | 0468 | Afci\_Ver\_Hard | NaN | ASCII | NaN | NaN | NaN | NaN | R | afci硬件版本\n高8位存放第1位；\n低8位存放第2位。 | NaN | NaN |
| NaN | 0469 | Afci\_Srs\_Hard | NaN | ASCII | NaN | NaN | NaN | NaN | R | afci硬件序列号。\n高8位存放第1位；\n低8位存放第2位。 | NaN | NaN |
| NaN | 046A | Afci\_Ver\_Com | NaN | ASCII | NaN | NaN | NaN | NaN | R | afci通信版本。\n高8位存放第1位；\n低8位存放第2位。 | NaN | NaN |
| 安规文件包\n版本号 | 046B | Safety\_Package\_Version0 | NaN | ASCII | NaN | NaN | NaN | NaN | R | 安规文件包版本号第1、2位。\n寄存器高8位存放序列号第1位；\n寄存器低8位存放序列号第2位。 | NaN | \n案例分析请查看通讯芯片软件版本号说明请对照ASCII码翻译查看 |
| NaN | 046C | Safety\_Package\_Version1 | NaN | ASCII | NaN | NaN | NaN | NaN | R | 安规文件包版本号第3、4位。\n寄存器高8位存放序列号第3位；\n寄存器低8位存放序列号第4位。 | NaN | NaN |
| NaN | 046D -- 046F | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 预留 | NaN | NaN |
| 机器序列号\n2-2 | 0470 -- 0471 | Serial\_Number8 -- 9 | NaN | ASCII | NaN | NaN | NaN | NaN | R | 机器序列号Serial\_Number8-9。\n表示第17-20位，第1-16位在寄存器地址0x0445\n | 终端用户 | 序列号第15-20位在20位序列号使用，14位序列号不使用\n寄存器0x0470高8位存放序列号第17位；\n寄存器0x0470低8位存放序列号第18位。 |
| NaN | 0472 -- 0476 | Serial\_Number11\_Rsvd0 -- 4 | NaN | ASCII | NaN | NaN | NaN | NaN | R | 预留0-4（5个） | NaN | NaN |
| 状态信息表 | 0477 | State1 | NaN | U16 | NaN | NaN | NaN | NaN | R | 状态信息1 | 终端用户 | 对应状态信息查看此表格的另外一张工作表“状态信息表” |
| NaN | 0478 | State2 | NaN | U16 | NaN | NaN | NaN | NaN | R | 状态信息2 | 终端用户 | NaN |
| NaN | 0479 | State3 | NaN | U16 | NaN | NaN | NaN | NaN | R | 状态信息3 | 终端用户 | NaN |
| NaN | 047A | State4 | NaN | U16 | NaN | NaN | NaN | NaN | R | 状态信息4 | 终端用户 | NaN |
| NaN | 047B | State5 | NaN | U16 | NaN | NaN | NaN | NaN | R | 状态信息5 | 终端用户 | NaN |
| NaN | 047C | State6 | NaN | U16 | NaN | NaN | NaN | NaN | R | 状态信息6 | 终端用户 | NaN |
| NaN | 047D | State7 | NaN | U16 | NaN | NaN | NaN | NaN | R | 状态信息7 | 终端用户 | NaN |
| NaN | 047E | State8 | NaN | U16 | NaN | NaN | NaN | NaN | R | 状态信息8 | 终端用户 | NaN |
| NaN | 047F | State9 | NaN | U16 | NaN | NaN | NaN | NaN | R | 状态信息9 | 终端用户 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 2.2并网输出 | (0x0480-0x04FF) | 并网运行的实时采集数据 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 0480 -- 0483 | AddressMask\_Realtime\_GridOutput1 | NaN | U64 | NaN | NaN | NaN | NaN | R | 本地址开始的64个寄存器地址字的掩码区。\n参看地址0x0040的说明 | 终端用户 | NaN |
| 电网频率 | 0484 | Frequency\_Grid | NaN | U16 | 0.01 | Hz | NaN | NaN | R | 电网频率。 | 终端用户 | 例：0x138B表示50.03Hz |
| 功率数据 | 0485 | ActivePower\_Output\_Total | NaN | I16 | 0.01/0.1 | kW | NaN | NaN | R | 总有功功率。\n功率达到320kW或以上机型，有功功率精度为0.1，320kW以下的机型，精度为0.01（例如：320KTLX0-HV机型精度使用0.1） | 终端用户 | 逆变器的输出功率，放电为正，充电为负\n例：0x006A表示1.06KW（功率小于320KW机型）\n例：0x006A表示10.6KW（功率大于等于320KW机型） |
| NaN | 0486 | ReactivePower\_Output\_Total | NaN | I16 | 0.01 | kVar | NaN | NaN | R | 总无功功率。 | 终端用户 | 用来在设备中建立和维持磁场的电功率，逆变器端超前为正，滞后为负 |
| NaN | 0487 | ApparentPower\_Output\_Total | NaN | I16 | 0.01/0.1 | kVA | NaN | NaN | R | 总视在功率。\n功率达到320KW或以上机型，视在功率精度为0.1，320kW以下的机型，精度为0.01（例如：320KTLX0-HV机型精度使用0.1） | 终端用户 | 逆变器当前电压电流的最大有功功率，放电为正，充电为负 |
| NaN | 0488 | ActivePower\_PCC\_Total | NaN | I16 | 0.01/0.1 | kW | NaN | NaN | R | 总PCC有功功率。\n功率达到320KW或以上机型，有功功率精度为0.1，320kW以下的机型，精度为0.01（例如：320KTLX0-HV机型精度使用0.1） | 终端用户 | 能流图电网功率的读取地址，部分机型需要接电表才有数据，卖电为正，买电为负 |
| NaN | 0489 | ReactivePower\_PCC\_Total | NaN | I16 | 0.01 | kVar | NaN | NaN | R | 总PCC无功功率。 | 终端用户 | 逆变器端超前为正，滞后为负 |
| NaN | 048A | ApparentPower\_PCC\_Total | NaN | I16 | 0.01/0.1 | kVA | NaN | NaN | R | 总PCC视在功率。\n功率达到320KW或以上机型，视在功率精度为0.1，320kW以下的机型，精度为0.01（例如：320KTLX0-HV机型精度使用0.1） | 终端用户 | 卖电为正，买电为负 |
| NaN | 048B | ActivePower\_PCC\_Total2 | NaN | I16 | 0.1 | kW | NaN | NaN | R | 总PCC有功功率2。\n1.与0488地址区别是精度不同\n2.0488地址数据溢出，则使用本地址 | 终端用户 | NaN |
| NaN | 048C | GridOutput\_Rsvd1 | NaN | NaN | NaN | NaN | NaN | NaN | R | 并网输出预留1 | 终端用户 | NaN |
| R相并网\n实时数据 | 048D | Voltage\_Phase\_R | NaN | U16 | 0.1 | V | NaN | NaN | R | R相电网电压 | 终端用户 | 例：0x093E表示236.6V |
| NaN | 048E | Current\_Output\_R | NaN | U16 | 0.01 | A | NaN | NaN | R | R相逆变器输出电流 | 终端用户 | 例：0x0049表示0.73A |
| NaN | 048F | ActivePower\_Output\_R | NaN | I16 | 0.01 | kW | NaN | NaN | R | R相逆变器输出有功功率。 | 终端用户 | 放电为正，充电为负 |
| NaN | 0490 | ReactivePower\_Output\_R | NaN | I16 | 0.01 | kVar | NaN | NaN | R | R相逆变器输出无功功率。 | 终端用户 | 逆变器端超前为正，滞后为负 |
| NaN | 0491 | PowerFactor\_Output\_R | NaN | I16 | 0.001 | p.u. | NaN | NaN | R | R相功率因数。 | 终端用户 | 逆变器端超前为正，滞后为负 |
| NaN | 0492 | Current\_PCC\_R | NaN | U16 | 0.01 | A | NaN | NaN | R | R相PCC电流。 | 终端用户 | 部分机型需要接电表才有数据 |
| NaN | 0493 | ActivePower\_PCC\_R | NaN | I16 | 0.01 | kW | NaN | NaN | R | R相PCC有功功率 | 终端用户 | 逆变器端超前为正，滞后为负 |
| NaN | 0494 | ReactivePower\_PCC\_R | NaN | I16 | 0.01 | kVar | NaN | NaN | R | R相PCC无功功率。 | 终端用户 | NaN |
| NaN | 0495 | PowerFactor\_PCC\_R | NaN | I16 | 0.001 | p.u. | NaN | NaN | R | R相PCC功率因数。 | 终端用户 | 逆变器端超前为正，滞后为负 |
| NaN | 0496 -- 0497 | R\_Rsvd1 -- 2 | NaN | NaN | NaN | NaN | NaN | NaN | R | R相预留1-2 | 终端用户 | NaN |
| S相并网\n实时数据 | 0498 | Voltage\_Phase\_S | NaN | U16 | 0.1 | V | NaN | NaN | R | S相电网电压 | 终端用户 | 参考上面R相的相关说明 |
| NaN | 0499 | Current\_Output\_S | NaN | U16 | 0.01 | A | NaN | NaN | R | S相逆变器输出电流 | 终端用户 | NaN |
| NaN | 049A | ActivePower\_Output\_S | NaN | I16 | 0.01 | kW | NaN | NaN | R | S相逆变器输出有功功率。 | 终端用户 | NaN |
| NaN | 049B | ReactivePower\_Output\_S | NaN | I16 | 0.01 | kVar | NaN | NaN | R | S相逆变器输出无功功率。 | 终端用户 | NaN |
| NaN | 049C | PowerFactor\_Output\_S | NaN | I16 | 0.001 | p.u. | NaN | NaN | R | S相功率因数。 | 终端用户 | NaN |
| NaN | 049D | Current\_PCC\_S | NaN | U16 | 0.01 | A | NaN | NaN | R | S相PCC电流 | 终端用户 | NaN |
| NaN | 049E | ActivePower\_PCC\_S | NaN | I16 | 0.01 | kW | NaN | NaN | R | S相PCC有功功率。 | 终端用户 | NaN |
| NaN | 049F | ReactivePower\_PCC\_S | NaN | I16 | 0.01 | kVar | NaN | NaN | R | S相PCC无功功率。 | 终端用户 | NaN |
| NaN | 04A0 | PowerFactor\_PCC\_S | NaN | I16 | 0.001 | p.u. | NaN | NaN | R | S相PCC功率因数。 | 终端用户 | NaN |
| NaN | 04A1 -- 04A2 | S\_Rsvd1 -- 2 | NaN | NaN | NaN | NaN | NaN | NaN | R | S相预留1-2 | 终端用户 | NaN |
| T相并网\n实时数据 | 04A3 | Voltage\_Phase\_T | NaN | U16 | 0.1 | V | NaN | NaN | R | T相电网电压 | 终端用户 | 参考上面R相的相关说明 |
| NaN | 04A4 | Current\_Output\_T | NaN | U16 | 0.01 | A | NaN | NaN | R | T相逆变器输出电流 | 终端用户 | NaN |
| NaN | 04A5 | ActivePower\_Output\_T | NaN | I16 | 0.01 | kW | NaN | NaN | R | T相逆变器输出有功功率。 | 终端用户 | NaN |
| NaN | 04A6 | ReactivePower\_Output\_T | NaN | I16 | 0.01 | kVar | NaN | NaN | R | T相逆变器输出无功功率。 | 终端用户 | NaN |
| NaN | 04A7 | PowerFactor\_Output\_T | NaN | I16 | 0.001 | p.u. | NaN | NaN | R | T相功率因数。 | 终端用户 | NaN |
| NaN | 04A8 | Current\_PCC\_T | NaN | U16 | 0.01 | A | NaN | NaN | R | T相PCC电流。 | 终端用户 | NaN |
| NaN | 04A9 | ActivePower\_PCC\_T | NaN | I16 | 0.01 | kW | NaN | NaN | R | T相PCC有功功率。 | 终端用户 | NaN |
| NaN | 04AA | ReactivePower\_PCC\_T | NaN | I16 | 0.01 | \nkVar | NaN | NaN | R | T相PCC无功功率。 | 终端用户 | NaN |
| NaN | 04AB | PowerFactor\_PCC\_T | NaN | I16 | 0.001 | p.u. | NaN | NaN | R | T相PCC功率因数。 | 终端用户 | NaN |
| NaN | 04AC -- 04AD | T\_Rsvd1 -- 2 | NaN | NaN | NaN | NaN | NaN | NaN | R | T相预留1-2 | 终端用户 | NaN |
| 其他并网\n实时数据 | 04AE | ActivePower\_PV\_Ext | NaN | U16 | 0.01 | kW | NaN | NaN | R | 外部发电功率 | 终端用户 | 读出来的数乘精度即为最终数据 |
| NaN | 04AF | ActivePower\_Load\_Sys | NaN | U16 | 0.01 | kW | NaN | NaN | R | 系统总负载功率 | 终端用户 | 需要接负载，能流图负载功率的读取地址 |
| NaN | 04B0 | Voltage\_Phase\_L1N | NaN | U16 | 0.1 | V | NaN | NaN | R | 电网L1对N电压有效值 | 终端用户 | NaN |
| NaN | 04B1 | Current\_Output\_L1N | NaN | U16 | 0.01 | A | NaN | NaN | R | L1输出电流有效值 | 终端用户 | NaN |
| NaN | 04B2 | ActivePower\_Output\_L1N | NaN | I16 | 0.01 | kW | NaN | NaN | R | L1线上输出有功功率 | 终端用户 | NaN |
| NaN | 04B3 | Current\_PCC\_L1N | NaN | U16 | 0.01 | A | NaN | NaN | R | L1线上CT电流有效值 | 终端用户 | NaN |
| NaN | 04B4 | ActivePower\_PCC\_L1N | NaN | I16 | 0.01 | kW | NaN | NaN | R | L1线上PCC有功功率 | 终端用户 | NaN |
| NaN | 04B5 | Voltage\_Phase\_L2N | NaN | U16 | 0.1 | V | NaN | NaN | R | 电网L2对N电压有效值 | 终端用户 | NaN |
| NaN | 04B6 | Current\_Output\_L2N | NaN | U16 | 0.01 | A | NaN | NaN | R | L2输出电流有效值 | 终端用户 | NaN |
| NaN | 04B7 | ActivePower\_Output\_L2N | NaN | I16 | 0.01 | kW | NaN | NaN | R | L2线上输出有功功率 | 终端用户 | NaN |
| NaN | 04B8 | Current\_PCC\_L2N | NaN | U16 | 0.01 | A | NaN | NaN | R | L2线上CT电流有效值 | 终端用户 | NaN |
| NaN | 04B9 | ActivePower\_PCC\_L2N | NaN | I16 | 0.01 | kW | NaN | NaN | R | L2线上PCC有功功率 | 终端用户 | NaN |
| NaN | 04BA | Voltage\_Line\_L1 | NaN | U16 | 0.1 | V | NaN | NaN | R | L1线电压：R/S相之间的电压 | 终端用户 | 三相机型才有此功能,例：0x1014表示411.6V |
| NaN | 04BB | Voltage\_Line\_L2 | NaN | U16 | 0.1 | V | NaN | NaN | R | L2线电压：S/T相之间的电压 | 终端用户 | 参考L1线电压 |
| NaN | 04BC | Voltage\_Line\_L3 | NaN | U16 | 0.1 | V | NaN | NaN | R | L3线电压：T/R相之间的电压 | 终端用户 | NaN |
| NaN | 04BD | Power\_Factor | NaN | I16 | 0.001 | p.u. | NaN | NaN | R | 总功率因数。 | 终端用户 | 逆变器端超前为正，滞后为负 |
| NaN | 04BE | Current\_HV\_LLC\_Chg\_Dchg | NaN | I16 | 0.01 | A | NaN | NaN | R | 高压侧LLC充放电电流 | 终端用户 | NaN |
| NaN | 04BF | Electrical\_Generation\_Efficiency | NaN | U16 | 0.01 | % | NaN | NaN | R | 发电效率 | 终端用户 | NaN |
| NaN | 04C0 --04FF | 预留 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 2.3离网输出 | (0x0500-0x057F) | 离网运行的实时采集数据 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 0500 -- 0503 | AddressMask\_Realtime\_EmergencyOutput1 | NaN | U64 | NaN | NaN | NaN | NaN | R | 本地址开始的64个寄存器地址字的掩码区。\n参看地址0x0040的说明 | 终端用户 | NaN |
| 负载功率 | 0504 | ActivePower\_Load\_Total | NaN | I16 | 0.01 | kW | NaN | NaN | R | 负载有功功率。 | 终端用户 | 负载消耗为正，回馈为负。 |
| NaN | 0505 | ReactivePower\_Load\_Total | NaN | I16 | 0.01 | kVar | NaN | NaN | R | 负载无功功率 | 终端用户 | NaN |
| NaN | 0506 | ApparentPower\_Load\_Total | NaN | I16 | 0.01 | kVA | NaN | NaN | R | 负载视在功率。 | 终端用户 | 负载消耗为正，回馈为负。 |
| 输出电压频率 | 0507 | Frequency\_Output | NaN | U16 | 0.01 | Hz | NaN | NaN | R | 输出电压频率 | 终端用户 | 逆变器输出的电压频率 |
| NaN | 0508 -- 0509 | ESOutput\_Rsvd1 -- 2 | NaN | NaN | NaN | NaN | NaN | NaN | R | 离网总输出预留1-2 | 终端用户 | NaN |
| R相离网\n实时数据 | 050A | Voltage\_Output\_R | NaN | U16 | 0.1 | V | NaN | NaN | R | R相逆变器输出电压 | 终端用户 | NaN |
| NaN | 050B | Current\_Load\_R | NaN | I16 | 0.01 | A | NaN | NaN | R | R相负载电流 | 终端用户 | R相与负载的电流 |
| NaN | 050C | ActivePower\_Load\_R | NaN | I16 | 0.01 | kW | NaN | NaN | R | R相负载有功功率。 | 终端用户 | 单相负载有功功率，负载消耗为正，回馈为负。 |
| NaN | 050D | ReactivePower\_Load\_R | NaN | I16 | 0.01 | kVar | NaN | NaN | R | R相负载无功功率。 | 终端用户 | 逆变器端超前为正，滞后为负 |
| NaN | 050E | ApparentPower\_Load\_R | NaN | I16 | 0.01 | kVA | NaN | NaN | R | R相负载视在功率。 | 终端用户 | 负载消耗为正，回馈为负。 |
| NaN | 050F | LoadPeakRatio\_R | NaN | U16 | 0.01 | p.u. | NaN | NaN | R | R相负载峰值比 | 终端用户 | NaN |
| NaN | 0510 | Voltage\_Load\_R | NaN | U16 | 0.1 | V | NaN | NaN | R | R相应急负载电压 | 终端用户 | NaN |
| NaN | 0511 | ESR\_Rsvd2 | NaN | NaN | NaN | NaN | NaN | NaN | R | R相预留2 | 终端用户 | NaN |
| S相离网\n实时数据 | 0512 | Voltage\_Output\_S | NaN | U16 | 0.1 | V | NaN | NaN | R | S相逆变器输出电压 | 终端用户 | 参考上面R相的相关说明 |
| NaN | 0513 | Current\_Load\_S | NaN | I16 | 0.01 | A | NaN | NaN | R | S相负载电流 | 终端用户 | NaN |
| NaN | 0514 | ActivePower\_Load\_S | NaN | I16 | 0.01 | kW | NaN | NaN | R | S相负载有功功率。 | 终端用户 | NaN |
| NaN | 0515 | ReactivePower\_Load\_S | NaN | I16 | 0.01 | kVar | NaN | NaN | R | S相负载无功功率。 | 终端用户 | NaN |
| NaN | 0516 | ApparentPower\_Load\_S | NaN | I16 | 0.01 | kVA | NaN | NaN | R | S相负载视在功率。 | 终端用户 | NaN |
| NaN | 0517 | LoadPeakRatio\_S | NaN | U16 | 0.01 | p.u. | NaN | NaN | R | S相负载峰值比 | 终端用户 | NaN |
| NaN | 0518 | Voltage\_Load\_S | NaN | U16 | 0.1 | V | NaN | NaN | R | S相应急负载电压 | 终端用户 | NaN |
| NaN | 0519 | ESS\_Rsvd2 | NaN | NaN | NaN | NaN | NaN | NaN | R | S相预留2 | 终端用户 | NaN |
| T相离网\n实时数据 | 051A | Voltage\_Output\_T | NaN | U16 | 0.1 | V | NaN | NaN | R | T相逆变器输出电压 | 终端用户 | 参考上面R相的相关说明 |
| NaN | 051B | Current\_Load\_T | NaN | I16 | 0.01 | A | NaN | NaN | R | T相负载电流 | 终端用户 | NaN |
| NaN | 051C | ActivePower\_Load\_T | NaN | I16 | 0.01 | kW | NaN | NaN | R | T相负载有功功率。 | 终端用户 | NaN |
| NaN | 051D | ReactivePower\_Load\_T | NaN | I16 | 0.01 | kVar | NaN | NaN | R | T相负载无功功率。 | 终端用户 | NaN |
| NaN | 051E | ApparentPower\_Load\_T | NaN | I16 | 0.01 | kVA | NaN | NaN | R | T相负载视在功率。 | 终端用户 | NaN |
| NaN | 051F | LoadPeakRatio\_T | NaN | U16 | 0.01 | p.u. | NaN | NaN | R | T相负载峰值比 | 终端用户 | NaN |
| NaN | 0520 | Voltage\_Load\_T | NaN | U16 | 0.1 | V | NaN | NaN | R | T相应急负载电压 | 终端用户 | NaN |
| NaN | 0521 | EST\_Rsvd2 | NaN | NaN | NaN | NaN | NaN | NaN | R | T相预留2 | 终端用户 | NaN |
| 其他离网\n实时数据 | 0522 | Voltage\_Output\_L1N | NaN | U16 | 0.1 | V | NaN | NaN | R | 逆变L1对N电压有效值 | 终端用户 | NaN |
| NaN | 0523 | Current\_Load\_L1N | NaN | I16 | 0.01 | A | NaN | NaN | R | L1负载电流有效值 | 终端用户 | NaN |
| NaN | 0524 | ActivePower\_Load\_L1N | NaN | I16 | 0.01 | kW | NaN | NaN | R | 负载L1对N有功功率 | 终端用户 | NaN |
| NaN | 0525 | Voltage\_Output\_L2N | NaN | U16 | 0.1 | V | NaN | NaN | R | 逆变L2对N电压有效值 | 终端用户 | NaN |
| NaN | 0526 | Current\_Load\_L2N | NaN | I16 | 0.01 | A | NaN | NaN | R | L2负载电流有效值 | 终端用户 | NaN |
| NaN | 0527 | ActivePower\_Load\_L2N | NaN | I16 | 0.01 | kW | NaN | NaN | R | 负载L2对N有功功率 | 终端用户 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 2.4PV输入 | (0x0580-0x05FF) | 第1-16路PV电压，电流和功率值和总PV功率 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 0580 -- 0583 | AddressMask\_Realtime\_Input\_PV1 | NaN | U64 | NaN | NaN | NaN | NaN | R | 本地址开始的64个寄存器地址字的掩码区。\n参看地址0x0040的说明 | 终端用户 | NaN |
| PV1-16\n电压\n电流\n功率\n数据 | 0584 | Voltage\_PV1 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 1 路PV电压 | 终端用户 | PV的路数和具体机型有关。\n读出来的数乘精度即为最终数据\n例1：地址0x0584读取：0x0906为231V\n例2：地址0x0585读取：0x01BB为4.43A\n例3：地址0x0586读取：0x0066为1.02KW\n其他参考第1路PV电压、电流和功率 |
| NaN | 0585 | Current\_PV1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 1 路PV电流 | 终端用户 | NaN |
| NaN | 0586 | Power\_PV1 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 1 路PV功率 | 终端用户 | NaN |
| NaN | 0587 | Voltage\_PV2 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 2 路PV电压 | 终端用户 | 参见第1路说明 |
| NaN | 0588 | Current\_PV2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 2 路PV电流 | 终端用户 | NaN |
| NaN | 0589 | Power\_PV2 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 2 路PV功率 | 终端用户 | NaN |
| NaN | 058A | Voltage\_PV3 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 3 路PV电压 | 终端用户 | 参见第1路说明 |
| NaN | 058B | Current\_PV3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 3 路PV电流 | 终端用户 | NaN |
| NaN | 058C | Power\_PV3 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 3 路PV功率 | 终端用户 | NaN |
| NaN | 058D | Voltage\_PV4 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 4 路PV电压 | 终端用户 | 参见第1路说明 |
| NaN | 058E | Current\_PV4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 4 路PV电流 | 终端用户 | NaN |
| NaN | 058F | Power\_PV4 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 4 路PV功率 | 终端用户 | NaN |
| NaN | 0590 | Voltage\_PV5 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 5 路PV电压 | 终端用户 | 参见第1路说明 |
| NaN | 0591 | Current\_PV5 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 5 路PV电流 | 终端用户 | NaN |
| NaN | 0592 | Power\_PV5 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 5 路PV功率 | 终端用户 | NaN |
| NaN | 0593 | Voltage\_PV6 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 6 路PV电压 | 终端用户 | 参见第1路说明 |
| NaN | 0594 | Current\_PV6 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 6 路PV电流 | 终端用户 | NaN |
| NaN | 0595 | Power\_PV6 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 6 路PV功率 | 终端用户 | NaN |
| NaN | 0596 | Voltage\_PV7 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 7 路PV电压 | 终端用户 | 参见第1路说明 |
| NaN | 0597 | Current\_PV7 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 7 路PV电流 | 终端用户 | NaN |
| NaN | 0598 | Power\_PV7 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 7 路PV功率 | 终端用户 | NaN |
| NaN | 0599 | Voltage\_PV8 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 8 路PV电压 | 终端用户 | 参见第1路说明 |
| NaN | 059A | Current\_PV8 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 8 路PV电流 | 终端用户 | NaN |
| NaN | 059B | Power\_PV8 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 8 路PV功率 | 终端用户 | NaN |
| NaN | 059C | Voltage\_PV9 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 9 路PV电压 | 终端用户 | 参见第1路说明 |
| NaN | 059D | Current\_PV9 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 9 路PV电流 | 终端用户 | NaN |
| NaN | 059E | Power\_PV9 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 9 路PV功率 | 终端用户 | NaN |
| NaN | 059F | Voltage\_PV10 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 10 路PV电压 | 终端用户 | 参见第1路说明 |
| NaN | 05A0 | Current\_PV10 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 10 路PV电流 | 终端用户 | NaN |
| NaN | 05A1 | Power\_PV10 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 10 路PV功率 | 终端用户 | NaN |
| NaN | 05A2 | Voltage\_PV11 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 11 路PV电压 | 终端用户 | 参见第1路说明 |
| NaN | 05A3 | Current\_PV11 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 11 路PV电流 | 终端用户 | NaN |
| NaN | 05A4 | Power\_PV11 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 11 路PV功率 | 终端用户 | NaN |
| NaN | 05A5 | Voltage\_PV12 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 12 路PV电压 | 终端用户 | 参见第1路说明 |
| NaN | 05A6 | Current\_PV12 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 12 路PV电流 | 终端用户 | NaN |
| NaN | 05A7 | Power\_PV12 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 12 路PV功率 | 终端用户 | NaN |
| NaN | 05A8 | Voltage\_PV13 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 13 路PV电压 | 终端用户 | 参见第1路说明 |
| NaN | 05A9 | Current\_PV13 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 13 路PV电流 | 终端用户 | NaN |
| NaN | 05AA | Power\_PV13 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 13 路PV功率 | 终端用户 | NaN |
| NaN | 05AB | Voltage\_PV14 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 14 路PV电压 | 终端用户 | 参见第1路说明 |
| NaN | 05AC | Current\_PV14 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 14 路PV电流 | 终端用户 | NaN |
| NaN | 05AD | Power\_PV14 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 14 路PV功率 | 终端用户 | NaN |
| NaN | 05AE | Voltage\_PV15 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 15 路PV电压 | 终端用户 | 参见第1路说明 |
| NaN | 05AF | Current\_PV15 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 15 路PV电流 | 终端用户 | NaN |
| NaN | 05B0 | Power\_PV15 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 15 路PV功率 | 终端用户 | NaN |
| NaN | 05B1 | Voltage\_PV16 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 16 路PV电压 | 终端用户 | 参见第1路说明 |
| NaN | 05B2 | Current\_PV16 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 16 路PV电流 | 终端用户 | NaN |
| NaN | 05B3 | Power\_PV16 | NaN | U16 | 0.01 | kW | NaN | NaN | R | 第 16 路PV功率 | 终端用户 | NaN |
| NaN | 05B4 -- 05B6 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 预留 | NaN | NaN |
| NaN | 05C0 -- 05C3 | AddressMask\_Realtime\_Input\_PV2 | NaN | U64 | NaN | NaN | NaN | NaN | R | 本地址开始的64个寄存器地址字的掩码区。\n参看地址0x0040的说明 | 终端用户 | NaN |
| 总PV功率 | 05C4 | Power\_PV\_Total | NaN | U16 | 0.1 | kW | NaN | NaN | R | 总PV功率。 | 终端用户 | 所有PV功率之和,读出来的数乘精度即为最终数据\n例：0x0007表示0.7kw |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 2.5电池输入 | (0x0600-0x067F) | 第1-12路电池组：电压，充放电电流，充放电功率，环境温度，SOC，SOH，循环次数和汇总信息 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 0600 -- 0603 | AddressMask\_Realtime\_Input\_Bat1 | NaN | U64 | NaN | NaN | NaN | NaN | R | 本地址开始的64个寄存器地址字的掩码区。\n参看地址0x0040的说明 | 终端用户 | NaN |
| 第1-8路电池组\n数据1 | 0604 | Voltage\_Bat1 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第1-8路电池组电压。 | 终端用户 | 电池路数与具体机型有关\n读出来的数乘精度即为最终数据\n充放电电流：充电为正，放电为负\n例：0x016C表示36.4V |
| NaN | 0605 | Current\_Bat1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第1-8路电池组充放电电流。 | 终端用户 | NaN |
| NaN | 0606 | Power\_Bat1 | NaN | I16 | 0.01 | kW | NaN | NaN | R | 第1-8路电池组充放电功率。 | 终端用户 | NaN |
| NaN | 0607 | Temperature\_Env\_Bat1 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 第1-8路电池组环境温度。 | 终端用户 | 电池外围温度，负数表示零下温度。 |
| NaN | 0608 | SOC\_Bat1 | NaN | U16 | 1 | % | NaN | NaN | R | 第1-8路电池组SOC。 | 终端用户 | 电池电量 |
| NaN | 0609 | SOH\_Bat1 | NaN | U16 | 1 | % | NaN | NaN | R | 第1-8路电池组SOH。 | 终端用户 | 当前电池相对于新电池存储电能的能力 |
| NaN | 060A | ChargeCycle\_Bat1 | NaN | U16 | 1 | cycle | NaN | NaN | R | 第1-8路电池组循环次数。 | 终端用户 | 电池充放电循环次数 |
| NaN | 060B | Voltage\_Bat2 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第2路电池组电压 | 终端用户 | 参见第1组说明 |
| NaN | 060C | Current\_Bat2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第2路电池组充放电电流 | 终端用户 | NaN |
| NaN | 060D | Power\_Bat2 | NaN | I16 | 0.01 | kW | NaN | NaN | R | 第2路电池组充放电功率 | 终端用户 | NaN |
| NaN | 060E | Temperature\_Env\_Bat2 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 第2路电池组环境温度 | 终端用户 | NaN |
| NaN | 060F | SOC\_Bat2 | NaN | U16 | 1 | % | NaN | NaN | R | 第2路电池组SOC | 终端用户 | NaN |
| NaN | 0610 | SOH\_Bat2 | NaN | U16 | 1 | % | NaN | NaN | R | 第2路电池组SOH | 终端用户 | NaN |
| NaN | 0611 | ChargeCycle\_Bat2 | NaN | U16 | 1 | cycle | NaN | NaN | R | 第2路电池组循环次数 | 终端用户 | NaN |
| NaN | 0612 | Voltage\_Bat3 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第3路电池组电压 | 终端用户 | 参见第1组说明 |
| NaN | 0613 | Current\_Bat3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第3路电池组充放电电流 | 终端用户 | NaN |
| NaN | 0614 | Power\_Bat3 | NaN | I16 | 0.01 | kW | NaN | NaN | R | 第3路电池组充放电功率 | 终端用户 | NaN |
| NaN | 0615 | Temperature\_Env\_Bat3 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 第3路电池组环境温度 | 终端用户 | NaN |
| NaN | 0616 | SOC\_Bat3 | NaN | U16 | 1 | % | NaN | NaN | R | 第3路电池组SOC | 终端用户 | NaN |
| NaN | 0617 | SOH\_Bat3 | NaN | U16 | 1 | % | NaN | NaN | R | 第3路电池组SOH | 终端用户 | NaN |
| NaN | 0618 | ChargeCycle\_Bat3 | NaN | U16 | 1 | cycle | NaN | NaN | R | 第3路电池组循环次数 | 终端用户 | NaN |
| NaN | 0619 | Voltage\_Bat4 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第4路电池组电压 | 终端用户 | 参见第1组说明 |
| NaN | 061A | Current\_Bat4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第4路电池组充放电电流 | 终端用户 | NaN |
| NaN | 061B | Power\_Bat4 | NaN | I16 | 0.01 | kW | NaN | NaN | R | 第4路电池组充放电功率 | 终端用户 | NaN |
| NaN | 061C | Temperature\_Env\_Bat4 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 第4路电池组环境温度 | 终端用户 | NaN |
| NaN | 061D | SOC\_Bat4 | NaN | U16 | 1 | % | NaN | NaN | R | 第4路电池组SOC | 终端用户 | NaN |
| NaN | 061E | SOH\_Bat4 | NaN | U16 | 1 | % | NaN | NaN | R | 第4路电池组SOH | 终端用户 | NaN |
| NaN | 061F | ChargeCycle\_Bat4 | NaN | U16 | 1 | cycle | NaN | NaN | R | 第4路电池组循环次数 | 终端用户 | NaN |
| NaN | 0620 | Voltage\_Bat5 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第5路电池组电压 | 终端用户 | 参见第1组说明 |
| NaN | 0621 | Current\_Bat5 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第5路电池组充放电电流 | 终端用户 | NaN |
| NaN | 0622 | Power\_Bat5 | NaN | I16 | 0.01 | kW | NaN | NaN | R | 第5路电池组充放电功率 | 终端用户 | NaN |
| NaN | 0623 | Temperature\_Env\_Bat5 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 第5路电池组环境温度 | 终端用户 | NaN |
| NaN | 0624 | SOC\_Bat5 | NaN | U16 | 1 | % | NaN | NaN | R | 第5路电池组SOC | 终端用户 | NaN |
| NaN | 0625 | SOH\_Bat5 | NaN | U16 | 1 | % | NaN | NaN | R | 第5路电池组SOH | 终端用户 | NaN |
| NaN | 0626 | ChargeCycle\_Bat5 | NaN | U16 | 1 | cycle | NaN | NaN | R | 第5路电池组循环次数 | 终端用户 | NaN |
| NaN | 0627 | Voltage\_Bat6 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第6路电池组电压 | 终端用户 | 参见第1组说明 |
| NaN | 0628 | Current\_Bat6 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第6路电池组充放电电流 | 终端用户 | NaN |
| NaN | 0629 | Power\_Bat6 | NaN | I16 | 0.01 | kW | NaN | NaN | R | 第6路电池组充放电功率 | 终端用户 | NaN |
| NaN | 062A | Temperature\_Env\_Bat6 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 第6路电池组环境温度 | 终端用户 | NaN |
| NaN | 062B | SOC\_Bat6 | NaN | U16 | 1 | % | NaN | NaN | R | 第6路电池组SOC | 终端用户 | NaN |
| NaN | 062C | SOH\_Bat6 | NaN | U16 | 1 | % | NaN | NaN | R | 第6路电池组SOH | 终端用户 | NaN |
| NaN | 062D | ChargeCycle\_Bat6 | NaN | U16 | 1 | cycle | NaN | NaN | R | 第6路电池组循环次数 | 终端用户 | NaN |
| NaN | 062E | Voltage\_Bat7 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第7路电池组电压 | 终端用户 | 参见第1组说明 |
| NaN | 062F | Current\_Bat7 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第7路电池组充放电电流 | 终端用户 | NaN |
| NaN | 0630 | Power\_Bat7 | NaN | I16 | 0.01 | kW | NaN | NaN | R | 第7路电池组充放电功率 | 终端用户 | NaN |
| NaN | 0631 | Temperature\_Env\_Bat7 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 第7路电池组环境温度 | 终端用户 | NaN |
| NaN | 0632 | SOC\_Bat7 | NaN | U16 | 1 | % | NaN | NaN | R | 第7路电池组SOC | 终端用户 | NaN |
| NaN | 0633 | SOH\_Bat7 | NaN | U16 | 1 | % | NaN | NaN | R | 第7路电池组SOH | 终端用户 | NaN |
| NaN | 0634 | ChargeCycle\_Bat7 | NaN | U16 | 1 | cycle | NaN | NaN | R | 第7路电池组循环次数 | 终端用户 | NaN |
| NaN | 0635 | Voltage\_Bat8 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第8路电池组电压 | 终端用户 | 参见第1组说明 |
| NaN | 0636 | Current\_Bat8 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第8路电池组充放电电流 | 终端用户 | NaN |
| NaN | 0637 | Power\_Bat8 | NaN | I16 | 0.01 | kW | NaN | NaN | R | 第8路电池组充放电功率 | 终端用户 | NaN |
| NaN | 0638 | Temperature\_Env\_Bat8 | NaN | I16 | 1 | ℃ | NaN | NaN | R | 第8路电池组环境温度 | 终端用户 | NaN |
| NaN | 0639 | SOC\_Bat8 | NaN | U16 | 1 | % | NaN | NaN | R | 第8路电池组SOC | 终端用户 | NaN |
| NaN | 063A | SOH\_Bat8 | NaN | U16 | 1 | % | NaN | NaN | R | 第8路电池组SOH | 终端用户 | NaN |
| NaN | 063B | ChargeCycle\_Bat8 | NaN | U16 | 1 | cycle | NaN | NaN | R | 第8路电池组循环次数 | 终端用户 | NaN |
| NaN | 063C -- 063F | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 预留 | NaN | NaN |
| NaN | 0640 -- 0643 | AddressMask\_Realtime\_Input\_Bat2 | NaN | U64 | NaN | NaN | NaN | NaN | R | 本地址开始的64个寄存器地址字的掩码区。\n参看地址0x0040的说明 | 终端用户 | NaN |
| 第1-8路电池组\n数据2 | 0644 | Charge\_Current\_Limitation1 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 1 路电池组充电电流上限 | 终端用户 | 电池路数与具体机型有关\n案例参考第1路电池组说明 |
| NaN | 0645 | Discharge\_Current\_limitation1 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 1 路电池组放电电流上限 | 终端用户 | NaN |
| NaN | 0646 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 1 路电池组预留 | 终端用户 | NaN |
| NaN | 0647 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 1 路电池组预留 | 终端用户 | NaN |
| NaN | 0648 | Charge\_Current\_Limitation2 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 2 路电池组充电电流上限 | 终端用户 | 电池路数与具体机型有关\n案例参考第1路电池组说明 |
| NaN | 0649 | Discharge\_Current\_limitation2 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 2 路电池组放电电流上限 | 终端用户 | NaN |
| NaN | 064A | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 2 路电池组预留 | 终端用户 | NaN |
| NaN | 064B | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 2 路电池组预留 | 终端用户 | NaN |
| NaN | 064C | Charge\_Current\_Limitation3 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 3 路电池组充电电流上限 | 终端用户 | 电池路数与具体机型有关\n案例参考第1路电池组说明 |
| NaN | 064D | Discharge\_Current\_limitation3 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 3 路电池组放电电流上限 | 终端用户 | NaN |
| NaN | 064E | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 3 路电池组预留 | 终端用户 | NaN |
| NaN | 064F | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 3 路电池组预留 | 终端用户 | NaN |
| NaN | 0650 | Charge\_Current\_Limitation4 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 4 路电池组充电电流上限 | 终端用户 | 电池路数与具体机型有关\n案例参考第1路电池组说明 |
| NaN | 0651 | Discharge\_Current\_limitation4 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 4 路电池组放电电流上限 | 终端用户 | NaN |
| NaN | 0652 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 4 路电池组预留 | 终端用户 | NaN |
| NaN | 0653 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 4 路电池组预留 | 终端用户 | NaN |
| NaN | 0654 | Charge\_Current\_Limitation5 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 5 路电池组充电电流上限 | 终端用户 | 电池路数与具体机型有关\n案例参考第1路电池组说明 |
| NaN | 0655 | Discharge\_Current\_limitation5 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 5 路电池组放电电流上限 | 终端用户 | NaN |
| NaN | 0656 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 5 路电池组预留 | 终端用户 | NaN |
| NaN | 0657 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 5 路电池组预留 | 终端用户 | NaN |
| NaN | 0658 | Charge\_Current\_Limitation6 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 6 路电池组充电电流上限 | 终端用户 | 电池路数与具体机型有关\n案例参考第1路电池组说明 |
| NaN | 0659 | Discharge\_Current\_limitation6 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 6 路电池组放电电流上限 | 终端用户 | NaN |
| NaN | 065A | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 6 路电池组预留 | 终端用户 | NaN |
| NaN | 065B | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 6 路电池组预留 | 终端用户 | NaN |
| NaN | 065C | Charge\_Current\_Limitation7 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 7 路电池组充电电流上限 | 终端用户 | 电池路数与具体机型有关\n案例参考第1路电池组说明 |
| NaN | 065D | Discharge\_Current\_limitation7 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 7 路电池组放电电流上限 | 终端用户 | NaN |
| NaN | 065E | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 7 路电池组预留 | 终端用户 | NaN |
| NaN | 065F | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 7 路电池组预留 | 终端用户 | NaN |
| NaN | 0660 | Charge\_Current\_Limitation8 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 8 路电池组充电电流上限 | 终端用户 | 电池路数与具体机型有关\n案例参考第1路电池组说明 |
| NaN | 0661 | Discharge\_Current\_limitation8 | NaN | U16 | 0.01 | A | NaN | NaN | R | 第 8 路电池组放电电流上限 | 终端用户 | NaN |
| NaN | 0662 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 8 路电池组预留 | 终端用户 | NaN |
| NaN | 0663 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | R | 第 8 路电池组预留 | 终端用户 | NaN |
| NaN | 0664 -- 0666 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 预留 | NaN | NaN |
| 电池组\n其他数据 | 0667 | Power\_Bat\_Total | NaN | I16 | 0.1 | kW | NaN | NaN | R | 总电池充放电功率。充电为正，放电为负 | 终端用户 | NaN |
| NaN | 0668 | SOC\_Bat\_Average | NaN | U16 | 1 | % | NaN | NaN | R | 电池组SOC的平均值 | 终端用户 | 平均电量 |
| NaN | 0669 | SOH\_Bat | NaN | U16 | 1 | % | NaN | NaN | R | 电池组SOH | 终端用户 | 当前电池相对于新电池存储电能的能力 |
| NaN | 066A | CurrentBattery\_num | NaN | U16 | 1 | NaN | NaN | NaN | R | 实时电池路数 | NaN | NaN |
| NaN | 066B | BatteryCapacity | NaN | U16 | 1 | Ah | 1.0 | 65535.0 | R | 电池总容量 | 终端用户 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 2.6电量 | (0x0680-0x06BF) | 电量信息：发电量(当日+总)，负载耗电量(当日+总)，买电量(当日+总)，卖电量(当日+总)，电池充电量(当日+总)，电池放电量(当日+总) | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 0680 -- 0683 | AddressMask\_Realtime\_ElectricityStatistics1 | NaN | U64 | NaN | NaN | NaN | NaN | R | 本地址开始的64个寄存器地址字的掩码区。\n参看地址0x0040的说明 | 终端用户 | NaN |
| 电量数据 | 0684 -- 0685 | PV\_Generation\_Today | NaN | U32 | 0.01 | kWh | NaN | NaN | R | 当日发电量 | 终端用户 | 低地址为高位，高地址为低位，读出来的数乘精度即为最终数据，例：0x0000 0x00EF表示2.39KWh |
| NaN | 0686 -- 0687 | PV\_Generation\_Total | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 总发电量 | 终端用户 | 低地址为高位，高地址为低位，读出来的数乘精度即为最终数据，例：0x0000 0x0017表示2.3KWh |
| NaN | 0688 -- 0689 | Load\_Consumption\_Today | NaN | U32 | 0.01 | kWh | NaN | NaN | R | 当日负载耗电量 | 终端用户 | 低地址为高位，高地址为低位\n读出来的数乘精度即为最终数据\n案例请参考0x0684与0x0685地址 |
| NaN | 068A -- 068B | Load\_Consumption\_Total | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 总负载耗电量 | 终端用户 | NaN |
| NaN | 068C -- 068D | Energy\_Purchase\_Today | NaN | U32 | 0.01 | kWh | NaN | NaN | R | 当日买电量 | 终端用户 | NaN |
| NaN | 068E -- 068F | Energy\_Purchase\_Total | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 总买电量 | 终端用户 | NaN |
| NaN | 0690 -- 0691 | Energy\_Selling\_Today | NaN | U32 | 0.01 | kWh | NaN | NaN | R | 当日卖电量 | 终端用户 | NaN |
| NaN | 0692 -- 0693 | Energy\_Selling\_Total | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 总卖电量 | 终端用户 | NaN |
| NaN | 0694 -- 0695 | Bat\_Charge\_Today | NaN | U32 | 0.01 | kWh | NaN | NaN | R | 当日电池充电量 | 终端用户 | NaN |
| NaN | 0696 -- 0697 | Bat\_Charge\_Total | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 总电池充电量 | 终端用户 | NaN |
| NaN | 0698 -- 0699 | Bat\_Discharge\_Today | NaN | U32 | 0.01 | kWh | NaN | NaN | R | 当日电池放电量 | 终端用户 | NaN |
| NaN | 069A -- 069B | Bat\_Discharge\_Total | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 总电池放电量 | 终端用户 | NaN |
| 当年当月\n电量数据 | 069C -- 069D | PV\_Generation\_Month | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 本月发电量 | 终端用户 | NaN |
| NaN | 069E -- 069F | PV\_Generation\_Year | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 本年发电量 | 终端用户 | NaN |
| NaN | 06A0 -- 06A1 | Load\_Consumption\_Month | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 本月负载耗电量 | 终端用户 | NaN |
| NaN | 06A2 -- 06A3 | Load\_Consumption\_Year | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 本年负载耗电量 | 终端用户 | NaN |
| NaN | 06A4 -- 06A5 | Energy\_Purchase\_Month | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 本月买电量 | 终端用户 | NaN |
| NaN | 06A6 -- 06A7 | Energy\_Purchase\_Year | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 本年买电量 | 终端用户 | NaN |
| NaN | 06A8 -- 06A9 | Energy\_Selling\_Month | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 本月卖电量 | 终端用户 | NaN |
| NaN | 06AA -- 06AB | Energy\_Selling\_Year | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 本年卖电量 | 终端用户 | NaN |
| NaN | 06AC -- 06AD | Bat\_Charge\_Month | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 本月电池充电量 | 终端用户 | NaN |
| NaN | 06AE -- 06AF | Bat\_Charge\_Year | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 本年电池充电量 | 终端用户 | NaN |
| NaN | 06B0 -- 06B1 | Bat\_Discharge\_Month | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 本月电池放电量 | 终端用户 | NaN |
| NaN | 06B2 -- 06B3 | Bat\_Discharge\_Year | NaN | U32 | 0.1 | kWh | NaN | NaN | R | 本年电池放电量 | 终端用户 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 2.7内部信息 | (0x06C0-0x06FF) | 漏电流，平衡电流，R/S/T电流直流分量，总BUS电压，PV1-16飞跨电容电压，额定功率，IV扫描有效点数等 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 06C0 -- 06C3 | AddressMask\_Realtime\_ClassifiedInfo1 | NaN | U64 | NaN | NaN | NaN | NaN | R | 本地址开始的64个寄存器地址字的掩码区。\n参看地址0x0040的说明 | 安装商 | NaN |
| 漏电流 | 06C4 | GFCI | NaN | U16 | 1 | mA | NaN | NaN | R | 漏电流 | 安装商 | 例：0x0005表示5mA |
| 平衡电流 | 06C5 | Current\_Bus\_Balance | NaN | I16 | 0.01 | A | NaN | NaN | R | 平衡电流 | 安装商 | 注：实现三相平衡 |
| 直流分量 | 06C6 | DCI\_R | NaN | I16 | 1 | mA | NaN | NaN | R | R相电流直流分量 | 安装商 | NaN |
| NaN | 06C7 | DCI\_S | NaN | I16 | 1 | mA | NaN | NaN | R | S相电流直流分量 | 安装商 | NaN |
| NaN | 06C8 | DCI\_T | NaN | I16 | 1 | mA | NaN | NaN | R | T相电流直流分量 | 安装商 | NaN |
| NaN | 06C9 | DCV\_R | NaN | I16 | 1 | mV | NaN | NaN | R | R相电压直流分量 | 安装商 | NaN |
| NaN | 06CA | DCV\_S | NaN | I16 | 1 | mV | NaN | NaN | R | S相电压直流分量 | 安装商 | NaN |
| NaN | 06CB | DCV\_T | NaN | I16 | 1 | mV | NaN | NaN | R | T相电压直流分量 | 安装商 | NaN |
| BUS电压信息\nBuckBoost电流 | 06CC | Voltage\_Bus | NaN | U16 | 0.1 | V | NaN | NaN | R | 总BUS电压 | 安装商 | 母线电压，逆变器会将PV的输入电压升压到BUS电压，达到逆变要求，再进行逆变 |
| NaN | 06CD | Voltage\_Bus\_P | NaN | U16 | 0.1 | V | NaN | NaN | R | BUS正电压 | 安装商 | bus+,对地电压为正 |
| NaN | 06CE | Voltage\_Bus\_N | NaN | U16 | 0.1 | V | NaN | NaN | R | BUS负电压 | 安装商 | bus-,对地电压为负 |
| NaN | 06CF | Voltage\_Bus\_LLC | NaN | U16 | 0.1 | V | NaN | NaN | R | LLC Bus电压 | 安装商 | NaN |
| NaN | 06D0 | Current\_BuckBoost | NaN | I16 | 0.01 | A | NaN | NaN | R | BuckBoost电流 | 安装商 | NaN |
| NaN | 06D1 | Voltage\_Bus\_P\_Half | NaN | U16 | 0.1 | V | NaN | NaN | R | BUS正半电压 | 安装商 | NaN |
| NaN | 06D2 | Voltage\_Bus\_N\_Half | NaN | U16 | 0.1 | V | NaN | NaN | R | BUS负半电压 | 安装商 | NaN |
| 飞跨电容电压 | 06D3 | FlyingCap\_Voltage1 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV1 飞跨电容电压 | 安装商 | NaN |
| NaN | 06D4 | FlyingCap\_Voltage2 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV2 飞跨电容电压 | 安装商 | NaN |
| NaN | 06D5 | FlyingCap\_Voltage3 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV3 飞跨电容电压 | 安装商 | NaN |
| NaN | 06D6 | FlyingCap\_Voltage4 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV4 飞跨电容电压 | 安装商 | NaN |
| NaN | 06D7 | FlyingCap\_Voltage5 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV5 飞跨电容电压 | 安装商 | NaN |
| NaN | 06D8 | FlyingCap\_Voltage6 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV6 飞跨电容电压 | 安装商 | NaN |
| NaN | 06D9 | FlyingCap\_Voltage7 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV7 飞跨电容电压 | 安装商 | NaN |
| NaN | 06DA | FlyingCap\_Voltage8 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV8 飞跨电容电压 | 安装商 | NaN |
| NaN | 06DB | FlyingCap\_Voltage9 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV9 飞跨电容电压 | 安装商 | NaN |
| NaN | 06DC | FlyingCap\_Voltage10 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV10 飞跨电容电压 | 安装商 | NaN |
| NaN | 06DD | FlyingCap\_Voltage11 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV11 飞跨电容电压 | 安装商 | NaN |
| NaN | 06DE | FlyingCap\_Voltage12 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV12 飞跨电容电压 | 安装商 | NaN |
| NaN | 06DF | FlyingCap\_Voltage13 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV13 飞跨电容电压 | 安装商 | NaN |
| NaN | 06E0 | FlyingCap\_Voltage14 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV14 飞跨电容电压 | 安装商 | NaN |
| NaN | 06E1 | FlyingCap\_Voltage15 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV15 飞跨电容电压 | 安装商 | NaN |
| NaN | 06E2 | FlyingCap\_Voltage16 | NaN | U16 | 0.1 | V | NaN | NaN | R | PV16 飞跨电容电压 | 安装商 | NaN |
| 内部信息 | 06E3 -- 06EC | Internal\_Info1 -- 10 | NaN | U16 | 0.1 | V | NaN | NaN | R | 内部信息1-10（10个，调试信息区） | 安装商 | NaN |
| 逆变器额定功率 | 06ED | RatedPower\_Inverter | NaN | U16 | 0.1kW | kW | NaN | NaN | R | 逆变器额定功率 | 安装商 | NaN |
| IV曲线扫描 | 06EE | IVPoints\_Effec\_Num | NaN | U16 | 1 | NaN | 1.0 | 150.0 | R | IV曲线扫描有效点的个数 | 安装商 | NaN |
| BUS负对地电压 | 06EF | Voltage\_Bus\_N\_GND | NaN | I16 | 0.1 | V | NaN | NaN | R | BUS负对地电压 | 安装商 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| 设备信息 | 06FC | ProjectNum | R | U16 \* 1 | NaN | NaN | NaN | NaN | NaN | 项目代号，用于区分该区域数据定义，枚举类型：\n0：0-225KTLX-HV项目；\n其它-预留 | NaN | NaN |
| 设备控制预留 | 06FD -- 06FF | reserved | RW | U16 \* 3 | NaN | NaN | NaN | NaN | NaN | 预留，读出为0 | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 2.8汇流信息 | (0x0700-0x077F) | 第1-16组汇流电压，1-4路组串电流，与机型相关 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | 0700 -- 0703 | AddressMask\_Realtime\_CombinerInfo1 | NaN | U64 | NaN | NaN | NaN | NaN | R | 本地址开始的64个寄存器地址字的掩码区。\n参看地址0x0040的说明 | 安装商 | NaN |
| 第1-16组\n汇流电压\n组串电流 | 0704 | Voltage\_Group1 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 1 组汇流电压 | 安装商 | 与PV1电压相等，地址从0x0704开始，每组间隔3个地址。例：0x0866表示215V |
| NaN | 0705 | Current\_Group1\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 1 组第1路组串电流 | 安装商 | 与PV1电流相等，地址从0x0705开始，每组间隔3个地址，注意还有第3-4路组串电流，地址从0x0744开始。\n例：0x015F表示3.51A |
| NaN | 0706 | Current\_Group1\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 1 组第2路组串电流 | 安装商 | 是否具备此功能与机型相关，案例参考第1组第1路组串电流，地址从0x0706开始，每组间隔3个地址，注意还有第3-4路组串电流，地址从0x0744开始。 |
| NaN | 0707 | Voltage\_Group2 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 2 组汇流电压 | 安装商 | 参见第1组说明 |
| NaN | 0708 | Current\_Group2\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 2 组第1路组串电流 | 安装商 | NaN |
| NaN | 0709 | Current\_Group2\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 2 组第2路组串电流 | 安装商 | NaN |
| NaN | 070A | Voltage\_Group3 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 3 组汇流电压 | 安装商 | 参见第1组说明 |
| NaN | 070B | Current\_Group3\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 3 组第1路组串电流 | 安装商 | NaN |
| NaN | 070C | Current\_Group3\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 3 组第2路组串电流 | 安装商 | NaN |
| NaN | 070D | Voltage\_Group4 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 4 组汇流电压 | 安装商 | 参见第1组说明 |
| NaN | 070E | Current\_Group4\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 4 组第1路组串电流 | 安装商 | NaN |
| NaN | 070F | Current\_Group4\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 4 组第2路组串电流 | 安装商 | NaN |
| NaN | 0710 | Voltage\_Group5 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 5 组汇流电压 | 安装商 | 参见第1组说明 |
| NaN | 0711 | Current\_Group5\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 5 组第1路组串电流 | 安装商 | NaN |
| NaN | 0712 | Current\_Group5\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 5 组第2路组串电流 | 安装商 | NaN |
| NaN | 0713 | Voltage\_Group6 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 6 组汇流电压 | 安装商 | 参见第1组说明 |
| NaN | 0714 | Current\_Group6\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 6 组第1路组串电流 | 安装商 | NaN |
| NaN | 0715 | Current\_Group6\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 6 组第2路组串电流 | 安装商 | NaN |
| NaN | 0716 | Voltage\_Group7 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 7 组汇流电压 | 安装商 | 参见第1组说明 |
| NaN | 0717 | Current\_Group7\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 7 组第1路组串电流 | 安装商 | NaN |
| NaN | 0718 | Current\_Group7\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 7 组第2路组串电流 | 安装商 | NaN |
| NaN | 0719 | Voltage\_Group8 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 8 组汇流电压 | 安装商 | 参见第1组说明 |
| NaN | 071A | Current\_Group8\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 8 组第1路组串电流 | 安装商 | NaN |
| NaN | 071B | Current\_Group8\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 8 组第2路组串电流 | 安装商 | NaN |
| NaN | 071C | Voltage\_Group9 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 9 组汇流电压 | 安装商 | 参见第1组说明 |
| NaN | 071D | Current\_Group9\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 9 组第1路组串电流 | 安装商 | NaN |
| NaN | 071E | Current\_Group9\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 9 组第2路组串电流 | 安装商 | NaN |
| NaN | 071F | Voltage\_Group10 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 10 组汇流电压 | 安装商 | 参见第1组说明 |
| NaN | 0720 | Current\_Group10\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 10 组第1路组串电流 | 安装商 | NaN |
| NaN | 0721 | Current\_Group10\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 10 组第2路组串电流 | 安装商 | NaN |
| NaN | 0722 | Voltage\_Group11 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 11 组汇流电压 | 安装商 | 参见第1组说明 |
| NaN | 0723 | Current\_Group11\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 11 组第1路组串电流 | 安装商 | NaN |
| NaN | 0724 | Current\_Group11\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 11 组第2路组串电流 | 安装商 | NaN |
| NaN | 0725 | Voltage\_Group12 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 12 组汇流电压 | 安装商 | 参见第1组说明 |
| NaN | 0726 | Current\_Group12\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 12 组第1路组串电流 | 安装商 | NaN |
| NaN | 0727 | Current\_Group12\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 12 组第2路组串电流 | 安装商 | NaN |
| NaN | 0728 | Voltage\_Group13 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 13 组汇流电压 | 安装商 | 参见第1组说明 |
| NaN | 0729 | Current\_Group13\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 13 组第1路组串电流 | 安装商 | NaN |
| NaN | 072A | Current\_Group13\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 13 组第2路组串电流 | 安装商 | NaN |
| NaN | 072B | Voltage\_Group14 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 14 组汇流电压 | 安装商 | 参见第1组说明 |
| NaN | 072C | Current\_Group14\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 14 组第1路组串电流 | 安装商 | NaN |
| NaN | 072D | Current\_Group14\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 14 组第2路组串电流 | 安装商 | NaN |
| NaN | 072E | Voltage\_Group15 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 15 组汇流电压 | 安装商 | 参见第1组说明 |
| NaN | 072F | Current\_Group15\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 15 组第1路组串电流 | 安装商 | NaN |
| NaN | 0730 | Current\_Group15\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 15 组第2路组串电流 | 安装商 | NaN |
| NaN | 0731 | Voltage\_Group16 | NaN | U16 | 0.1 | V | NaN | NaN | R | 第 16 组汇流电压 | 安装商 | 参见第1组说明 |
| NaN | 0732 | Current\_Group16\_Branch1 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 16 组第1路组串电流 | 安装商 | NaN |
| NaN | 0733 | Current\_Group16\_Branch2 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 16 组第2路组串电流 | 安装商 | NaN |
| NaN | 0734 -- 073F | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 预留 | NaN | NaN |
| NaN | 0740 -- 0743 | AddressMask\_Realtime\_CombinerInfo2 | NaN | U64 | NaN | NaN | NaN | NaN | R | 本地址开始的64个寄存器地址字的掩码区。\n参看地址0x0040的说明 | 安装商 | NaN |
| 第1-16组\n汇流\n组串电流 | 0744 | Current\_Group1\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 1 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 0745 | Current\_Group1\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 1 组第4路组串电流 | 安装商 | NaN |
| NaN | 0746 | Current\_Group2\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 2 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 0747 | Current\_Group2\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 2 组第4路组串电流 | 安装商 | NaN |
| NaN | 0748 | Current\_Group3\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 3 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 0749 | Current\_Group3\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 3 组第4路组串电流 | 安装商 | NaN |
| NaN | 074A | Current\_Group4\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 4 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 074B | Current\_Group4\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 4 组第4路组串电流 | 安装商 | NaN |
| NaN | 074C | Current\_Group5\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 5 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 074D | Current\_Group5\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 5 组第4路组串电流 | 安装商 | NaN |
| NaN | 074E | Current\_Group6\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 6 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 074F | Current\_Group6\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 6 组第4路组串电流 | 安装商 | NaN |
| NaN | 0750 | Current\_Group7\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 7 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 0751 | Current\_Group7\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 7 组第4路组串电流 | 安装商 | NaN |
| NaN | 0752 | Current\_Group8\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 8 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 0753 | Current\_Group8\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 8 组第4路组串电流 | 安装商 | NaN |
| NaN | 0754 | Current\_Group9\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 9 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 0755 | Current\_Group9\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 9 组第4路组串电流 | 安装商 | NaN |
| NaN | 0756 | Current\_Group10\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 10 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 0757 | Current\_Group10\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 10 组第4路组串电流 | 安装商 | NaN |
| NaN | 0758 | Current\_Group11\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 11 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 0759 | Current\_Group11\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 11 组第4路组串电流 | 安装商 | NaN |
| NaN | 075A | Current\_Group12\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 12 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 075B | Current\_Group12\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 12 组第4路组串电流 | 安装商 | NaN |
| NaN | 075C | Current\_Group13\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 13 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 075D | Current\_Group13\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 13 组第4路组串电流 | 安装商 | NaN |
| NaN | 075E | Current\_Group14\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 14 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 075F | Current\_Group14\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 14 组第4路组串电流 | 安装商 | NaN |
| NaN | 0760 | Current\_Group15\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 15 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 0761 | Current\_Group15\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 15 组第4路组串电流 | 安装商 | NaN |
| NaN | 0762 | Current\_Group16\_Branch3 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 16 组第3路组串电流 | 安装商 | 是否具备此功能与机型相关\n案例参考第1组第1路组串电流\n每组间隔2个地址。 |
| NaN | 0763 | Current\_Group16\_Branch4 | NaN | I16 | 0.01 | A | NaN | NaN | R | 第 16 组第4路组串电流 | 安装商 | NaN |
| NaN | 0764 -- 077F | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | 预留 | NaN | NaN |