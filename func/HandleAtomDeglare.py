import func.reflectionConditions.Space112
import func.reflectionConditions.Space037
import func.reflectionConditions.Space102
import func.reflectionConditions.Space017
import func.reflectionConditions.Space027
import func.reflectionConditions.Space080
import func.reflectionConditions.Space110
import func.reflectionConditions.Space169
import func.reflectionConditions.Space230
import func.reflectionConditions.Space020
import func.reflectionConditions.Space173
import func.reflectionConditions.Space126
import func.reflectionConditions.Space023
import func.reflectionConditions.Space227
import func.reflectionConditions.Space054
import func.reflectionConditions.Space161
import func.reflectionConditions.Space039
import func.reflectionConditions.Space136
import func.reflectionConditions.Space138
import func.reflectionConditions.Space051
import func.reflectionConditions.Space079
import func.reflectionConditions.Space101
import func.reflectionConditions.Space072
import func.reflectionConditions.Space082
import func.reflectionConditions.Space064
import func.reflectionConditions.Space046
import func.reflectionConditions.Space055
import func.reflectionConditions.Space009
import func.reflectionConditions.Space004
import func.reflectionConditions.Space001
import func.reflectionConditions.Space060
import func.reflectionConditions.Space184
import func.reflectionConditions.Space069
import func.reflectionConditions.Space022
import func.reflectionConditions.Space007
import func.reflectionConditions.Space042
import func.reflectionConditions.Space226
import func.reflectionConditions.Space031
import func.reflectionConditions.Space159
import func.reflectionConditions.Space137
import func.reflectionConditions.Space015
import func.reflectionConditions.Space219
import func.reflectionConditions.Space223
import func.reflectionConditions.Space125
import func.reflectionConditions.Space021
import func.reflectionConditions.Space053
import func.reflectionConditions.Space056
import func.reflectionConditions.Space058
import func.reflectionConditions.Space222
import func.reflectionConditions.Space220
import func.reflectionConditions.Space018
import func.reflectionConditions.Space228
import func.reflectionConditions.Space045
import func.reflectionConditions.Space092
import func.reflectionConditions.Space196
import func.reflectionConditions.Space086
import func.reflectionConditions.Space036
import func.reflectionConditions.Space068
import func.reflectionConditions.Space071
import func.reflectionConditions.Space011
import func.reflectionConditions.Space158
import func.reflectionConditions.Space033
import func.reflectionConditions.Space013
import func.reflectionConditions.Space074
import func.reflectionConditions.Space100
import func.reflectionConditions.Space044
import func.reflectionConditions.Space170
import func.reflectionConditions.Space041
import func.reflectionConditions.Space105
import func.reflectionConditions.Space146
import func.reflectionConditions.Space076
import func.reflectionConditions.Space114
import func.reflectionConditions.Space203
import func.reflectionConditions.Space141
import func.reflectionConditions.Space035
import func.reflectionConditions.Space090
import func.reflectionConditions.Space028
import func.reflectionConditions.Space142
import func.reflectionConditions.Space198
import func.reflectionConditions.Space029
import func.reflectionConditions.Space043
import func.reflectionConditions.Space144
import func.reflectionConditions.Space040
import func.reflectionConditions.Space032
import func.reflectionConditions.Space059
import func.reflectionConditions.Space061
import func.reflectionConditions.Space106
import func.reflectionConditions.Space066
import func.reflectionConditions.Space133
import func.reflectionConditions.Space197
import func.reflectionConditions.Space103
import func.reflectionConditions.Space014
import func.reflectionConditions.Space109
import func.reflectionConditions.Space067
import func.reflectionConditions.Space165
import func.reflectionConditions.Space094
import func.reflectionConditions.Space073
import func.reflectionConditions.Space026
import func.reflectionConditions.Space087
import func.reflectionConditions.Space201
import func.reflectionConditions.Space130
import func.reflectionConditions.Space019
import func.reflectionConditions.Space030
import func.reflectionConditions.Space085
import func.reflectionConditions.Space063
import func.reflectionConditions.Space088
import func.reflectionConditions.Space052
import func.reflectionConditions.Space057
import func.reflectionConditions.Space005
import func.reflectionConditions.Space108
import func.reflectionConditions.Space062
import func.reflectionConditions.Space104
import func.reflectionConditions.Space012
import func.reflectionConditions.Space034
import func.reflectionConditions.Space038
import func.reflectionConditions.Space049
import func.reflectionConditions.Space050


