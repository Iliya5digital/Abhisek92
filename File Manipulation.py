import os
import copy

os.chdir("D:\\Module_5-Lab\\Python\\KP\\") #Change this according to the location of the File

#Properly Store the File in Memory
def import_data(fileURI):
    fileMap=[]
    fileObject=open(fileURI, "r")
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
                        author_list = [a.strip().upper() for a in author_list]
                        for index in range(len(author_list)):
                            researcher = author_list[index]
                            if r'&' in researcher:
                                new_authors = researcher.split('&')
                                new_authors = [auth.strip().upper() for auth in new_authors]
                                del author_list[index]
                                author_list[index:index] = new_authors
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


def count_field(filemap, attr):
    field_set=set()
    for i in filemap:
        field_set.add(i[attr])
    return len(field_set)


def freq_dist(parent, child, filemap):
    list_child = dict() #Family Wise Species List
    parent_child_count=dict() #Frequency of Species per Family
    for i in filemap:
        if i[child] != '' and i[parent] != '':
            if i[parent].upper() in list_child.keys():
                list_child[i[parent].upper()].add(i[child].upper())
            else:
                list_child[i[parent].upper()]={i[child].upper()}
    for j in list_child.keys():
        parent_child_count[j]=len(list_child[j])
    return list_child, parent_child_count


def list_max_freq(parent, child):
    parent_child_count = freq_dist(parent, child, filemap)[1]
    max_freq=max(parent_child_count.values()) #family_species_count.values())
    xparent=set()
    for key in parent_child_count.keys():
        if parent_child_count[key]==max_freq:
            xparent.add(key.upper())
    return (xparent, max_freq)

#print freq_dist("FAMILY_NAME", "SPECIES_NAME", filemap)[1]

def discovered_by(discovery, author):
    unique_discoveries=set()
    for record in filemap:
        if author.upper() in [element.upper() for element in record['AUTHORS']]:
            if record[discovery] != '':
                unique_discoveries.add(record[discovery].upper())
    return unique_discoveries


def get_all_author(filemap):
    scientists = set() #Set of All Authors
    for record in filemap:
        scientists = scientists.union(set(record["AUTHORS"]))
    return scientists

def duration(filemap):
    author_active=dict()
    for scientist in get_all_author(filemap):
        unique_years=set()
        for record in filemap:
            if scientist.upper() in (author.upper() for author in record['AUTHORS']):
                unique_years.add(int(record['YEAR']))
        author_active[scientist.upper()]=(min(unique_years),max(unique_years))
    return author_active


def active_community(author, filemap):
    author_active = duration(filemap)
    ref_years=author_active[author.upper()]
    active_scientists=set()
    for key in duration(filemap).keys():
        active_years=author_active[key]
        if (active_years[0]>=ref_years[0]) and (active_years[1]<=ref_years[1]):
            active_scientists.add(key)
    active_scientists.remove(author.upper())
    return active_scientists

def get_discovery_table(filemap):
    discovery_table=dict() #Scientists with their Corresponding Discoveries
    for scientist in get_all_author(filemap):
        discovered=set()
        for record in filemap:
            if scientist.upper() in map(str.upper, record['AUTHORS']):
                name=record['SPECIES_NAME'].strip().upper()+" "+record['SUBSPECIES_NAME'].strip().upper()
                discovered.add(name)
        discovery_table[scientist]=discovered
    return discovery_table


def most_recent_discovery(filemap):
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
    return recent_discoveries, most_recent


def find_co_authors(author, filemap):
    author_set = {author.upper()}
    co_authors = set()
    for record in filemap:
        if (author.upper() in record["AUTHORS"]) and (len(record["AUTHORS"]) > 1):
            co_authors = co_authors.union(set(record["AUTHORS"]))
    return co_authors - author_set


#Read the File and Organize it
filemap=rectify(remove_attributes(import_data("orthoptera.txt"),{'SPECIES'}))

#Count Unique Species
print "No. of Unique Species: ", count_field(filemap, 'SPECIES_NAME')

#Families with most Species
print "Families with most Species: ",list(list_max_freq("FAMILY_NAME", "SPECIES_NAME")[0]),".\tCount: ",list_max_freq("FAMILY_NAME", "SPECIES_NAME")[1]

#No. of Unique Species discovered by Linnaeus
print "No. of Unique Species discovered by Linnaeus: ", len(discovered_by("SPECIES_NAME", "Linnaeus")), "\t", list(discovered_by("SPECIES_NAME", "Linnaeus"))

#No. of Unique Subspecies discovered by Linnaeus
print "No. of Unique Subspecies discovered by Linnaeus: ", list(discovered_by("SUBSPECIES_NAME", "Linnaeus")), "\tCount: ", len(discovered_by("SUBSPECIES_NAME", "Linnaeus"))

#Active Years of Linnaeus
print "Active Years of Linnaeus:",duration(filemap)["Linnaeus".upper()][0]," - ",duration(filemap)["Linnaeus".upper()][1],". Duration: ",duration(filemap)["Linnaeus".upper()][1]-duration(filemap)["Linnaeus".upper()][0]," years."

#Active Scientists during active years of Linnaeus
if not active_community('Linnaeus', filemap):
    print "Active Scientists during active years of Linnaeus: ", active_community('Linnaeus', filemap)
else:
    print "No Scientists were active during Active Years of Linnaeus"

#Co-authors of Linnaeus
if find_co_authors('Linnaeus', filemap):
    print "Co-authors of Linnaeus: ", list(find_co_authors('Linnaeus'.upper(), filemap))
else:
    print "Linnaeus has no Co-author"

#Co-authors of Willemse
if find_co_authors('F. Willemse'.upper(), filemap):
    print "Co-authors of F. Willemse: ", list(find_co_authors('F. Willemse'.upper(), filemap))
else:
    print "F. Willemse has no Co-author"

#Discoveries made by Willemse
print "Discoveries made by Willemse"," :",list(get_discovery_table(filemap)["Willemse".upper()]),". Count: ",len(get_discovery_table(filemap)["Willemse".upper()])

#Most Recent Discovery
print "Most Recent(",most_recent_discovery(filemap)[1],") Discoveries: ",list(most_recent_discovery(filemap)[0])