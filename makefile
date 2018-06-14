DESTDIR ?= /usr/local/bin

install:
	@sudo pip install -r requirements.txt
	@sudo touch ~/.setting.txt
	@sudo cp mantool $(DESTDIR)
	@sudo chmod +x $(DESTDIR)/mantool
	@echo "Everything is setup! Enter 'mantool -h' in terminal to use mantool"

uninstall:
	@sudo rm -f $(DESTDIR)/mantool
	@sudo rm -f ~/.setting.txt
	@echo "mantool has been removed"
