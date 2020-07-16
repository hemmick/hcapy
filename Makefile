CC = gcc
default: hcapy

LIB_DIR := $(PWD)/lib
SHELL := /bin/bash

ZWAVE_PATH_OPTIMISTIC := ${HOME}/zwportal/src/zwave

ZWAVE_PATH ?= ${ZWAVE_PATH_OPTIMISTIC}
HCAPI_PATH ?= ${ZWAVE_PATH}/hcapi

hcapy: lib/libhcapy.so
	python3 setup.py sdist bdist_wheel

lib/libhcapy.so: hcapi $(ZWAVE_PATH)/openssl
	mkdir lib
	cd lib; ar -x $(HCAPI_PATH)/src/***.a; \
		ar -x $(HCAPI_PATH)/lib/***.a; \
	       	ar -x $(ZWAVE_PATH)/openssl/install/lib/libcrypto.a; \
		ar -x $(ZWAVE_PATH)/openssl/install/lib/libssl.a
	$(CC) -shared -g lib/*.o -o lib/libhcapy.so -Wno-undef -L$(ZWAVE_PATH)/openssl/install/lib -lcrypto -lssl -I$(ZWAVE_PATH)/openssl/include

hcapi:  $(ZWAVE_PATH)/openssl
	make -C $(HCAPI_PATH) TARGET_PLATFORM=LINUX_ZIP2

$(ZWAVE_PATH)/openssl:
	cd $(HCAPI_PATH); source install_openssl_lib.sh;
	cd $(HCAPI_PATH); opt_shared="-shared" source build_openssl_lib.sh linux release


clean:
	rm -rf lib dist build *.egg-info
