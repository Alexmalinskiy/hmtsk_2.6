# folder SOurce and convert.exe lays in the same dir as python file
def convert_file():
    import subprocess
    import os.path

    file_path = os.getcwd()
    images_path = os.path.join(file_path, "Source")
    files = os.listdir(images_path)

    for file in files:
        if os.path.isfile(os.path.join(images_path, file)):
            command = "convert " + os.path.join("Source", file) + " -resize 200 " + \
                      os.path.join("Source", "Result", file.replace(".jpg", "(new).jpg"))
            proc_to_run = os.path.join(file_path, command)
            process = subprocess.run(proc_to_run)
            if process.returncode == 0:
                print("{0} successfully converted".format(file))


convert_file()
