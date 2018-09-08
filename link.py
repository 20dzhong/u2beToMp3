class video:
    def __init__(self, link, name, d_plist):
        self.link = link
        self.name = name
        self.d_plist = d_plist
        if not self.d_plist: self.strip()

    def strip(self):
        tmp = ""
        for i in range(len(self.link)):
            if self.link[i] == "&":
                break
            tmp += self.link[i]
        self.link = tmp
        return


number_one = video("https://www.youtube.com/watch?v=PfYnvDL0Qcw&list=RDPfYnvDL0Qcw&t=1", "number_one", False)
print(number_one.link)
