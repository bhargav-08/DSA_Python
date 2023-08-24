from collections import defaultdict


def accountsMerge(accounts):
    par = [i for i in range(len(accounts))]
    mailMap = {}
    for idx, emails in enumerate(accounts):
        for email in emails[1:]:
            if email not in mailMap:
                mailMap[email] = idx
            else:
                par[idx] = par[mailMap[email]]

    # res = [[]] * len(accounts)
    res = []
    temp = defaultdict(set)

    for idx, emails in enumerate(accounts):
        for email in emails[1:]:
            UPar = par[mailMap[email]]
            while UPar != par[UPar]:
                UPar = par[UPar]
            temp[UPar].add(email)

    print(temp)
    for idx, emails in enumerate(accounts):
        if temp[idx]:
            res.append([emails[0]])
            # res[idx].append(emails[0])
            # res[idx].append(sorted(temp[idx]))
            res[-1].extend(sorted(temp[idx]))

    return res


accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"]]

accounts = [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"], ["David",
                                                                                               "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"], ["David", "David1@m.co", "David2@m.co"]]

print(accountsMerge(accounts))
