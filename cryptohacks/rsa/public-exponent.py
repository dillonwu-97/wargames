import gmpy2
import hashlib
import owiener
from sympy.ntheory.modular import crt 
from libnum import solve_crt

def trans(x):
	return bytes.fromhex(hex(x)[2:]).decode("ascii")

def salty():
	n = 110581795715958566206600392161360212579669637391437097703685154237017351570464767725324182051199901920318211290404777259728923614917211291562555864753005179326101890427669819834642007924406862482343614488768256951616086287044725034412802176312273081322195866046098595306261781788276570920467840172004530873767                                                                  
	e = 1
	ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485
	return bytes.fromhex(hex(ct)[2:])

def modulus_inutilis():
	n = 17258212916191948536348548470938004244269544560039009244721959293554822498047075403658429865201816363311805874117705688359853941515579440852166618074161313773416434156467811969628473425365608002907061241714688204565170146117869742910273064909154666642642308154422770994836108669814632309362483307560217924183202838588431342622551598499747369771295105890359290073146330677383341121242366368309126850094371525078749496850520075015636716490087482193603562501577348571256210991732071282478547626856068209192987351212490642903450263288650415552403935705444809043563866466823492258216747445926536608548665086042098252335883
	e = 3
	ct = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957
	gmpy2.get_context().precision=1000
	plaintext = int(gmpy2.cbrt(ct))
	return trans(plaintext)

def everything_is_big():
	N = 0x8da7d2ec7bf9b322a539afb9962d4d2ebeb3e3d449d709b80a51dc680a14c87ffa863edfc7b5a2a542a0fa610febe2d967b58ae714c46a6eccb44cd5c90d1cf5e271224aa3367e5a13305f2744e2e56059b17bf520c95d521d34fdad3b0c12e7821a3169aa900c711e6923ca1a26c71fc5ac8a9ff8c878164e2434c724b68b508a030f86211c1307b6f90c0cd489a27fdc5e6190f6193447e0441a49edde165cf6074994ea260a21ea1fc7e2dfb038df437f02b9ddb7b5244a9620c8eca858865e83bab3413135e76a54ee718f4e431c29d3cb6e353a75d74f831bed2cc7bdce553f25b617b3bdd9ef901e249e43545c91b0cd8798b27804d61926e317a2b745
	e = 0x86d357db4e1b60a2e9f9f25e2db15204c820b6e8d8d04d29db168c890bc8a6c1e31b9316c9680174e128515a00256b775a1a8ccca9c6936f1b4c2298c03032cda4dd8eca1145828d31466bf56bfcf0c6a8b4a1b2fb27de7a57fae7430048d7590734b2f05b6443ad60d89606802409d2fa4c6767ad42bffae01a8ef1364418362e133fa7b2770af64a68ad50ad8d2bd5cebb99ceb13368fb31a6e7503e753f8638e21a96af1b6498c18578ba89b98d70fa482ad137d28fe701b4b77baa25d5e84c81b26ee9bddf8cbb51a071c60dd57714de379cd4bc14932809ba18524a0a18e4133665cfc46e2c4fcfbc28e0a0957e5513a7307c422b87a6182d0b6a074b4d
	c = 0x6a2f2e401a54eeb5dab1e6d5d80e92a6ca189049e22844c825012b8f0578f95b269b19644c7c8af3d544840d380ed75fdf86844aa8976622fa0501eaec0e5a1a5ab09d3d1037e55501c4e270060470c9f4019ced6c4e67673843daf2fd71c64f3dd8939ae322f2b79d283b3382052d076ebe9bb50b0042f1f7dd7beadf0f5686926ade9fc8370283ead781a21896e7a878d99e77c3bb1f470401062c0e0327fd85da1cf12901635f1df310e8f8c7d87aff5a01dbbecd739cd8f36462060d0eb237af8d613e2d9cebb67d612bcfc353ef2cd44b7ac85e471287eb04ae9b388b66ea8eb32429ae96dba5da8206894fa8c58a7440a127fceb5717a2eaa3c29f25f7
	
	# brute force not working
	# d_values = [2,3,5,17,257,65537]
	# for d in d_values:
	# for d in range(33521, 66000, 2):
	# 	print(d)
	# 	temp = pow(c, d, N)
	# 	if (pow(temp, e, N) == c):
	# 		print(d)
	# 		return temp

	# try weiner's attack instead
	d = owiener.attack(e, N)
	plaintext = pow(c, d, N)
	return trans(plaintext)

