#!/usr/bin/env python3


import re

maindict = dict()                                                                   # initialize main data structure

infile = open('people.db', "r")                                                     # open input file
flag = False
flag2 = False
for line in infile: 
	REresult1 = re.search(r'CPR:\s+(\d+(\d{2})\-\d+)\s*',line)                  # regex to isolate CPR
	if REresult1 is not None:
		if flag == True:

# Store all the data collected from the Regex above and bellow in a dict (maindict: keys: CPR of each entry, values: rest of data of the entry in key-value pairs)
			
			maindict[CPR] = {'Age': age,'Firstname':firstname,      
			'Lastname':lastname, 'Height':height, 'Weight': weight, 
			'Eyecolor':eyecolor, 'Bloodtype':bloodtype, 'Children':children, 'BMI':(int(weight)/((int(height)*int(height)))*10000)}

		
		CPR = REresult1.group(1)                                            # isolate 5th and 6th digit of CPR
		age = 100 - int(REresult1.group(2))                                 # calculate the person's age
		flag = True

	REresult2 = re.search(r'First name:\s+(\S+)\s*',line)                        # regex to isolate first name
	if REresult2 is not None:
		firstname = REresult2.group(1)
		
	REresult3 = re.search(r'Last name:\s+(\S+)\s*',line)                         # regex to isolate last name
	if REresult3 is not None:
		lastname = REresult3.group(1)

	REresult4 = re.search(r'Height:\s+(\S+)\s*',line)                            # regex to isolate height
	if REresult4 is not None:
		height = REresult4.group(1)

	REresult5 = re.search(r'Weight:\s+(\S+)\s*',line)                            # regex to isolate weight
	if REresult5 is not None:
		weight = REresult5.group(1)

	REresult6 = re.search(r'Eye color:\s+(\S+)\s*',line)                         # regex to isolate eyecolor
	if REresult6 is not None:
		eyecolor = REresult6.group(1)

	if flag2 == True:
		REresult8 = re.search(r'Children:(.+)',line)                         # regex to isolate children, if they exist
		if REresult8 is not None:
			children = REresult8.group(1).split()
		else:
			children = None
		flag2 = False
	REresult7 = re.search(r'^\s*Blood type:\s+(\S+)\s*',line)                    # regex to isolate blood type
	if REresult7 is not None:
		bloodtype = REresult7.group(1)
		flag2 = True                                                         # flag turns true to collect children-if they exist

maindict[CPR] = {'Age': age,'Firstname':firstname, 'Lastname':lastname, 
'Height':height, 'Weight': weight, 'Eyecolor':eyecolor, 'Bloodtype':bloodtype,       # repeat the command that creates main dict to include the last entry of the input file
'Children':children, 'BMI':(int(weight)/((int(height)*int(height)))*10000)}




# Function that takes a list and divides its elements into smaller groups:

def dividetogroups(alist):                                                           
	minage = str(alist[0])[0]
	maxage = str(alist[-1])[0]
	counts = []
	string = ""
	agerangedict = dict()
	agegrangeperc = dict()

	if int(str(alist[0])[-1]) < 5 :                                              # round minimun and maximum age
		minage = int(minage)*10
	else:
		minage = int(minage)*10+5

	
	if int(str(alist[-1])[-1]) < 5 :                                             # round minimun and maximum age
		maxage = int(maxage)*10 + 5 
	else:
		maxage = (int(maxage)+1)*10

	for i in range (minage, maxage+1, 5):                                        # define the age groups
		groups.append(i)

	for m in range(len(groups)):                                                 # count how many entries belong to each group
		count1 = 0
		if m != len(groups)-1:
			for k in range(len(alist)):
				if alist[k] < groups[m+1] and alist[k] >= groups[m]:
					count1+=1
			counts.append(count1)

	for i in range (len(counts)):                                               # store results in dict
		string = str(groups[i])+'-'+str(groups[i+1])
		agerangedict[string] = counts[i]                                    # display results as normal numbers
					
		string = str(groups[i])+'-'+str(groups[i+1])
		agegrangeperc[string] = str(counts[i]*100/len(alist))+'%'           # display results as percentages

	return (agegrangeperc)




