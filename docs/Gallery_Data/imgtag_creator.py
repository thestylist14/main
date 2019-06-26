def create_img_tag(directory_name, img_num):
  for i in range(img_num):
    ind = str(i + 1)
    diff = len(str(img_num)) - len(ind)
    if diff != 0:
      for i in range(diff):
        ind = "0"+ind
    val = " <a target='_blank' href='http://felab.kaist.ac.kr/Gallery_Data/" + directory_name +"/" + str(ind) + ".jpg'>"
    print("<div class='gallery'>")
    print(val)
    val = "   <img src='http://felab.kaist.ac.kr/Gallery_Data/" +directory_name +"/" + str(ind) +".jpg' alt='" + str(ind)+ "' width='600' height='400'>"
    print(val)
    print(" </a>")
    print("</div>")

def create_img_tag_optimized(directory_name, img_num):
  for i in range(img_num):
    ind = str(i + 1)
    diff = len(str(img_num)) - len(ind)
    if diff != 0:
      for i in range(diff):
        ind = "0"+ind
    val = " <a target='_blank' href='http://felab.kaist.ac.kr/Gallery_Data/" + directory_name +"/" + str(ind) + ".jpg'>"
    print("<div class='gallery'>")
    print(val)
    val = "   <img src='http://felab.kaist.ac.kr/Gallery_Data/" +directory_name +"/output/" + str(ind) +".jpg' alt='" + str(ind)+ "' width='600' height='400'>"
    print(val)
    print(" </a>")
    print("</div>")

if __name__ == '__main__':
  #create_img_tag("2015/20150408제주도학회", 122)
  create_img_tag_optimized("연구실생활", 13)