# this problem involves finding p and q
def crossed_wires():
	encrypted_flag = 20304610279578186738172766224224793119885071262464464448863461184092225736054747976985179673905441502689126216282897704508745403799054734121583968853999791604281615154100736259131453424385364324630229671185343778172807262640709301838274824603101692485662726226902121105591137437331463201881264245562214012160875177167442010952439360623396658974413900469093836794752270399520074596329058725874834082188697377597949405779039139194196065364426213208345461407030771089787529200057105746584493554722790592530472869581310117300343461207750821737840042745530876391793484035024644475535353227851321505537398888106855012746117
	original = encrypted_flag
	friends_public_keys = [(21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 106979), (21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 108533), (21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 69557), (21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 97117), (21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 103231)]
	private_key = (21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771, 2734411677251148030723138005716109733838866545375527602018255159319631026653190783670493107936401603981429171880504360560494771017246468702902647370954220312452541342858747590576273775107870450853533717116684326976263006435733382045807971890762018747729574021057430331778033982359184838159747331236538501849965329264774927607570410347019418407451937875684373454982306923178403161216817237890962651214718831954215200637651103907209347900857824722653217179548148145687181377220544864521808230122730967452981435355334932104265488075777638608041325256776275200067541533022527964743478554948792578057708522350812154888097)
	N = friends_public_keys[0][0]
	friends_exponents = [i[1] for i in friends_public_keys]
	d = private_key[1]
	my_e = 0x10001
	# print(e)
	# print(my_e)

	ed = my_e * d
	# print(ed)
	gmpy2.get_context().precision=10000
	# my_ed * d = phi(n) * k + 1
	# print (my_e * d - 1) # <-- this is a multiple of phi(n)
	# the range is 1 -> e for k 
	p = -1
	q = -1
	for k in range(1, my_e):
		temp = (ed-1)
		if temp % k == 0:
			temp //= k # phi(n) possibility
			p_plus_q = N + 1 - temp
			# ((p+q) + sqrt((p+q)2 - 4*pq))/2
			sqrt_check = gmpy2.is_square( pow(p_plus_q, 2) - 4 * N)
			if sqrt_check == True:
				# p = ((p+q) + sqrt((p+q)2 - 4*pq))/2
				# q = ((p+q) - sqrt((p+q)2 - 4*pq))/2
				p = (p_plus_q + gmpy2.sqrt( pow(p_plus_q, 2) - 4 * N)) //2
				p = int(p)
				q = (p_plus_q - gmpy2.sqrt( pow(p_plus_q, 2) - 4 * N)) //2
				q = int(q)

	# after finding p and q, calculate phi(n) for real
	assert (p * q == N)
	phi = (p-1) * (q-1)

	# for each encryption step for friend's public keys, reverse the encryption
	# start from last item in list and go to first
	# observation: order of decryption doesn't matter?
	my_d = d
	# encrypted_flag= pow(encrypted_flag, my_d, N)
	# friends_exponents.reverse()
	# print(friends_exponents)
	for e in friends_exponents:
		d = gmpy2.invert(e, phi)
		# print(d*e % phi) # just checking
		encrypted_flag = pow(encrypted_flag, d, N)

	return trans(encrypted_flag)