# Function that takes a list and calculates the mean of its elements:

def averagefunc(alist):                                                       
	
	sumlist = 0                                                            # initialize local variable
	
	for i in range(len(alist)):                                            # iterate over the list
		sumlist+= int(alist[i])                                        # add every element of the list
	average = sumlist/len(alist)                                           # divide summary by the number of elements of list

	return average

#Question1 & 6
agelist = list()                                                               # initialize dicts
mothers = dict()
fathers = dict()

nc_men = 0                                                                     # initialize counters
nc_women = 0

 
CPRlist = list(maindict.keys())                                                # store all CPRs in a list (CPRlist)              

summed_w_height =0                                                             # initialize variables that will be used for questions 12, 13
summed_m_height=0


for i in range(len(CPRlist)):
	
	lastdigit = CPRlist[i][-1]                                                 # isolate last CPR digit

	if int(lastdigit)%2 == 0:                                                  # count males and females
		females +=1
		summed_w_height += int(maindict[CPRlist[i]]['Height'])             # calculate the summary of womens' heights for q12
		
		if maindict[CPRlist[i]]['Children'] is not None:                   # check for each woman, if she is a mother
			mothers[CPRlist[i]]= maindict[CPRlist[i]]['Children']      # store mothers and their children in dict (mothers: keys:mothers, values: children)
		else:
			nc_women += 1                                              # count women without children

	else:
		males+=1
		summed_m_height += int(maindict[CPRlist[i]]['Height'])             # calculate the summary of mens' heights for q12
		            
		if maindict[CPRlist[i]]['Children'] is not None:                   # check for each man, if he is a father
			fathers[CPRlist[i]]= maindict[CPRlist[i]]['Children']      # store fathers and their children in dict (fathers: keys:fathers, values: children)
		else:
			nc_men += 1                                                # count men without children


	agelist.append(maindict[CPRlist[i]]['Age'])

#question 1
agelist.sort()
print('Question 1---------')
print(dividetogroups(agelist))
print('Percentage of men:', (males/len(CPRlist))*100, '%')
print('Percentage of women:', (females/len(CPRlist))*100, '%')
print('---------------')
print('   ')

#question6
print('Question 6---------')
print('Percentage of men without children :', (nc_men/males) *100, "%")
print('Percentage of women without children :', (nc_women/females) *100, "%")

print('Percentage of all the mothers:',(len(list(mothers.keys()))/females)*100,' %')
print('Percentage of all the fathers:',(len(list(fathers.keys()))/males)*100,' %')
print('---------------')
print('   ')

#-----------


#making childrens dictionary---------                              
kids_age = list()
kidlist = list()
firstfatherlist = list()
childict = dict()

motherlist = list(mothers.keys())         #creating a list of all mothers
fatherlist = list(fathers.keys())         #creating a list of all fathers


for i in range(len(fatherlist)):          #iterating through CPR numbers of all fathers                                   
	kidlist = []
	kids_age = []
	kidlist = fathers[fatherlist[i]]  #taking the children each father has and adding it to a temporary list
	 
	for j in range (len(kidlist)):            #iterating through each fathers children
		for k,v in mothers.items():       #checking if the child is present in the values(children) of the mothers dict
			if kidlist[j] in v:
				childict[kidlist[j]] = [fatherlist[i], k]      #creating a new dict with child as key and the father and mother as values
#-------------


#question7------
ChildCPR_sortlist = sorted(childict.keys(), key=childict.get)                # storing all children from childrens dict into a list based on sorted values 
kids_age = list()
parent_agediff = list()
uniqueparentspairs= list()

