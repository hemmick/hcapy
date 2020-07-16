CC = gcc
default: hcapy

HCAPI_PATH_OPTIMISTIC := ${HOME}/zwportal/src/zwave/hcapi

HCAPI_PATH ?= ${HCAPI_PATH_OPTIMISTIC}

hcapy: lib/libhcapy.so
	python3 setup.py sdist bdist_wheel

lib/libhcapy.so: hcapi
	mkdir lib
	cd lib; ar -x $(HCAPI_PATH)/src/***.a; ar -x $(HCAPI_PATH)/lib/***.a
	$(CC) -shared -g lib/*.o -o lib/libhcapy.so

hcapi:  $(HCAPI_PATH)/src/libzip_ctl.a $(HCAPI_PATH)/lib/libzip_api.a
	make -C $(HCAPI_PATH) TARGET_PLATFORM=LINUX_ZIP2

clean:
	rm -rf lib dist build *.egg-info
