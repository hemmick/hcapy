CC = gcc
default: hcapy

HCAPI_PATH_OPTIMISTIC := ${HOME}/zwportal/src/zwave/hcapi

HCAPI_PATH ?= ${HCAPI_PATH_OPTIMISTIC}

hcapy:

libhcapy.so: hcapi
        ar -x $(HCAPI_PATH)/src/***.a
        ar -x $(HCAPI_PATH)/lib/***.a
        $(CC) -shared *.o -o libhcapy.so


hcapi:
        make -C $(HCAPI_PATH) TARGET_PLATFORM=LINUX_ZIP2

clean:
        rm *.so *.o