for i in range(len(ChildCPR_sortlist)):                                      # iterating though the list of children              
	if i != len(ChildCPR_sortlist)-1:
		if childict[ChildCPR_sortlist[i]] != childict[ChildCPR_sortlist[i+1]]:                      #checking if children are not siblings
			father = childict[ChildCPR_sortlist[i]][0]
			mother = childict[ChildCPR_sortlist[i]][1]
			parent_agediff.append(abs(maindict[father]['Age'] - maindict[mother]['Age']))       #creating a list with age difference between parents
			uniqueparentspairs.append(childict[ChildCPR_sortlist[i]])                           # make a list of unique pairs of parents for q12
		

	else:           										   #creating a seperate condition to look at the last childs parents
		mother = childict[ChildCPR_sortlist[i]][1]
		father = childict[ChildCPR_sortlist[i]][0]
		parent_agediff.append(abs(maindict[father]['Age'] - maindict[mother]['Age']))
		uniqueparentspairs.append(childict[ChildCPR_sortlist[i]])                                 # make a list of unique pairs of parents for question 12
		
print('Question 7----------')
print ('Average age difference between parents: ',averagefunc(parent_agediff))	
print('---------------')
print('   ')
#--------------


#Question 4 & 5 & 10

motherlist = list(mothers.keys())
firstmotherlist = list()
firstborngirls = 0
firstbornboys = 0

for i in range(len(motherlist)):                  #iterating through all mothers
	
	kidlist =[]                               # initializing kidlist for each mother
	kidsagedict = dict()                      # initializing kids_age for each mother
	eldest_kids = []                          # initializing list for each mothers' eldest kids (q10)
	kidlist = mothers[motherlist[i]]          #storing each mothers children in temporary list
	keysSortedbyAge = []

	for j in range(len(kidlist)):                                                #iterating through the children every mother has
		kidsagedict[kidlist[j]] = (maindict[kidlist[j]]['Age'])              #store the age of each child in dict
		keysSortedbyAge = sorted(kidsagedict.keys(), key= kidsagedict.get)   #sort the keys of dict, along with values so that last key will be the firstborn
		
		firstmotherlist.append(maindict[motherlist[i]]['Age'] - int(kidsagedict[keysSortedbyAge[-1]]))   #append the age of the first time mother to a list

	for n in range(len(keysSortedbyAge)):
		if kidsagedict[keysSortedbyAge[n]] == kidsagedict[keysSortedbyAge[-1]]:      # check if there are twins as firstborn
			eldest_kids.append(keysSortedbyAge[n])                               # append firstborn kid / kids to list
	
	for k in range(len(eldest_kids)):
		
		if int(eldest_kids[k][-1])%2 == 0:                    # identify if the first born is male or female
			firstborngirls+=1                             # count males
		else: 
			firstbornboys+=1                              # count females

		
print('The oldest age at which a person became a mother: ',firstmotherlist[-1])
print('The youngest age at which a person became a mother: ',firstmotherlist[0])
print('---------------')
print('   ')
#--------------



#Question2 & 3
										
for i in range(len(fatherlist)):						 # iterating through the list of all fathers
	
	kidlist =[]                                                              # initializing kidlist for each father                                           
	kids_age =[]                                                             # initialize kids_age for each father
	kidlist = fathers[fatherlist[i]]				         # adding all the children to one list
	
	for j in range(len(kidlist)):					         #iterating through all children of this father
		Ag_e = maindict[kidlist[j]]['Age']
		kids_age.append(Ag_e)					         #adding the age of every kid to a new list
	kids_age.sort()                                                          # sort list so that the firstborn will be last element
	firstfatherlist.append(maindict[fatherlist[i]]['Age'] - kids_age[-1])	 #finding when the father became a father for the first time and adding it to a list
print('Question 2 and 3')
print(dividetogroups(firstfatherlist))
print ('Average age at which a person became a father for the first time: ',averagefunc(firstfatherlist))
firstfatherlist.sort()
print('The oldest age at which a person became a father: ',firstfatherlist[-1])
print('The youngest age at which a person became a father: ',firstfatherlist[0])
print('---------------')
print('   ')

#-------------------

#question 8------------

grandkids = dict()                                           # initialize dictionary for all grandkids
childlist = list(childict.keys())                            # store all kids from childict into a list