# class Space221:
#     pass


def handle(spaceGroupNum, spaceGroupName, hklRes):
    print("enter HandleAtomDeglare Function")
    spaceGroupName = spaceGroupName.replace(" ", "")

    # hklList = []

    spaceArc001 = {'1', '2', '3', '6', '10', '16', '25', '47', '75', '81', '83', '89', '99', '111', '115', '123', '143',
                   '147', '149', '150', '156', '157', '162', '164', '168', '174', '175', '177', '183', '187', '189',
                   '191', '195', '200', '207', '215', '221'}
    spaceArc004 = {'4'}
    spaceArc005 = {'5', '8'}
    spaceArc007 = {'7'}
    spaceArc009 = {'9'}
    spaceArc011 = {'11'}
    spaceArc012 = {'12'}
    spaceArc013 = {'13'}
    spaceArc014 = {'14'}
    spaceArc015 = {'15'}
    spaceArc017 = {'17', '77', '84', '93'}
    spaceArc018 = {'18'}
    spaceArc019 = {'19'}
    spaceArc020 = {'20'}
    spaceArc021 = {'21'}
    spaceArc022 = {'22'}
    spaceArc023 = {'23', '24'}
    spaceArc026 = {'26'}
    spaceArc027 = {'27'}
    spaceArc028 = {'28'}
    spaceArc029 = {'29'}
    spaceArc030 = {'30'}
    spaceArc031 = {'31'}
    spaceArc032 = {'32'}
    spaceArc033 = {'33'}
    spaceArc034 = {'34'}
    spaceArc035 = {'35', '65'}
    spaceArc036 = {'36'}
    spaceArc037 = {'37'}
    spaceArc038 = {'38'}
    spaceArc039 = {'39'}
    spaceArc040 = {'40'}
    spaceArc041 = {'41'}
    spaceArc042 = {'42'}
    spaceArc043 = {'43'}
    spaceArc044 = {'44'}
    spaceArc045 = {'45'}
    spaceArc046 = {'46'}
    spaceArc048 = {'48'}
    spaceArc049 = {'49'}
    spaceArc050 = {'50'}
    spaceArc051 = {'51'}
    spaceArc052 = {'52'}
    spaceArc053 = {'53'}
    spaceArc054 = {'54'}
    spaceArc055 = {'55'}
    spaceArc056 = {'56'}
    spaceArc057 = {'57'}
    spaceArc058 = {'58'}
    spaceArc059 = {'59'}
    spaceArc060 = {'60'}
    spaceArc061 = {'61'}
    spaceArc062 = {'62'}
    spaceArc063 = {'63'}
    spaceArc064 = {'64'}
    spaceArc066 = {'66'}
    spaceArc067 = {'67'}
    spaceArc068 = {'68'}
    spaceArc069 = {'69'}
    spaceArc070 = {'70'}
    spaceArc071 = {'71'}
    spaceArc072 = {'72'}
    spaceArc073 = {'73'}
    spaceArc074 = {'74'}
    spaceArc076 = {'76', '78', '91', '95'}
    spaceArc079 = {'79', '118'}
    spaceArc080 = {'80'}
    spaceArc082 = {'82', '107', '120'}
    spaceArc085 = {'85', '129'}
    spaceArc086 = {'86'}
    spaceArc087 = {'87', '97', '98', '139'}
    spaceArc088 = {'88'}
    spaceArc090 = {'90', '113'}
    spaceArc092 = {'92', '96'}
    spaceArc094 = {'94'}
    spaceArc100 = {'100', '117', '127'}
    spaceArc101 = {'101', '116', '132'}
    spaceArc102 = {'102'}
    spaceArc103 = {'103', '124'}
    spaceArc104 = {'104', '128'}
    spaceArc105 = {'105'}
    spaceArc106 = {'106', '135'}
    spaceArc108 = {'108', '119', '121', '140'}
    spaceArc109 = {'109', '122'}
    spaceArc110 = {'110'}
    spaceArc112 = {'112', '131'}
    spaceArc114 = {'114'}
    spaceArc125 = {'125'}
    spaceArc126 = {'126'}
    spaceArc130 = {'130', '186', '190', '194'}
    spaceArc133 = {'133'}
    spaceArc134 = {'134'}
    spaceArc136 = {'136'}
    spaceArc137 = {'137'}
    spaceArc138 = {'138'}
    spaceArc141 = {'141'}
    spaceArc142 = {'142'}
    spaceArc144 = {'144', '145', '151', '152', '153', '154'}
    spaceArc146 = {'146', '148', '155', '160', '166'}
    spaceArc158 = {'158', '185', '193'}
    spaceArc159 = {'159', '163'}
    spaceArc161 = {'161', '167'}
    spaceArc165 = {'165'}
    spaceArc169 = {'169', '178', '179'}
    spaceArc170 = {'170'}
    spaceArc171 = {'171', '172', '180', '181'}
    spaceArc173 = {'173', '176', '182'}
    spaceArc184 = {'184', '192'}
    spaceArc196 = {'196', '202', '209', '210', '216', '225'}
    spaceArc197 = {'197', '199', '204', '211', '212', '213', '214', '217', '229'}
    spaceArc198 = {'198', '208'}
    spaceArc201 = {'201'}
    spaceArc203 = {'203'}
    spaceArc205 = {'205'}
    spaceArc206 = {'206'}
    spaceArc218 = {'218'}
    spaceArc219 = {'219'}
    spaceArc220 = {'220'}
    spaceArc222 = {'222'}
    spaceArc223 = {'223'}
    spaceArc224 = {'224'}
    spaceArc226 = {'226'}
    spaceArc227 = {'227'}
    spaceArc228 = {'228'}
    spaceArc230 = {'230'}

    spaceHandleFun = ''

    if spaceGroupNum in spaceArc001:
        spaceHandleFun = func.reflectionConditions.func.reflectionConditions.Space001

    if spaceGroupNum in spaceArc004:
        spaceHandleFun = func.reflectionConditions.Space004

    if spaceGroupNum in spaceArc005:
        spaceHandleFun = func.reflectionConditions.Space005

    if spaceGroupNum in spaceArc007:
        spaceHandleFun = func.reflectionConditions.Space007

    if spaceGroupNum in spaceArc009:
        spaceHandleFun = func.reflectionConditions.Space009

    if spaceGroupNum in spaceArc011:
        spaceHandleFun = func.reflectionConditions.Space011

    if spaceGroupNum in spaceArc012:
        spaceHandleFun = func.reflectionConditions.Space012

    if spaceGroupNum in spaceArc013:
        spaceHandleFun = func.reflectionConditions.Space013

    if spaceGroupNum in spaceArc014:
        spaceHandleFun = func.reflectionConditions.Space014

    if spaceGroupNum in spaceArc015:
        spaceHandleFun = func.reflectionConditions.Space015

    if spaceGroupNum in spaceArc017:
        spaceHandleFun = func.reflectionConditions.Space017

    if spaceGroupNum in spaceArc018:
        spaceHandleFun = func.reflectionConditions.Space018

    if spaceGroupNum in spaceArc019:
        spaceHandleFun = func.reflectionConditions.Space019

    if spaceGroupNum in spaceArc020:
        spaceHandleFun = func.reflectionConditions.Space020

    if spaceGroupNum in spaceArc021:
        spaceHandleFun = func.reflectionConditions.Space021

    if spaceGroupNum in spaceArc022:
        spaceHandleFun = func.reflectionConditions.Space022

    if spaceGroupNum in spaceArc023:
        spaceHandleFun = func.reflectionConditions.Space023

    if spaceGroupNum in spaceArc026:
        spaceHandleFun = func.reflectionConditions.Space026

    if spaceGroupNum in spaceArc027:
        spaceHandleFun = func.reflectionConditions.Space027

    if spaceGroupNum in spaceArc028:
        spaceHandleFun = func.reflectionConditions.Space028

    if spaceGroupNum in spaceArc029:
        spaceHandleFun = func.reflectionConditions.Space029

    if spaceGroupNum in spaceArc030:
        spaceHandleFun = func.reflectionConditions.Space030

    if spaceGroupNum in spaceArc031:
        spaceHandleFun = func.reflectionConditions.Space031

    if spaceGroupNum in spaceArc032:
        spaceHandleFun = func.reflectionConditions.Space032

    if spaceGroupNum in spaceArc033:
        spaceHandleFun = func.reflectionConditions.Space033

    if spaceGroupNum in spaceArc034:
        spaceHandleFun = func.reflectionConditions.Space034

    if spaceGroupNum in spaceArc035:
        spaceHandleFun = func.reflectionConditions.Space035

    if spaceGroupNum in spaceArc036:
        spaceHandleFun = func.reflectionConditions.Space036

    if spaceGroupNum in spaceArc037:
        spaceHandleFun = func.reflectionConditions.Space037

    if spaceGroupNum in spaceArc038:
        spaceHandleFun = func.reflectionConditions.Space038

    if spaceGroupNum in spaceArc039:
        spaceHandleFun = func.reflectionConditions.Space039

    if spaceGroupNum in spaceArc040:
        spaceHandleFun = func.reflectionConditions.Space040

    if spaceGroupNum in spaceArc041:
        spaceHandleFun = func.reflectionConditions.Space041

    if spaceGroupNum in spaceArc042:
        spaceHandleFun = func.reflectionConditions.Space042

    if spaceGroupNum in spaceArc043:
        spaceHandleFun = func.reflectionConditions.Space043

    if spaceGroupNum in spaceArc044:
        spaceHandleFun = func.reflectionConditions.Space044

    if spaceGroupNum in spaceArc045:
        spaceHandleFun = func.reflectionConditions.Space045

    if spaceGroupNum in spaceArc046:
        spaceHandleFun = func.reflectionConditions.Space046

    if spaceGroupNum in spaceArc048:
        spaceHandleFun = func.reflectionConditions.Space048

    if spaceGroupNum in spaceArc049:
        spaceHandleFun = func.reflectionConditions.Space049

    if spaceGroupNum in spaceArc050:
        spaceHandleFun = func.reflectionConditions.Space050

    if spaceGroupNum in spaceArc051:
        spaceHandleFun = func.reflectionConditions.Space051

    if spaceGroupNum in spaceArc052:
        spaceHandleFun = func.reflectionConditions.Space052

    if spaceGroupNum in spaceArc053:
        spaceHandleFun = func.reflectionConditions.Space053

    if spaceGroupNum in spaceArc054:
        spaceHandleFun = func.reflectionConditions.Space054

    if spaceGroupNum in spaceArc055:
        spaceHandleFun = func.reflectionConditions.Space055

    if spaceGroupNum in spaceArc056:
        spaceHandleFun = func.reflectionConditions.Space056

    if spaceGroupNum in spaceArc057:
        spaceHandleFun = func.reflectionConditions.Space057

    if spaceGroupNum in spaceArc058:
        spaceHandleFun = func.reflectionConditions.Space058

    if spaceGroupNum in spaceArc059:
        spaceHandleFun = func.reflectionConditions.Space059

    if spaceGroupNum in spaceArc060:
        spaceHandleFun = func.reflectionConditions.Space060

    if spaceGroupNum in spaceArc061:
        spaceHandleFun = func.reflectionConditions.Space061

    if spaceGroupNum in spaceArc062:
        spaceHandleFun = func.reflectionConditions.Space062

    if spaceGroupNum in spaceArc063:
        spaceHandleFun = func.reflectionConditions.Space063

    if spaceGroupNum in spaceArc064:
        spaceHandleFun = func.reflectionConditions.Space064

    if spaceGroupNum in spaceArc066:
        spaceHandleFun = func.reflectionConditions.Space066

    if spaceGroupNum in spaceArc067:
        spaceHandleFun = func.reflectionConditions.Space067

    if spaceGroupNum in spaceArc068:
        spaceHandleFun = func.reflectionConditions.Space068

    if spaceGroupNum in spaceArc069:
        spaceHandleFun = func.reflectionConditions.Space069

    if spaceGroupNum in spaceArc070:
        spaceHandleFun = func.reflectionConditions.Space070

    if spaceGroupNum in spaceArc071:
        spaceHandleFun = func.reflectionConditions.Space071

    if spaceGroupNum in spaceArc072:
        spaceHandleFun = func.reflectionConditions.Space072

    if spaceGroupNum in spaceArc073:
        spaceHandleFun = func.reflectionConditions.Space073

    if spaceGroupNum in spaceArc074:
        spaceHandleFun = func.reflectionConditions.Space074

    if spaceGroupNum in spaceArc076:
        spaceHandleFun = func.reflectionConditions.Space076

    if spaceGroupNum in spaceArc079:
        spaceHandleFun = func.reflectionConditions.Space079

    if spaceGroupNum in spaceArc080:
        spaceHandleFun = func.reflectionConditions.Space080

    if spaceGroupNum in spaceArc082:
        spaceHandleFun = func.reflectionConditions.Space082

    if spaceGroupNum in spaceArc085:
        spaceHandleFun = func.reflectionConditions.Space085

    if spaceGroupNum in spaceArc086:
        spaceHandleFun = func.reflectionConditions.Space086

    if spaceGroupNum in spaceArc087:
        spaceHandleFun = func.reflectionConditions.Space087

    if spaceGroupNum in spaceArc088:
        spaceHandleFun = func.reflectionConditions.Space088

    if spaceGroupNum in spaceArc090:
        spaceHandleFun = func.reflectionConditions.Space090

    if spaceGroupNum in spaceArc092:
        spaceHandleFun = func.reflectionConditions.Space092

    if spaceGroupNum in spaceArc094:
        spaceHandleFun = func.reflectionConditions.Space094

    if spaceGroupNum in spaceArc100:
        spaceHandleFun = func.reflectionConditions.Space100

    if spaceGroupNum in spaceArc101:
        spaceHandleFun = func.reflectionConditions.Space101

    if spaceGroupNum in spaceArc102:
        spaceHandleFun = func.reflectionConditions.Space102

    if spaceGroupNum in spaceArc103:
        spaceHandleFun = func.reflectionConditions.Space103

    if spaceGroupNum in spaceArc104:
        spaceHandleFun = func.reflectionConditions.Space104

    if spaceGroupNum in spaceArc105:
        spaceHandleFun = func.reflectionConditions.Space105

    if spaceGroupNum in spaceArc106:
        spaceHandleFun = func.reflectionConditions.Space106

    if spaceGroupNum in spaceArc108:
        spaceHandleFun = func.reflectionConditions.Space108

    if spaceGroupNum in spaceArc109:
        spaceHandleFun = func.reflectionConditions.Space109

    if spaceGroupNum in spaceArc110:
        spaceHandleFun = func.reflectionConditions.Space110

    if spaceGroupNum in spaceArc112:
        spaceHandleFun = func.reflectionConditions.Space112

    if spaceGroupNum in spaceArc114:
        spaceHandleFun = func.reflectionConditions.Space114

    if spaceGroupNum in spaceArc125:
        spaceHandleFun = func.reflectionConditions.Space125

    if spaceGroupNum in spaceArc126:
        spaceHandleFun = func.reflectionConditions.Space126

    if spaceGroupNum in spaceArc130:
        spaceHandleFun = func.reflectionConditions.Space130

    if spaceGroupNum in spaceArc133:
        spaceHandleFun = func.reflectionConditions.Space133

    if spaceGroupNum in spaceArc134:
        spaceHandleFun = func.reflectionConditions.Space134

    if spaceGroupNum in spaceArc136:
        spaceHandleFun = func.reflectionConditions.Space136

    if spaceGroupNum in spaceArc137:
        spaceHandleFun = func.reflectionConditions.Space137

    if spaceGroupNum in spaceArc138:
        spaceHandleFun = func.reflectionConditions.Space138

    if spaceGroupNum in spaceArc141:
        spaceHandleFun = func.reflectionConditions.Space141

    if spaceGroupNum in spaceArc142:
        spaceHandleFun = func.reflectionConditions.Space142

    if spaceGroupNum in spaceArc144:
        spaceHandleFun = func.reflectionConditions.Space144

    if spaceGroupNum in spaceArc146:
        spaceHandleFun = func.reflectionConditions.Space146

    if spaceGroupNum in spaceArc158:
        spaceHandleFun = func.reflectionConditions.Space158

    if spaceGroupNum in spaceArc159:
        spaceHandleFun = func.reflectionConditions.Space159

    if spaceGroupNum in spaceArc161:
        spaceHandleFun = func.reflectionConditions.Space161

    if spaceGroupNum in spaceArc165:
        spaceHandleFun = func.reflectionConditions.Space165

    if spaceGroupNum in spaceArc169:
        spaceHandleFun = func.reflectionConditions.Space169

    if spaceGroupNum in spaceArc170:
        spaceHandleFun = func.reflectionConditions.Space170

    if spaceGroupNum in spaceArc171:
        spaceHandleFun = func.reflectionConditions.Space171

    if spaceGroupNum in spaceArc173:
        spaceHandleFun = func.reflectionConditions.Space173

    if spaceGroupNum in spaceArc184:
        spaceHandleFun = func.reflectionConditions.Space184

    if spaceGroupNum in spaceArc196:
        spaceHandleFun = func.reflectionConditions.Space196

    if spaceGroupNum in spaceArc197:
        spaceHandleFun = func.reflectionConditions.Space197

    if spaceGroupNum in spaceArc198:
        spaceHandleFun = func.reflectionConditions.Space198

    if spaceGroupNum in spaceArc201:
        spaceHandleFun = func.reflectionConditions.Space201

    if spaceGroupNum in spaceArc203:
        spaceHandleFun = func.reflectionConditions.Space203

    if spaceGroupNum in spaceArc205:
        spaceHandleFun = func.reflectionConditions.Space205

    if spaceGroupNum in spaceArc206:
        spaceHandleFun = func.reflectionConditions.Space206

    if spaceGroupNum in spaceArc218:
        spaceHandleFun = func.reflectionConditions.Space218

    if spaceGroupNum in spaceArc219:
        spaceHandleFun = func.reflectionConditions.Space219

    if spaceGroupNum in spaceArc220:
        spaceHandleFun = func.reflectionConditions.Space220

    if spaceGroupNum in spaceArc222:
        spaceHandleFun = func.reflectionConditions.Space222

    if spaceGroupNum in spaceArc223:
        spaceHandleFun = func.reflectionConditions.Space223

    if spaceGroupNum in spaceArc224:
        spaceHandleFun = func.reflectionConditions.Space224

    if spaceGroupNum in spaceArc226:
        spaceHandleFun = func.reflectionConditions.Space226

    if spaceGroupNum in spaceArc227:
        spaceHandleFun = func.reflectionConditions.Space227

    if spaceGroupNum in spaceArc228:
        spaceHandleFun = func.reflectionConditions.Space228

    if spaceGroupNum in spaceArc230:
        spaceHandleFun = func.reflectionConditions.Space230

    hklList = spaceHandleFun.spaceHandle(spaceGroupName, hklRes)

    hklList.sort(key=lambda hklList: (hklList[0], hklList[1][0], hklList[1][1], hklList[1][2]))

    print("exit HandleAtomDeglare Function")
    return hklList
