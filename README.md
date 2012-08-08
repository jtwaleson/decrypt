# Decrypt
This program takes over the screen, prints flickering random characters and slowly makes the piped content (or input file) visible. Effectively, it does what hackers on tv-shows have.

## Examples

Do this for example:
```tree ~/Downloads | ./decrypt.py```

or
```jp2a my_favourite_cat.jpg --term-width | ./decrypt.py```



## Use case

Recover some friend's hard drive (i.e.: he destroyed his mbr). After the "hard" work has been done, act like you are having a hard time and run some of his personal files through this program and ask if he recognizes the content.

Awesomeness guaranteed.


## Remarks

Warning: keeps the entire input in memory and uses an O(n^2) algorithm. It is not efficient cpu/ram wise. Easy rewrite is possible but this is just for fun.


## Screenshot

<a href='https://s3.amazonaws.com/files.droplr.com/files_production/acc_51755/ZMi?AWSAccessKeyId=AKIAJSVQN3Z4K7MT5U2A&Expires=1344402468&Signature=CQ%2FrNfEdfZcM2vCn43uFwGyoJV4%3D&response-content-disposition=inline%3B+filename%3D%22decryptpy.gif%22'>Large animated gif (3MB)</a> Thanks, someone on HN.

<iframe width="420" height="315" src="http://www.youtube.com/embed/DoDoOtlomsM" frameborder="0" allowfullscreen></iframe>
