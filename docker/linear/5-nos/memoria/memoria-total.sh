# /bin/bash
echo "Contador Consumo" >>"topologia-linear5-memoria".ods
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



intervalo=1073741824


while [ $i -lt $tempo ]
do
	val0=`cat /sys/fs/cgroup/memory/docker/$c/memory.usage_in_bytes`
	val1=`cat /sys/fs/cgroup/memory/docker/$s0/memory.usage_in_bytes`
	val2=`cat /sys/fs/cgroup/memory/docker/$s1/memory.usage_in_bytes`
	val3=`cat /sys/fs/cgroup/memory/docker/$s2/memory.usage_in_bytes`
	val4=`cat /sys/fs/cgroup/memory/docker/$s3/memory.usage_in_bytes`
	val5=`cat /sys/fs/cgroup/memory/docker/$s4/memory.usage_in_bytes`

	val32=`cat /sys/fs/cgroup/memory/docker/$h0/memory.usage_in_bytes`
	val33=`cat /sys/fs/cgroup/memory/docker/$h1/memory.usage_in_bytes`



	resul=`echo "scale=4 ; (($val0+$val1+$val2+$val3+$val4+$val5+$val32+$val33)/$intervalo)"  | bc`
	#echo $i $(cat /sys/fs/cgroup/memory/docker/$c/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s0/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s1/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s2/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s3/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s4/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s5/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s6/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s7/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s8/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s9/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s10/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s11/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s12/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s13/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s14/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s15/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s16/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s17/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s18/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s19/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s20/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s21/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s22/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s23/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$s24/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h0/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h1/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h2/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h3/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h4/memory.usage_in_bytes | awk '{print $1/1048576}') $(cat /sys/fs/cgroup/memory/docker/$h5/memory.usage_in_bytes | awk '{print $1/1048576}') >>"controlando".ods
	echo $i $resul >>"topologia-linear5-memoria".ods

	sleep 2
	i=`expr $i + 1`
done