for g in range(len(childlist)):                              # iterate over all the kids
	mother = childict[childlist[g]][1]                   # find kid's mother
	father = childict[childlist[g]][0]                   # find kid's father
	
	grandparents_m = []                                  # initialize list for grandparents from mother's side
	grandparents_f = []                                  # initialize list for grandparents from father's side
	
	for i in range(len(childlist)):                      # iterate again over all kids

		if mother == childlist[i]:
			grandparents_m = childict[childlist[i]]   # store the mother's parents
		elif father == childlist[i]:
			grandparents_f = childict[childlist[i]]   # store the father's parents

	if grandparents_f!= [] or grandparents_m!= []:            # exclude grandkids with no grandparents alive
		
		grandkids[childlist[g]] = grandparents_f+grandparents_m   # create dict (grandkids) with keys: grandkids and values: grandparents


print('Question 8')
print(grandkids)
print('Number of people with atleast one grandparent being alive : ',len(grandkids.keys()))                                             
print('percentage of people with atleast one grandparent: ',(len(grandkids.keys())/len(maindict))*100,'%')
print('---------------')
print('   ')


#--------------------
# question 9

cousinsdict = dict()                   # initialize dict for cousins
siblist= list()                        # initialize list for siblings' groups

for i in range(len(childlist)):        # iterate over all kids
	
	siblings_M = []                # initialize lists for cousins from mother's and father's side
	siblings_F = []
	
	cousins_m = 0                  # initialize cousins' counters
	cousins_f = 0
	totcousins = 0
	
	mother = childict[childlist[i]][1]   #store kid's mother
	father = childict[childlist[i]][0]   #store kid's father
	
	for CPR in maindict:          # iterate over every CPR entry                       
		
		if maindict[CPR]['Children'] is not None and cousins_m == 0 :     # Find people with kids
			if mother in maindict[CPR]['Children']:                   # Find mother in an entry's children            
				siblings_M = maindict[CPR]['Children']            # store mother with siblings in siblings_M
				
				for k in range(len(siblings_M)):                  # iterate over siblings
					
					if maindict[siblings_M[k]]['Children'] is not None and siblings_M[k]!= mother:    # find mothers' siblings that have kids
						cousins_m += len(maindict[siblings_M[k]]['Children'])                     # append their kids in cousins_m

			if father in maindict[CPR]['Children']:                   # Find father in an entry's children     
				siblings_F = maindict[CPR]['Children']            # store father with siblings in siblings_M
				
				for v in range(len(siblings_F)):                 # iterate over siblings
					
					if maindict[siblings_F[v]]['Children'] is not None and siblings_F[v]!= father:    # find fathers' siblings that have kids
						cousins_f += len(maindict[siblings_F[v]]['Children'])                     # append their kids in cousins_f

	cousinsdict[childlist[i]] = (cousins_f+cousins_m)          # create cousindict with keys: every child, and values: the number of cousins 

cousinslistclear = []                                              # initialize list for number of cousins
cousinslist = list(cousinsdict.values())                           # store values of cousinsdict in cousins list

for i in range (len(cousinslist)):                                 # get rid of people with 0 cousins
	if cousinslist[i] != 0:
		cousinslistclear.append(cousinslist[i])            # create a list with people with at leat one cousin



print('Question 9')
print('Average number of cousins: ',averagefunc(cousinslistclear), '\n')




#---------------------------

print('Question 10')
print ('The likelihood of the fistborn being a male is', (firstbornboys/(firstborngirls+firstbornboys))*100, '%') 
print ('The likelihood of the fistborn being a female is', (firstborngirls/(firstborngirls+firstbornboys))*100, '%', '\n') 

#---------------------------


# question 11:
multiplepartners = 0                                                # initialize
parents = list(childict.values())                                   # store all pairs of parents in a list
parents.sort()
multiplepartners_m = 0
multiplepartners_f = 0                                              # sort list (pairs with the same father will be next to each other)
for p in range (len(parents)):
	if p != len(parents)-1:
		if parents[p][0] == parents[p+1][0] and parents[p][1]!= parents[p+1][1]:
			
	

			multiplepartners_m += 1                      # count men with multiple partners
	
	(parents[p]).reverse()		                             # reverse the order of parents (first element: mother, second element: father)

