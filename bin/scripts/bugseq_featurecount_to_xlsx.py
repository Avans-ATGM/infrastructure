import pandas as pd
input_file = "F:/downloads/Spiike-in.tsv"


def explore_taxonomy(tax):
    d = "NA"
    p = "NA"
    c = "NA"
    o = "NA"
    f = "NA"
    g = "NA"
    s = "NA"

    tax=tax.split(";")
    for element in tax:
        if element[0] == 'd':
            d = element[3:]
        elif element[0] == 'p':
            p = element[3:]
        elif element[0] == 'c':
            c = element[3:]
        elif element[0] == 'o':
            o = element[3:]
        elif element[0] == 'f':
            f = element[3:]
        elif element[0] == 'g':
            g = element[3:]
        elif element[0] == 's':
            s = element[3:]
    return [d,p,c,o,f,g,s]
def input_data_table(lines):
    limit = 0
    data_table = {"total_reads": 0,
                  "Domain": {}}

    for line in lines:
        if line[0] != "#":
            limit += 1
            tmp = line.rstrip().split("\t")
            N_reads = float(tmp[1])
            data_table["total_reads"] += (N_reads)
            tax = explore_taxonomy(tmp[0])


            if limit == -2:
                break

            #import Domain
            if tax[0] not in data_table["Domain"].keys():
                data_table["Domain"][tax[0]] = {"total_Domain_reads": N_reads,
                                      "Phylum":{}}

            else:
                #data_table["Domain"][tax[0]]["total_Domain_reads"] = data_table["Domain"][tax[0]]["total_Domain_reads"] + N_reads
                data_table["Domain"][tax[0]]["total_Domain_reads"] += N_reads
            #import Phylium
            if tax[1] not in data_table["Domain"][tax[0]]["Phylum"].keys():
                data_table["Domain"][tax[0]]["Phylum"][tax[1]] = {"total_Phylum_reads": N_reads,
                                                        "Class":{}}

            else:
                data_table["Domain"][tax[0]]["Phylum"][tax[1]]["total_Phylum_reads"] += N_reads

            #import Class
            if tax[2] not in data_table["Domain"][tax[0]]["Phylum"][tax[1]]["Class"].keys():
                data_table["Domain"][tax[0]]["Phylum"][tax[1]]["Class"][tax[2]] = {"total_Class_reads": N_reads,
                                                        "Order":{}}

            else:
                data_table["Domain"][tax[0]]["Phylum"][tax[1]]["Class"][tax[2]]["total_Class_reads"] += N_reads

            #import Order
            if tax[3] not in data_table["Domain"][tax[0]]["Phylum"][tax[1]]["Class"][tax[2]]["Order"].keys():
                data_table["Domain"][tax[0]]["Phylum"][tax[1]]["Class"][tax[2]]["Order"][tax[3]] = {"total_Order_reads": N_reads,
                                                        "Family":{}}
            else:
                data_table["Domain"][tax[0]]["Phylum"][tax[1]]["Class"][tax[2]]["Order"][tax[3]]["total_Order_reads"] += N_reads

            #import Family
            if tax[4] not in data_table["Domain"][tax[0]]["Phylum"][tax[1]]["Class"][tax[2]]["Order"][tax[3]]["Family"].keys():
                data_table["Domain"][tax[0]]["Phylum"][tax[1]]["Class"][tax[2]]["Order"][tax[3]]["Family"][tax[4]]  = {"total_Family_reads": N_reads,
                                                        "Genus":{}}
            else:
                data_table["Domain"][tax[0]]["Phylum"][tax[1]]["Class"][tax[2]]["Order"][tax[3]]["Family"][tax[4]]["total_Family_reads"] += N_reads

            #import Genus
            if tax[5] not in data_table["Domain"][tax[0]]["Phylum"][tax[1]]["Class"][tax[2]]["Order"][tax[3]]["Family"][tax[4]]["Genus"].keys():
                data_table["Domain"][tax[0]]["Phylum"][tax[1]]["Class"][tax[2]]["Order"][tax[3]]["Family"][tax[4]]["Genus"][tax[5]]  = {"total_Genus_reads": N_reads,
                                                        "Species":{}}
            else:
                data_table["Domain"][tax[0]]["Phylum"][tax[1]]["Class"][tax[2]]["Order"][tax[3]]["Family"][tax[4]]["Genus"][tax[5]]["total_Genus_reads"] += N_reads


            #import species
            if tax[6] not in data_table["Domain"][tax[0]]["Phylum"][tax[1]]["Class"][tax[2]]["Order"][tax[3]]["Family"][tax[4]]["Genus"][tax[5]]["Species"].keys():
                data_table["Domain"][tax[0]]["Phylum"][tax[1]]["Class"][tax[2]]["Order"][tax[3]]["Family"][tax[4]]["Genus"][tax[5]]["Species"][tax[6]]  = {"total_species_reads": N_reads}
            else:
                data_table["Domain"][tax[0]]["Phylum"][tax[1]]["Class"][tax[2]]["Order"][tax[3]]["Family"][tax[4]]["Genus"][tax[5]]["Species"][tax[6]]["total_species_reads"] += N_reads

    return data_table
