import os
import copy

os.chdir("D:\\Module_5-Lab\\Python\\KP\\") #Change this according to the location of the File

#Properly Store the File in Memory
def import_data(fileURI):
    fileMap=[]
    fileObject=open(fileURI,"r")
    header_list=((fileObject.readline().decode("utf-8-sig").encode("utf-8")).strip()).split(';')
    contents=fileObject.readlines()
    for j in contents:
        j=j.decode("utf-8-sig").encode("utf-8").strip()
    for line in contents:
        element_list=line.strip().split(';')
        if len(element_list)==len(header_list):
            record={}
            for i in range(len(header_list)):
                record[header_list[i]]=element_list[i].strip()
            fileMap.append(record)
        else:
            print "Data Format Error!"
            return None
            break
    return fileMap

#Remove Derived Attributes
def remove_attributes(filemap, attribute_set):
    if isinstance(filemap, list) and isinstance(attribute_set, set):
        for record in filemap:
            if isinstance(record, dict):
                if attribute_set.issubset(set(record.keys())):
                    for key in attribute_set:
                        del record[key]
                else:
                    print "Input Error / Data Format Error"
                    return None
            else:
                print "Data Format Error"
                return None
    else:
        print "Input Error"
    return filemap

#Organize Clubbed Attributes
def rectify(fileMap):
    filemap=copy.deepcopy(fileMap)
    if isinstance(filemap, list):
        for record in filemap:
            if isinstance(record, dict):
                if 'AUTHORSHIP' in record.keys():
                    authorship=record['AUTHORSHIP']
                    if isinstance(authorship, str):
                        author_list=(authorship.strip("()")).split(',')
                        for element in author_list:
                            element.strip()
                        del record['AUTHORSHIP']
                        year=author_list[-1]
                        record['AUTHORS']=author_list[:(len(author_list)-1)]
                        record['YEAR']=year
                    else:
                        print "Rectify: Data Format Error"
                        return None
                else:
                    print "Rectify: Wrong Data"
            else:
                "Rectify: Wrong Data"
        return filemap
    else:
        print "Rectify: Input Error"
        return None


#Read the File and Organize it
filemap=rectify(remove_attributes(import_data("orthoptera.txt"),{'SPECIES'}))

#Count Unique Species
species_set=set()
for i in filemap:
    species_set.add(i['SPECIES_NAME'])
print "Unique Species Count: ",len(species_set)

family_species=dict() #Family Wise Species List
family_species_count=dict() #Frequency of Species per Family
for i in filemap:
    if i['FAMILY_NAME'] in family_species.keys():
        family_species[i['FAMILY_NAME']].append(i['SPECIES_NAME'])
    else:
        family_species[i['FAMILY_NAME']]=[i['SPECIES_NAME']]
for j in family_species.keys():
    family_species_count[j]=len(set(family_species[j]))

#Family with most Species
max_sfreq=max(family_species_count.values())
xfamily=set()
for key in family_species_count.keys():
    if family_species_count[key]==max_sfreq:
        xfamily.add(key.upper())
print  "Family with most Species: ",list(xfamily),".\tCount: ",max_sfreq

genus_subspecies=dict() #Genus Wise Subspecies List
genus_subspecies_count=dict() #Frequency of Subspecies per Genus
for i in filemap:
    if i['GENUS_NAME'].upper() in genus_subspecies.keys():
        genus_subspecies[i['GENUS_NAME'].upper()].add(i['SUBSPECIES_NAME'].upper())
    else:
        subspecies=set()
        subspecies.add(i['SUBSPECIES_NAME'].upper())
        genus_subspecies[i['GENUS_NAME'].upper()]=subspecies
for j in genus_subspecies.keys():
    genus_subspecies_count[j]=len(set(genus_subspecies[j]))

#Genus with most Subspecies
max_sgfreq=max(genus_subspecies_count.values())
sgset=set()
for key in genus_subspecies_count.keys():
    if genus_subspecies_count[key]==max_sgfreq:
        sgset.add(key)
print  "Genus with most Subspecies: ",list(sgset),".\tCount: ",max_sgfreq

#No. of Unique Species discovered by Linnaeus
unique_species=set()
for record in filemap:
    if 'Linnaeus'.upper() in map(str.upper, record['AUTHORS']):
        unique_species.add(record['SPECIES_NAME'])
print "No. of Unique Species discovered by Linnaeus is: ",len(unique_species)

#No. of Unique Subspecies discovered by Linnaeus
unique_subspecies=set()
for record in filemap:
    if 'Linnaeus'.upper() in map(str.upper, record['AUTHORS']):
        if record['SUBSPECIES_NAME']!='':
            unique_subspecies.add(record['SUBSPECIES_NAME'])
print "No. of Unique Subspecies discovered by Linnaeus is: ",len(unique_subspecies)


scientists=set()#Set of All Authors
for record in filemap:
    scientists=scientists.union(set(record["AUTHORS"]))

#Active Years of Linnaeus 
author_active=dict()
for scientist in scientists:
    unique_years=set()
    for record in filemap:
        if scientist.upper() in (author.upper() for author in record['AUTHORS']):
            unique_years.add(int(record['YEAR']))
    author_active[scientist.upper()]=(min(unique_years),max(unique_years))
print "Active Years of Linnaeus:",author_active["Linnaeus".upper()][0]," - ",author_active["Linnaeus".upper()][1],". Duration: ",author_active["Linnaeus".upper()][1]-author_active["Linnaeus".upper()][0]," years."

#Active Scientists during active years of Linnaeus
author="Linnaeus"
ref_years=author_active[author.upper()]
active_scientists=set()
for key in author_active.keys():
    active_years=author_active[key]
    if (active_years[0]>=ref_years[0]) and (active_years[1]<=ref_years[1]):
        active_scientists.add(key)
active_scientists.remove(author.upper())
if len(active_scientists)!=0:
    print "Active Scientists during active years of Linnaeus: ",list(active_scientists),"\tCount: ",len(active_scientists)
else:
    print "No Scientists active during active years of Linnaeus"


discovery_table=dict() #Scientists with their Corresponding Discoveries
for scientist in scientists:
    discovered=set()
    for record in filemap:
        if scientist.upper() in map(str.upper, record['AUTHORS']):
            name=record['SPECIES_NAME'].strip().upper()+" "+record['SUBSPECIES_NAME'].strip().upper()
            discovered.add(name)
    discovery_table[scientist]=discovered

#Discoveries made by Willemse
authorx="Willemse"
print "Discoveries made by ",authorx," :",list(discovery_table[authorx]),". Count: ",len(discovery_table[authorx])

years=set()
for r in filemap:
    if r['YEAR']!='':
        years.add(int(r['YEAR']))

#Year of Most Recent Discovery
most_recent=max(years)

#Most Recent Discoveries
recent_discoveries=set()
for r in filemap:
    if int(r['YEAR'])==most_recent:
        recent_discoveries.add((r["SPECIES_NAME"]).upper())
print "Most Recent(",most_recent,") Discoveries: ",list(recent_discoveries)