# /bin/bash
echo "Contador cpu$" >>"cpu-linear30-total-docker".ods
i=0
tempo=300
c=
c="c3b73567b036f4374cd10f8aec5972287e92c14320eb7532d38f49e66e0b0d21"
s0="82386e5e43eb602c2696af89fd57174fc47804f3203f7845e01b85b3de834732"
s1="bc13ff90f5f5de2c64f864867778d8430e330fa84256da765c127bff577f4148"
s2="e313d326f1240d768970d8fa70f66b3eab121e80a36c7b316198f7858a977b64"
s3="a1b8dc0a43b47c3d65397b1b7293906b293cd0da1a72035f81ed4cb825d5105c"
s4="76aa94a6e05a2f366cc20bc7c9fcf53e0c28c58391834a5b26a6a2bb2699740d"
s5="e4595a91ed7b314c3560f218ef2f82674dbce45cca8b72093c1814f8e0cdf66b"
s6="bd336ad0fcf4455ab75a377ab23c4227428566840fa7573d14d429ba42a1e559"
s7="590f8d6fd90244673819b4434c8ff44c8f55619568c591298aa20b0c5aad300f"
s8="5a985730883d154539779be1045c24685dcf8f05d427c412984f21edd761ba6e"
s9="8c692617c733da19313e93e214a7d5496b437f087a64786c6edc69d131d08322"
s10="238c105bc6add10999b6402e54857f420ad0cfa987d1f160b6626b2f37c72f72"
s11="e63ad478fd915a19b97742f5d01d3c37ef89bbbaf794d531231ba04b024c3234"
s12="e1345f8f3d3b9009b135ba5dd13ae37bdecaa0475e98f35a778f83c2d1e60462"
s13="8cd73a03de34af5dcd4af7f2df11972c54ab968ba37d47162ed7ab2077843132"
s14="b9c9d000c27e32169b62f03996f3654f9c3e5b934aeb1033281921eec8d34037"
s15="e65654901e6dd2707995efcf94ac1a1f79a72ea418713628db8b7be7f9a0921e"
s16="4ea4ea71d6aad44fc5fa558c2f0b6c7ea17660c00034f15d4f634ce058f58a7d"
s17="6bb8e725d9597d4477595e820c7fb81b9e0d0fe09aacdd08bb459ac7e2f9c12c"
s18="26314cb95b97ff6c8751fdbd7067d402ff6a4a2426a47d6c41b1e5d979a64e0f"
s19="0a79111792382a15e7f44293dc082c2b67a3cd5be2dd65457914d3e58a20526d"
s20="70b0891cd10e637dedc76f792c72d7729d36bdfc0a79ac30e72f32f3825a683a"
s21="4e6eca3f64c21071ef04c91193359056192dbab12ec5006c8063e9da1155245f"
s22="cc936389b3b2681baeff79f5e3460a01a46417bf36294504511a49116a5ccd50"
s23="214656c9f94412204b6c07311e62e7337396c4704cc6ad3e6ec7688eaf3acf50"
s24="0c34f3f39feb3c74729bfdc5296a0051d67f56c588909525e6d7fde5151e8e05"
s25="9e381fa8654db76f1f3e8d12e2ff584c6ac1aed46807b410aac68a91fce5632e"
s26="195f565a2db3ff6d6ab776c6f9a2ab3fae758de849cea1266c8157853d132111"
s27="963c2836b92680756da397490f134454a0fefe25401545719d0c787338666d5c"
s28="7c3764068ce3fb27fe0dde57273eac6cfcefe93fb467cd2bf299ea9eb124e221"
s29="9eb6eeb97e0c533429c56a33385ffd3dd272ed71dc82ad43e1e089de4fce4d45"
s30="dc3d910c79f5e045edec1b0c74ad0e35ea4584c5126ac53e19e4a067dc06ed5c"
h0="1dcd11312f54136b58742513837c131e598e04956589ae5e6f3b59d78018a71f"
h1="39b541a6cb48c101221debc8c6ce2c4d447e045a1d519e041a18d67ed99ba115"
h2="e9b761e5d216df7804eb8e25c09b6071e1774d00fe0f7f44a3e67b24b883302f"
h3="0b262bb78b75a125cad0c71696bad95285e2d1be2d08884a93bde3e143defb71"
h4="03d00b9b51ff244ddd03c501249d14036ce7e29c22f7a86676dc7d7c283ae330"
h5="8c6034472ed68c52ac64032e783f6466314fad37e7321f58de02bf0c3b4f8072"
h6="152fa4c71ac9853fd67f27e46ec56c4ca32beb01282ab068e4160583af873e02"
h7="f618fd276c432a607cb578af0285f9033896af3bbb825156e248bcdeba2d063d"
h8="33e4dfbc11183d5925437ebe1c8f2d530c4d4d50840acd414c0464f6a23e5139"
h9="7b44a28f0655ed48ce1a0fe39eeebf507722e7646ef772403f03699cabad5a02"
h10="51d11bbe6d0fda1fd5f478c03bf7b16ac6c6bbceacfba608978ce8c2c48e4e04"
h11="efc8d11806ffe1522be5d019b103702ac5f7e5c0146032fcaa4150cabfb20a40"
h12="c2dddc272733eb7463d2daf856e0fc1854c36b957c6b952b7586267ef0926e23"
h13="4d2574fdd461305353e63007e82fde2191cdd8d9ebb2b05c50472b5e05648151"
h14="c334fbe0314b2e356bd60e01ef2de0044ca16b93a24c102408323ff3bd731538"
h15="f697e3833af3bb666284184943a22c389c8e455499b9d01c62beb83e6966852c"



