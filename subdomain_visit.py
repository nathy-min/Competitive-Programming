class Solution(object):
    def subdomainVisits(self, cpdomains):
        dic = collections.defaultdict(int)
        for cpdomain in cpdomains:
            current = cpdomain.split()
            count = int(current[0])
            domain = current[1]

            curr_domain = ''
            for sub in domain.split('.')[::-1]:
                if curr_domain == '':
                    curr_domain = sub
                else:
                    curr_domain = sub + '.' + curr_domain
                dic[curr_domain] += count

        result = []
        print(dic)
        for k,v in dic.items():
            res = str(v) + ' ' + k
            result.append(res)  

        return result 