def convert_to_dataframe(data_dict):
    print(data_dict)
    total_reads=data_dict["total_reads"]
    for Domain in data_dict["Domain"].keys():
        if Domain != "NA":
            reads = (data_dict["Domain"][Domain]["total_Domain_reads"])
            data_dict["Domain"][Domain]["percentage"] = (reads / total_reads * 100)

            for Phylum in data_dict["Domain"][Domain]["Phylum"].keys():
                if Phylum != "NA":
                    reads = (data_dict["Domain"][Domain]["Phylum"][Phylum]["total_Phylum_reads"])
                    data_dict["Domain"][Domain]["Phylum"][Phylum]["percentage"] = (reads / total_reads * 100)

                    for Class in data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"].keys():
                            if Class != "NA":
                                reads = (data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["total_Class_reads"])
                                data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["percentage"] = (reads / total_reads * 100)

                                for Order in data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"].keys():
                                        if Order != "NA":
                                            reads = (data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["total_Order_reads"])
                                            data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["percentage"] = (reads / total_reads * 100)


                                            for Family in data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"].keys():
                                                if Family != "NA":
                                                    reads = (data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["total_Family_reads"])
                                                    data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["percentage"] = (reads / total_reads * 100)

                                                    for Genus in data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["Genus"].keys():
                                                        if Genus != "NA":
                                                            reads = (data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["Genus"][Genus]["total_Genus_reads"])
                                                            data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["Genus"][Genus]["percentage"] = (reads / total_reads * 100)

                                                            for Species in data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["Genus"][Genus]["Species"].keys():
                                                                    if Species != "NA":
                                                                        reads = (data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["Genus"][Genus]["Species"][Species]["total_species_reads"])
                                                                        data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["Genus"][Genus]["Species"][Species]["percentage"] = (reads / total_reads * 100)
    return(data_dict)
def write_results(domain_dict,phylum_dict,class_dict,order_dict,family_dict,genus_dict,species_dict,input_file):

    output_file = (input_file.rsplit("/",1))
    file = str((output_file[-1].rsplit(".",1))[0])+".xlsx"
    output_file = f"{output_file[0]}/{file}"

    Domain = pd.DataFrame(domain_dict).transpose()
    Phylium = pd.DataFrame(phylum_dict).transpose()
    Class = pd.DataFrame(class_dict).transpose()
    Order = pd.DataFrame(order_dict).transpose()
    family = pd.DataFrame(family_dict).transpose()
    genus = pd.DataFrame(genus_dict).transpose()
    species = pd.DataFrame(species_dict).transpose()

    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    Domain.to_excel(writer, sheet_name='Domain')
    Phylium.to_excel(writer, sheet_name='Phylum')
    Class.to_excel(writer, sheet_name='Class')
    Order.to_excel(writer, sheet_name='Order')
    family.to_excel(writer, sheet_name='Family')
    genus.to_excel(writer, sheet_name='Genus')
    species.to_excel(writer, sheet_name='Species')
    writer.save()


