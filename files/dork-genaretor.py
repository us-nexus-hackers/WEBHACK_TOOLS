ó
ÿÿc           @   sÙ   e  Z e r# d  d  Z   Z n  d d l Z d d l Z d d l Z e d d  Z e d d  Z e d d  Z	 e d d  Z
 e d d  Z d	 Z d
   Z d   Z d   Z d   Z d   Z d   Z e   d S(   i    iÿÿÿÿNs	   sqli3.txtt   rs   dork-list.txts	   sqlid.txts   xssd.txts	   lafid.txtsÝ   [1;94m
 _    _  _____   _   _ ________   ___    _  _____        
 | |  | |/ ____| | \ | |  ____\ \ / / |  | |/ ____|       
 | |  | | (___   |  \| | |__   \ V /| |  | | (___         
 | |  | |\___ \  | . ` |  __|   > < | |  | |\___ \        
 | |__| |____) | | |\  | |____ / . \| |__| |____) |       
 _\____/|_____/__|_|_\_|______/_/_\_\\____/|_____/ _      
 \ \        / /  ____|  _ \  |__   __/ __ \ / __ \| |     
  \ \  /\  / /| |__  | |_) |    | | | |  | | |  | | |     
   \ \/  \/ / |  __| |  _ <     | | | |  | | |  | | |     
    \  /\  /  | |____| |_) |    | | | |__| | |__| | |____ 
     \/  \/   |______|____/     |_|  \____/ \____/|______|
                                                          
Created By : [1;96mUSNEXUS [1;31m|[1;0m [V H3NTAI V1]

[1;32m------------------------------------------
[93m AUTHOR  : US NEXUS HACKERS
[93m GITHUB  : github.com/us-nexus-hackers
[93m TG      : t.me/usnexushacker
[93m TYPE    : Admin-Finder
[1;32m-------------------------------------------
c          C   s=   t  j d  t GHHx# t D] }  |  j   }  d |  GHq Wd  S(   Nt   clears   [1;31m[+] [1;32m(   t   ost   systemt   logot   lafidt   strip(   t   word4(    (    s   dork-genaretor.pyt   lafi    s    c          C   s=   t  j d  t GHHx# t D] }  |  j   }  d |  GHq Wd  S(   NR   s   [1;31m[+] [1;32m(   R   R   R   t   xss_dorkR   (   t   word3(    (    s   dork-genaretor.pyt   xss+   s    c          C   s   t  j d  t GHHt d  }  xs |  d k rB d GHt d  }  q" WHxN t D]F } | j   } d d |  | GHd |  | } | d k rK Hd GHqK qK Wd  S(	   NR   s*   [1;31m[+][1;32m ENTER KEYWORDS :[1;36m t    s   [1;31mEx- News,Gellarys   [1;31m[+][1;32m s   inurl:s   inurl:news.php?maincat_id=s    [1;33m   << Thanks For Using >>(   R   R   R   t	   raw_inputt   dorkR   (   t   keyt   wordt   d(    (    s   dork-genaretor.pyt   sqli15   s    c          C   s=   t  j d  t GHHx# t D] }  |  j   }  d |  GHq Wd  S(   NR   s   [1;31m[+] [1;32minurl:(   R   R   t   logoXyt   dork2R   (   t   word2(    (    s   dork-genaretor.pyt   sqli2K   s    c          C   s=   t  j d  t GHHx# t D] }  |  j   }  d |  GHq Wd  S(   NR   s   [1;31m[+] [1;32minurl:(   R   R   R   t   dork3R   (   R
   (    (    s   dork-genaretor.pyt   sqli3U   s    c          C   s·   t  j d  t GHHd GHd GHd GHd GHd GHHt d  }  |  d k rO t   nd |  d	 k re t   nN |  d
 k r{ t   n8 |  d k r t   n" |  d k r§ t   n t	   d GHd  S(   NR   sB   [1;32m[1][1;31m >>[1;36m SQLI [1;33m|[1;31m With Own Keywordss6   [1;32m[2][1;31m >>[1;36m SQLI [1;33m|[1;31m Dorkss:   [1;32m[3][1;31m >>[1;36m SQLI [1;33m|[1;31m New Dorkss@   [1;32m[4][1;31m >>[1;36m XSS [1;33m |[1;31m Dork & Payloadss6   [1;32m[5][1;31m >>[1;36m LFI [1;33m |[1;31m Dorkss&   [1;31m[+][1;32m Enter Your Choice : t   1t   2t   3t   4t   5s   <<< Thanks For Using >>>(
   R   R   R   R   R   R   R   R   R   t   exit(   t   user(    (    s   dork-genaretor.pyt   intro_   s,    




(   t   Falset   foot   barR   t   timet   syst   openR   R   R   R	   R   R   R   R   R   R   R   R    (    (    (    s   dork-genaretor.pyt   <module>   s&   
		
		
	
	