import os, time, shutil

class Sort:

    def __init__(self):
        print("-: Welcome To Auto Sort File Manager :-")
        self.path = input("\nEnter targeted path : ")
        self.count = 0
        self.pic = 0
        self.vid = 0
        self.doc = 0
        self.app = 0
        self.aud = 0
        self.other = 0
        self.audFormat = (".mp3", ".aac", ".wma", ".wav")
        self.appFormat = (".exe", ".bat", ".bin", ".iso", ".msi", ".reg")
        self.docFormat = (".doc", ".txt", ".xml", ".pdf", ".docx", ".xls", ".ppt", ".xlsx")
        self.vidFormat = (".mp4", ".3gp", ".avi", ".wmv", ".mkv")
        self.picFormat = (".jpg", ".png", ".jpeg", ".tif", ".gif")

    def __del__(self):
        print()
        print("All files are sorted..!!")
        print("Have a nice day..!!")
        time.sleep(1)

    #count present files
    def counter(self): 
        for root, dir, files in os.walk(self.path):
            for file in files:
                    self.count += 1
                    if file.endswith(self.audFormat):
                        self.aud += 1
                    elif file.endswith(self.appFormat):
                        self.app += 1
                    elif file.endswith(self.docFormat):
                        self.doc += 1
                    elif file.endswith(self.vidFormat):
                        self.vid +=1
                    elif file.endswith(self.picFormat):
                        self.pic += 1
                    else:
                        self.other += 1
        l = len("{0:<20}:{1}".format("Total Files", self.count))
        print()
        print("{0:<20}:{1}".format("Image Files", self.pic))
        print("{0:<20}:{1}".format("Video Files", self.vid))
        print("{0:<20}:{1}".format("Document Files", self.doc))
        print("{0:<20}:{1}".format("Audio Files", self.aud))
        print("{0:<20}:{1}".format("Application Files", self.app))
        print("{0:<20}:{1}".format("Other Files", self.other))
        print("="*(l+1))
        print("{0:<20}:{1}".format("Total Files", self.count))
        print()

     # create require directories   
    def creater(self):
        try:
            if self.aud > 0:
                os.mkdir(os.path.join(self.path, "audios"))
        except FileExistsError:
            print("Audio Directory Already Exist..!!")
        try:
            if self.pic > 0:
                os.mkdir(os.path.join(self.path, "pictures"))
        except FileExistsError:
            print("Picture Directory Already Exist..!!")
        try:
            if self.doc > 0:
                os.mkdir(os.path.join(self.path, "documents"))
        except FileExistsError:
            print("Document Directory Already Exist..!!")
        try:
            if self.app > 0:
                os.mkdir(os.path.join(self.path, "applications"))
        except FileExistsError:
            print("Appliction Directory Already Exist..!!")
        try:
            if self.vid > 0:
                os.mkdir(os.path.join(self.path, "videos"))
        except FileExistsError:
            print("Video Directory Already Exist..!!")
        try:
            if self.other > 0:
                os.mkdir(os.path.join(self.path, "others"))
        except FileExistsError:
            print("Other Directory Already Exist..!!")
        print()

    # move file to respective directory 
    def sorting(self):
        for root, dir, files in os.walk(self.path):
            for file in files:
                print("Total remaining files : "+str(self.count))
                if self.count == 0:
                    break
                else:
                    try:
                        if file.endswith(self.audFormat):
                            shutil.move(os.path.join(self.path, root, file), os.path.join(self.path, "audios"))
                        elif file.endswith(self.appFormat):
                            shutil.move(os.path.join(self.path, root, file), os.path.join(self.path, "applications"))
                        elif file.endswith(self.docFormat):
                            shutil.move(os.path.join(self.path, root, file), os.path.join(self.path, "documents"))
                        elif file.endswith(self.vidFormat):
                            shutil.move(os.path.join(self.path, root, file), os.path.join(self.path, "videos"))
                        elif file.endswith(self.picFormat):
                            shutil.move(os.path.join(self.path, root, file), os.path.join(self.path, "pictures"))
                        else:
                            shutil.move(os.path.join(self.path, root, file), os.path.join(self.path, "others"))
                    except shutil.Error:
                            pass
                    self.count -= 1

    #delete unwanted directories
    def checker(self):
        directories = ("audios","pictures","videos","applications","documents","others")
        for root, dir, files in os.walk(self.path):
                for d in dir:
                    if d not in directories:
                        shutil.rmtree(os.path.join(root, d))
                        
sort = Sort()
sort.counter()
sort.creater()
sort.sorting()
sort.checker()
