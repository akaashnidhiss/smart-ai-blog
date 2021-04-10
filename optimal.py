
total = int(input("Put no of frames: "))

files = []
pf = 'No'
pageFaults = 0

ref_string = list(map(int, input("Enter reference string").strip().split()))

for i in range (total)

print(I, end= ' ')

print("Page Faults\n  ↓\n")

occurrence = [None for i in range(total)]


for i in range (len(ref_string));

      if ref_string[i] not in files;

        if len(files)< total

       files.append(ref_string[i])

     else:

       for x in range(len(files));

         if files[x] not in ref_string[i+1]:

         files[x] = ref_string[i]

         break

    else:

       occurrence[x] = ref_string[i+1:].index(f[x])

   else:
   

  if[occurance.index(max(occurence))] = ref_string[i]

  pageFaults += 1

  pf= 'Yes'

  else:

  pf = 'No'

  print("%d\t\t" %s[i], end= '')

  for x in files:

      print (x, end = ' ')

      for x in range (total – len(f)):

        print(' ', end = ' ')

        for x in range (total – len(f)):

          print (' ', end = ' ')

          print (pf)

print('\n Total number of requests: %d\n Total number of page pageFaultss: %d, pageFaults Rate: %0.2files%%"%(len(ref_string),pageFaults,(pageFaults/len(ref_string))*100)'))