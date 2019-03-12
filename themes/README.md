#Install solarize color theme in ubuntu 14.04 or 16.04 Gnome Terminal
Solarized is the best color scheme. You can follow the below instruction to install it.

Before we install Solarized for Ubuntu, we might need git to be installed to that we can clone some repository from GitHub.

Check if git is installed by issuing the following command

git

if you get an output like this.

The program ‘git’ is currently not installed. You can install it by typing:
sudo apt-get install git

So you can install git by issuing the command

sudo apt-get install git

After git is installed you can clone one repository from github by using this command

git clone https://github.com/sigurdga/gnome-terminal-colors-solarized.git

just remember that the above command create’s a directory gnome-terminal-colors-solarized

Now change to the above directory by giving this command and install dark or light theme.

cd gnome-terminal-colors-solarized
./install



//coming from https://archerimagine.wordpress.com/2014/05/01/things-to-do-after-a-fresh-install-of-ubuntu-14-04-trusty-tahr/