import csv

class csv_to_others:
    def population_csv_to_list(self):
        list_of_csv = []
        with open('总人口分省年度数据.csv', 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            list_of_csv = list(csv_reader)
        del list_of_csv[0:3]
        # del list_of_csv[-3:-1] 奶奶滴这么写不行，这-1就是删不掉
        list_of_csv.pop()
        list_of_csv.pop()
        # 年份列表
        years = list_of_csv[0]
        years.pop(0)
        years.reverse()
        list_of_csv.pop(0)
        # 地区列表、历年人口列表
        areas = []
        populations = []
        for index in range(len(list_of_csv)):
            areas.append(list_of_csv[index][0])
            list_of_csv[index].pop(0)
        for y in range(10):
            population = []
            for x in range(31):
                population.append(list_of_csv[x][y])
            populations.append(population)
        return (years, areas, populations)
# print(csv_to_others().population_csv_to_list())
    def mining_csv_to_list(self):
        list_of_csv = []
        with open('矿产储量.csv', 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            list_of_csv = list(csv_reader)
        del list_of_csv[0:3]
        # del list_of_csv[-3:-1] 奶奶滴这么写不行，这-1就是删不掉
        del list_of_csv[-4:-1]
        list_of_csv.pop()
        miningname=[]
        miningnum=[]
        for item in list_of_csv:
            miningname.append(item[0])
            miningnum.append(item[1])
        return (miningname, miningnum)

    def water_csv_to_list(self):
        list_of_csv = []
        with open('水资源数据.csv', 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            list_of_csv = list(csv_reader)
        del list_of_csv[0:3]
        # del list_of_csv[-3:-1] 奶奶滴这么写不行，这-1就是删不掉
        list_of_csv.pop()
        watername=[]
        waternum=[]
        for item in list_of_csv:
            watername.append(item[0])
            waternum.append(item[1])
        return (watername, waternum)

    def forest_csv_to_list(self):
        list_of_csv = []
        with open('森林资源数据.csv', 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            list_of_csv = list(csv_reader)
        del list_of_csv[0:3]
        # del list_of_csv[-3:-1] 奶奶滴这么写不行，这-1就是删不掉
        del list_of_csv[-3:-1]
        list_of_csv.pop()
        forestname=[]
        forestnum=[]
        for item in list_of_csv:
            forestname.append(item[0])
            forestnum.append(item[1])
        return (forestname, forestnum)
    def report_csv_to_list(self):
        with open('二十大报告.txt', 'r',encoding='utf-8') as read_obj:
            reader = read_obj.read()
        renmin=str(reader.count('人民'))
        renmin=tuple(['人民',renmin])

        heping=str(reader.count('和平'))
        heping = tuple(['和平', heping])

        taiwan=str(reader.count('台湾'))
        taiwan = tuple(['台湾', taiwan])

        minsheng=str(reader.count('民生'))
        minsheng = tuple(['民生', minsheng])

        fendou=str(reader.count('奋斗'))
        fendou = tuple(['奋斗', fendou])

        zixin=str(reader.count('自信'))
        zixin = tuple(['自信', zixin])

        xinshidai=str(reader.count('新时代'))
        xinshidai = tuple(['新时代', xinshidai])

        zgtsshzy=str(reader.count('中国特色社会主义'))
        zgtsshzy = tuple(['中国特色社会主义', zgtsshzy])

        zggcd=str(reader.count('中国共产党'))
        zggcd = tuple(['中国共产党', zggcd])

        guojia=str(reader.count('国家'))
        guojia = tuple(['国家', guojia])

        xiandaihua=str(reader.count('现代化'))
        xiandaihua = tuple(['现代化', xiandaihua])

        mkszy = str(reader.count('马克思主义'))
        mkszy = tuple(['马克思主义', mkszy])

        minzu = str(reader.count('民族'))
        minzu = tuple(['民族', minzu])

        wenhua = str(reader.count('文化'))
        wenhua = tuple(['文化', wenhua])

        zhongguo = str(reader.count('中国'))
        zhongguo = tuple(['中国', zhongguo])

        zhmzwdfx = str(reader.count('中华民族伟大复兴'))
        zhmzwdfx = tuple(['中华民族伟大复兴', zhmzwdfx])

        ggkf = str(reader.count('改革开放'))
        ggkf = tuple(['改革开放', ggkf])

        data=[renmin,heping,taiwan,minsheng,fendou,zixin,xinshidai,zgtsshzy,zggcd,guojia,xiandaihua,mkszy,minzu,wenhua,zhongguo,zhmzwdfx,ggkf]
        data.extend(data)
        return data
print(csv_to_others().report_csv_to_list())
