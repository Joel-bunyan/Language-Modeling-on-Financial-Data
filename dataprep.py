def preparedata(data_list):
    max_str_length = max(len(item[0]) for item in data_list)
    
    columnar_data = ""
    for item in data_list:
        str_item = item[0].ljust(max_str_length) 
        int1_item = str(item[1]).rjust(10)        
        int2_item = str(item[2]).rjust(10)        
        
        row = f"{str_item} | {int1_item} | {int2_item}\n"
        columnar_data += row
    
    column_headers = f"{'String':{max_str_length}} | {'Integer 1':>10} | {'Integer 2':>10}\n"
    separator_line = "-" * (max_str_length + 14) + "\n"
    
    final_string = column_headers + separator_line + columnar_data
    
    return final_string


