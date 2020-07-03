# Collaborative Filtering Coding Question
import re
class Solution(object):
    def collaborativeFiltering(self, user):
        """
        input: str
        return: str
        """
        # omit null input
        if not user:
            return
        # count users and features
        Nu, Nf = self.countUserAndFeature(user)
        # omit case with only 1 user
        if Nu == 1:
            return
        # construct an initial dictionary with user basic info
        nameList,userDict = self.userInfoDict(user, Nu, Nf)
        # construct a standard for rank based on the first user
        rankBaseDict1 = self.rankBaseDict(Nf, nameList, userDict)
        # construct inversion for the first user
        inversionDict1=self.inversionDict(Nf, userDict, rankBaseDict1)
        # sort name list based on inversion dictionary
        self.sortNameList(Nu, inversionDict1, nameList)
        # return complete result of user similarity
        resultString=""
        i=1
        while i<Nu-1:
            resultString += nameList[i]+","
            i+=1
        resultString += nameList[i]
        return resultString

    def countUserAndFeature(self, user):
        """
        input: str
        return: two non-negative integers
        """
        N, M = 0, 0
        for i in range(len(user)):
            if user[i] == ":":
                N += 1
            if user[i] == ",":
                M += 1
        return N, int(M / N + 1)

    def userInfoDict(self, user, Nu, Nf):
        userDict = {}
        nameList = []
        # remove : and , ,then remove \n to construct name list and user dictionary
        nameAndColons = re.findall('\S+?:', user)
        #print(nameAndColons)
        for nameAndColon in nameAndColons:
            name = nameAndColon[0:len(nameAndColon) - 1]
            nameList.append(name)
        for i in range(Nu):
            j=Nu-i-1
            userSplitted=user.split(nameList[j]+":")
            user=userSplitted[0]
            userRawInfo0=userSplitted[1]
            #print(userRawInfo0)
            userRawInfo1=userRawInfo0.split(",")
            #print(userRawInfo1)
            for k in range(Nf):
              str_k=userRawInfo1[k]
              userRawInfo1[k]=str_k.replace("\n","").strip()
            #print(userRawInfo1)
            userDict[nameList[j]]=userRawInfo1

        #print(nameList)
        #print(userDict)

        return nameList,userDict

    def rankBaseDict(self, Nf, nameList, userDict):
        rankBaseDict=dict()
        userRankBase=userDict[nameList[0]]
        #print(userRankBase)
        for i in range(Nf):
            rankBaseDict[userRankBase[i]]=i+1
        #print(rankBaseDict)
        return rankBaseDict

    def inversionDict(self, Nf, userDict, rankBaseDict):
        inversionDict=dict()
        for name,rank in userDict.items():
            inversion = 0
            for i in range(Nf-1):
                for j in range(i+1,Nf):
                    if rankBaseDict[rank[i]] > rankBaseDict[rank[j]]:
                      inversion += 1
            inversionDict[name]=inversion
        #print(inversionDict)
        return inversionDict

    def sortNameList(self, Nu, inversionDict, nameList):
        for i in range(Nu-1,1,-1):
            for j in range(1, i):
                k=j+1
                if inversionDict[nameList[j]]>inversionDict[nameList[k]]:
                    nameList[j],nameList[k]=nameList[k],nameList[j]
                elif inversionDict[nameList[j]]<inversionDict[nameList[k]]:
                    continue
                else:
                    if nameList[j]>nameList[k]:
                        nameList[j], nameList[k] = nameList[k], nameList[j]
        #print(nameList)



testSolution = Solution()

case0 = '''
Bob:Rock,Blues,Jazz
Alice:Rock,Jazz,Blues
John:Jazz,Blues,Rock
'''
test0 = testSolution.collaborativeFiltering(case0)
print(test0)# Alice,John


case1='''
rabbit:carrot,cabbage,fish,meat turtle:cabbage,carrot,fish,meat 
cat:fish,meat,carrot,cabbage dog:meat,fish,cabbage,carrot
'''
test1=testSolution.collaborativeFiltering(case1) 
print(test1)#turtle,cat,dog

case2='''
Smith:helicopter,car,motorcycle,bicycle,bus 
Johnson:bus,helicopter,motorcycle,car,bicycle 
Williams:bicycle,helicopter,car,motorcycle,bus 
Jones:helicopter,bicycle,motorcycle,car,bus 
Brown:bus,motorcycle,helicopter,bicycle,car 
Davis:motorcycle,bus,car,bicycle,helicopter 
Miller:bicycle,helicopter,car,bus,motorcycle 
Wilson:helicopter,car,bicycle,bus,motorcycle
'''
test2=testSolution.collaborativeFiltering(case2) 
print(test2)#Wilson,Jones,Williams,Miller,Johnson,Brown,Davis


case3='''
James:Avengers,Captain Marvel,Dumbo,Shazam,Hellboy,Joker,Spider-Man,Aladdin,Toy Story,Dark 
Phoenix Olivia:Aladdin,Captain Marvel,Hellboy,Avengers,Toy Story,Spider-Man,Dark Phoenix,Joker,Dumbo,Shazam 
Sophia:Toy Story,Dark Phoenix,Aladdin,Joker,Captain Marvel,Hellboy,Dumbo,Shazam,Avengers,Spider-Man 
Jacob:Dumbo,Avengers,Spider-Man,Dark 
Phoenix,Hellboy,Joker,Aladdin,Captain Marvel,Shazam,Toy Story 
Oliver:Dumbo,Spider-Man,Aladdin,Toy Story,Avengers,Hellboy,Dark Phoenix,Shazam,Joker,Captain Marvel Johannes:Captain Marvel,Joker,Toy Story,Avengers,Aladdin,Hellboy,Shazam,Dark Phoenix,Spider-Man,Dumbo
'''
test3=testSolution.collaborativeFiltering(case3)
print(test3)#Jacob,Johannes,Olivia,Oliver,Sophia


"""
(combined results)
Alice,John
turtle,cat,dog
Wilson,Jones,Williams,Miller,Johnson,Brown,Davis
Jacob,Johannes,Olivia,Oliver,Sophia
"""
