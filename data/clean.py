import re
import os

PATTERNS = [r"\( født ?i?( \d\d?\.)? \w{3,9} \d{3,4} , død \d\d?\. \w{3,9} \d{3,4} \)"
,r"\( født \d\d?\. \w{3,9} (\w+ )?\d{3,4} \)"
,r"\( ?([\'\w-]+ ){0,3};? født \d\d?\. \w{3,9} \d{3,4} i ([,\w-]+ )+[;,] død \w+ ?\d\d?\. \w{3,9} \d{3,4} i ([\w-]+ )+\)"
,r"\( født \d\d?\. \w{3,9} \d{3,4} i [\w-]+ \( \w+ \) , \w+ \)"
,r"\( født \d\d?\. \w{3,9} \d{3,4} i [\w-]+ \( \w+ \) , død \d\d?\. \w{3,9} \d{3,4} i [\w-]+ , \w+ \)"
,r"\( født \d\d?\. \w{3,9} \d{3,4} , død \d\d?\. \w{3,9} \d{3,4} i [\w-]+ \)"
,r"\( født ca\.? \d{3,4} , død \d\d?\. \w{3,9} \d{3,4} \)"
, r"[,\(] født \d\d?\. \w{3,9} \d{3,4} i (['\(\)\w-]+ )+[;,] død \d\d?\. \w{3,9} \d{3,4} i (['\w-]+ )+[,\)]"
, r"\( født ca\.? år \d{3,4} i [\w-]+ , død \d\d?\. \w{3,9} \d{3,4} ([\w-]+ )+\)"
, r"\( født (\d\d?\. \w{3,9} )?\d{3,4} i [\w-]+ [,i] \w+ \)"
, r"\{ \| (\w+=[\d\w\"\ |]+ )+\|"
, r"\( født \d\d?\. \w{3,9} \d{3,4} [ \w-]+ , død \d\d?\. \w{3,9} \d{3,4}( i [\w-]+)+ \)"
, r"\( født \d\d?\. \w{3,9} \d{3,4} i [\w-]+ , (\w+ )+, død \d\d?\. \w{3,9} \d{3,4} (i|på) (\w+ )+\)"
, r"\( ?([,\'\w-]+ ){0,15};? født (\d\d?\. \w{3,9} )?\d{3,4} i ([,\w-]+ )+[;,] død \d\d?\. \w{3,9} \d{3,4} (i ([,\w-]+ )+)?\)"
, r"\( født [\d/]+ (f\.kr ?\. )?, død [\d/]+ [ef]\.kr ?\.? ?\)"
, r"\( født \d\d?\. \w{3,9} \d{3,4} i \w+ , død \d\d?\. \w{3,9} \d{3,4} i \w+ , bisatt i \w+ \d\d?\. \w{3,9} \d{3,4} \)"
, r"\( født ?i? \d\d?\. \w{3,9} \d{3,4} i \w+ , død \d\d?\. \w{3,9} \d{3,4} \)"
, r"\( født \d\d?\. \w{3,9} \d{3,4} (i [\w-]+ )+, død \d\d?\. \w{3,9} \d{3,4} ([\w-]+ )+\)"
, r"\( født ([',\w-]+ )+(\d\d?\. \w{3,9} )?\d{3,4} [;,] død \d\d?\. \w{3,9} \d{3,4} (i ([,\w-]+ )+)?\)"
, r"\( født \d\d?\. \w{3,9} \d{3,4} (i|på) (\w+ )+, død \d\d?\. \w{3,9} \d{3,4} (i|på) (\w+ )+\)"
, r"\( ?([\(\),\'\w-]+ ){0,15};? født .+ død( mellom \d\d?\. og)? \d\d?\. \w{3,9} \d{3,4} (i ([,\w-]+ )+)?\)"
,r"\( født .+ (død|besøkt) \d\d?\. \w{3,9} \d{3,4} ?,? \)"
,r"\( født (\d\d?\. \w{3,9}|rundt) \d{3,4} i \w+ \)"
,r"\( født (\d\d?\. \w{3,9}|rundt) \d{3,4} .+ død ([,\.\w]+ ){1,12}\)"
,r"\( ?([,\.\w]+ ){0,12}født .+ (død|drept|henrettet) (\d\d?\. \w{3,9}|rundt) \d{3,4} ([,\.\w]+ ){1,12}\)"
,r"\( født (\d\d?\. \w{3,9}|rundt) \d{3,4} ([,\.\w]+ ){1,12}\)"
,r"\( født .+ død [\w\.\d ]+ \d{3,4} \)"
,r"født ca\. \d+"]



def clean(infile):
    with open(os.path.join('..',infile),'r',encoding='utf-8') as f:
        data = f.read().replace('image','')
        for pat in PATTERNS:
            data = re.sub(pat,' ',data)
        data = data.replace('\'',' ').replace('\"',' ').replace('«',' ').replace('»',' ')
        data = re.sub(' +',' ',data)
        with open(os.path.join('..','cleaned'+infile),'w',encoding='utf-8') as fout:
            fout.write(data)

if __name__ == '__main__':
    for name in ['testtokens.txt.tgt',
                 'testtokens.txt.src',
                 'traintokens.txt.src',
                 'traintokens.txt.tgt',
                 'valtokens.txt.src',
                 'valtokens.txt.tgt']:
        clean(name)