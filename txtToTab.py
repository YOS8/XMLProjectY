
# coding: utf-8

# In[5]:

#Ce programme convertit un fichier texte en un fichier tabulaire. 
f = open("/Users/nino/Desktop/cour_M2/xml/projet/xml/Dico_Français_Klingon.txt","r") 
fic = open("/Users/nino/Desktop/cour_M2/xml/projet/xml/Dico_Français_Klingon2.tab","w") 
for  line in f:
    line=line.replace(':', '\t')
    #print(line)
    fic.write(line)
f.close()
fic.close()


# In[ ]:



