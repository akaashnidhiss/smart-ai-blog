
# In[40]:


# >> Importing modules
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import collections
import numpy as np
import collections
import sys
import json
import os
nltk.download('stopwords')

# >> Initializing classes
s_words = list(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')
# dataset = ['You know the drill: there is a population and you would like to estimate a characteristic, for example, the mean.', 'Recall that we need to maintain different weights for title and body. To calculate TF-IDF of body or title we need to consider both the title and body. To make our job little easier, let’s use dictionary as with (document, token) pair as key and any TF-IDF score as the value.', 'IDF is the inverse of the document frequency which measures the informativeness of term t. When we calculate IDF, it will be very low for the most occurring words such as stop words (because stop words such as “is” is present in almost all of the documents, and N/df will give a very low value to that word). This finally gives what we want, a relative weightage.', 'Now there are few other problems with the IDF, in case of a large corpus, say 10,000, the IDF value explodes. So to dampen the effect we take log of IDF.During the query time, when a word which is not in vocab occurs, the df will be 0. As we cannot divide by 0, we smoothen the value by adding 1 to the denominator.', 'This war crime, which was later called "the most shocking episode of the Vietnam War",[3] took place in two hamlets of Sơn Mỹ village in Quảng Ngãi Province.[4] These hamlets were marked on the U.S. Army topographic maps as Mỹ Lai and Mỹ Khê. The incident prompted global outrage when it became public knowledge in November 1969. The incident increased, to some extent,[11] domestic opposition to the U.S. involvement in the Vietnam War when the scope of killing and cover-up attempts were exposed. Initially, three U.S. servicemen who had tried to halt the massacre and rescue the hiding civilians were shunned, and even denounced as traitors by several U.S. Congressmen, including Mendel Rivers, Chairman of the House Armed Services Committee. Only after 30 years were they recognized and decorated, one posthumously, by the U.S. Army for shielding non-combatants from harm in a war zone.[12] Along with the No Gun Ri massacre in South Korea 18 years earlier, Mỹ Lai was one of the largest publicized massacres of civilians by U.S. forces in the 20th century.[13]', 'Charlie Company, 1st Battalion, 20th Infantry Regiment, 11th Brigade, 23rd Infantry Division, arrived in South Vietnam in December 1967. Though their first three months in Vietnam passed without any direct contact with People\'s Army of Vietnam or Viet Cong (VC) forces, by mid-March the company had suffered 28 casualties involving mines or booby-traps.[14] Two days before the My Lai massacre, the company had lost a popular sergeant to a land mine.[15]During the Tet Offensive in January 1968, attacks were carried out in Quảng Ngãi by the VC 48th Local Force Battalion. U.S. military intelligence assumed that the 48th Battalion, having retreated and dispersed, was taking refuge in the village of Sơn Mỹ, in Quảng Ngãi Province. A number of specific hamlets within that village—designated Mỹ Lai (1) through Mỹ Lai (6) — were suspected of harboring the 48th.[16] Sơn Mỹ was located southwest of the Batangan Peninsula, a VC stronghold throughout the war.', 'On the morning of 16 March at 7:30 a.m., around 100 soldiers from Charlie Company led by Medina, following a short artillery and helicopter gunship barrage, landed in helicopters at Sơn Mỹ, a patchwork of individual homesteads, grouped settlements, rice paddies, irrigation ditches, dikes, and dirt roads, connecting an assortment of hamlets and sub-hamlets. The largest among them were the hamlets Mỹ Lai, Cổ Lũy, Mỹ Khê, and Tu Cung.[30]:1–2Although the GIs were not fired upon after landing, they still suspected there were VC guerrillas hiding underground or in the huts. Confirming their suspicions, the gunships engaged several armed enemies in a vicinity of Mỹ Lai; later, one weapon was retrieved from the site.[31]', 'A large group of approximately 70–80 villagers was rounded up by 1st Platoon in Xom Lang and led to an irrigation ditch east of the settlement. They were then pushed into the ditch and shot dead by soldiers after repeated orders issued by Calley, who was also shooting. PFC Paul Meadlo testified that he expended several M16 rifle magazines. He recollected that women were allegedly saying "No VC" and were trying to shield their children.[35] He remembered that he was shooting old men and women, ranging in ages from grandmothers to teenagers, many with babies or small children in their arms, since he was convinced at that time that they were all booby-trapped with grenades and were poised to attack.[37] On another occasion during the security sweep of My Lai, Meadlo again fired into civilians side by side with Lieutenant Calley.[38]']

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

file_name = str(str(ROOT_DIR) + '/array.txt')

with open(file_name, 'r',encoding = 'utf-8') as file:
    data = file.read()
dataset = data.split(',/n"')

# dataset = sys.argv[1:]


# inputArgs = sys.argv

# for i in inputArgs[1:]:
#     dataset += i




# >> Preprocessing Function
def preprocessing(text):
    # >>> Lowering the text
    text = text.lower()
    
    # >>> Stemming
    arr = tokenizer.tokenize(text)
        
    # >>> Removing Stopwords
    arr = [word for word in arr if not word in s_words]

    return arr
# >> Document Frequency
def df(dataset):
    DF = {}
    for i in range(len(dataset)):
        for word in dataset[i]:
            try:
                DF[word].add(i)
            except:
                DF[word] = {i}
    return DF
   
# >> TF IDF Function
def tf_idf(dataset):
    N = len(dataset)
    tf_idf_score = {}
    for i in range(N):
        counter = collections.Counter(dataset[i])
        for token in np.unique(dataset[i]):
            tf = counter[token]/len(dataset[i])
            df = len(DF[token])
            idf = np.log(N/(df+1))
            tf_idf_score[i, token] = "{0:.5f}".format(tf*idf)
    return tf_idf_score


# In[42]:


fin_dataset = []

for article in dataset:
    fin_dataset.append(preprocessing(article))
    
DF = df(fin_dataset)
corpus = list(DF.keys())
solved = tf_idf(fin_dataset)
# final = sorted(solved.items(), key=lambda x: x[1], reverse=True)
finalfinal = {}

for key in solved.keys():
    if key[0] == 0:
        finalfinal[key[1]] = solved[key]



sorted_scores = {}
sorted_score_temp = sorted(finalfinal, key=finalfinal.get, reverse=True)  # [1, 3, 2]
i = 0
for w in sorted_score_temp:
    if i in range(5):
        sorted_scores[w] = finalfinal[w]
        i += 1

answer = {}
answer['tags'] = list(sorted_scores.keys())
    

print(json.dumps(answer))







# print(sorted(finalfinal.items(), key=lambda x: x[1], reverse=True))

# std.out('yo')


# print (dataset)

# In[25]:


# print(fin_dataset)

