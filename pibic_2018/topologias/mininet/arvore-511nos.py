#!/usr/bin/python
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

if __name__ == '__main__':
	
	net = Mininet( controller=RemoteController )
	info( "Adicionando o IP do Controller SDN e a porta" )
	net.addController( 'c0',controller=RemoteController,ip='172.17.0.2',port=6653)
	info( 'Add hosts\n' )
	h1 = net.addHost( 'h1', ip='10.0.0.1', netmask='255.255.255.0' )
	h2 = net.addHost( 'h2', ip='10.0.0.2', netmask='255.255.255.0' )
	info( 'Add switch\n' )
	# Create Switch Nodes
	wth = 512
	for i in range(1, wth):
		locals()['s'+str(i)] = net.addSwitch('s'+str(i))

	info( 'Criando os links\n' )
	net.addLink(s1,s2)
	net.addLink(s1,s257)
	net.addLink(s2,s3)
	net.addLink(s2,s130)
	net.addLink(s3,s4)
	net.addLink(s3,s67)
	net.addLink(s4,s5)
	net.addLink(s4,s36)
	net.addLink(s5,s6)
	net.addLink(s5,s21)
	net.addLink(s6,s7)
	net.addLink(s6,s14)
	net.addLink(s7,s8)
	net.addLink(s7,s11)
	net.addLink(s8,s9)
	net.addLink(s8,s10)
	net.addLink(s11,s12)
	net.addLink(s11,s13)
	net.addLink(s14,s15)
	net.addLink(s14,s18)
	net.addLink(s15,s16)
	net.addLink(s15,s17)
	net.addLink(s18,s19)
	net.addLink(s18,s20)
	net.addLink(s21,s22)
	net.addLink(s21,s29)
	net.addLink(s22,s23)
	net.addLink(s22,s26)
	net.addLink(s23,s24)
	net.addLink(s23,s25)
	net.addLink(s26,s27)
	net.addLink(s26,s28)
	net.addLink(s29,s30)
	net.addLink(s29,s33)
	net.addLink(s30,s31)
	net.addLink(s30,s32)
	net.addLink(s33,s34)
	net.addLink(s33,s35)
	net.addLink(s36,s37)
	net.addLink(s36,s52)
	net.addLink(s37,s38)
	net.addLink(s37,s45)
	net.addLink(s38,s39)
	net.addLink(s38,s42)
	net.addLink(s39,s40)
	net.addLink(s39,s41)
	net.addLink(s42,s43)
	net.addLink(s42,s44)
	net.addLink(s45,s46)
	net.addLink(s45,s49)
	net.addLink(s46,s47)
	net.addLink(s46,s48)
	net.addLink(s49,s50)
	net.addLink(s49,s51)
	net.addLink(s52,s53)
	net.addLink(s52,s60)
	net.addLink(s53,s54)
	net.addLink(s53,s57)
	net.addLink(s54,s55)
	net.addLink(s54,s56)
	net.addLink(s57,s58)
	net.addLink(s57,s59)
	net.addLink(s60,s61)
	net.addLink(s60,s64)
	net.addLink(s61,s62)
	net.addLink(s61,s63)
	net.addLink(s64,s65)
	net.addLink(s64,s66)
	net.addLink(s67,s68)
	net.addLink(s67,s99)
	net.addLink(s68,s69)
	net.addLink(s68,s84)
	net.addLink(s69,s70)
	net.addLink(s69,s77)
	net.addLink(s70,s71)
	net.addLink(s70,s74)
	net.addLink(s71,s72)
	net.addLink(s71,s73)
	net.addLink(s74,s75)
	net.addLink(s74,s76)
	net.addLink(s77,s78)
	net.addLink(s77,s81)
	net.addLink(s78,s79)
	net.addLink(s78,s80)
	net.addLink(s81,s82)
	net.addLink(s81,s83)
	net.addLink(s84,s85)
	net.addLink(s84,s92)
	net.addLink(s85,s86)
	net.addLink(s85,s89)
	net.addLink(s86,s87)
	net.addLink(s86,s88)
	net.addLink(s89,s90)
	net.addLink(s89,s91)
	net.addLink(s92,s93)
	net.addLink(s92,s96)
	net.addLink(s93,s94)
	net.addLink(s93,s95)
	net.addLink(s96,s97)
	net.addLink(s96,s98)
	net.addLink(s99,s100)
	net.addLink(s99,s115)
	net.addLink(s100,s101)
	net.addLink(s100,s108)
	net.addLink(s101,s102)
	net.addLink(s101,s105)
	net.addLink(s102,s103)
	net.addLink(s102,s104)
	net.addLink(s105,s106)
	net.addLink(s105,s107)
	net.addLink(s108,s109)
	net.addLink(s108,s112)
	net.addLink(s109,s110)
	net.addLink(s109,s111)
	net.addLink(s112,s113)
	net.addLink(s112,s114)
	net.addLink(s115,s116)
	net.addLink(s115,s123)
	net.addLink(s116,s117)
	net.addLink(s116,s120)
	net.addLink(s117,s118)
	net.addLink(s117,s119)
	net.addLink(s120,s121)
	net.addLink(s120,s122)
	net.addLink(s123,s124)
	net.addLink(s123,s127)
	net.addLink(s124,s125)
	net.addLink(s124,s126)
	net.addLink(s127,s128)
	net.addLink(s127,s129)
	net.addLink(s130,s131)
	net.addLink(s130,s194)
	net.addLink(s131,s132)
	net.addLink(s131,s163)
	net.addLink(s132,s133)
	net.addLink(s132,s148)
	net.addLink(s133,s134)
	net.addLink(s133,s141)
	net.addLink(s134,s135)
	net.addLink(s134,s138)
	net.addLink(s135,s136)
	net.addLink(s135,s137)
	net.addLink(s138,s139)
	net.addLink(s138,s140)
	net.addLink(s141,s142)
	net.addLink(s141,s145)
	net.addLink(s142,s143)
	net.addLink(s142,s144)
	net.addLink(s145,s146)
	net.addLink(s145,s147)
	net.addLink(s148,s149)
	net.addLink(s148,s156)
	net.addLink(s149,s150)
	net.addLink(s149,s153)
	net.addLink(s150,s151)
	net.addLink(s150,s152)
	net.addLink(s153,s154)
	net.addLink(s153,s155)
	net.addLink(s156,s157)
	net.addLink(s156,s160)
	net.addLink(s157,s158)
	net.addLink(s157,s159)
	net.addLink(s160,s161)
	net.addLink(s160,s162)
	net.addLink(s163,s164)
	net.addLink(s163,s179)
	net.addLink(s164,s165)
	net.addLink(s164,s172)
	net.addLink(s165,s166)
	net.addLink(s165,s169)
	net.addLink(s166,s167)
	net.addLink(s166,s168)
	net.addLink(s169,s170)
	net.addLink(s169,s171)
	net.addLink(s172,s173)
	net.addLink(s172,s176)
	net.addLink(s173,s174)
	net.addLink(s173,s175)
	net.addLink(s176,s177)
	net.addLink(s176,s178)
	net.addLink(s179,s180)
	net.addLink(s179,s187)
	net.addLink(s180,s181)
	net.addLink(s180,s184)
	net.addLink(s181,s182)
	net.addLink(s181,s183)
	net.addLink(s184,s185)
	net.addLink(s184,s186)
	net.addLink(s187,s188)
	net.addLink(s187,s191)
	net.addLink(s188,s189)
	net.addLink(s188,s190)
	net.addLink(s191,s192)
	net.addLink(s191,s193)
	net.addLink(s194,s195)
	net.addLink(s194,s226)
	net.addLink(s195,s196)
	net.addLink(s195,s211)
	net.addLink(s196,s197)
	net.addLink(s196,s204)
	net.addLink(s197,s198)
	net.addLink(s197,s201)
	net.addLink(s198,s199)
	net.addLink(s198,s200)
	net.addLink(s201,s202)
	net.addLink(s201,s203)
	net.addLink(s204,s205)
	net.addLink(s204,s208)
	net.addLink(s205,s206)
	net.addLink(s205,s207)
	net.addLink(s208,s209)
	net.addLink(s208,s210)
	net.addLink(s211,s212)
	net.addLink(s211,s219)
	net.addLink(s212,s213)
	net.addLink(s212,s216)
	net.addLink(s213,s214)
	net.addLink(s213,s215)
	net.addLink(s216,s217)
	net.addLink(s216,s218)
	net.addLink(s219,s220)
	net.addLink(s219,s223)
	net.addLink(s220,s221)
	net.addLink(s220,s222)
	net.addLink(s223,s224)
	net.addLink(s223,s225)
	net.addLink(s226,s227)
	net.addLink(s226,s242)
	net.addLink(s227,s228)
	net.addLink(s227,s235)
	net.addLink(s228,s229)
	net.addLink(s228,s232)
	net.addLink(s229,s230)
	net.addLink(s229,s231)
	net.addLink(s232,s233)
	net.addLink(s232,s234)
	net.addLink(s235,s236)
	net.addLink(s235,s239)
	net.addLink(s236,s237)
	net.addLink(s236,s238)
	net.addLink(s239,s240)
	net.addLink(s239,s241)
	net.addLink(s242,s243)
	net.addLink(s242,s250)
	net.addLink(s243,s244)
	net.addLink(s243,s247)
	net.addLink(s244,s245)
	net.addLink(s244,s246)
	net.addLink(s247,s248)
	net.addLink(s247,s249)
	net.addLink(s250,s251)
	net.addLink(s250,s254)
	net.addLink(s254,s255)
	net.addLink(s254,s256)
	net.addLink(s257,s258)
	net.addLink(s257,s385)
	net.addLink(s258,s259)
	net.addLink(s258,s322)
	net.addLink(s259,s260)
	net.addLink(s259,s291)
	net.addLink(s260,s261)
	net.addLink(s260,s276)
	net.addLink(s261,s262)
	net.addLink(s261,s269)
	net.addLink(s262,s263)
	net.addLink(s262,s266)
	net.addLink(s263,s264)
	net.addLink(s263,s265)
	net.addLink(s266,s267)
	net.addLink(s266,s268)
	net.addLink(s269,s270)
	net.addLink(s269,s273)
	net.addLink(s270,s271)
	net.addLink(s270,s272)
	net.addLink(s273,s274)
	net.addLink(s273,s275)
	net.addLink(s276,s277)
	net.addLink(s276,s284)
	net.addLink(s277,s278)
	net.addLink(s277,s281)
	net.addLink(s278,s279)
	net.addLink(s278,s280)
	net.addLink(s281,s282)
	net.addLink(s281,s283)
	net.addLink(s284,s285)
	net.addLink(s284,s288)
	net.addLink(s285,s286)
	net.addLink(s285,s287)
	net.addLink(s288,s289)
	net.addLink(s288,s290)
	net.addLink(s291,s292)
	net.addLink(s291,s307)
	net.addLink(s292,s293)
	net.addLink(s292,s300)
	net.addLink(s293,s294)
	net.addLink(s293,s297)
	net.addLink(s294,s295)
	net.addLink(s294,s296)
	net.addLink(s297,s298)
	net.addLink(s297,s299)
	net.addLink(s300,s301)
	net.addLink(s300,s304)
	net.addLink(s301,s302)
	net.addLink(s301,s303)
	net.addLink(s304,s305)
	net.addLink(s304,s306)
	net.addLink(s307,s308)
	net.addLink(s307,s315)
	net.addLink(s308,s309)
	net.addLink(s308,s312)
	net.addLink(s309,s310)
	net.addLink(s309,s311)
	net.addLink(s312,s313)
	net.addLink(s312,s314)
	net.addLink(s315,s316)
	net.addLink(s315,s319)
	net.addLink(s316,s317)
	net.addLink(s316,s318)
	net.addLink(s319,s320)
	net.addLink(s319,s321)
	net.addLink(s322,s323)
	net.addLink(s322,s354)
	net.addLink(s323,s324)
	net.addLink(s323,s339)
	net.addLink(s324,s325)
	net.addLink(s324,s332)
	net.addLink(s325,s326)
	net.addLink(s325,s329)
	net.addLink(s326,s327)
	net.addLink(s326,s328)
	net.addLink(s329,s330)
	net.addLink(s329,s331)
	net.addLink(s332,s333)
	net.addLink(s332,s336)
	net.addLink(s333,s334)
	net.addLink(s333,s335)
	net.addLink(s336,s337)
	net.addLink(s336,s338)
	net.addLink(s339,s340)
	net.addLink(s339,s347)
	net.addLink(s340,s341)
	net.addLink(s340,s344)
	net.addLink(s341,s342)
	net.addLink(s341,s343)
	net.addLink(s344,s345)
	net.addLink(s344,s346)
	net.addLink(s347,s348)
	net.addLink(s347,s351)
	net.addLink(s348,s349)
	net.addLink(s348,s350)
	net.addLink(s351,s352)
	net.addLink(s351,s353)
	net.addLink(s354,s355)
	net.addLink(s354,s370)
	net.addLink(s355,s356)
	net.addLink(s355,s363)
	net.addLink(s356,s357)
	net.addLink(s356,s360)
	net.addLink(s357,s358)
	net.addLink(s357,s359)
	net.addLink(s360,s361)
	net.addLink(s360,s362)
	net.addLink(s363,s364)
	net.addLink(s363,s367)
	net.addLink(s364,s365)
	net.addLink(s364,s366)
	net.addLink(s367,s368)
	net.addLink(s367,s369)
	net.addLink(s370,s371)
	net.addLink(s370,s378)
	net.addLink(s371,s372)
	net.addLink(s371,s375)
	net.addLink(s372,s373)
	net.addLink(s372,s374)
	net.addLink(s375,s376)
	net.addLink(s375,s377)
	net.addLink(s378,s379)
	net.addLink(s378,s382)
	net.addLink(s379,s380)
	net.addLink(s379,s381)
	net.addLink(s382,s383)
	net.addLink(s382,s384)
	net.addLink(s385,s386)
	net.addLink(s385,s449)
	net.addLink(s386,s387)
	net.addLink(s386,s418)
	net.addLink(s387,s388)
	net.addLink(s387,s403)
	net.addLink(s388,s389)
	net.addLink(s388,s396)
	net.addLink(s389,s390)
	net.addLink(s389,s393)
	net.addLink(s390,s391)
	net.addLink(s390,s392)
	net.addLink(s393,s394)
	net.addLink(s393,s395)
	net.addLink(s396,s397)
	net.addLink(s396,s400)
	net.addLink(s397,s398)
	net.addLink(s397,s399)
	net.addLink(s400,s401)
	net.addLink(s400,s402)
	net.addLink(s403,s404)
	net.addLink(s403,s411)
	net.addLink(s404,s405)
	net.addLink(s404,s408)
	net.addLink(s405,s406)
	net.addLink(s405,s407)
	net.addLink(s408,s409)
	net.addLink(s408,s410)
	net.addLink(s411,s412)
	net.addLink(s411,s415)
	net.addLink(s412,s413)
	net.addLink(s412,s414)
	net.addLink(s415,s416)
	net.addLink(s415,s417)
	net.addLink(s418,s419)
	net.addLink(s418,s434)
	net.addLink(s419,s420)
	net.addLink(s419,s427)
	net.addLink(s420,s421)
	net.addLink(s420,s424)
	net.addLink(s421,s422)
	net.addLink(s421,s423)
	net.addLink(s424,s425)
	net.addLink(s424,s426)
	net.addLink(s427,s428)
	net.addLink(s427,s431)
	net.addLink(s428,s429)
	net.addLink(s428,s430)
	net.addLink(s431,s432)
	net.addLink(s431,s433)
	net.addLink(s434,s435)
	net.addLink(s434,s442)
	net.addLink(s435,s436)
	net.addLink(s435,s439)
	net.addLink(s436,s437)
	net.addLink(s436,s438)
	net.addLink(s439,s440)
	net.addLink(s439,s441)
	net.addLink(s442,s443)
	net.addLink(s442,s446)
	net.addLink(s443,s444)
	net.addLink(s443,s445)
	net.addLink(s446,s447)
	net.addLink(s446,s448)
	net.addLink(s449,s450)
	net.addLink(s449,s481)
	net.addLink(s450,s451)
	net.addLink(s450,s466)
	net.addLink(s451,s452)
	net.addLink(s451,s459)
	net.addLink(s452,s453)
	net.addLink(s452,s456)
	net.addLink(s453,s454)
	net.addLink(s453,s455)
	net.addLink(s456,s457)
	net.addLink(s456,s458)
	net.addLink(s459,s460)
	net.addLink(s459,s463)
	net.addLink(s460,s461)
	net.addLink(s460,s462)
	net.addLink(s463,s464)
	net.addLink(s463,s465)
	net.addLink(s466,s467)
	net.addLink(s466,s474)
	net.addLink(s467,s468)
	net.addLink(s467,s471)
	net.addLink(s468,s469)
	net.addLink(s468,s470)
	net.addLink(s471,s472)
	net.addLink(s471,s473)
	net.addLink(s474,s475)
	net.addLink(s474,s478)
	net.addLink(s475,s476)
	net.addLink(s475,s477)
	net.addLink(s478,s479)
	net.addLink(s478,s480)
	net.addLink(s481,s482)
	net.addLink(s481,s497)
	net.addLink(s482,s483)
	net.addLink(s482,s490)
	net.addLink(s483,s484)
	net.addLink(s483,s487)
	net.addLink(s484,s485)
	net.addLink(s484,s486)
	net.addLink(s487,s488)
	net.addLink(s487,s489)
	net.addLink(s490,s491)
	net.addLink(s490,s494)
	net.addLink(s491,s492)
	net.addLink(s491,s493)
	net.addLink(s494,s495)
	net.addLink(s494,s496)
	net.addLink(s497,s498)
	net.addLink(s497,s505)
	net.addLink(s498,s499)
	net.addLink(s498,s502)
	net.addLink(s499,s500)
	net.addLink(s499,s501)
	net.addLink(s502,s503)
	net.addLink(s502,s504)
	net.addLink(s505,s506)
	net.addLink(s505,s509)
	net.addLink(s506,s507)
	net.addLink(s506,s508)
	net.addLink(s509,s510)
	net.addLink(s509,s511)
	net.addLink(s251,s252)
	net.addLink(s251,s253)

	net.addLink(h1,s30)
	net.addLink(h2,s500)


	net.start()
	CLI( net )
	net.stop()