intervalo=1000000000


while true 
do	
	c1=`cat /sys/fs/cgroup/cpuacct/docker/$c/cpuacct.usage`
	sw0=`cat /sys/fs/cgroup/cpuacct/docker/$s0/cpuacct.usage`
	sw1=`cat /sys/fs/cgroup/cpuacct/docker/$s1/cpuacct.usage`
	sw2=`cat /sys/fs/cgroup/cpuacct/docker/$s2/cpuacct.usage`
	sw3=`cat /sys/fs/cgroup/cpuacct/docker/$s3/cpuacct.usage`
	sw4=`cat /sys/fs/cgroup/cpuacct/docker/$s4/cpuacct.usage`
	sw5=`cat /sys/fs/cgroup/cpuacct/docker/$s5/cpuacct.usage`
	sw6=`cat /sys/fs/cgroup/cpuacct/docker/$s6/cpuacct.usage`
	sw7=`cat /sys/fs/cgroup/cpuacct/docker/$s7/cpuacct.usage`
	sw8=`cat /sys/fs/cgroup/cpuacct/docker/$s8/cpuacct.usage`
	sw9=`cat /sys/fs/cgroup/cpuacct/docker/$s9/cpuacct.usage`
	sw10=`cat /sys/fs/cgroup/cpuacct/docker/$s10/cpuacct.usage`
	sw11=`cat /sys/fs/cgroup/cpuacct/docker/$s11/cpuacct.usage`
	sw12=`cat /sys/fs/cgroup/cpuacct/docker/$s12/cpuacct.usage`
	sw13=`cat /sys/fs/cgroup/cpuacct/docker/$s13/cpuacct.usage`
	sw14=`cat /sys/fs/cgroup/cpuacct/docker/$s14/cpuacct.usage`
	sw15=`cat /sys/fs/cgroup/cpuacct/docker/$s15/cpuacct.usage`
	sw16=`cat /sys/fs/cgroup/cpuacct/docker/$s16/cpuacct.usage`
	sw17=`cat /sys/fs/cgroup/cpuacct/docker/$s17/cpuacct.usage`
	sw18=`cat /sys/fs/cgroup/cpuacct/docker/$s18/cpuacct.usage`
	sw19=`cat /sys/fs/cgroup/cpuacct/docker/$s19/cpuacct.usage`
	sw20=`cat /sys/fs/cgroup/cpuacct/docker/$s20/cpuacct.usage`
	sw21=`cat /sys/fs/cgroup/cpuacct/docker/$s21/cpuacct.usage`
	sw22=`cat /sys/fs/cgroup/cpuacct/docker/$s22/cpuacct.usage`
	sw23=`cat /sys/fs/cgroup/cpuacct/docker/$s23/cpuacct.usage`
	sw24=`cat /sys/fs/cgroup/cpuacct/docker/$s24/cpuacct.usage`
	sw25=`cat /sys/fs/cgroup/cpuacct/docker/$s25/cpuacct.usage`
	sw26=`cat /sys/fs/cgroup/cpuacct/docker/$s26/cpuacct.usage`
	sw27=`cat /sys/fs/cgroup/cpuacct/docker/$s27/cpuacct.usage`
	sw28=`cat /sys/fs/cgroup/cpuacct/docker/$s28/cpuacct.usage`
	sw29=`cat /sys/fs/cgroup/cpuacct/docker/$s29/cpuacct.usage`
	#sw30=`cat /sys/fs/cgroup/cpuacct/docker/$s30/cpuacct.usage`
	ht0=`cat /sys/fs/cgroup/cpuacct/docker/$h0/cpuacct.usage`
	ht1=`cat /sys/fs/cgroup/cpuacct/docker/$h1/cpuacct.usage`
	#ht2=`cat /sys/fs/cgroup/cpuacct/docker/$h2/cpuacct.usage`
	#ht3=`cat /sys/fs/cgroup/cpuacct/docker/$h3/cpuacct.usage`
	#ht4=`cat /sys/fs/cgroup/cpuacct/docker/$h4/cpuacct.usage`
	#ht5=`cat /sys/fs/cgroup/cpuacct/docker/$h5/cpuacct.usage`
	#ht6=`cat /sys/fs/cgroup/cpuacct/docker/$h6/cpuacct.usage`
	#ht7=`cat /sys/fs/cgroup/cpuacct/docker/$h7/cpuacct.usage`
	#ht8=`cat /sys/fs/cgroup/cpuacct/docker/$h8/cpuacct.usage`
	#ht9=`cat /sys/fs/cgroup/cpuacct/docker/$h9/cpuacct.usage`
	#ht10=`cat /sys/fs/cgroup/cpuacct/docker/$h10/cpuacct.usage`
	#ht11=`cat /sys/fs/cgroup/cpuacct/docker/$h11/cpuacct.usage`
	#ht12=`cat /sys/fs/cgroup/cpuacct/docker/$h12/cpuacct.usage`
	#ht13=`cat /sys/fs/cgroup/cpuacct/docker/$h13/cpuacct.usage`
	#ht14=`cat /sys/fs/cgroup/cpuacct/docker/$h14/cpuacct.usage`
	#ht15=`cat /sys/fs/cgroup/cpuacct/docker/$h15/cpuacct.usage`

	sleep 1

	c2=`cat /sys/fs/cgroup/cpuacct/docker/$c/cpuacct.usage`
	sw00=`cat /sys/fs/cgroup/cpuacct/docker/$s0/cpuacct.usage`
	sw01=`cat /sys/fs/cgroup/cpuacct/docker/$s1/cpuacct.usage`
	sw02=`cat /sys/fs/cgroup/cpuacct/docker/$s2/cpuacct.usage`
	sw03=`cat /sys/fs/cgroup/cpuacct/docker/$s3/cpuacct.usage`
	sw04=`cat /sys/fs/cgroup/cpuacct/docker/$s4/cpuacct.usage`
	sw05=`cat /sys/fs/cgroup/cpuacct/docker/$s5/cpuacct.usage`
	sw06=`cat /sys/fs/cgroup/cpuacct/docker/$s6/cpuacct.usage`
	sw07=`cat /sys/fs/cgroup/cpuacct/docker/$s7/cpuacct.usage`
	sw08=`cat /sys/fs/cgroup/cpuacct/docker/$s8/cpuacct.usage`
	sw09=`cat /sys/fs/cgroup/cpuacct/docker/$s9/cpuacct.usage`
	sw010=`cat /sys/fs/cgroup/cpuacct/docker/$s10/cpuacct.usage`
	sw011=`cat /sys/fs/cgroup/cpuacct/docker/$s11/cpuacct.usage`
	sw012=`cat /sys/fs/cgroup/cpuacct/docker/$s12/cpuacct.usage`
	sw013=`cat /sys/fs/cgroup/cpuacct/docker/$s13/cpuacct.usage`
	sw014=`cat /sys/fs/cgroup/cpuacct/docker/$s14/cpuacct.usage`
	sw015=`cat /sys/fs/cgroup/cpuacct/docker/$s15/cpuacct.usage`
	sw016=`cat /sys/fs/cgroup/cpuacct/docker/$s16/cpuacct.usage`
	sw017=`cat /sys/fs/cgroup/cpuacct/docker/$s17/cpuacct.usage`
	sw018=`cat /sys/fs/cgroup/cpuacct/docker/$s18/cpuacct.usage`
	sw019=`cat /sys/fs/cgroup/cpuacct/docker/$s19/cpuacct.usage`
	sw020=`cat /sys/fs/cgroup/cpuacct/docker/$s20/cpuacct.usage`
	sw021=`cat /sys/fs/cgroup/cpuacct/docker/$s21/cpuacct.usage`
	sw022=`cat /sys/fs/cgroup/cpuacct/docker/$s22/cpuacct.usage`
	sw023=`cat /sys/fs/cgroup/cpuacct/docker/$s23/cpuacct.usage`
	sw024=`cat /sys/fs/cgroup/cpuacct/docker/$s24/cpuacct.usage`
	sw025=`cat /sys/fs/cgroup/cpuacct/docker/$s25/cpuacct.usage`
	sw026=`cat /sys/fs/cgroup/cpuacct/docker/$s26/cpuacct.usage`
	sw027=`cat /sys/fs/cgroup/cpuacct/docker/$s27/cpuacct.usage`
	sw028=`cat /sys/fs/cgroup/cpuacct/docker/$s28/cpuacct.usage`
	sw029=`cat /sys/fs/cgroup/cpuacct/docker/$s29/cpuacct.usage`
	#sw030=`cat /sys/fs/cgroup/cpuacct/docker/$s30/cpuacct.usage`
	ht00=`cat /sys/fs/cgroup/cpuacct/docker/$h0/cpuacct.usage`
	ht01=`cat /sys/fs/cgroup/cpuacct/docker/$h1/cpuacct.usage`
	#ht02=`cat /sys/fs/cgroup/cpuacct/docker/$h2/cpuacct.usage`
	#ht03=`cat /sys/fs/cgroup/cpuacct/docker/$h3/cpuacct.usage`
	#ht04=`cat /sys/fs/cgroup/cpuacct/docker/$h4/cpuacct.usage`
	#ht05=`cat /sys/fs/cgroup/cpuacct/docker/$h5/cpuacct.usage`
	#ht06=`cat /sys/fs/cgroup/cpuacct/docker/$h6/cpuacct.usage`
	#ht07=`cat /sys/fs/cgroup/cpuacct/docker/$h7/cpuacct.usage`
	#ht08=`cat /sys/fs/cgroup/cpuacct/docker/$h8/cpuacct.usage`
	#ht09=`cat /sys/fs/cgroup/cpuacct/docker/$h9/cpuacct.usage`
	#ht010=`cat /sys/fs/cgroup/cpuacct/docker/$h10/cpuacct.usage`
	#ht011=`cat /sys/fs/cgroup/cpuacct/docker/$h11/cpuacct.usage`
	#ht012=`cat /sys/fs/cgroup/cpuacct/docker/$h12/cpuacct.usage`
	#ht013=`cat /sys/fs/cgroup/cpuacct/docker/$h13/cpuacct.usage`
	#ht014=`cat /sys/fs/cgroup/cpuacct/docker/$h14/cpuacct.usage`
	#ht015=`cat /sys/fs/cgroup/cpuacct/docker/$h15/cpuacct.usage`
	
	contr=`echo "scale=4 ; (($c2 - $c1)/$intervalo)*100"  | bc`
	stch0=`echo "scale=4 ; (($sw00 - $sw0)/$intervalo)*100"  | bc`
	stch1=`echo "scale=4 ; (($sw01 - $sw1)/$intervalo)*100"  | bc`
	stch2=`echo "scale=4 ; (($sw02 - $sw2)/$intervalo)*100"  | bc`
	stch3=`echo "scale=4 ; (($sw03 - $sw3)/$intervalo)*100"  | bc`
	stch4=`echo "scale=4 ; (($sw04 - $sw4)/$intervalo)*100"  | bc`
	stch5=`echo "scale=4 ; (($sw05 - $sw5)/$intervalo)*100"  | bc`
	stch6=`echo "scale=4 ; (($sw06 - $sw6)/$intervalo)*100"  | bc`
	stch7=`echo "scale=4 ; (($sw07 - $sw7)/$intervalo)*100"  | bc`
	stch8=`echo "scale=4 ; (($sw08 - $sw8)/$intervalo)*100"  | bc`
	stch9=`echo "scale=4 ; (($sw09 - $sw9)/$intervalo)*100"  | bc`
	stch10=`echo "scale=4 ; (($sw010 - $sw10)/$intervalo)*100"  | bc`
	stch11=`echo "scale=4 ; (($sw011 - $sw11)/$intervalo)*100"  | bc`
	stch12=`echo "scale=4 ; (($sw012 - $sw12)/$intervalo)*100"  | bc`
	stch13=`echo "scale=4 ; (($sw013 - $sw13)/$intervalo)*100"  | bc`
	stch14=`echo "scale=4 ; (($sw014 - $sw14)/$intervalo)*100"  | bc`
	stch15=`echo "scale=4 ; (($sw015 - $sw15)/$intervalo)*100"  | bc`
	stch16=`echo "scale=4 ; (($sw016 - $sw16)/$intervalo)*100"  | bc`
	stch17=`echo "scale=4 ; (($sw017 - $sw17)/$intervalo)*100"  | bc`
	stch18=`echo "scale=4 ; (($sw018 - $sw18)/$intervalo)*100"  | bc`
	stch19=`echo "scale=4 ; (($sw019 - $sw19)/$intervalo)*100"  | bc`
	stch20=`echo "scale=4 ; (($sw020 - $sw20)/$intervalo)*100"  | bc`
	stch21=`echo "scale=4 ; (($sw021 - $sw21)/$intervalo)*100"  | bc`
	stch22=`echo "scale=4 ; (($sw022 - $sw22)/$intervalo)*100"  | bc`
	stch23=`echo "scale=4 ; (($sw023 - $sw23)/$intervalo)*100"  | bc`
	stch24=`echo "scale=4 ; (($sw024 - $sw24)/$intervalo)*100"  | bc`
	stch25=`echo "scale=4 ; (($sw025 - $sw25)/$intervalo)*100"  | bc`
	stch26=`echo "scale=4 ; (($sw026 - $sw26)/$intervalo)*100"  | bc`
	stch27=`echo "scale=4 ; (($sw027 - $sw27)/$intervalo)*100"  | bc`
	stch28=`echo "scale=4 ; (($sw028 - $sw28)/$intervalo)*100"  | bc`
	stch29=`echo "scale=4 ; (($sw029 - $sw29)/$intervalo)*100"  | bc`
	#stch30=`echo "scale=4 ; (($sw030 - $sw30)/$intervalo)*100"  | bc`
	host0=`echo "scale=4 ; (($ht00 - $ht0)/$intervalo)*100"  | bc`
	host1=`echo "scale=4 ; (($ht01 - $ht1)/$intervalo)*100"  | bc`
	#host2=`echo "scale=4 ; (($ht02 - $ht2)/$intervalo)*100"  | bc`
	#host3=`echo "scale=4 ; (($ht03 - $ht3)/$intervalo)*100"  | bc`
	#host4=`echo "scale=4 ; (($ht04 - $ht4)/$intervalo)*100"  | bc`
	#host5=`echo "scale=4 ; (($ht05 - $ht5)/$intervalo)*100"  | bc`
	#host6=`echo "scale=4 ; (($ht06 - $ht6)/$intervalo)*100"  | bc`
	#host7=`echo "scale=4 ; (($ht07 - $ht7)/$intervalo)*100"  | bc`
	#host8=`echo "scale=4 ; (($ht08 - $ht8)/$intervalo)*100"  | bc`
	#host9=`echo "scale=4 ; (($ht09 - $ht9)/$intervalo)*100"  | bc`
	#host10=`echo "scale=4 ; (($ht010 - $ht10)/$intervalo)*100"  | bc`
	#host11=`echo "scale=4 ; (($ht011 - $ht11)/$intervalo)*100"  | bc`
	#host12=`echo "scale=4 ; (($ht012 - $ht12)/$intervalo)*100"  | bc`
	#host13=`echo "scale=4 ; (($ht013 - $ht13)/$intervalo)*100"  | bc`
	#host14=`echo "scale=4 ; (($ht014 - $ht14)/$intervalo)*100"  | bc`
	#host15=`echo "scale=4 ; (($ht015 - $ht15)/$intervalo)*100"  | bc`

	#cpu_total=`echo "scale=4 ; ($contr+$stch0+$stch1+$stch2+$stch3+$stch4+$stch5+$stch6+$stch7+$stch8+$stch9+$stch10+$stch11+$stch012+$stch13+$stch14+$stch15+$stch16+$stch17+$stch18+$stch19+$stch20+$stch21+$stch22+$stch23+$stch24+$stch25+$stch26+$stch27+$stch28+$stch29+$stch30+$host0+$host1+$host2+$host3+$host4+$host5+$host6+$host7+$host8+$host9+$host10+$host11+$host12+$host13+$host14+$host15)"  | bc`
	cpu_total=`echo "scale=4 ; ($contr+$stch0+$stch1+$stch2+$stch3+$stch4+$stch5+$stch6+$stch7+$stch8+$stch9+$stch10+$stch11+$stch12+$stch13+$stch14+$stch15+$stch16+$stch17+$stch18+$stch19+$stch20+$stch21+$stch22+$stch23+$stch24+$stch25+$stch26+$stch27+$stch28+$stch29+$host0+$host1)" | bc`
	echo $cpu_total >>"cpu-linear30-total-docker".ods
	i=`expr $i + 1`
done
