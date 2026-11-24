# Linux Device Driver – Master Knowledge Dataset Collection List

A collection index for Linux driver development RAG and LLM fine-tuning. Prefer version-matched official source, preserve provenance and licenses, and validate training examples.

## 1. Linux kernel fundamentals

| S.No | Driver for / Module | Details | Link |
|---:|---|---|---|
| 1 | Linux Kernel | Complete kernel source | [Reference](https://github.com/torvalds/linux) |
| 2 | Linux Kernel | Official documentation | [Reference](https://docs.kernel.org/) |
| 3 | Kernel Architecture | Core architecture and subsystems | [Reference](https://docs.kernel.org/core-api/) |
| 4 | Kernel Modules | Loadable modules | [Reference](https://docs.kernel.org/kbuild/modules.html) |
| 5 | Kernel Build | Kbuild and Makefiles | [Reference](https://docs.kernel.org/kbuild/) |
| 6 | Kernel Configuration | Kconfig syntax | [Reference](https://docs.kernel.org/kbuild/kconfig-language.html) |
| 7 | Kernel APIs | Core functions and APIs | [Reference](https://docs.kernel.org/core-api/) |
| 8 | Kernel Headers | Header files and structures | [Reference](https://github.com/torvalds/linux/tree/master/include/linux) |
| 9 | Kernel Memory | Memory management | [Reference](https://docs.kernel.org/mm/) |
| 10 | Kernel Synchronization | Mutex and spinlock | [Reference](https://docs.kernel.org/locking/) |
| 11 | Kernel Programming | Coding standards | [Reference](https://docs.kernel.org/process/coding-style.html) |
| 12 | Kernel Versions | Historical releases | [Reference](https://www.kernel.org/) |
| 13 | Kernel Internals | Searchable source | [Reference](https://elixir.bootlin.com/) |
| 14 | Kernel Development | Practical exercises | [Reference](https://linux-kernel-labs.github.io/) |
| 15 | Kernel System Calls | System call implementation | [Reference](https://github.com/torvalds/linux/tree/master/kernel) |

## 2. Device driver fundamentals

| S.No | Driver for / Module | Details | Link |
|---:|---|---|---|
| 16 | Device Driver | Driver architecture | [Reference](https://docs.kernel.org/driver-api/) |
| 17 | Device Model | Registration and lifecycle | [Reference](https://docs.kernel.org/driver-api/driver-model/) |
| 18 | Character Driver | Registration and file operations | [Reference](https://github.com/torvalds/linux/tree/master/drivers/char) |
| 19 | Character Driver | Practical examples | [Reference](https://linux-kernel-labs.github.io/refs/heads/master/labs/device_drivers.html) |
| 20 | Block Driver | Request queues and architecture | [Reference](https://docs.kernel.org/block/) |
| 21 | Block Driver | Implementations | [Reference](https://github.com/torvalds/linux/tree/master/drivers/block) |
| 22 | Platform Driver | Probe and remove | [Reference](https://docs.kernel.org/driver-api/driver-model/platform.html) |
| 23 | Miscellaneous Driver | Character device examples | [Reference](https://github.com/torvalds/linux/tree/master/drivers/misc) |
| 24 | IOCTL | Commands and structures | [Reference](https://docs.kernel.org/driver-api/ioctl.html) |
| 25 | IOCTL | User-space system call | [Reference](https://man7.org/linux/man-pages/man2/ioctl.2.html) |
| 26 | IOCTL | Command number conventions | [Reference](https://docs.kernel.org/userspace-api/ioctl/) |
| 27 | IOCTL | Kernel implementation | [Reference](https://github.com/torvalds/linux/blob/master/fs/ioctl.c) |
| 28 | UIO | User-space I/O | [Reference](https://docs.kernel.org/driver-api/uio-howto.html) |
| 29 | UIO | Driver examples | [Reference](https://github.com/torvalds/linux/tree/master/drivers/uio) |
| 30 | VFIO | Direct device access | [Reference](https://docs.kernel.org/driver-api/vfio.html) |
| 31 | VFIO | Implementation | [Reference](https://github.com/torvalds/linux/tree/master/drivers/vfio) |
| 32 | Device Resources | Managed resource cleanup | [Reference](https://docs.kernel.org/driver-api/driver-model/devres.html) |
| 33 | Register Map | Regmap framework | [Reference](https://github.com/torvalds/linux/tree/master/drivers/base/regmap) |
| 34 | User Space API | Kernel-to-user interfaces | [Reference](https://docs.kernel.org/userspace-api/) |
| 35 | Driver Headers | Shared UAPI structures | [Reference](https://github.com/torvalds/linux/tree/master/include/uapi) |

## 3. PCI and PCIe

| S.No | Driver for / Module | Details | Link |
|---:|---|---|---|
| 36 | PCIe | Protocol specifications | [Reference](https://pcisig.com/specifications) |
| 37 | PCIe | Subsystem documentation | [Reference](https://docs.kernel.org/PCI/) |
| 38 | PCIe | Driver development guide | [Reference](https://docs.kernel.org/PCI/pci.html) |
| 39 | PCIe | Subsystem implementation | [Reference](https://github.com/torvalds/linux/tree/master/drivers/pci) |
| 40 | PCIe | Controller drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/pci/controller) |
| 41 | PCIe | Endpoint framework | [Reference](https://docs.kernel.org/PCI/endpoint/) |
| 42 | PCIe | Endpoint implementation | [Reference](https://github.com/torvalds/linux/tree/master/drivers/pci/endpoint) |
| 43 | PCIe | BAR mapping and MMIO | [Reference](https://docs.kernel.org/driver-api/device-io.html) |
| 44 | PCIe | Configuration space and capabilities | [Reference](https://github.com/torvalds/linux/blob/master/include/uapi/linux/pci_regs.h) |
| 45 | PCIe | MSI and MSI-X | [Reference](https://docs.kernel.org/PCI/msi-howto.html) |
| 46 | PCIe | Error recovery | [Reference](https://docs.kernel.org/PCI/pci-error-recovery.html) |
| 47 | PCIe | SR-IOV | [Reference](https://docs.kernel.org/PCI/pci-iov-howto.html) |
| 48 | PCIe | Device ID database | [Reference](https://pci-ids.ucw.cz/) |
| 49 | PCIe | Diagnostic utilities | [Reference](https://github.com/pciutils/pciutils) |
| 50 | PCIe | Discovery and configuration APIs | [Reference](https://github.com/torvalds/linux/blob/master/include/linux/pci.h) |
| 51 | PCIe FPGA | XDMA and QDMA drivers | [Reference](https://github.com/Xilinx/dma_ip_drivers) |
| 52 | PCIe FPGA | IP programming manuals | [Reference](https://docs.amd.com/) |
| 53 | PCIe FPGA | Implementation examples | [Reference](https://github.com/enjoy-digital/litepcie) |
| 54 | PCIe | Endpoint test driver and IOCTL | [Reference](https://github.com/torvalds/linux/blob/master/drivers/misc/pci_endpoint_test.c) |
| 55 | PCIe | Simulated hardware | [Reference](https://www.qemu.org/docs/master/specs/edu.html) |

## 4. Communication interfaces

| S.No | Driver for / Module | Details | Link |
|---:|---|---|---|
| 56 | I2C | Protocol specification | [Reference](https://www.nxp.com/docs/en/user-guide/UM10204.pdf) |
| 57 | I2C | Subsystem APIs | [Reference](https://docs.kernel.org/i2c/) |
| 58 | I2C | Controller drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/i2c/busses) |
| 59 | I2C | User-space IOCTL | [Reference](https://docs.kernel.org/i2c/dev-interface.html) |
| 60 | I2C | Diagnostic tools | [Reference](https://git.kernel.org/pub/scm/utils/i2c-tools/i2c-tools.git/) |
| 61 | I2C | User-space driver | [Reference](https://github.com/torvalds/linux/blob/master/drivers/i2c/i2c-dev.c) |
| 62 | SPI | Subsystem architecture | [Reference](https://docs.kernel.org/spi/) |
| 63 | SPI | Controller drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/spi) |
| 64 | SPI | User-space programming | [Reference](https://docs.kernel.org/spi/spidev.html) |
| 65 | SPI | IOCTL implementation | [Reference](https://github.com/torvalds/linux/blob/master/drivers/spi/spidev.c) |
| 66 | SPI | Test application | [Reference](https://github.com/torvalds/linux/blob/master/tools/spi/spidev_test.c) |
| 67 | QSPI | Controller examples | [Reference](https://github.com/torvalds/linux/tree/master/drivers/spi) |
| 68 | QSPI | SPI NOR framework | [Reference](https://docs.kernel.org/driver-api/mtd/spi-nor.html) |
| 69 | QSPI | NOR drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/mtd/spi-nor) |
| 70 | UART | Serial architecture | [Reference](https://docs.kernel.org/driver-api/serial/) |
| 71 | UART | Controller drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/tty/serial) |
| 72 | UART | 8250/16550 drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/tty/serial/8250) |
| 73 | UART | Termios configuration | [Reference](https://man7.org/linux/man-pages/man3/termios.3.html) |
| 74 | CAN | SocketCAN APIs | [Reference](https://docs.kernel.org/networking/can.html) |
| 75 | CAN | CAN and CAN-FD drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/net/can) |
| 76 | CAN | Test utilities | [Reference](https://github.com/linux-can/can-utils) |
| 77 | I3C | Architecture | [Reference](https://docs.kernel.org/driver-api/i3c/) |
| 78 | I3C | Controller drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/i3c) |
| 79 | 1-Wire | Protocol | [Reference](https://docs.kernel.org/w1/) |
| 80 | 1-Wire | Driver examples | [Reference](https://github.com/torvalds/linux/tree/master/drivers/w1) |

## 5. USB and HID

| S.No | Driver for / Module | Details | Link |
|---:|---|---|---|
| 81 | USB | Protocol specifications | [Reference](https://www.usb.org/documents) |
| 82 | USB | Driver documentation | [Reference](https://docs.kernel.org/driver-api/usb/) |
| 83 | USB | Subsystem source | [Reference](https://github.com/torvalds/linux/tree/master/drivers/usb) |
| 84 | USB | Skeleton driver | [Reference](https://github.com/torvalds/linux/blob/master/drivers/usb/usb-skeleton.c) |
| 85 | USB | User-space library | [Reference](https://github.com/libusb/libusb) |
| 86 | USB | Transfer APIs | [Reference](https://libusb.sourceforge.io/api-1.0/) |
| 87 | USB | Host controllers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/usb/host) |
| 88 | USB | Gadget drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/usb/gadget) |
| 89 | USB | Serial converters | [Reference](https://github.com/torvalds/linux/tree/master/drivers/usb/serial) |
| 90 | HID | Architecture and reports | [Reference](https://docs.kernel.org/hid/) |
| 91 | HID | Keyboard and mouse drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/hid) |
| 92 | HID | HIDRAW API | [Reference](https://docs.kernel.org/hid/hidraw.html) |
| 93 | HID | User-space examples | [Reference](https://github.com/libusb/hidapi) |
| 94 | FTDI | Datasheets | [Reference](https://ftdichip.com/document/datasheets/) |
| 95 | FTDI | MPSSE application notes | [Reference](https://ftdichip.com/document/application-notes/) |

## 6. DMA, interrupts and memory

| S.No | Driver for / Module | Details | Link |
|---:|---|---|---|
| 96 | DMA | Mapping architecture | [Reference](https://docs.kernel.org/core-api/dma-api.html) |
| 97 | DMA | Coherent and streaming mappings | [Reference](https://docs.kernel.org/core-api/dma-api-howto.html) |
| 98 | DMA | DMAEngine framework | [Reference](https://docs.kernel.org/driver-api/dmaengine/) |
| 99 | DMA | Controller drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/dma) |
| 100 | DMA | Test implementation | [Reference](https://github.com/torvalds/linux/blob/master/drivers/dma/dmatest.c) |
| 101 | DMA | Scatter-gather | [Reference](https://github.com/torvalds/linux/blob/master/include/linux/scatterlist.h) |
| 102 | Interrupt | Generic IRQ handling | [Reference](https://docs.kernel.org/core-api/genericirq.html) |
| 103 | Interrupt | Controller drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/irqchip) |
| 104 | Interrupt | Kernel implementation | [Reference](https://github.com/torvalds/linux/tree/master/kernel/irq) |
| 105 | Memory | Management | [Reference](https://docs.kernel.org/mm/) |
| 106 | Memory | Allocation APIs | [Reference](https://docs.kernel.org/core-api/memory-allocation.html) |
| 107 | Memory | Implementation | [Reference](https://github.com/torvalds/linux/tree/master/mm) |
| 108 | Memory | Barriers and ordering | [Reference](https://docs.kernel.org/core-api/wrappers/memory-barriers.html) |
| 109 | Memory | MMIO | [Reference](https://docs.kernel.org/driver-api/device-io.html) |
| 110 | Memory | mmap API | [Reference](https://man7.org/linux/man-pages/man2/mmap.2.html) |
| 111 | IOMMU | Address translation | [Reference](https://github.com/torvalds/linux/tree/master/drivers/iommu) |
| 112 | DDR | Memory testing | [Reference](https://pyropus.ca/software/memtester/) |
| 113 | DDR | ECC and EDAC | [Reference](https://github.com/torvalds/linux/tree/master/drivers/edac) |
| 114 | Workqueue | Deferred execution | [Reference](https://docs.kernel.org/core-api/workqueue.html) |
| 115 | Synchronization | Atomics and reference counting | [Reference](https://docs.kernel.org/core-api/) |

## 7. Storage drivers

| S.No | Driver for / Module | Details | Link |
|---:|---|---|---|
| 116 | NVMe | Specifications | [Reference](https://nvmexpress.org/specifications/) |
| 117 | NVMe | Driver source | [Reference](https://github.com/torvalds/linux/tree/master/drivers/nvme) |
| 118 | NVMe | IOCTL and management | [Reference](https://github.com/linux-nvme/nvme-cli) |
| 119 | SATA | ATA controllers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/ata) |
| 120 | SCSI | Architecture | [Reference](https://docs.kernel.org/scsi/) |
| 121 | SCSI | Drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/scsi) |
| 122 | MMC/eMMC | Subsystem APIs | [Reference](https://docs.kernel.org/driver-api/mmc/) |
| 123 | MMC/eMMC | Controllers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/mmc) |
| 124 | SD/MMC | Test tools | [Reference](https://git.kernel.org/pub/scm/utils/mmc/mmc-utils.git/) |
| 125 | NAND/NOR | MTD drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/mtd) |
| 126 | NAND | Controllers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/mtd/nand) |
| 127 | Flash | Management tools | [Reference](https://git.infraroot.at/mtd-utils.git/) |
| 128 | EEPROM | Peripheral drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/misc/eeprom) |
| 129 | NVMEM | Framework | [Reference](https://docs.kernel.org/driver-api/nvmem.html) |
| 130 | Storage Testing | Performance tests | [Reference](https://github.com/axboe/fio) |

## 8. Networking drivers

| S.No | Driver for / Module | Details | Link |
|---:|---|---|---|
| 131 | Ethernet | Architecture | [Reference](https://docs.kernel.org/networking/) |
| 132 | Ethernet | MAC drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/net/ethernet) |
| 133 | Ethernet | Intel examples | [Reference](https://github.com/torvalds/linux/tree/master/drivers/net/ethernet/intel) |
| 134 | Ethernet | PHY framework | [Reference](https://docs.kernel.org/networking/phy.html) |
| 135 | Ethernet | PHY and MDIO drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/net/phy) |
| 136 | Ethernet | Ethtool | [Reference](https://git.kernel.org/pub/scm/network/ethtool/ethtool.git/) |
| 137 | Wi-Fi | Architecture | [Reference](https://wireless.docs.kernel.org/) |
| 138 | Wi-Fi | Drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/net/wireless) |
| 139 | Bluetooth | Controller drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/bluetooth) |
| 140 | Bluetooth | BlueZ | [Reference](https://github.com/bluez/bluez) |
| 141 | TCP/UDP | Networking stack | [Reference](https://github.com/torvalds/linux/tree/master/net) |
| 142 | Network Testing | Throughput tests | [Reference](https://github.com/esnet/iperf) |
| 143 | Network Debugging | Packet capture | [Reference](https://github.com/the-tcpdump-group/tcpdump) |
| 144 | Network Driver | Registration APIs | [Reference](https://docs.kernel.org/networking/netdevices.html) |
| 145 | Network Driver | NAPI | [Reference](https://docs.kernel.org/networking/napi.html) |

## 9. Display, camera and multimedia

| S.No | Driver for / Module | Details | Link |
|---:|---|---|---|
| 146 | Display | DRM/KMS architecture | [Reference](https://docs.kernel.org/gpu/) |
| 147 | Display | DRM source | [Reference](https://github.com/torvalds/linux/tree/master/drivers/gpu/drm) |
| 148 | DisplayPort | Standards | [Reference](https://vesa.org/) |
| 149 | DisplayPort | Helper implementation | [Reference](https://github.com/torvalds/linux/tree/master/drivers/gpu/drm/display) |
| 150 | HDMI | Specifications | [Reference](https://www.hdmi.org/) |
| 151 | EDID | Parsing and validation | [Reference](https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/drm_edid.c) |
| 152 | EDID | Decoder | [Reference](https://git.linuxtv.org/edid-decode.git/) |
| 153 | Framebuffer | Drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/video/fbdev) |
| 154 | Camera | V4L2 APIs | [Reference](https://docs.kernel.org/userspace-api/media/) |
| 155 | Camera | Driver architecture | [Reference](https://docs.kernel.org/driver-api/media/) |
| 156 | Camera | Sensor drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/media/i2c) |
| 157 | USB Camera | UVC drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/media/usb/uvc) |
| 158 | MIPI CSI | Specifications | [Reference](https://www.mipi.org/specifications) |
| 159 | MIPI DSI | Specifications | [Reference](https://www.mipi.org/specifications) |
| 160 | Camera Testing | V4L2 tools | [Reference](https://git.linuxtv.org/v4l-utils.git/) |
| 161 | Audio | ALSA development | [Reference](https://docs.kernel.org/sound/) |
| 162 | Audio | Driver implementation | [Reference](https://github.com/torvalds/linux/tree/master/sound) |
| 163 | Audio | ASoC and I2S | [Reference](https://github.com/torvalds/linux/tree/master/sound/soc) |
| 164 | Audio | User-space library | [Reference](https://github.com/alsa-project/alsa-lib) |
| 165 | Input | Subsystem | [Reference](https://docs.kernel.org/input/) |

## 10. GPIO, sensors and peripherals

| S.No | Driver for / Module | Details | Link |
|---:|---|---|---|
| 166 | GPIO | Controller APIs | [Reference](https://docs.kernel.org/driver-api/gpio/) |
| 167 | GPIO | Drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/gpio) |
| 168 | GPIO | User-space control | [Reference](https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/) |
| 169 | PWM | Framework | [Reference](https://docs.kernel.org/driver-api/pwm.html) |
| 170 | PWM | Drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/pwm) |
| 171 | ADC | IIO framework | [Reference](https://docs.kernel.org/driver-api/iio/) |
| 172 | ADC | Drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/iio/adc) |
| 173 | DAC | Drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/iio/dac) |
| 174 | Temperature Sensor | Monitoring framework | [Reference](https://docs.kernel.org/hwmon/) |
| 175 | Temperature Sensor | Drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/hwmon) |
| 176 | RTC | Drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/rtc) |
| 177 | Watchdog | Development | [Reference](https://docs.kernel.org/watchdog/) |
| 178 | Watchdog | Source | [Reference](https://github.com/torvalds/linux/tree/master/drivers/watchdog) |
| 179 | Touchscreen | Drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/input/touchscreen) |
| 180 | LED | Architecture | [Reference](https://docs.kernel.org/leds/) |
| 181 | LED | Controllers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/leds) |
| 182 | Sensors | Accelerometers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/iio/accel) |
| 183 | Sensors | Gyroscopes | [Reference](https://github.com/torvalds/linux/tree/master/drivers/iio/gyro) |
| 184 | Thermal | Management drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/thermal) |
| 185 | Crypto | Hardware accelerators | [Reference](https://github.com/torvalds/linux/tree/master/drivers/crypto) |

## 11. BSP and board bring-up

| S.No | Driver for / Module | Details | Link |
|---:|---|---|---|
| 186 | BSP | Embedded Linux training | [Reference](https://bootlin.com/docs/) |
| 187 | Bootloader | U-Boot documentation | [Reference](https://docs.u-boot.org/) |
| 188 | Bootloader | U-Boot source | [Reference](https://github.com/u-boot/u-boot) |
| 189 | Device Tree | Specification | [Reference](https://devicetree-specification.readthedocs.io/) |
| 190 | Device Tree | Linux API | [Reference](https://docs.kernel.org/devicetree/) |
| 191 | Device Tree | Bindings and YAML schemas | [Reference](https://github.com/torvalds/linux/tree/master/Documentation/devicetree/bindings) |
| 192 | Device Tree | ARM64 DTS examples | [Reference](https://github.com/torvalds/linux/tree/master/arch/arm64/boot/dts) |
| 193 | Device Tree | Compiler | [Reference](https://github.com/dgibson/dtc) |
| 194 | Clock | Framework | [Reference](https://docs.kernel.org/driver-api/clk.html) |
| 195 | Clock | Controllers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/clk) |
| 196 | Pin Control | Multiplexing API | [Reference](https://docs.kernel.org/driver-api/pin-control.html) |
| 197 | Pin Control | Drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/pinctrl) |
| 198 | Power Management | Framework | [Reference](https://docs.kernel.org/power/) |
| 199 | Regulator | APIs | [Reference](https://docs.kernel.org/driver-api/regulator.html) |
| 200 | Regulator | Drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/regulator) |
| 201 | Reset Controller | Framework | [Reference](https://github.com/torvalds/linux/tree/master/drivers/reset) |
| 202 | Buildroot | Image creation | [Reference](https://buildroot.org/docs.html) |
| 203 | Buildroot | Source | [Reference](https://github.com/buildroot/buildroot) |
| 204 | Yocto | Documentation | [Reference](https://docs.yoctoproject.org/) |
| 205 | Yocto | Layers and recipes | [Reference](https://layers.openembedded.org/) |
| 206 | ARM | Architecture manuals | [Reference](https://developer.arm.com/documentation) |
| 207 | RISC-V | Specifications | [Reference](https://riscv.org/specifications/) |
| 208 | ACPI | Specifications | [Reference](https://uefi.org/specifications) |
| 209 | Firmware | Trusted firmware | [Reference](https://trustedfirmware-a.readthedocs.io/) |
| 210 | Firmware | Linux firmware repository | [Reference](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/) |

## 12. Hardware manuals and vendor references

| S.No | Driver for / Module | Details | Link |
|---:|---|---|---|
| 211 | AMD/Xilinx FPGA | PCIe, AXI and DMA manuals | [Reference](https://docs.amd.com/) |
| 212 | AMD/Xilinx PCIe | PG195 XDMA guide | [Reference](https://docs.amd.com/r/en-US/pg195-pcie-dma) |
| 213 | AMD/Xilinx PCIe | PG302 QDMA guide | [Reference](https://docs.amd.com/r/en-US/pg302-qdma) |
| 214 | AMD/Xilinx BSP | Vendor kernel | [Reference](https://github.com/Xilinx/linux-xlnx) |
| 215 | AMD/Xilinx Firmware | Peripheral drivers | [Reference](https://github.com/Xilinx/embeddedsw) |
| 216 | Intel/Altera FPGA | PCIe and DDR manuals | [Reference](https://www.intel.com/content/www/us/en/products/details/fpga.html) |
| 217 | Intel/Altera BSP | Vendor kernel | [Reference](https://github.com/altera-opensource/linux-socfpga) |
| 218 | Intel Processor | System programming manuals | [Reference](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html) |
| 219 | Microchip | Datasheets and errata | [Reference](https://www.microchip.com/) |
| 220 | Microchip | Harmony CSP drivers | [Reference](https://github.com/Microchip-MPLAB-Harmony/csp) |
| 221 | NXP | SoC manuals | [Reference](https://www.nxp.com/) |
| 222 | NXP | i.MX Linux BSP | [Reference](https://github.com/nxp-imx/linux-imx) |
| 223 | Texas Instruments | Processor SDK | [Reference](https://dev.ti.com/) |
| 224 | STMicroelectronics | Datasheets | [Reference](https://www.st.com/) |
| 225 | STMicroelectronics | STM32MP kernel | [Reference](https://github.com/STMicroelectronics/linux) |
| 226 | Raspberry Pi | Hardware documentation | [Reference](https://www.raspberrypi.com/documentation/) |
| 227 | Raspberry Pi | Kernel source | [Reference](https://github.com/raspberrypi/linux) |
| 228 | NVIDIA | Jetson BSP | [Reference](https://docs.nvidia.com/jetson/) |
| 229 | Analog Devices | ADC, DAC and sensor drivers | [Reference](https://github.com/analogdevicesinc/linux) |
| 230 | DDR Memory | Datasheets and timing | [Reference](https://www.micron.com/) |
| 231 | Memory Standards | JEDEC specifications | [Reference](https://www.jedec.org/standards-documents) |
| 232 | Flash Memory | NOR and NAND datasheets | [Reference](https://www.winbond.com/) |
| 233 | FPGA | Manager framework | [Reference](https://docs.kernel.org/driver-api/fpga/) |
| 234 | FPGA | Manager drivers | [Reference](https://github.com/torvalds/linux/tree/master/drivers/fpga) |
| 235 | Hardware Simulation | Virtual hardware | [Reference](https://github.com/qemu/qemu) |

## 13. Debugging, testing and validation

| S.No | Driver for / Module | Details | Link |
|---:|---|---|---|
| 236 | Kernel Debugging | Development tools | [Reference](https://docs.kernel.org/dev-tools/) |
| 237 | Kernel Debugging | KGDB and KDB | [Reference](https://docs.kernel.org/process/debugging/kgdb.html) |
| 238 | Kernel Debugging | Kdump | [Reference](https://docs.kernel.org/admin-guide/kdump/) |
| 239 | Kernel Debugging | Crash utility | [Reference](https://github.com/crash-utility/crash) |
| 240 | Kernel Logging | printk | [Reference](https://docs.kernel.org/core-api/printk-basics.html) |
| 241 | Kernel Tracing | ftrace | [Reference](https://docs.kernel.org/trace/ftrace.html) |
| 242 | Kernel Tracing | Tracepoints | [Reference](https://docs.kernel.org/trace/) |
| 243 | Performance | Perf source | [Reference](https://github.com/torvalds/linux/tree/master/tools/perf) |
| 244 | System Calls | Strace | [Reference](https://github.com/strace/strace) |
| 245 | Hardware Debugging | JTAG and OpenOCD | [Reference](https://github.com/openocd-org/openocd) |
| 246 | Hardware Debugging | Logic analyzer | [Reference](https://sigrok.org/) |
| 247 | Static Analysis | Sparse | [Reference](https://sparse.docs.kernel.org/) |
| 248 | Static Analysis | Coccinelle | [Reference](https://docs.kernel.org/dev-tools/coccinelle.html) |
| 249 | Static Analysis | Cppcheck | [Reference](https://github.com/danmar/cppcheck) |
| 250 | Memory Debugging | KASAN | [Reference](https://docs.kernel.org/dev-tools/kasan.html) |
| 251 | Concurrency Debugging | KCSAN | [Reference](https://docs.kernel.org/dev-tools/kcsan.html) |
| 252 | Memory Leak | Kmemleak | [Reference](https://docs.kernel.org/dev-tools/kmemleak.html) |
| 253 | Unit Testing | KUnit framework | [Reference](https://docs.kernel.org/dev-tools/kunit/) |
| 254 | Unit Testing | KUnit examples | [Reference](https://github.com/torvalds/linux/tree/master/lib/kunit) |
| 255 | Integration Testing | Kernel selftests | [Reference](https://github.com/torvalds/linux/tree/master/tools/testing/selftests) |
| 256 | System Testing | Linux Test Project | [Reference](https://github.com/linux-test-project/ltp) |
| 257 | Stress Testing | Stress-ng | [Reference](https://github.com/ColinIanKing/stress-ng) |
| 258 | Fault Injection | Failure simulation | [Reference](https://docs.kernel.org/fault-injection/) |
| 259 | Fuzz Testing | Syzkaller | [Reference](https://github.com/google/syzkaller) |
| 260 | Bug Tracking | Syzbot | [Reference](https://syzkaller.appspot.com/) |

## 14. Engineering knowledge, tutorials and bug fixes

| S.No | Driver for / Module | Details | Link |
|---:|---|---|---|
| 261 | All Drivers | Linux Device Drivers book (historical) | [Reference](https://lwn.net/Kernel/LDD3/) |
| 262 | All Drivers | Bootlin training | [Reference](https://bootlin.com/docs/) |
| 263 | All Drivers | Practical labs | [Reference](https://linux-kernel-labs.github.io/) |
| 264 | All Drivers | Kernel tutorials | [Reference](https://kernelnewbies.org/) |
| 265 | All Drivers | Patches and discussions | [Reference](https://lore.kernel.org/) |
| 266 | All Drivers | Bug reports | [Reference](https://bugzilla.kernel.org/) |
| 267 | All Drivers | Technical articles | [Reference](https://lwn.net/Kernel/) |
| 268 | All Drivers | Programming Q&A | [Reference](https://stackoverflow.com/questions/tagged/linux-device-driver) |
| 269 | All Drivers | Structured Q&A API | [Reference](https://api.stackexchange.com/) |
| 270 | All Drivers | System programming | [Reference](https://man7.org/linux/man-pages/) |
| 271 | All Drivers | Maintainers | [Reference](https://github.com/torvalds/linux/blob/master/MAINTAINERS) |
| 272 | All Drivers | Commit history | [Reference](https://github.com/torvalds/linux/commits/master/) |
| 273 | All Drivers | Stable patches | [Reference](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/) |
| 274 | All Drivers | Patch reviews | [Reference](https://patchwork.kernel.org/) |
| 275 | C Programming | GNU C reference | [Reference](https://www.gnu.org/software/c-intro-and-ref/manual/) |
| 276 | Compilation | GCC | [Reference](https://gcc.gnu.org/onlinedocs/) |
| 277 | Compilation | Clang | [Reference](https://clang.llvm.org/docs/) |
| 278 | Debugging | GDB | [Reference](https://sourceware.org/gdb/documentation/) |
| 279 | Compilation | Binutils | [Reference](https://sourceware.org/binutils/docs/) |
| 280 | Emulation | QEMU documentation | [Reference](https://www.qemu.org/docs/master/) |

## 15. Dataset collection summary

| Category | Entries |
|---|---:|
| Linux kernel fundamentals | 15 |
| Device driver fundamentals | 20 |
| PCI and PCIe | 20 |
| Communication interfaces | 25 |
| USB and HID | 15 |
| DMA, interrupts and memory | 20 |
| Storage drivers | 15 |
| Networking drivers | 15 |
| Display, camera and multimedia | 20 |
| GPIO, sensors and peripherals | 20 |
| BSP and board bring-up | 25 |
| Hardware manuals and vendor references | 25 |
| Debugging, testing and validation | 25 |
| Engineering knowledge, tutorials and bug fixes | 20 |
| **Total** | **280** |

## 16. Information to extract

| S.No | Knowledge type | Information | Format |
|---:|---|---|---|
| 1 | Theory | Architecture and concepts | Markdown |
| 2 | Protocol | Rules and packet structures | Markdown / JSON |
| 3 | API | Functions, parameters, return values | JSON |
| 4 | Source code | Implementations and headers | C / H |
| 5 | Hardware | Datasheets and manuals | PDF / Markdown |
| 6 | Registers | Address, offset, width, bit fields, access mode | JSON |
| 7 | Examples | Working implementations | C / Markdown |
| 8 | Configuration | Device tree, Kconfig, Makefiles | DTS / YAML / Text |
| 9 | Debugging | Symptoms and verified solutions | JSONL |
| 10 | Errors | errno and failure conditions | JSON |
| 11 | Testing | Procedures and expected results | JSON / Markdown |
| 12 | Code review | Incorrect and corrected code | JSONL |
| 13 | Versions | Deprecated APIs and replacements | JSON |
| 14 | Q&A | Expert-verified answers | JSONL |
| 15 | Performance | Latency, throughput, benchmarks | CSV / JSON |

## 17. Automated collection tools

| Source | Tool | Output |
|---|---|---|
| Documentation websites | Crawl4AI | Markdown |
| Bulk crawling | Scrapy | JSONL |
| Repositories | Git | Original source |
| PDF manuals | Docling | Markdown / JSON |
| Register tables | Docling / PyMuPDF | JSON |
| C source | Tree-sitter | Structured chunks |
| Commit history | Git log / diff | JSONL |
| Engineering Q&A | Official APIs | JSON |
| Deduplication | SHA-256 / MinHash | Clean dataset |
| Dataset storage | Hugging Face Datasets | Parquet / JSONL |
| RAG indexing | ChromaDB / FAISS | Vector index |

## 18. Collection priority

| Phase | Modules | Priority |
|---|---|---|
| 1 | Kernel fundamentals, character drivers, IOCTL | P0 |
| 2 | PCIe, DMA, interrupts, memory | P0 |
| 3 | SPI, QSPI, I2C, UART, USB, HID | P1 |
| 4 | Hardware manuals and register maps | P0 |
| 5 | BSP, device tree, bootloader | P1 |
| 6 | Display, camera, DDR, storage, Ethernet | P1 |
| 7 | Debugging, testing and validation | P0 |
| 8 | Verified engineering Q&A and fine-tuning examples | P0 |

## Collection and quality guidelines

- Separate Global Knowledge (general Linux driver information) from Project Knowledge (board-specific registers, schematics, requirements and existing drivers).
- For PCIe IOCTL, prioritize entries 24–27 and 36–55.
- Preserve source URLs, licenses, document revisions, kernel versions and Git commit hashes.
- Prefer official repositories and APIs over scraping. Respect access restrictions, website terms and rate limits.
- Use only authorized data. Do not upload confidential company materials to external services without permission.
- Validate code by compilation, static analysis and hardware testing; separate training and evaluation examples.
- These 280 entries are collection categories, not unique websites or an exhaustive inventory. Links are reference starting points and have not all been independently rechecked.
