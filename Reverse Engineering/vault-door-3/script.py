import operator

def vault_door_3():

    old_string = "jU5t_a_sna_3lpm17ga45_u_4_mbrf4c"
    convestion_table=[]
    new_string = "picoCTF{"

    for i in range(0,8):
        convestion_table.append({"original_index":i,"go_to":i})
    for i in range(8,16):
        convestion_table.append({"original_index": i, "go_to": 23-i})
    for i in range(16,32,2):
        convestion_table.append({"original_index": i, "go_to": 46-i})
    for i in range(31,16,-2):
        convestion_table.append({"original_index": i, "go_to": i})


    convestion_table.sort(key=operator.itemgetter('original_index'))
    for one in convestion_table:
        new_string+=old_string[one['go_to']]

    new_string+="}"
    print(new_string)

if __name__ == '__main__':
    vault_door_3()
