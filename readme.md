**Problem** :

Auburn Student Directories have the incorrect privileges resulting in
the ability for any user to be able to access other students directories
and files

**Extent of Problem** :

Students have the ability to read and write certain user directories
such as Java Eclipse workspaces. This could present opportunities for an
attacker to write malicious code to student directories or even encrypt
student files for ransom. Additionally, with the access to over 15,000
usernames, it opens a huge attack surface of phishing attacks and brute
force attacks to Auburn student email accounts and canvas accounts.

**How I came across the issue :**

When first logging into my student account through ssh and
**gate.eng.auburn.edu** I noticed that my home directory had the
privileges below.

*drwxr-xr-x+*

This can be particularly concerning as others have read access to my
student account home directory and have the ability to potentially
read/write to certain directories.

To view the extent of this issue on other student home directories, I
built the program below to parse, and crawl through accessible student
directories to assess the attack surface of a potential attacker.

**Proof Of Concept :**

**Note** : None of the files parsed were read/written to in this
program. The only data that was taken in the program was metadata such
as which students had readable/writeable files and how many students
created files in there home directory. **No files were read, copied, or
written to.**

The Python program that I built first would change the directory to the
home directory. Next it would loop through the different directories
where users directories were stored and would count how many students
were in these directories.

Next, the program looped through the student directories and would count
the files that were stored there while also checking the different
privileges of these files. The program would also crawl to any
accessible folders such as the Documents folder which is readable
currently.

Since the **umask** of the users is correct where others cannot view
files, I think that Microsoft Word, Eclipse, and other programs are
leaving documents readable to other users.

Finally, the program would print out each user and the data gathered in
there student account as well as a final report of metadata of the
Auburn Engineering student accounts as a whole. Screenshots can be seen
below.

**Final Report**

![](https://image.ibb.co/n9WwUo/Screenshot_2018_06_27_12_31_23.png)

**Small Data Example**

![](https://image.ibb.co/gz8oaT/Screenshot_2018_06_21_23_30_34.jpg)

**Total Vulnerable Data as of 06/27/2018 :**

**Accessible Student Directories** : 15097

**Accessible Files** : 6670

**Writeable Files** : 399 \| **These are only writeable files, users
would also be able to create new files in the directories of these files
**

**Solution** :

The solution to fix this issue is as easy as changing the privileges of
the student directories where only the owner of the directory can
read/write. The Linux command below will do just this!

***chmod 700 \<folder name\>***

Since there are over 15,000 accessible accounts in the
**gate.eng.auburn.edu** you would have to loop through all of the
student home directories and run that command against them all which
would be relatively easy. As you probably know, only an account with
root privileges can run this command against the student directories.

Please keep in mind that there are over 15,000 accessible student home
directories and their usernames are accessible, so please fix this
quickly.

With this data, I was able to build some simple graphs displaying the activity of 
different student accounts. I judged a student account as active, if there were
files that they are/were working on in their directory. 

![](https://image.ibb.co/mzkkg8/foo.png)

Next, I plotted the different student directories in the Auburn root directory. Different 
users are stored in different student directories. For example, I found alot of engineering
professors had their account in the 'new-ece' directory.

![](https://image.ibb.co/mZsgM8/Directory_Graph.png)


