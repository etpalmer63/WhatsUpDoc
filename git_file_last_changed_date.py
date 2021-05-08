def find_last_change(file_types,date_fmt):

    from datetime import datetime
    
    #run the bash script first --> creates git_file_last_Changed_date.tmp 
    import os
    os.system('./git_file_last_changed_date.sh')
    
    f = open("git_file_last_changed_date.tmp","r")
    
    file_date_list = [] 
    
    #included file types
    #f_types = ["cpp", "c", "py", "sh", "rst"]
    
    
    
    while f.readline():
        line = f.readline()
        line_splt = line.split(".")
        line_splt[-1] = line_splt[-1].rstrip()
        #print(line)
        if line_splt[-1] in file_types:
            line_splt2 = line.split(" ")
            file_date_list.append(line_splt2[1:6])
    
    
    
    #print(file_date_list)
    
    
    
    time_stamp_list =[]
    sep=" "
    date_fmt_shell = "%b %d %H:%M:%S %Y %z"
    
    for n in file_date_list:
        #print(n.join(" ")
        print(sep.join(n))
        #T1 = datetime.strptime(sep.join(n),"%b %d %H:%M:%S %Y %z") 
        #print(T1)
        time1 = datetime.strptime(sep.join(n), date_fmt_shell)
        time_stamp_list.append(time1)
    
    
    #print(time_stamp_list)
    
    most_recent_change = datetime.strftime(max(time_stamp_list), date_fmt)    
        
    return most_recent_change

if __name__ == '__main__':
    find_last_change()

