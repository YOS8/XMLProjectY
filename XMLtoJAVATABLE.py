
# coding: utf-8

# In[1]:

#Ce programme convertit le fichier xml en data table pour le javascript. 
from lxml import etree

fic = '/Users/nino/Desktop/cour_M2/xml/projet/xml/Dico_Français_Klingon2.xml'

tree = etree.parse(fic)
root = tree.getroot()

print("var dataSet = [")
for child in root:
    print("[")
    for texte in child:
        print('  "{}",'.format(texte.text))
    print("]\n,")
print("]")
    


# In[ ]:




# In[ ]:



