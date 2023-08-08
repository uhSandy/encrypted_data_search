import json
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import utils.appearance
from cryptography.hazmat.backends import default_backend
import csv


def encryptData():
    # Load public key
    # with open("../keys/public_key.pem", "rb") as key_file:
    #     public_key = serialization.load_pem_public_key(
    #         key_file.read(),
    #         backend=default_backend()
    #     )
    # Serialize the public key to PEM format
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )
    public_key1 = private_key.public_key()

    public_key_pem = public_key1.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    # Load the public key from PEM format
    public_key = serialization.load_pem_public_key(public_key_pem)

    print("& & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & &")


    # Dictionary with Appearance objects
    data = {'calcium': {'docName': ' emartemp.csv', 'frequency': 22, 'tag': 7576674972035569706360956425676775494306367900892798132340893925821174956838936849161027869191725642272563207342696891265345960477028588111130539891052920}, 'care': {'docName': ' emartemp.csv', 'frequency': 18, 'tag': 12779158712373313182466584282706366992391653073770612241046994659128135082755968519749908812492964360311061571327401026405866873731053887217531528253723542}, 'chlorid': {'docName': ' emartemp.csv', 'frequency': 4, 'tag': 1662853839658565050621770056806394488187584530979148352153850404346714910525915519385641285365438169638652774778887782669842629874370882751338202654400}, 'chloride': {'docName': ' emartemp.csv', 'frequency': 5, 'tag': 6987525769788233791387883457332377722319311713248740600450705392235491798366156871849305251078314481320139364652387588512416420487178052486374444724905572}, 'citr': {'docName': ' emartemp.csv', 'frequency': 3, 'tag': 4164338212308116408613470002960363317856918593592534731940219132512361095201715486341458902153071740342764933556817992661659437658918821397093309018123910}, 'critical': {'docName': ' emartemp.csv', 'frequency': 18, 'tag': 7520559940915352599152011189802621513756556661512064825583290077625813520103345777569467035941460032033320551410737410607132688445168443989377490812169652}, 'fentanyl': {'docName': ' emartemp.csv', 'frequency': 3, 'tag': 3747904401073775945131209970736531264202833981654442781663299667157499914331923760685438591436919604023737723702808557469045138398293071955756455406422756}, 'fumar': {'docName': ' emartemp.csv', 'frequency': 2, 'tag': 3179658507466290526300221162945030842764848048613988938291416092465383092329684299905450175936091768014231433956630522627448286916092358958794530213913572}, 'gluconate': {'docName': ' emartemp.csv', 'frequency': 11, 'tag': 3928854984921356702470795670239202392840741926171791431180760680738502900882791411587191291943447954191811282467506051832344293134544741016409781291475556}, 'heparin': {'docName': ' emartemp.csv', 'frequency': 1, 'tag': 9383302241063662132460857129124636714561285083204087057406767484784472563539975876851789371430761066367491211147546016843566846456110824935149043031208270}, 'insert': {'docName': ' emartemp.csv', 'frequency': 1, 'tag': 185778321788588301930391258097733446079374718169390173058519946448596969797380985984435815180748835711781526714617930875770549119403817553800112236551352}, 'insulin': {'docName': ' emartemp.csv', 'frequency': 1, 'tag': 3938654184526384322736406572982271631892043557127396307652220008700400534145626365386817222559920044227554619677759073181508761240473551945221948605367460}, 'ionized': {'docName': ' emartemp.csv', 'frequency': 11, 'tag': 1021024673064263809895779574216155445554350684414010632603925703572245031766024817241867740991315950364346495574915372797479428665091565735737125605556522}, 'lidocaine': {'docName': ' emartemp.csv', 'frequency': 2, 'tag': 8806199194822621927172931719349797978089986147620053748102161180284998287025528588121090888291233118295287659634429966823548624087582410273349642562268562}, 'magnesium': {'docName': ' emartemp.csv', 'frequency': 12, 'tag': 4257458415133223407368277277084870448867306103328786998733158947322165468308462871494793693860079369892847290174970727080348710533868768411980636311926552}, 'metoprolol': {'docName': ' emartemp.csv', 'frequency': 4, 'tag': 12522112636828468026872696331060573224668240311810966278926274375129132196032538633321165194377370023086984065760994413256973279817785293993456007743655256}, 'midline': {'docName': ' emartemp.csv', 'frequency': 1, 'tag': 3415547259051893824908013768126445003812767888847129442372900186918406883474009176938713713473812932444497477316747546479617365386425870344905848723411842}, 'morphine': {'docName': ' emartemp.csv', 'frequency': 2, 'tag': 311039075337890944731433119429239152872695724514113711699650892189547042314931261850528050175624856366338675981222791735164185984730832446417783577510506}, 'oncolog': {'docName': ' emartemp.csv', 'frequency': 7, 'tag': 1360810635165604532675121471957636388687733968319856937303398327258340111950554297881419637912657885751498112464882319661583040467680590003309985471694556}, 'p14csq': {'docName': ' emartemp.csv', 'frequency': 1, 'tag': 3135974411386929515990245702189986010294076969911116611844263650872582147044706926259714010646651346465595447876532538287418733098227893192468513661051682}, 'p26pkf': {'docName': ' emartemp.csv', 'frequency': 1, 'tag': 2272484646769150356951195874438755377862995967682559535028788261495776932233338897592768613074934093972646590280929796678872145739562211778285097729691930}, 'p28ev2': {'docName': ' emartemp.csv', 'frequency': 1, 'tag': 2146060319742347044655343865165566305679495281218703704851058059132430747096762573379160408026202556331694746965610468465881542320250644399123331989580900}, 'p33k2x': {'docName': ' emartemp.csv', 'frequency': 1, 'tag': 9460940944450318122892197347865303431765288484690677216873809349369610204590878633420780169561076742303207547715943689527385144712217063097762846954760530}, 'p54tss': {'docName': ' emartemp.csv', 'frequency': 2, 'tag': 10131675467008715083724244171065393011231673866784350035874540380824868148431441227807534237087902833118287078853677964177116420321252443133783051139696532}, 'p851dg': {'docName': ' emartemp.csv', 'frequency': 1, 'tag': 2783282667773757548348674542771922336106776775466775332900774779240407706295660691825969679479049938865845868292469792713661033086793926906541230095343522}, 'picc': {'docName': ' emartemp.csv', 'frequency': 1, 'tag': 101318699119352185586158043517994627718839333323651768329585619299540601093837900200425840516623114029712358124498656895588858874785911238605148216404982}, 'potassium': {'docName': ' emartemp.csv', 'frequency': 9, 'tag': 5768467316199939030191742442510580847122933687865355800101873230682367979224147810357342323874017790450224735240619081546087000125742947555027155184389742}, 'quetiapine': {'docName': ' emartemp.csv', 'frequency': 2, 'tag': 3542999466924771782308518688222941278476944231392356060906079360142016614254757222435285324585971878617151734663426510829051105152314766808937782725049412}, 'replacement': {'docName': ' emartemp.csv', 'frequency': 7, 'tag': 4569043507462857106776363026675431130330306438855842238742002874100909355902420894559866665889840931117512094804595952194099686905213515246851671699337352}, 'scale': {'docName': ' emartemp.csv', 'frequency': 11, 'tag': 12221465795532958791533500847535357524203653871997620547735288403509237351918201808722687097459928889497589908427996115095283548437692128197519424362765610}, 'sliding': {'docName': ' emartemp.csv', 'frequency': 11, 'tag': 1614851040954142731264540013158490160833517635871593373579013205258740924596502102983353371033982154907106093964556716221858051336414943071462425697672506}, 'sulf': {'docName': ' emartemp.csv', 'frequency': 12, 'tag': 10029777201012422242728225573912001077658752654228235189690214246189999424293947773386163993515225093156056053374829229639534355296457330789646646853599512}, 'sulfate': {'docName': ' emartemp.csv', 'frequency': 2, 'tag': 892197815478991218806718161153912138070070032016454766032068904119097501964483861700707941262835435231815629789064728212383825762394112523104495273808252}, 'tartr': {'docName': ' emartemp.csv', 'frequency': 4, 'tag': 5711101352242944147515407796562131720857060826215952487423789409478239226338592151401963807552392513969159845638877768185381740398091075404275084004287250}, 'test': {'docName': ' Book1.csv', 'frequency': 1, 'tag': 5206479603229504388156608851882332876541701453368020120598321951728174230041288452125501274614862934157678841977642906517209135456084036504548057235635802}, 'test2': {'docName': ' Book1.csv', 'frequency': 1, 'tag': 1892880673949031039110159653376232841040703014596892594988924501255473919036726963996579942704414837971774622456954906342029439118213061285225144523549756}, 'test3': {'docName': ' Book1.csv', 'frequency': 1, 'tag': 13134911312720367403477169202728889506079881512035512057432676521752550153587605956705013448286066592480800529609396257776496142255234695014428170956725156}, 'cefepim': {'docName': ' Book1.csv emartemp.csv', 'frequency': 3, 'tag': 4878153727206732778001149107822125021775220818852326317081625609483608912986752521334625330661797909087972646799924908079473909800434131335172688750303312}}

    # Convert the dictionary to a JSON serializable format
    json_data = json.dumps(data)
    # Convert the JSON data to bytes
    json_data_bytes = json_data.encode()
    print(json_data_bytes)
    # Encrypt the JSON data
    encrypted_data = public_key.encrypt(
        json_data_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Encode the encrypted data as base64 for easy storage and transmission
    # encrypted_data_base64 = encrypted_data.encode('base64')
    # print(encrypted_data_base64)
    # print("encrypted_data_base64")

def find_rows_with_word(input_file, output_file, word):
    input_file = 'documents/'+input_file.strip()
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Search for the specific word in each row (case-insensitive)
            if any(word.lower() in cell.lower() for cell in row):
                writer.writerow(row)

# Example usage
input_csv_file = 'documents/chartevents.csv'  # Replace with the path to your input CSV file
output_csv_file = 'output.csv'  # Replace with the path to the output CSV file
search_word = 'doppler'  # Replace with the word you want to search for

#find_rows_with_word(input_csv_file, output_csv_file, search_word)

#encryptData()