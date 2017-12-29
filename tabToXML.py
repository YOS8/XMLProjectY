
# coding: utf-8

# Ce Programme convertit un fichier tabulaire (2 colonnes) à un fichier XML

# In[10]:

with open("/Users/nino/Desktop/cour_M2/xml/projet/xml/Dico_Français_Klingon2.tab", "r") as f:
    with open("/Users/nino/Desktop/cour_M2/xml/projet/xml/Dico_Français_Klingon3.xml","w") as fic:
        fic.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
        fic.write("<!DOCTYPE Root SYSTEM \"Dico_Français_klingon.dtd\">\n")
        fic.write("<racine>\n")
        i = 0
        for line in f:
            splits = f.readline().rstrip().split("\t")
            if len(splits) < 2:
                continue
            i+=1
            fic.write("<mot id=\"{}\">\n".format(i))
            fic.write("\t<mot_fr>{}</mot_fr>\n".format(splits[0]))
            fic.write("\t<mot_klg>{}</mot_klg>\n".format(splits[1]))
            fic.write("\t<phrase_fr>NULL</phrase_fr>\n")
            fic.write("\t<phrase_klg>NULL</phrase_klg>\n")
            fic.write("</mot>\n")
            fic.write("\n")
        fic.write("</racine>")
            
