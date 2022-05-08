train_path = 'PlantVillage/train'
lists = os.listdir(train_path)
image_per_classe=10
ens_img=[]
#print("len of classes",len(lists))

#print("background in  lists = ", 'background' in  lists)

#print(len(lists))
lists.remove ('background')
#print("background in  lists = ", 'background' in  lists)
for classe in lists: 
  classe_path= os.path.join(train_path,classe)
  #print(classe_path)
 # classe_img_list= os.listdir(classe_path)[:2]
  classe_img_list= os.listdir(classe_path)
  #print(classe_img_list)
  
  for i in range(image_per_classe):
    str= os.path.join(classe_path,classe_img_list[i])
    ens_img.append([classe_img_list[i],classe,str])
    if i == len(classe_img_list):# sort de la boucle if atteint limit des image existe dans cette classe
      break

#print("----------res---------")
#for i in  ens_img: 
#  print(i)

print(len(ens_img))
#for l in lists:
#  print(l)

#print(lists.index('background'))

df_img_choisi=pd.DataFrame(ens_img,columns=[ "image_Name","Diseases","image_abs_path"])
#df_img_choisi.rename(columns={"0" : "image Name", "1" : "Diseases", "2": "image abs path"})
#df_img_choisi.rename(columns={"image Name", "Diseases", "image abs path"})
df_img_choisi


def create_small_dataset():
  train_path = 'PlantVillage/train'
lists = os.listdir(train_path)
image_per_classe=10
ens_img=[]
#print("len of classes",len(lists))

#print("background in  lists = ", 'background' in  lists)

#print(len(lists))
lists.remove ('background')
#print("background in  lists = ", 'background' in  lists)
for classe in lists: 
  classe_path= os.path.join('/content/PlantVillage/train',classe)
  #print(classe_path)
 # classe_img_list= os.listdir(classe_path)[:2]
  classe_img_list= os.listdir(classe_path)
  #print(classe_img_list)
  
  for i in range(image_per_classe):
    str= os.path.join(classe_path,classe_img_list[i])
    ens_img.append([classe_img_list[i],classe,str])
    if i == len(classe_img_list):# sort de la boucle if atteint limit des image existe dans cette classe
      break

#print("----------res---------")
#for i in  ens_img: 
#  print(i)

print(len(ens_img))
#for l in lists:
#  print(l)

#print(lists.index('background'))

df_img_choisi=pd.DataFrame(ens_img,columns=[ "image_Name","Diseases","image_abs_path"])
#df_img_choisi.rename(columns={"0" : "image Name", "1" : "Diseases", "2": "image abs path"})
#df_img_choisi.rename(columns={"image Name", "Diseases", "image abs path"})
df_img_choisi

# create small dataset

import shutil

#number_images =100
#selected_images_df = train_df.sample(number_images)
selected_images_df = df_img_choisi
idx=0

dst_folder = '/content/small_dataset/train/'

for index, row in selected_images_df.iterrows():
#  if(row.Diseases == 'background'): 
#    continue
  image_path_src = row.image_abs_path # os.path.join(train_path,row.Paths)
  image_path_dst= os.path.join(dst_folder,row.Diseases) # ex :/content/small_dataset/train/Apple___Black_rot


  os.makedirs(image_path_dst, exist_ok=True)
  #print("image_path_dst ")
 # print(image_path_dst)
   
  shutil.copyfile(image_path_src, os.path.join(dst_folder,row.Diseases,row.image_Name ))  
  print("{} ---> {} ".format(image_path_src,os.path.join(dst_folder, row.Diseases,row.image_Name)))

  idx= idx + 1



def create_small_dataset_validation():
  validation_path = 'PlantVillage/val'
  lists = os.listdir(validation_path)
  image_per_classe=10
  ens_img=[]
  #print("len of classes",len(lists))

  #print("background in  lists = ", 'background' in  lists)

  #print(len(lists))
  lists.remove ('background')
  #print("background in  lists = ", 'background' in  lists)
  for classe in lists: 
    classe_path= os.path.join(validation_path,classe)
    #print(classe_path)
  # classe_img_list= os.listdir(classe_path)[:2]
    classe_img_list= os.listdir(classe_path)
    #print(classe_img_list)
    
    for i in range(image_per_classe):
      str= os.path.join(classe_path,classe_img_list[i])
      ens_img.append([classe_img_list[i],classe,str])
      if i == len(classe_img_list):# sort de la boucle if atteint limit des image existe dans cette classe
        break

  #print("----------res---------")
  #for i in  ens_img: 
  #  print(i)

  print(len(ens_img))
  #for l in lists:
  #  print(l)

  #print(lists.index('background'))

  df_img_choisi=pd.DataFrame(ens_img,columns=[ "image_Name","Diseases","image_abs_path"])
  #df_img_choisi.rename(columns={"0" : "image Name", "1" : "Diseases", "2": "image abs path"})
  #df_img_choisi.rename(columns={"image Name", "Diseases", "image abs path"})
  df_img_choisi

  # create small dataset

  import shutil

  #number_images =100
  #selected_images_df = train_df.sample(number_images)
  selected_images_df = df_img_choisi
  idx=0

  dst_folder = 'small_dataset/val/'

  for index, row in selected_images_df.iterrows():
  #  if(row.Diseases == 'background'): 
  #    continue
    image_path_src = row.image_abs_path # os.path.join(train_path,row.Paths)
    image_path_dst= os.path.join(dst_folder,row.Diseases) # ex :/content/small_dataset/train/Apple___Black_rot


    os.makedirs(image_path_dst, exist_ok=True)
    #print("image_path_dst ")
  # print(image_path_dst)
    
    shutil.copyfile(image_path_src, os.path.join(dst_folder,row.Diseases,row.image_Name ))  
    print("{} ---> {} ".format(image_path_src,os.path.join(dst_folder, row.Diseases,row.image_Name)))

    idx= idx + 1

create_small_dataset_validation()


# create small dataset

import shutil

#number_images =100
#selected_images_df = train_df.sample(number_images)
selected_images_df = df_img_choisi
idx=0

dst_folder = 'small_dataset/train/'

for index, row in selected_images_df.iterrows():
#  if(row.Diseases == 'background'): 
#    continue
  image_path_src = row.image_abs_path # os.path.join(train_path,row.Paths)
  image_path_dst= os.path.join(dst_folder,row.Diseases) # ex :/content/small_dataset/train/Apple___Black_rot


  os.makedirs(image_path_dst, exist_ok=True)
  #print("image_path_dst ")
 # print(image_path_dst)
   
  shutil.copyfile(image_path_src, os.path.join(dst_folder,row.Diseases,row.image_Name ))  
  print("{} ---> {} ".format(image_path_src,os.path.join(dst_folder, row.Diseases,row.image_Name)))

  idx= idx + 1