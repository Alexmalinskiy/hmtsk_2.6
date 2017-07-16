# folder SOurce and convert.exe lays in the same dir as python file
import subprocess
import os.path
import os


def convert_file():
    file_path = os.getcwd()
    images_path = os.path.join(file_path, "Source")
    result_path = os.path.join(images_path, "Result")
    if not os.path.exists(result_path):
        os.makedirs(result_path)
    files = os.listdir(images_path)

    for file in files:
        if os.path.isfile(os.path.join(images_path, file)):
            command = "convert " + os.path.join(os.path.relpath(images_path), file) + " -resize 200 " + \
                      os.path.join(os.path.relpath(result_path), file.replace(".jpg", "(new).jpg"))

            process = subprocess.run(command)
            if process.returncode == 0:
                print("{0} successfully converted".format(file))


if __name__ == '__main__':
    convert_file()
