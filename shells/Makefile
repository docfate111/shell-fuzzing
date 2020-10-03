CC = which afl-gcc
make:
	make tcsh && make tcsh && make zsh && make yash && make ksh && make mksh && make bash5 && make bash4 && make bash3 

make tcsh:
	cd tcsh/src && $(CC) ./configure --without-tcsetpgrp  && make && mv tcsh ..

make zsh:
	cd zsh/src && $(CC) ./configure --without-tcsetpgrp  && make && mv zsh ..

make yash:
	cd yash/src && $(CC) ./configure --enable-array --enable-dirstack --enable-help --enable-history --enable-lineedit
	\ --enable-nls --enable-printf --enable-socket --enable-test --enable-ulimit && make && mv yash ..

make ksh:
	cd ksh/src && $(CC) ninja -C build install && mv ksh ..

make mksh:
	cd mksh/src && $(CC) /bin/sh ./Build.sh && mv mksh ..

make bash5:
	cd bash5/src && $(CC) ./configure && $(CC) make && cp bash ../bash5

make bash4:
	cd bash4/src && $(CC) ./configure && $(CC) make && cp bash ../bash4

make bash3:
	cd bash3/src && $(CC) ./configure && $(CC) make && cp bash ../bash3

make heirloom-sh:
	cd heirloom-sh/src &&  $(CC) make && cp sh ../heirloom-sh

make osh:
	cd osh/src && $(CC) ./configure  && $(CC) make && mv osh ..

make posh:
	cd posh/src && $(CC) autoreconf -fiv &&  $(CC) --disable-dependency-tracking --disable-silent-rules && $(CC) make && mv posh .. 