parents.sort()
for p in range(len(parents)):
	if p != len(parents)-1:
		if parents[p][0] == parents[p+1][0] and parents[p][1]!= parents[p+1][1]:

			multiplepartners_f += 1                       # count women with multiple partners

multiplepartners = multiplepartners_f + multiplepartners_m            # add men and women having multiple partners

print('Question 11')
print ("The percentage of people who have kids with more than one partner is ", (multiplepartners / (2*len(parents)))*100, '%', '\n')

#---------------------------



# question 12:
avr_w_height = summed_w_height / females                               # calculate average womens' height
avr_m_height = summed_m_height / males                                 # calculate average mens' height

ttcouples = 0                                                          # initialize couples' counters for height categories
sscouples = 0
nncouples = 0
sncouples = 0
tscouples = 0 
tncouples = 0 


tallparents = []                                                      # initialize list for tall parents



# If statements to count how many couples belong to each of the categories initialized above: 
for y in range (len(uniqueparentspairs)):
	
	if int(maindict[uniqueparentspairs[y][0]]['Height']) > (avr_w_height + avr_w_height*0.025) and int(maindict[uniqueparentspairs[y][1]]['Height']) > (avr_m_height + avr_m_height*0.025):
		ttcouples+=1
		tallparents.append(uniqueparentspairs[y])                              #store CPRs of tall parent pairs for q13
	
	elif int(maindict[uniqueparentspairs[y][0]]['Height']) < (avr_w_height - avr_w_height*0.025) and int(maindict[uniqueparentspairs[y][1]]['Height']) < (avr_m_height - avr_m_height*0.025):
		sscouples+=1
	elif int(maindict[uniqueparentspairs[y][0]]['Height']) <= (avr_w_height + avr_w_height*0.025) and int(maindict[uniqueparentspairs[y][0]]['Height']) >= (avr_w_height - avr_w_height*0.025) and int(maindict[uniqueparentspairs[y][1]]['Height']) <= (avr_m_height + avr_m_height*0.025) and int(maindict[uniqueparentspairs[y][1]]['Height']) >= (avr_m_height - avr_m_height*0.025):
		nncouples+=1
	elif (int(maindict[uniqueparentspairs[y][0]]['Height']) > (avr_w_height + avr_w_height*0.025) and int(maindict[uniqueparentspairs[y][1]]['Height']) < (avr_m_height - avr_m_height*0.025)) or (int(maindict[uniqueparentspairs[y][0]]['Height']) < (avr_w_height - avr_w_height*0.025) and int(maindict[uniqueparentspairs[y][1]]['Height']) > (avr_m_height + avr_m_height*0.025)):
		tscouples+=1
	elif (int(maindict[uniqueparentspairs[y][0]]['Height']) <= (avr_w_height + avr_w_height*0.025) and int(maindict[uniqueparentspairs[y][0]]['Height']) >= (avr_w_height - avr_w_height*0.025) and int(maindict[uniqueparentspairs[y][1]]['Height']) > (avr_m_height + avr_m_height*0.025)) or (int(maindict[uniqueparentspairs[y][1]]['Height']) <= (avr_m_height + avr_m_height*0.025) and int(maindict[uniqueparentspairs[y][1]]['Height']) >= (avr_m_height - avr_m_height*0.025) and int(maindict[uniqueparentspairs[y][0]]['Height']) > (avr_w_height + avr_w_height*0.025)):
		tncouples+=1
	elif (int(maindict[uniqueparentspairs[y][0]]['Height']) <= (avr_w_height + avr_w_height*0.025) and int(maindict[uniqueparentspairs[y][0]]['Height']) >= (avr_w_height - avr_w_height*0.025) and int(maindict[uniqueparentspairs[y][1]]['Height']) < (avr_m_height - avr_m_height*0.025)) or (int(maindict[uniqueparentspairs[y][1]]['Height']) <= (avr_m_height + avr_m_height*0.025) and int(maindict[uniqueparentspairs[y][1]]['Height']) >= (avr_m_height - avr_m_height*0.025) and int(maindict[uniqueparentspairs[y][0]]['Height']) < (avr_w_height - avr_w_height*0.025)):
		sncouples+=1


