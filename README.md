# Honeypot-Implementation


In this project we tried to implement Honey-Pot like server which will act
as a proxy server for any main server. Honey-Pot is used to track the
behavior of attacks which are done on any main servers. By studying the
type of attacks, the system designers design the system update in such a
way that it may cover all the loopholes in the system. As the title states
that it’ll be a honeypot like structure and not the exact honeypot. Our
system will not only record the IPs and location but it will also take the
screenshots of the user’s system so that the images can be studied later
and the exact activities can be traced out. The need for this system is
because along with tracking IP of the user, taking screenshots might give
us a clear vision of any kind of unusual activity

## Working

**hash.py**

![](/images/1.jpg)
![](/images/2.jpg)


**Input Given in Python Script**
![](/images/3.jpg)


**Data Stored in Json file**
![](/images/13.jpg)


This data Stored in Json file contains username and password of a specified user and then the user might use this credentials for logging into a Web Server.


**Login Page**
Now we enter the Credentials taken from the json data and thus we enter in the Login page
![](/images/4.png)



**Case: i) If username and Password is correct**

![](/images/5.png)


**Case: ii) If Password is either Wrong or Username is Wrong**

![](/images/6.png)


Then We Are given 3 attempts for the purpose of Login.


If user entered the wrong credentials for 3 times out honeypot system will began where,</br>
We Store IP of the user and all other details

![](/images/7.png)


**The Keylogger:** 

![](/images/8.jpg)
![](/images/9.jpg)

Screenshots and logs taken by the keylogger

![](/images/10.jpg)


**Image Capture:** 

![](/images/11.jpg)




</br></br>
 Licensed under the [MIT License](LICENSE).
