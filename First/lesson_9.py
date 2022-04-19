class IpProccessing():
    def expanded_list(self, ip_adresses):
        self.ip_adresses= ip_adresses
        ip_adresses_complite=[]
        for i in range(len(ip_adresses)):
            ip=""
            split=ip_adresses[i].split('.')
            split.reverse()
            for i in range(len(split)-1):
                split.insert(i*2+1,".")
            for i in range(len(split)):
                ip+=split[i]
            ip_adresses_complite.append(ip)
        return(ip_adresses_complite)
    def clear_first_otk(self, ip_adresses):
        self.ip_adresses= ip_adresses
        ip_adresses_complite=[]
        for i in range(len(ip_adresses)):
            ip=""
            split=ip_adresses[i].split('.')
            split.pop(0)
            for i in range(len(split)-1):
                split.insert(i*2+1,".")
            for i in range(len(split)):
                ip+=split[i]
            ip_adresses_complite.append(ip)

        return(ip_adresses_complite)
    def clear_last_otk(self, ip_adresses):
        self.ip_adresses= ip_adresses
        ip_adresses_complite=[]
        for i in range(len(ip_adresses)):
            ip=""
            split=ip_adresses[i].split('.')
            ip+=split[-1]
            ip_adresses_complite.append(ip)

        return(ip_adresses_complite)

ip_adresses = ["10.11.12.13", "10.11.12.14", "10.11.12.15"]
print(ip_adresses)
print("--------------------------------------------")
ip_adresses1 = IpProccessing()
print(ip_adresses1.expanded_list(ip_adresses))
print(ip_adresses1.clear_first_otk(ip_adresses))
print(ip_adresses1.clear_last_otk(ip_adresses))

# Task 2:

class FilesProccessing():

    def read_file(self, file_adress, mode):
        print("---------------" + file_adress + "-------------")
        filel = open(file_adress, mode)
        print(filel.read())
        print("---------------" + file_adress + "-------------")
        filel.close()

    def write_file(self, file_adress, mode):
        filel = open(file_adress, mode)
        filel.write(input("Your text message:"))
        filel.close()

    def clear_file(self, file_adress, mode):
        filel = open(file_adress, mode)
        filel.close()


file_adress = 'Test.txt'

file = FilesProccessing()

file.read_file(file_adress, 'r')
file.write_file(file_adress, 'a')
# file.clear_file(file_adress,'w')