print('Question 12')
print('The percentage of couples consisting of two tall people is', ttcouples/len(uniqueparentspairs), '%, out of all couples. Out of all couples with at least one tall partner, couples with 2 tall partners are', (ttcouples/(ttcouples+tscouples+tncouples))*100, '%.', '\n')

#---------------------------


# question 13:

     
tallkids = 0                 #initialize counter for tall kids 
kidsoftt = 0                 #initialize counter for kids of tall parents

dict_items=childict.items()
for j in range (len(tallparents)):
	kids= [k for k, v in childict.items() if v == tallparents[j]]
	kidsoftt+= len(kids)
	for g in range (len(kids)):
		if int(kids[g][-1]) % 2 == 0 and int(maindict[kids[g]]['Height']) > (avr_w_height + avr_w_height*0.025):
			tallkids+=1
		elif int(kids[g][-1]) % 2 != 0 and int(maindict[kids[g]]['Height']) > (avr_m_height + avr_m_height*0.025):
			tallkids+=1
		

print('Question 13')
print ('The percentage of kids of tall parents that are tall is', (tallkids/kidsoftt)*100, '%.', '\n')

#---------------------------


# question 14:

f_f_couples =0                         # initialize couples' counters for weight categories
sl_sl_couples = 0
f_sl_couples = 0
n_n_couples = 0
f_n_couples = 0
sl_f_couples = 0


# If statements to count how many couples belong to each of the categories initialized above
for n in range (len(uniqueparentspairs)):
	if int(maindict[uniqueparentspairs[n][0]]['BMI']) > 24.9 and int(maindict[uniqueparentspairs[n][1]]['BMI']) > 24.9 :
		f_f_couples+=1
	elif int(maindict[uniqueparentspairs[n][0]]['BMI']) < 18.5 and int(maindict[uniqueparentspairs[n][1]]['BMI']) < 18.5 :
		sl_sl_couples+=1
	elif (int(maindict[uniqueparentspairs[n][0]]['BMI']) > 24.9 and int(maindict[uniqueparentspairs[n][1]]['BMI']) < 18.5) or (int(maindict[uniqueparentspairs[n][0]]['BMI']) < 18.5 and int(maindict[uniqueparentspairs[n][1]]['BMI']) > 24.9) :
		f_sl_couples+=1
	elif (int(maindict[uniqueparentspairs[n][0]]['BMI']) <= 24.9 and int(maindict[uniqueparentspairs[n][0]]['BMI'])>= 18.5) and (int(maindict[uniqueparentspairs[n][1]]['BMI']) <= 24.9 and int(maindict[uniqueparentspairs[n][1]]['BMI'])>= 18.5) :
		n_n_couples+=1
	elif ((int(maindict[uniqueparentspairs[n][0]]['BMI']) <= 24.9 and int(maindict[uniqueparentspairs[n][0]]['BMI'])>= 18.5) and int(maindict[uniqueparentspairs[n][1]]['BMI']) > 24.9) or ((int(maindict[uniqueparentspairs[n][1]]['BMI']) <= 24.9 and int(maindict[uniqueparentspairs[n][1]]['BMI'])>= 18.5) and int(maindict[uniqueparentspairs[n][0]]['BMI']) > 24.9):
		f_n_couples+=1
	elif ((int(maindict[uniqueparentspairs[n][0]]['BMI']) <= 24.9 and int(maindict[uniqueparentspairs[n][0]]['BMI'])>= 18.5) and int(maindict[uniqueparentspairs[n][1]]['BMI']) < 18.5) or ((int(maindict[uniqueparentspairs[n][1]]['BMI']) <= 24.9 and int(maindict[uniqueparentspairs[n][1]]['BMI'])>= 18.5) and int(maindict[uniqueparentspairs[n][0]]['BMI']) < 18.5):
		sl_f_couples+=1

