# SHA2017
All finished projects written during the SHA2017 camp


## Projects list
* Badge Ransomware
* Pong Multiplayer
* Junior CTF


## Badge Ransomware
We came up with the idea of hijacking the badge and holding it hostage, we chose to allow reboots to reset the ransomware was done intentionally.
To trick people into installing the malware, we used the oldest trick in the book and called it "ASCII porn".

We could have hijacked `boot.py` and forced the ransomware to run on each reboot,
but since that (could) brick your badge and possibly force you to re-flash it, we 
decided to be nice and not do it.

The ransomware consists of a client and a server, the client intially connects to the server
to get a random secret and id (since the badge can't generate random data) and then locks the badge
until the right secret is entered. 

**Edit: SUNDAY** One of the badge admins liked the project and made it persistent, we also registered a duplicate called *The Legend of Zelda* which was another social engineering attack to get people to install the app as a game. We later found out that that version of the app tried to restore the `ascii_porn` app, which left your badge in a vegitative state. To the people whose badges we bricked, sorry :heart:. So far three people have showed up to ask about the ransomware but no Club Mate has been paid. :cry:

**Edit: TUESDAY** Two people paid their ransom, seven badges were unlocked in total end one grumpy father didn't appreciate the joke.

## Pong Multiplayer
Yup, mutliplayer pong on an event badge! The game allows you to play pong with another person through your badge.
Use *UP / DOWN* for player one, and use *A / B* for player two. The game has bounce physics, ball randomisation and
some other fun features. It's listed in the store under **games**.

## Junior CTF
On the second to last day of SHA, I decided to get my CTF game up and wanted to take part in the Junior CTF, sadly however this 
ctf had already ended, meaning you couldn't win any prizes and such; however you could still do the challenge and get on the highscores.
In the end I managed to get 100% of the flags which got me in the 171st place (out of the ~4k that took part, not sure on that figure though, I'll have to double check). I'd like to thank Rik van Duijn, Vincent van der Eijk for brainstorming on some challenges and an special thanks to an awesome guy who goes by the name of *perzik* for giving a hint on how to solve the last challenge: *reverse*.

![Screencap after getting 100% of the challenges done](https://raw.githubusercontent.com/Paradoxis/SHA2017/master/ctf/junior-ctf-100-percent.png)
