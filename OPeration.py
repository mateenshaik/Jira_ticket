def update(file_path, key, value):
    with open(file_path, "r") as file:
      lines =  file.readlines()


    with open(file_path, "w") as file:
       for line in lines:
        if key in line:
          lines = file.write(key + "=" + value + "\n")  
        else:
          file.write(line)


update("server.conf", "MAX_CONNECTIONS", "1000")