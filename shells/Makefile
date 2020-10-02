CC = which afl-gcc
make:


make tcsh:
	cd tcsh/src && $(CC) ./configure --without-tcsetpgrp  && make install && mv tcsh ..

make zsh:
	cd zsh/src && $(CC) ./configure --without-tcsetpgrp  && make install && mv zsh ..

make yash:
	cd yash/src && $(CC) ./configure --enable-array --enable-dirstack --enable-help --enable-history --enable-lineedit
	\ --enable-nls --enable-printf --enable-socket --enable-test --enable-ulimit" && make install && mv yash ..

make ksh:
	cd ksh/src && $(CC) ninja -C build install && mv ksh ..

make mksh:
	cd mksh/src && $(CC) /bin/sh ./Build.sh && mv mksh ..

make bash5:
	cd mksh/src && $(CC) ./configure && $(CC) make install && cp bash ../bash5
