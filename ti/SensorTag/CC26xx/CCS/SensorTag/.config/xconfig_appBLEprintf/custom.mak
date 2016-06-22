## THIS IS A GENERATED FILE -- DO NOT EDIT
.configuro: .libraries,em3 linker.cmd package/cfg/appBLEprintf_pem3.oem3

# To simplify configuro usage in makefiles:
#     o create a generic linker command file name 
#     o set modification times of compiler.opt* files to be greater than
#       or equal to the generated config header
#
linker.cmd: package/cfg/appBLEprintf_pem3.xdl
	$(SED) 's"^\"\(package/cfg/appBLEprintf_pem3cfg.cmd\)\"$""\"C:/ti/simplelink/ble_cc26xx_2_01_01_44627/Projects/ble/SensorTag/CC26xx/CCS/SensorTag/.config/xconfig_appBLEprintf/\1\""' package/cfg/appBLEprintf_pem3.xdl > $@
	-$(SETDATE) -r:max package/cfg/appBLEprintf_pem3.h compiler.opt compiler.opt.defs