print('Question 14')
print('The percentage of couples consisting of two fat people is', f_f_couples/len(uniqueparentspairs), '%, out of all couples. Out of all couples with at least one fat partner, couples with 2 fat partners are', (f_f_couples/(f_f_couples+ f_n_couples+ f_sl_couples))*100, '%.', '\n')
#------------------------


#question15

adopted = list()                            #initialize list for kids with non biological parents

for i in range (len(childlist)):
	
	fathersblood= maindict[childict[childlist[i]][1]]['Bloodtype']        # store father's blood in variable
	
	mothersblood = maindict[childict[childlist[i]][0]]['Bloodtype']       # store mother's blood in variable

	childsblood = maindict[childlist[i]]['Bloodtype']                     # store child's blood in variable
	
	
	
	if mothersblood[-1] == '+' and fathersblood[-1] == '+':              # Rhesus check:
		if childsblood[-1] ==  '-':
			adopted.append(childlist[i])
	elif mothersblood[-1] == '-' and fathersblood[-1] == '-':
		if childsblood[-1] ==  '+':
			adopted.append(childlist[i])
	
	
	
	else:                                                              # if the blood types comply with the Rhesus inheritance, then ABO type is checked


	#If statements to detect children with blood type that can not have been inherited from their parents:
		
	if mothersblood[:-1] == 'A' and fathersblood[:-1] == 'A':
			if childsblood[:-1]!= 'A' and childsblood[:-1]!= 'O':
				adopted.append(childlist[i])


		elif mothersblood[:-1] == 'O' and fathersblood[:-1] == 'O':
			if childsblood[:-1]!= 'O' :
				adopted.append(childlist[i])

		elif mothersblood[:-1] == 'B' and fathersblood[:-1] == 'B':
			if childsblood[:-1]!= 'O' and childsblood[:-1]!= 'B' :
				adopted.append(childlist[i])

		elif mothersblood[:-1] == 'AB' and fathersblood[:-1] == 'AB':
			if childsblood[:-1] == 'O' :
				adopted.append(childlist[i])

		elif (mothersblood[:-1] == 'A' and fathersblood[:-1] == 'AB') or (mothersblood[:-1] == 'AB' and fathersblood[:-1] == 'A') :
			if childsblood[:-1] == 'O' :
				adopted.append(childlist[i])
	
		elif (mothersblood[:-1] == 'B' and fathersblood[:-1] == 'AB') or (mothersblood[:-1] == 'AB' and fathersblood[:-1] == 'B') :
			if childsblood[:-1] == 'O' :
				adopted.append(childlist[i])
				
		elif (mothersblood[:-1] == 'O' and fathersblood[:-1] == 'AB') or (mothersblood[:-1] == 'AB' and fathersblood[:-1] == 'O') :
			if childsblood[:-1]!= 'A' and childsblood[:-1]!= 'B':
				adopted.append(childlist[i])

		elif (mothersblood[:-1] == 'O' and fathersblood[:-1] == 'A') or (mothersblood[:-1] == 'A' and fathersblood[:-1] == 'O') :
			if childsblood[:-1]!= 'A' and childsblood[:-1]!= 'O':
				adopted.append(childlist[i])

		elif (mothersblood[:-1] == 'O' and fathersblood[:-1] == 'B') or (mothersblood[:-1] == 'B' and fathersblood[:-1] == 'O') :
			if childsblood[:-1]!= 'B' and childsblood[:-1]!= 'O':
				adopted.append(childlist[i])


print('Question 15')
print('Children with non biological parents in the database is: ', len(adopted))
print(adopted, '\n')
#--------------------------


#question16

f_cbloodict = dict()                                         # initialize dictionary with fathers hou can donate to sons ande their blood types
 