def everything_is_still_big():
	N = 0x665166804cd78e8197073f65f58bca14e019982245fcc7cad74535e948a4e0258b2e919bf3720968a00e5240c5e1d6b8831d8fec300d969fccec6cce11dde826d3fbe0837194f2dc64194c78379440671563c6c75267f0286d779e6d91d3e9037c642a860a894d8c45b7ed564d341501cedf260d3019234f2964ccc6c56b6de8a4f66667e9672a03f6c29d95100cdf5cb363d66f2131823a953621680300ab3a2eb51c12999b6d4249dde499055584925399f3a8c7a4a5a21f095878e80bbc772f785d2cbf70a87c6b854eb566e1e1beb7d4ac6eb46023b3dc7fdf34529a40f5fc5797f9c15c54ed4cb018c072168e9c30ca3602e00ea4047d2e5686c6eb37b9
	e = 0x2c998e57bc651fe4807443dbb3e794711ca22b473d7792a64b7a326538dc528a17c79c72e425bf29937e47b2d6f6330ee5c13bfd8564b50e49132d47befd0ee2e85f4bfe2c9452d62ef838d487c099b3d7c80f14e362b3d97ca4774f1e4e851d38a4a834b077ded3d40cd20ddc45d57581beaa7b4d299da9dec8a1f361c808637238fa368e07c7d08f5654c7b2f8a90d47857e9b9c0a81a46769f6307d5a4442707afb017959d9a681fa1dc8d97565e55f02df34b04a3d0a0bf98b7798d7084db4b3f6696fa139f83ada3dc70d0b4c57bf49f530dec938096071f9c4498fdef9641dfbfe516c985b27d1748cc6ce1a4beb1381fb165a3d14f61032e0f76f095d
	c = 0x503d5dd3bf3d76918b868c0789c81b4a384184ddadef81142eabdcb78656632e54c9cb22ac2c41178607aa41adebdf89cd24ec1876365994f54f2b8fc492636b59382eb5094c46b5818cf8d9b42aed7e8051d7ca1537202d20ef945876e94f502e048ad71c7ad89200341f8071dc73c2cc1c7688494cad0110fca4854ee6a1ba999005a650062a5d55063693e8b018b08c4591946a3fc961dae2ba0c046f0848fbe5206d56767aae8812d55ee9decc1587cf5905887846cd3ecc6fc069e40d36b29ee48229c0c79eceab9a95b11d15421b8585a2576a63b9f09c56a4ca1729680410da237ac5b05850604e2af1f4ede9cf3928cbb3193a159e64482928b585ac

	# Wiener attack no longer works
	# d = owiener.attack(e, N)
	# print(d)
	# print('./RsaCtfTool.py --createpub ./pk.txt -n %d -e %d' % (N, e))
	# print('./RsaCtfTool.py --publickey ./pk.txt --private')
	d = '00:E0:ED:BE:73:3C:B4:43:32:4E:C0:63:3A:56:FB:CC:19:EE:15:DA:46:F7:5F:91:90:26:2C:58:D1:DF:A3:9C:CB:C5:DD:EC:CA:39:B2:EA:69:9F:16:2C:CD:41:C3:1A:15:A3:01:5C:EE:D5:38:D6:A7:C0:F3:ED:2F:63:22:05:35'
	d = d.lower().replace(':','')
	d = int(d,16)
	return trans(pow(c, d, N))

	
