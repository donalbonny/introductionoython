#!/opt/anaconda/bin/python

def printHelloworld():
    return 'hello, world'

def getRevCompl(nuclStr):

        ''' (str) --> str
        return the reversed complemetant of a nucleotide string.
        >>> getRevCompl('gattaca')
        '''
        complDict = {'a':'t', 'c':'g', 'g':'c', 't':'a'}
        outputStr=''
        for nucleotide in nuclStr:
                outputStr= complDict[nucleotide]+ outputStr
        return outputStr