for i in range(len(fatherlist)):                             # iterate through all fathers
	fathersblood = maindict[fatherlist[i]]['Bloodtype']  
	fathers_children = fathers[fatherlist[i]]            # append father's children into list
	f_cbloodlist = []                                    # list with the sons that receive blood and their blood type
	
	for j in range(len(fathers_children)):
	
		if int(fathers_children[j][-1])%2 != 0:                              # exclude daughters

			childsblood = maindict[fathers_children[j]]['Bloodtype']     # identify its son's bloodtype

			#If statements to detect sons that can receive blood from their father and append themselves and their bloodtype into f_cbloodlist :
			if childsblood == fathersblood:
				f_cbloodlist.append(fathers_children[j]+' '+childsblood)

			elif childsblood == 'AB+':
				f_cbloodlist.append(fathers_children[j]+' '+childsblood)

			elif fathersblood == 'O-':
				f_cbloodlist.append(fathers_children[j]+' '+childsblood)
		
			elif fathersblood == 'O+' and (childsblood == 'A+' or childsblood == 'B+'):
				f_cbloodlist.append(fathers_children[j]+' '+childsblood)

			elif fathersblood == 'B-' and (childsblood == 'AB-' or childsblood == 'B+'):
				f_cbloodlist.append(fathers_children[j]+' '+childsblood)
		
			elif fathersblood == 'A-' and (childsblood == 'AB-' or childsblood == 'A+'):
				f_cbloodlist.append(fathers_children[j]+' '+childsblood)

	if f_cbloodlist != []:                                                                  # exclude cases where sons cannot receive blood form father
		f_cbloodict[fatherlist[i]+' '+fathersblood] = f_cbloodlist                      # create f_cbloodict

print('Question 16')
print('Fathers that can donate blood to atleast one of their sons: ',len(f_cbloodict.keys()))

f_cbloodkeylist = list(f_cbloodict.keys())                                                     # store keys from f_cbloodict in list
sonscounter = 0                                                                                # initialize counter for compatible sons

for i in range(len(f_cbloodkeylist)):
	sons = f_cbloodict[f_cbloodkeylist[i]]
	sonscounter += len(sons)                                                              # calculate sum of compatible sons
print('Sons that can receive blood from their father: ', sonscounter, '\n')

#---------------------


#question17
gc_gpbloodict = dict()                                   #dict for grankids who grantparent
grandkids_list = list(grandkids.keys())

for i in range(len(grandkids_list)):
	grandkidblood = maindict[grandkids_list[i]]['Bloodtype']
	grandparents = grandkids[grandkids_list[i]]
	gc_gpbloodlist = []
	for j in range(len(grandparents)):
		
		grandparentblood = maindict[grandparents[j]]['Bloodtype']

		if grandkidblood == grandparentblood:
			gc_gpbloodlist.append(grandparents[j]+' '+grandparentblood)

		elif grandparentblood == 'AB+':
			gc_gpbloodlist.append(grandparents[j]+' '+grandparentblood)

		elif grandkidblood == 'O-':
			gc_gpbloodlist.append(grandparents[j]+' '+grandparentblood)
		
		elif grandkidblood == 'O+' and (grandkidblood == 'A+' or grandkidblood == 'B+'):
			gc_gpbloodlist.append(grandparents[j]+' '+grandparentblood)

		elif grandkidblood == 'B-' and (grandkidblood == 'AB-' or grandkidblood == 'B+'):
			gc_gpbloodlist.append(grandparents[j]+' '+grandparentblood)
		
		elif grandkidblood == 'A-' and (grandkidblood == 'AB-' or grandkidblood == 'A+'):
			gc_gpbloodlist.append(grandparents[j]+' '+grandparentblood)

	if gc_gpbloodlist != []:
		gc_gpbloodict[grandkids_list[i]+' '+grandkidblood] = gc_gpbloodlist
print('Question 17')
print('The number of grandkids that can donate blood to atleast one grandparent',len(gc_gpbloodict.keys()))
gc_gplist = list(gc_gpbloodict.keys())
gp_counter = 0
for i in range(len(gc_gplist)):
	grandparents = gc_gpbloodict[gc_gplist[i]]
	gp_counter += len(grandparents)

print('The number of grandparents that can recieve blood from their grandkids is: ',gp_counter)


