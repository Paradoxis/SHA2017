# SHA2017
All finished projects written during the SHA2017 camp


## Projects list
* Badge Ransomware
* Pong Multiplayer


## Badge Ransomware
We came up with the idea of hijacking the badge and holding it hostage, we chose to allow reboots to reset the ransomware was done intentionally.
To trick people into installing the malware, we used the oldest trick in the book and called it "ASCII porn".

We could have hijacked `boot.py` and forced the ransomware to run on each reboot,
but since that (could) brick your badge and possibly force you to re-flash it, we 
decided to be nice and not do it.

The ransomware consists of a client and a server, the client intially connects to the server
to get a random secret and id (since the badge can't generate random data) and then locks the badge
until the right secret is entered.


## Pong Multiplayer
Yup, mutliplayer pong on an event badge! The game allows you to play pong with another person through your badge.
Use *UP / DOWN* for player one, and use *A / B* for player two. The game has bounce physics, ball randomisation and
some other fun features. It's listed in the store under **games**.
