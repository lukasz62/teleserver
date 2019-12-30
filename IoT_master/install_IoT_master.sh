#!/bin/sh

# Installation of required apt packages
cat apt-requirements.txt | xargs sudo apt install -y
if [ $? -ne 0 ]; then
	echo "Could not install required packages. Please check your packages. Exitting..."
	exit 1
fi

crontab -l | { cat; echo "*/5 * * * * /var/lib/teleserver/app/IoT_master/desks_reservation.py"; } | crontab -

echo "Teleserver IoT master has been installed successfully."
exit 0