def split_in_dataframes(data_dict):


    domain_dict = {}
    phylum_dict = {}
    class_dict = {}
    order_dict = {}
    family_dict = {}
    genus_dict = {}
    species_dict = {}


    for Domain in data_dict["Domain"].keys():
        if Domain != "NA":
            reads = (data_dict["Domain"][Domain]["total_Domain_reads"])
            perc = data_dict["Domain"][Domain]["percentage"]

            domain_dict[Domain]={"Reads":reads,
                                 "perc":perc}

            for Phylum in data_dict["Domain"][Domain]["Phylum"].keys():
                if Phylum != "NA":
                    reads = (data_dict["Domain"][Domain]["Phylum"][Phylum]["total_Phylum_reads"])
                    perc = data_dict["Domain"][Domain]["Phylum"][Phylum]["percentage"]

                    phylum_dict[Phylum] = {"Domain":Domain,
                                           "Phylum":Phylum,
                                           "Reads": reads,
                                           "perc": perc}

                    for Class in data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"].keys():
                            if Class != "NA":
                                reads = (data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["total_Class_reads"])
                                perc = data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["percentage"]

                                class_dict[Class] = {"Domain": Domain,
                                                       "Phylum": Phylum,
                                                      "class":Class,
                                                       "Reads": reads,
                                                       "perc": perc}

                                for Order in data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"].keys():
                                        if Order != "NA":
                                            reads = (data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["total_Order_reads"])
                                            perc = data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["percentage"]

                                            order_dict[Order] = {"Domain": Domain,
                                                                 "Phylum": Phylum,
                                                                 "class": Class,
                                                                 "order": Order,
                                                                 "Reads": reads,
                                                                 "perc": perc}

                                            for Family in data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"].keys():
                                                if Family != "NA":
                                                    reads = (data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["total_Family_reads"])
                                                    perc = data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["percentage"]

                                                    family_dict[Family] = {"Domain": Domain,
                                                                         "Phylum": Phylum,
                                                                         "class": Class,
                                                                         "order": Order,
                                                                           "Family":Family,
                                                                         "Reads": reads,
                                                                         "perc": perc}

                                                    for Genus in data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["Genus"].keys():
                                                        if Genus != "NA":
                                                            reads = (data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["Genus"][Genus]["total_Genus_reads"])
                                                            perc = data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["Genus"][Genus]["percentage"]

                                                            genus_dict[Genus] = {"Domain": Domain,
                                                                                   "Phylum": Phylum,
                                                                                   "class": Class,
                                                                                   "order": Order,
                                                                                   "Family": Family,
                                                                                   "Genus": Genus,
                                                                                   "Reads": reads,
                                                                                   "perc": perc}

                                                            for Species in data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["Genus"][Genus]["Species"].keys():
                                                                    if Species != "NA":
                                                                        reads = (data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["Genus"][Genus]["Species"][Species]["total_species_reads"])
                                                                        perc = data_dict["Domain"][Domain]["Phylum"][Phylum]["Class"][Class]["Order"][Order]["Family"][Family]["Genus"][Genus]["Species"][Species]["percentage"]

                                                                        species_dict[Species] = {"Domain": Domain,
                                                                                             "Phylum": Phylum,
                                                                                             "class": Class,
                                                                                             "order": Order,
                                                                                             "Family": Family,
                                                                                             "Genus": Genus,
                                                                                             "species":Species,
                                                                                             "Reads": reads,
                                                                                             "perc": perc}

    return (domain_dict,
            phylum_dict,
            class_dict,
            order_dict,
            family_dict,
            genus_dict,
            species_dict)

with open(input_file,'r') as file_in:
            lines = file_in.readlines()
            data_table = input_data_table(lines)


data_dict = convert_to_dataframe(data_table)
(domain_dict,phylum_dict,class_dict,order_dict,family_dict,genus_dict,species_dict) = split_in_dataframes(data_dict)

write_results(domain_dict,phylum_dict,class_dict,order_dict,family_dict,genus_dict,species_dict,input_file)