def endless_emails():
	modulo = [
		14528915758150659907677315938876872514853653132820394367681510019000469589767908107293777996420037715293478868775354645306536953789897501630398061779084810058931494642860729799059325051840331449914529594113593835549493208246333437945551639983056810855435396444978249093419290651847764073607607794045076386643023306458718171574989185213684263628336385268818202054811378810216623440644076846464902798568705083282619513191855087399010760232112434412274701034094429954231366422968991322244343038458681255035356984900384509158858007713047428143658924970374944616430311056440919114824023838380098825914755712289724493770021,
		20463913454649855046677206889944639231694511458416906994298079596685813354570085475890888433776403011296145408951323816323011550738170573801417972453504044678801608709931200059967157605416809387753258251914788761202456830940944486915292626560515250805017229876565916349963923702612584484875113691057716315466239062005206014542088484387389725058070917118549621598629964819596412564094627030747720659155558690124005400257685883230881015636066183743516494701900125788836869358634031031172536767950943858472257519195392986989232477630794600444813136409000056443035171453870906346401936687214432176829528484662373633624123,
		19402640770593345339726386104915705450969517850985511418263141255686982818547710008822417349818201858549321868878490314025136645036980129976820137486252202687238348587398336652955435182090722844668488842986318211649569593089444781595159045372322540131250208258093613844753021272389255069398553523848975530563989367082896404719544411946864594527708058887475595056033713361893808330341623804367785721774271084389159493974946320359512776328984487126583015777989991635428744050868653379191842998345721260216953918203248167079072442948732000084754225272238189439501737066178901505257566388862947536332343196537495085729147,
		12005639978012754274325188681720834222130605634919280945697102906256738419912110187245315232437501890545637047506165123606573171374281507075652554737014979927883759915891863646221205835211640845714836927373844277878562666545230876640830141637371729405545509920889968046268135809999117856968692236742804637929866632908329522087977077849045608566911654234541526643235586433065170392920102840518192803854740398478305598092197183671292154743153130012885747243219372709669879863098708318993844005566984491622761795349455404952285937152423145150066181043576492305166964448141091092142224906843816547235826717179687198833961,
		17795451956221451086587651307408104001363221003775928432650752466563818944480119932209305765249625841644339021308118433529490162294175590972336954199870002456682453215153111182451526643055812311071588382409549045943806869173323058059908678022558101041630272658592291327387549001621625757585079662873501990182250368909302040015518454068699267914137675644695523752851229148887052774845777699287718342916530122031495267122700912518207571821367123013164125109174399486158717604851125244356586369921144640969262427220828940652994276084225196272504355264547588369516271460361233556643313911651916709471353368924621122725823,
		25252721057733555082592677470459355315816761410478159901637469821096129654501579313856822193168570733800370301193041607236223065376987811309968760580864569059669890823406084313841678888031103461972888346942160731039637326224716901940943571445217827960353637825523862324133203094843228068077462983941899571736153227764822122334838436875488289162659100652956252427378476004164698656662333892963348126931771536472674447932268282205545229907715893139346941832367885319597198474180888087658441880346681594927881517150425610145518942545293750127300041942766820911120196262215703079164895767115681864075574707999253396530263,
		19833203629283018227011925157509157967003736370320129764863076831617271290326613531892600790037451229326924414757856123643351635022817441101879725227161178559229328259469472961665857650693413215087493448372860837806619850188734619829580286541292997729705909899738951228555834773273676515143550091710004139734080727392121405772911510746025807070635102249154615454505080376920778703360178295901552323611120184737429513669167641846902598281621408629883487079110172218735807477275590367110861255756289520114719860000347219161944020067099398239199863252349401303744451903546571864062825485984573414652422054433066179558897
	]

	ciphertext = [
		6965891612987861726975066977377253961837139691220763821370036576350605576485706330714192837336331493653283305241193883593410988132245791554283874785871849223291134571366093850082919285063130119121338290718389659761443563666214229749009468327825320914097376664888912663806925746474243439550004354390822079954583102082178617110721589392875875474288168921403550415531707419931040583019529612270482482718035497554779733578411057633524971870399893851589345476307695799567919550426417015815455141863703835142223300228230547255523815097431420381177861163863791690147876158039619438793849367921927840731088518955045807722225,
		5109363605089618816120178319361171115590171352048506021650539639521356666986308721062843132905170261025772850941702085683855336653472949146012700116070022531926476625467538166881085235022484711752960666438445574269179358850309578627747024264968893862296953506803423930414569834210215223172069261612934281834174103316403670168299182121939323001232617718327977313659290755318972603958579000300780685344728301503641583806648227416781898538367971983562236770576174308965929275267929379934367736694110684569576575266348020800723535121638175505282145714117112442582416208209171027273743686645470434557028336357172288865172,
		5603386396458228314230975500760833991383866638504216400766044200173576179323437058101562931430558738148852367292802918725271632845889728711316688681080762762324367273332764959495900563756768440309595248691744845766607436966468714038018108912467618638117493367675937079141350328486149333053000366933205635396038539236203203489974033629281145427277222568989469994178084357460160310598260365030056631222346691527861696116334946201074529417984624304973747653407317290664224507485684421999527164122395674469650155851869651072847303136621932989550786722041915603539800197077294166881952724017065404825258494318993054344153,
		1522280741383024774933280198410525846833410931417064479278161088248621390305797210285777845359812715909342595804742710152832168365433905718629465545306028275498667935929180318276445229415104842407145880223983428713335709038026249381363564625791656631137936935477777236936508600353416079028339774876425198789629900265348122040413865209592074731028757972968635601695468594123523892918747882221891834598896483393711851510479989203644477972694520237262271530260496342247355761992646827057846109181410462131875377404309983072358313960427035348425800940661373272947647516867525052504539561289941374722179778872627956360577,
		8752507806125480063647081749506966428026005464325535765874589376572431101816084498482064083887400646438977437273700004934257274516197148448425455243811009944321764771392044345410680448204581679548854193081394891841223548418812679441816502910830861271884276608891963388657558218620911858230760629700918375750796354647493524576614017731938584618983084762612414591830024113057983483156974095503392359946722756364412399187910604029583464521617256125933111786441852765229820406911991809039519015434793656710199153380699319611499255869045311421603167606551250174746275803467549814529124250122560661739949229005127507540805,
		23399624135645767243362438536844425089018405258626828336566973656156553220156563508607371562416462491581383453279478716239823054532476006642583363934314982675152824147243749715830794488268846671670287617324522740126594148159945137948643597981681529145611463534109482209520448640622103718682323158039797577387254265854218727476928164074249568031493984825273382959147078839665114417896463735635546290504843957780546550577300001452747760982468547756427137284830133305010038339400230477403836856663883956463830571934657200851598986174177386323915542033293658596818231793744261192870485152396793393026198817787033127061749,
		15239683995712538665992887055453717247160229941400011601942125542239446512492703769284448009141905335544729440961349343533346436084176947090230267995060908954209742736573986319254695570265339469489948102562072983996668361864286444602534666284339466797477805372109723178841788198177337648499899079471221924276590042183382182326518312979109378616306364363630519677884849945606288881683625944365927809405420540525867173639222696027472336981838588256771671910217553150588878434061862840893045763456457939944572192848992333115479951110622066173007227047527992906364658618631373790704267650950755276227747600169403361509144
	]

	# coprime check
	for i in range(len(modulo)):
		for j in range(i+1, len(modulo)):
			assert(gmpy2.gcd(modulo[i], modulo[j]) == 1)

	# checking to make sure it works
	# ciphertext = [529, 414, 558]
	# modulo = [629, 2173, 1159]

	product = 1
	for i in modulo:
		product *= i

	gmpy2.get_context().precision = 10000
	ret = (crt (modulo, ciphertext)[0])

	# run a check to make sure the crt value is correct
	for i in range(7):
		assert((ret + product) % modulo[i] == ciphertext[i])
	
	assert(int(ret) == ret)

	# Turns out not all messages are the same
	for i in range(len(modulo)):
		for j in range(i + 1, len(modulo)):
			for k in range(j + 1, len(modulo)):
				temp1 = [modulo[i], modulo[j], modulo[k]]
				temp2 = [ciphertext[i], ciphertext[j], ciphertext[k]]
				ret = crt(temp1, temp2)[0]
				temp3 = gmpy2.cbrt(ret)
				if (temp3 == int(temp3)):
					return trans(int(temp3))

	# print(ret % product == ret)
	# print(gmpy2.cbrt(ret))
	# orig = ret
	# ret = gmpy2.iroot(ret, 3)[0]
	# print(ret)
	# print(orig)
	# print(6163435258792081155570563724535482791203179091979152504421757686683886493041873412493545277924714159737287201858788975497745808400937668458605428592558762083014850528313290613930252878249664198812745222654769820800241714978826271054236532198430467610687313659504279838226086861781305095949833574849716879096699647639958527921958637834064006172266890540479928345057273368544415806236989595476517313435658885845707049493257058926418496568638144697200407609515013103968647293188517382989530930549157220335692939060237456534893474572240265398889167814394704328134737878272985108974227486747707167006223245092132605468821480666851989946884699570651793971720879741935255673412957496812959560447653617121882766833325630820418452175677609504859541364979563245379911740546513300811333775982093598441414943432903846748986044773051271273074178187927616383656534025093239974329202223312844777650132177288938999947223314403450951104308875899846070329618172976449337886028742891717458284020666066406018267577671532200481210396120408114235438891394741637492599984773722590015110968648852335612801270812495940724242254856590121053924868070702836783742218196309136657025599313169326518028561002568919672558441696873251945314360866858517591470667708009596072897901621906067954652464219937450386826886270166857948082249114796422275205761431557543779017703807244769877494961517975032755320293361788375328727084392074072910374720592266764026634565924091861726 ** 3)
	# print(orig - 6163435258792081155570563724535482791203179091979152504421757686683886493041873412493545277924714159737287201858788975497745808400937668458605428592558762083014850528313290613930252878249664198812745222654769820800241714978826271054236532198430467610687313659504279838226086861781305095949833574849716879096699647639958527921958637834064006172266890540479928345057273368544415806236989595476517313435658885845707049493257058926418496568638144697200407609515013103968647293188517382989530930549157220335692939060237456534893474572240265398889167814394704328134737878272985108974227486747707167006223245092132605468821480666851989946884699570651793971720879741935255673412957496812959560447653617121882766833325630820418452175677609504859541364979563245379911740546513300811333775982093598441414943432903846748986044773051271273074178187927616383656534025093239974329202223312844777650132177288938999947223314403450951104308875899846070329618172976449337886028742891717458284020666066406018267577671532200481210396120408114235438891394741637492599984773722590015110968648852335612801270812495940724242254856590121053924868070702836783742218196309136657025599313169326518028561002568919672558441696873251945314360866858517591470667708009596072897901621906067954652464219937450386826886270166857948082249114796422275205761431557543779017703807244769877494961517975032755320293361788375328727084392074072910374720592266764026634565924091861726 ** 3)
	# print(hex(ret))
	# print(bytes.fromhex('0' + hex(ret)[2:]))
	
	# Idea 1: I thought maybe there was a cube root error
	# ret = int(gmpy2.cbrt(ret)) - 200
	# # print(ret)
	# for i in range(100 * 2):
	# 	try:
	# 		# print(trans(ret + i))
	# 		print(bytes.fromhex(hex(ret)[2:] + '0'))
	# 	except:
	# 		continue
	
	# Idea 2: I thoughtmaybe one of the algs was implemented incorrectly
	# ret2 = solve_crt(ciphertext, modulo)
	# assert(ret == ret2)
	
	# Idea 3: I tried to take the cube root of the ret value and brute forced k*product + residue
	# factor = 1
	# factor = 70000000
	# ret += (product * factor)
	# while (factor < 10000000000):
	# 	ret += product
	# 	if factor % 10000000 == 0:
	# 		print(factor)
	# 	if gmpy2.is_power(ret):
	# 		print("factor is: ", factor)
	# 	factor +=1 
		
	return None


def main():
	# print("salty solution: ", salty())
	# print("modulus inutilis solution: ", modulus_inutilis())
	# print("everything is big solution: ", everything_is_big())
	# print("crossed_wires solution: ", crossed_wires())
	print("everything is still big solution: ", everything_is_still_big())
	# print("endless emails solution: ", endless_emails())

if __name__ == '__main__':
	main()