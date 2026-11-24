# Linux Driver Development – Technical Knowledge Source Collection

214 reference entries for collecting concepts, code, implementation logic, dependencies, execution flow, testing, debugging, hardware and related knowledge. URLs are reference candidates, not live-verified links. Some overlap intentionally.

## 1. Conceptual knowledge and implementation logic

| S.No | Knowledge type | Information to collect | Reference URL | Output format |
|---:|---|---|---|---|
| 1 | Concepts / logic | Driver fundamentals | <https://embetronicx.com/linux-device-driver-tutorials/> | JSON / MD |
| 2 | Concepts / logic | Practical driver exercises | <https://linux-kernel-labs.github.io/> | JSON / MD |
| 3 | Concepts / logic | Kernel architecture | <https://github.com/0xAX/linux-insides> | JSON / MD |
| 4 | Concepts / logic | Kernel module development | <https://sysprog21.github.io/lkmpg/> | JSON / MD |
| 5 | Concepts / logic | Embedded Linux training | <https://bootlin.com/docs/> | JSON / MD |
| 6 | Concepts / logic | Driver registration and lifecycle | <https://docs.kernel.org/driver-api/driver-model/> | JSON / MD |
| 7 | Concepts / logic | Character driver implementation | <https://linux-kernel-labs.github.io/refs/heads/master/labs/device_drivers.html> | JSON / MD |
| 8 | Concepts / logic | IOCTL implementation | <https://embetronicx.com/tutorials/linux/device-drivers/ioctl-tutorial-in-linux/> | JSON / C |
| 9 | Concepts / logic | PCIe initialization | <https://docs.kernel.org/PCI/pci.html> | JSON / MD |
| 10 | Concepts / logic | USB driver development | <https://docs.kernel.org/driver-api/usb/writing_usb_driver.html> | JSON / MD |

## 2. Source code and practical examples

| S.No | Knowledge type | Information to collect | Reference URL | Output format |
|---:|---|---|---|---|
| 11 | Source code | Complete Linux kernel | <https://github.com/torvalds/linux/> | C / H |
| 12 | Source code | Character drivers | <https://github.com/torvalds/linux/tree/master/drivers/char> | C / H |
| 13 | Source code | PCIe drivers | <https://github.com/torvalds/linux/tree/master/drivers/pci> | C / H |
| 14 | Source code | FPGA PCIe DMA examples | <https://github.com/Xilinx/dma_ip_drivers> | C / H |
| 15 | Source code | USB skeleton | <https://github.com/torvalds/linux/blob/master/drivers/usb/usb-skeleton.c> | C / H |
| 16 | Source code | SPI IOCTL | <https://github.com/torvalds/linux/blob/master/drivers/spi/spidev.c> | C / H |
| 17 | Source code | I2C IOCTL | <https://github.com/torvalds/linux/blob/master/drivers/i2c/i2c-dev.c> | C / H |
| 18 | Source code | DMA controllers | <https://github.com/torvalds/linux/tree/master/drivers/dma> | C / H |
| 19 | Source code | PCI endpoint test | <https://github.com/torvalds/linux/blob/master/drivers/misc/pci_endpoint_test.c> | C / H |
| 20 | Source code | Kernel samples | <https://github.com/torvalds/linux/tree/master/samples> | C / H |
| 21 | Source code | UIO drivers | <https://github.com/torvalds/linux/tree/master/drivers/uio> | C / H |
| 22 | Source code | Embedded drivers | <https://github.com/Xilinx/embeddedsw> | C / H |

## 3. Required headers, modules and libraries

| S.No | Knowledge type | Information to collect | Reference URL | Output format |
|---:|---|---|---|---|
| 23 | Dependencies | Kernel headers | <https://github.com/torvalds/linux/tree/master/include/linux> | H / JSON |
| 24 | Dependencies | User-space API headers | <https://github.com/torvalds/linux/tree/master/include/uapi> | H / JSON |
| 25 | Dependencies | Module registration | <https://github.com/torvalds/linux/blob/master/include/linux/module.h> | H / JSON |
| 26 | Dependencies | File operations | <https://github.com/torvalds/linux/blob/master/include/linux/fs.h> | H / JSON |
| 27 | Dependencies | Character device APIs | <https://github.com/torvalds/linux/blob/master/include/linux/cdev.h> | H / JSON |
| 28 | Dependencies | IOCTL macros | <https://github.com/torvalds/linux/blob/master/include/uapi/linux/ioctl.h> | H / JSON |
| 29 | Dependencies | User memory access | <https://github.com/torvalds/linux/blob/master/include/linux/uaccess.h> | H / JSON |
| 30 | Dependencies | PCI APIs | <https://github.com/torvalds/linux/blob/master/include/linux/pci.h> | H / JSON |
| 31 | Dependencies | PCI registers | <https://github.com/torvalds/linux/blob/master/include/uapi/linux/pci_regs.h> | H / JSON |
| 32 | Dependencies | MMIO APIs | <https://github.com/torvalds/linux/blob/master/include/linux/io.h> | H / JSON |
| 33 | Dependencies | Interrupt APIs | <https://github.com/torvalds/linux/blob/master/include/linux/interrupt.h> | H / JSON |
| 34 | Dependencies | DMA mapping | <https://github.com/torvalds/linux/blob/master/include/linux/dma-mapping.h> | H / JSON |
| 35 | Dependencies | Memory allocation | <https://github.com/torvalds/linux/blob/master/include/linux/slab.h> | H / JSON |
| 36 | Dependencies | Mutexes | <https://github.com/torvalds/linux/blob/master/include/linux/mutex.h> | H / JSON |
| 37 | Dependencies | Spinlocks | <https://github.com/torvalds/linux/blob/master/include/linux/spinlock.h> | H / JSON |
| 38 | Dependencies | Workqueues | <https://github.com/torvalds/linux/blob/master/include/linux/workqueue.h> | H / JSON |
| 39 | Dependencies | USB library | <https://github.com/libusb/libusb> | C / H / JSON |
| 40 | Dependencies | GPIO library | <https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/> | C / H / JSON |
| 41 | Dependencies | Standard C library | <https://sourceware.org/git/glibc.git> | C / H |
| 42 | Dependencies | Module management | <https://github.com/kmod-project/kmod> | C / JSON |

## 4. API knowledge and function references

| S.No | Knowledge type | Information to collect | Reference URL | Output format |
|---:|---|---|---|---|
| 43 | API knowledge | Kernel core APIs | <https://docs.kernel.org/core-api/> | JSON |
| 44 | API knowledge | Driver APIs | <https://docs.kernel.org/driver-api/> | JSON |
| 45 | API knowledge | Kernel-doc format | <https://docs.kernel.org/doc-guide/kernel-doc.html> | JSON |
| 46 | API knowledge | Function cross-references | <https://elixir.bootlin.com/> | JSON |
| 47 | API knowledge | System calls | <https://man7.org/linux/man-pages/> | JSON |
| 48 | API knowledge | IOCTL syscall | <https://man7.org/linux/man-pages/man2/ioctl.2.html> | JSON |
| 49 | API knowledge | Memory mapping | <https://man7.org/linux/man-pages/man2/mmap.2.html> | JSON |
| 50 | API knowledge | Device I/O | <https://docs.kernel.org/driver-api/device-io.html> | JSON |
| 51 | API knowledge | DMA API | <https://docs.kernel.org/core-api/dma-api.html> | JSON |
| 52 | API knowledge | Interrupt handling | <https://docs.kernel.org/core-api/genericirq.html> | JSON |
| 53 | API knowledge | Memory allocation | <https://docs.kernel.org/core-api/memory-allocation.html> | JSON |
| 54 | API knowledge | Managed resources | <https://docs.kernel.org/driver-api/driver-model/devres.html> | JSON |

## 5. Execution flow and function relationships

| S.No | Knowledge type | Information to collect | Reference URL | Output format |
|---:|---|---|---|---|
| 55 | Execution flow | Kernel boot flow | <https://github.com/0xAX/linux-insides> | JSON / Mermaid |
| 56 | Execution flow | Device binding | <https://docs.kernel.org/driver-api/driver-model/binding.html> | JSON / Mermaid |
| 57 | Execution flow | IOCTL syscall implementation | <https://github.com/torvalds/linux/blob/master/fs/ioctl.c> | JSON / Mermaid |
| 58 | Execution flow | PCI initialization | <https://github.com/torvalds/linux/blob/master/drivers/pci/probe.c> | JSON / Mermaid |
| 59 | Execution flow | PCI driver probing | <https://github.com/torvalds/linux/blob/master/drivers/pci/pci-driver.c> | JSON / Mermaid |
| 60 | Execution flow | Character device registration | <https://github.com/torvalds/linux/blob/master/fs/char_dev.c> | JSON / Mermaid |
| 61 | Execution flow | Workqueue scheduling | <https://github.com/torvalds/linux/blob/master/kernel/workqueue.c> | JSON / Mermaid |
| 62 | Execution flow | IRQ management | <https://github.com/torvalds/linux/blob/master/kernel/irq/manage.c> | JSON / Mermaid |
| 63 | Execution flow | DMA lifecycle | <https://docs.kernel.org/driver-api/dmaengine/client.html> | JSON / Mermaid |
| 64 | Execution flow | USB URB lifecycle | <https://docs.kernel.org/driver-api/usb/URB.html> | JSON / Mermaid |
| 65 | Execution flow | Static call graphs | <https://www.doxygen.nl/manual/> | XML / DOT |
| 66 | Execution flow | C syntax trees | <https://github.com/tree-sitter/tree-sitter-c> | AST / JSON |
| 67 | Execution flow | Semantic code analysis | <https://clang.llvm.org/docs/LibTooling.html> | JSON |
| 68 | Execution flow | Runtime tracing | <https://docs.kernel.org/trace/ftrace.html> | Trace / JSON |

## 6. Build and configuration knowledge

| S.No | Knowledge type | Information to collect | Reference URL | Output format |
|---:|---|---|---|---|
| 69 | Build knowledge | External module compilation | <https://docs.kernel.org/kbuild/modules.html> | Makefile / JSON |
| 70 | Build knowledge | Kbuild architecture | <https://docs.kernel.org/kbuild/> | JSON |
| 71 | Build knowledge | Makefile syntax | <https://docs.kernel.org/kbuild/makefiles.html> | Makefile / JSON |
| 72 | Build knowledge | Kconfig syntax | <https://docs.kernel.org/kbuild/kconfig-language.html> | JSON |
| 73 | Build knowledge | Kernel Makefile | <https://github.com/torvalds/linux/blob/master/Makefile> | Makefile |
| 74 | Build knowledge | PCI Makefile | <https://github.com/torvalds/linux/blob/master/drivers/pci/Makefile> | Makefile |
| 75 | Build knowledge | PCI Kconfig | <https://github.com/torvalds/linux/blob/master/drivers/pci/Kconfig> | Kconfig |
| 76 | Build knowledge | GCC options | <https://gcc.gnu.org/onlinedocs/> | JSON |
| 77 | Build knowledge | Clang options | <https://clang.llvm.org/docs/> | JSON |
| 78 | Build knowledge | GNU Make | <https://www.gnu.org/software/make/manual/> | JSON |
| 79 | Build knowledge | Cross compilation | <https://bootlin.com/docs/> | JSON |
| 80 | Build knowledge | Buildroot | <https://buildroot.org/docs.html> | JSON |
| 81 | Build knowledge | Yocto BSP | <https://docs.yoctoproject.org/> | JSON |
| 82 | Build knowledge | Device tree bindings | <https://github.com/torvalds/linux/tree/master/Documentation/devicetree/bindings> | YAML / JSON |

## 7. Testing and validation knowledge

| S.No | Knowledge type | Information to collect | Reference URL | Output format |
|---:|---|---|---|---|
| 83 | Testing | Kernel testing methodology | <https://docs.kernel.org/dev-tools/testing-overview.html> | JSON |
| 84 | Testing | KUnit | <https://docs.kernel.org/dev-tools/kunit/> | C / JSON |
| 85 | Testing | Kernel selftests | <https://github.com/torvalds/linux/tree/master/tools/testing/selftests> | C / JSON |
| 86 | Testing | Linux Test Project | <https://github.com/linux-test-project/ltp> | C / JSON |
| 87 | Testing | PCI endpoint validation | <https://docs.kernel.org/PCI/endpoint/pci-test-howto.html> | JSON |
| 88 | Testing | PCI diagnostics | <https://github.com/pciutils/pciutils> | JSON |
| 89 | Testing | DMA testing | <https://docs.kernel.org/driver-api/dmaengine/dmatest.html> | JSON |
| 90 | Testing | DMA test code | <https://github.com/torvalds/linux/blob/master/drivers/dma/dmatest.c> | C |
| 91 | Testing | SPI test application | <https://github.com/torvalds/linux/blob/master/tools/spi/spidev_test.c> | C / JSON |
| 92 | Testing | I2C tools | <https://git.kernel.org/pub/scm/utils/i2c-tools/i2c-tools.git/> | JSON |
| 93 | Testing | USB test driver | <https://github.com/torvalds/linux/blob/master/drivers/usb/misc/usbtest.c> | C / JSON |
| 94 | Testing | DDR memory validation | <https://pyropus.ca/software/memtester/> | C / JSON |
| 95 | Testing | Storage performance | <https://github.com/axboe/fio> | JSON |
| 96 | Testing | Stress testing | <https://github.com/ColinIanKing/stress-ng> | JSON |
| 97 | Testing | Network throughput | <https://github.com/esnet/iperf> | JSON |
| 98 | Testing | Fault injection | <https://docs.kernel.org/fault-injection/> | JSON |
| 99 | Testing | Kernel fuzzing | <https://github.com/google/syzkaller> | JSONL |
| 100 | Testing | Virtual PCI hardware | <https://www.qemu.org/docs/master/specs/edu.html> | JSON |

## 8. Debugging knowledge, errors and solutions

| S.No | Knowledge type | Information to collect | Reference URL | Output format |
|---:|---|---|---|---|
| 101 | Debugging | Kernel developer tools | <https://docs.kernel.org/dev-tools/> | JSON |
| 102 | Debugging | Error codes | <https://man7.org/linux/man-pages/man3/errno.3.html> | JSON |
| 103 | Debugging | Error definitions | <https://github.com/torvalds/linux/blob/master/include/uapi/asm-generic/errno-base.h> | H / JSON |
| 104 | Debugging | Kernel logging | <https://docs.kernel.org/core-api/printk-basics.html> | JSON |
| 105 | Debugging | KGDB | <https://docs.kernel.org/process/debugging/kgdb.html> | JSON |
| 106 | Debugging | Crash dumps | <https://docs.kernel.org/admin-guide/kdump/> | JSON |
| 107 | Debugging | Memory leaks | <https://docs.kernel.org/dev-tools/kmemleak.html> | JSON |
| 108 | Debugging | Invalid memory access | <https://docs.kernel.org/dev-tools/kasan.html> | JSON |
| 109 | Debugging | Race detection | <https://docs.kernel.org/dev-tools/kcsan.html> | JSON |
| 110 | Debugging | Undefined behavior | <https://docs.kernel.org/dev-tools/ubsan.html> | JSON |
| 111 | Debugging | Lockdep | <https://docs.kernel.org/locking/lockdep-design.html> | JSON |
| 112 | Debugging | PCI error recovery | <https://docs.kernel.org/PCI/pci-error-recovery.html> | JSON |
| 113 | Debugging | PCI AER | <https://docs.kernel.org/PCI/pcieaer-howto.html> | JSON |
| 114 | Debugging | System call tracing | <https://github.com/strace/strace> | JSON |
| 115 | Debugging | Sparse | <https://sparse.docs.kernel.org/> | JSON |
| 116 | Debugging | Coccinelle | <https://docs.kernel.org/dev-tools/coccinelle.html> | JSON |
| 117 | Debugging | Bug reports | <https://bugzilla.kernel.org/> | JSONL |
| 118 | Debugging | Crash reproductions | <https://syzkaller.appspot.com/> | JSONL |
| 119 | Debugging | Kernel fixes | <https://github.com/torvalds/linux/commits/master/> | JSONL |
| 120 | Debugging | Stable fixes | <https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/> | JSONL |
| 121 | Debugging | Patch discussions | <https://lore.kernel.org/lkml/> | JSONL |
| 122 | Debugging | PCI problems and solutions | <https://lore.kernel.org/linux-pci/> | JSONL |

## 9. Related and interconnected technical knowledge

| S.No | Knowledge type | Information to collect | Reference URL | Output format |
|---:|---|---|---|---|
| 123 | Related knowledge | Connected driver tutorials | <https://embetronicx.com/linux-device-driver-tutorials/> | JSON |
| 124 | Related knowledge | Subsystem relationships | <https://docs.kernel.org/> | JSON |
| 125 | Related knowledge | Symbol relationships | <https://elixir.bootlin.com/> | JSON |
| 126 | Related knowledge | Kernel architecture dependencies | <https://github.com/0xAX/linux-insides> | JSON |
| 127 | Related knowledge | Device model | <https://docs.kernel.org/driver-api/driver-model/> | JSON |
| 128 | Related knowledge | PCI and DMA | <https://docs.kernel.org/core-api/dma-api-howto.html> | JSON |
| 129 | Related knowledge | PCI MSI | <https://docs.kernel.org/PCI/msi-howto.html> | JSON |
| 130 | Related knowledge | Memory ordering | <https://docs.kernel.org/core-api/wrappers/memory-barriers.html> | JSON |
| 131 | Related knowledge | Device tree binding | <https://docs.kernel.org/devicetree/> | JSON |
| 132 | Related knowledge | Power management | <https://docs.kernel.org/driver-api/pm/> | JSON |
| 133 | Related knowledge | Subsystem maintainers | <https://github.com/torvalds/linux/blob/master/MAINTAINERS> | JSON |
| 134 | Related knowledge | Engineering design discussions | <https://lwn.net/Kernel/> | JSON |

## 10. Hardware knowledge and register specifications

| S.No | Knowledge type | Information to collect | Reference URL | Output format |
|---:|---|---|---|---|
| 135 | Hardware | PCIe specifications | <https://pcisig.com/specifications> | PDF / JSON |
| 136 | Hardware | FPGA XDMA registers | <https://docs.amd.com/r/en-US/pg195-pcie-dma> | PDF / JSON |
| 137 | Hardware | FPGA QDMA registers | <https://docs.amd.com/r/en-US/pg302-qdma> | PDF / JSON |
| 138 | Hardware | AXI and peripherals | <https://docs.amd.com/> | PDF / JSON |
| 139 | Hardware | Intel processor registers | <https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html> | PDF / JSON |
| 140 | Hardware | ARM architecture | <https://developer.arm.com/documentation> | PDF / JSON |
| 141 | Hardware | RISC-V architecture | <https://riscv.org/specifications/> | PDF / JSON |
| 142 | Hardware | I2C protocol and timing | <https://www.nxp.com/docs/en/user-guide/UM10204.pdf> | PDF / JSON |
| 143 | Hardware | USB specifications | <https://www.usb.org/documents> | PDF / JSON |
| 144 | Hardware | FTDI datasheets | <https://ftdichip.com/document/datasheets/> | PDF / JSON |
| 145 | Hardware | FTDI application notes | <https://ftdichip.com/document/application-notes/> | PDF / JSON |
| 146 | Hardware | Microcontroller peripherals | <https://www.microchip.com/> | PDF / JSON |
| 147 | Hardware | SAM peripheral implementations | <https://github.com/Microchip-MPLAB-Harmony/csp> | C / JSON |
| 148 | Hardware | TI processor manuals | <https://dev.ti.com/> | PDF / JSON |
| 149 | Hardware | DDR standards | <https://www.jedec.org/standards-documents> | PDF / JSON |
| 150 | Hardware | DDR datasheets | <https://www.micron.com/> | PDF / JSON |
| 151 | Hardware | Flash registers | <https://www.winbond.com/> | PDF / JSON |
| 152 | Hardware | NVMe specifications | <https://nvmexpress.org/specifications/> | PDF / JSON |
| 153 | Hardware | DisplayPort and EDID | <https://vesa.org/> | PDF / JSON |
| 154 | Hardware | MIPI CSI and DSI | <https://www.mipi.org/specifications> | PDF / JSON |
| 155 | Hardware | Raspberry Pi peripherals | <https://www.raspberrypi.com/documentation/> | PDF / JSON |
| 156 | Hardware | Virtual PCI registers | <https://www.qemu.org/docs/master/specs/edu.html> | JSON |

## 11. Visual knowledge and architecture diagrams

| S.No | Knowledge type | Information to collect | Reference URL | Output format |
|---:|---|---|---|---|
| 157 | Visual knowledge | Driver architecture diagrams | <https://embetronicx.com/linux-device-driver-tutorials/> | PNG / JSON |
| 158 | Visual knowledge | Embedded architecture slides | <https://bootlin.com/docs/> | PDF / PNG |
| 159 | Visual knowledge | Subsystem diagrams | <https://linux-kernel-labs.github.io/> | SVG / JSON |
| 160 | Visual knowledge | Kernel internals illustrations | <https://github.com/0xAX/linux-insides> | PNG / JSON |
| 161 | Visual knowledge | PCIe FPGA architecture | <https://docs.amd.com/r/en-US/pg195-pcie-dma> | PNG / JSON |
| 162 | Visual knowledge | DMA block diagrams | <https://docs.amd.com/r/en-US/pg302-qdma> | PNG / JSON |
| 163 | Visual knowledge | I2C timing diagrams | <https://www.nxp.com/docs/en/user-guide/UM10204.pdf> | PNG / JSON |
| 164 | Visual knowledge | USB protocol diagrams | <https://www.usb.org/documents> | PNG / JSON |
| 165 | Visual knowledge | Graphics architecture | <https://docs.kernel.org/gpu/> | SVG / JSON |
| 166 | Visual knowledge | Multimedia architecture | <https://docs.kernel.org/driver-api/media/> | SVG / JSON |
| 167 | Visual knowledge | Function call diagrams | <https://www.doxygen.nl/manual/diagrams.html> | DOT / SVG |
| 168 | Visual knowledge | Execution flow diagrams | <https://mermaid.js.org/> | Mermaid / SVG |

## 12. Prerequisite engineering knowledge

| S.No | Knowledge type | Information to collect | Reference URL | Output format |
|---:|---|---|---|---|
| 169 | Prerequisite | C fundamentals | <https://www.gnu.org/software/c-intro-and-ref/manual/> | JSON / MD |
| 170 | Prerequisite | Pointers, structures and unions | <https://en.cppreference.com/w/c> | JSON |
| 171 | Prerequisite | Operating systems | <https://pages.cs.wisc.edu/~remzi/OSTEP/> | PDF / JSON |
| 172 | Prerequisite | Linux system programming | <https://man7.org/linux/man-pages/> | JSON |
| 173 | Prerequisite | Kernel and user space | <https://linux-kernel-labs.github.io/> | JSON |
| 174 | Prerequisite | Kernel programming | <https://sysprog21.github.io/lkmpg/> | JSON |
| 175 | Prerequisite | Memory management | <https://docs.kernel.org/mm/> | JSON |
| 176 | Prerequisite | Locking | <https://docs.kernel.org/locking/> | JSON |
| 177 | Prerequisite | Atomic operations | <https://docs.kernel.org/core-api/wrappers/atomic_t.html> | JSON |
| 178 | Prerequisite | Reference counting | <https://docs.kernel.org/core-api/kref.html> | JSON |
| 179 | Prerequisite | Linked lists | <https://docs.kernel.org/core-api/list.html> | JSON |
| 180 | Prerequisite | Interrupt handling | <https://docs.kernel.org/core-api/genericirq.html> | JSON |
| 181 | Prerequisite | DMA and physical memory | <https://docs.kernel.org/core-api/dma-api-howto.html> | JSON |
| 182 | Prerequisite | Coding standards | <https://docs.kernel.org/process/coding-style.html> | JSON |
| 183 | Prerequisite | Development workflow | <https://docs.kernel.org/process/development-process.html> | JSON |
| 184 | Prerequisite | Computer architecture | <https://computationstructures.org/> | JSON / PDF |

## 13. Engineering questions and answers

| S.No | Knowledge type | Information to collect | Reference URL | Output format |
|---:|---|---|---|---|
| 185 | Engineering Q&A | Device driver questions | <https://stackoverflow.com/questions/tagged/linux-device-driver> | JSONL |
| 186 | Engineering Q&A | Kernel questions | <https://stackoverflow.com/questions/tagged/linux-kernel> | JSONL |
| 187 | Engineering Q&A | IOCTL questions | <https://stackoverflow.com/questions/tagged/ioctl> | JSONL |
| 188 | Engineering Q&A | PCIe questions | <https://stackoverflow.com/questions/tagged/pcie> | JSONL |
| 189 | Engineering Q&A | Embedded Linux questions | <https://stackoverflow.com/questions/tagged/embedded-linux> | JSONL |
| 190 | Engineering Q&A | Programmatic Q&A collection | <https://api.stackexchange.com/> | JSONL |
| 191 | Engineering Q&A | Hardware interface questions | <https://electronics.stackexchange.com/> | JSONL |
| 192 | Engineering Q&A | System-level problems | <https://unix.stackexchange.com/> | JSONL |
| 193 | Engineering Q&A | Kernel developer discussions | <https://lore.kernel.org/lkml/> | JSONL |
| 194 | Engineering Q&A | PCI discussions | <https://lore.kernel.org/linux-pci/> | JSONL |
| 195 | Engineering Q&A | USB discussions | <https://lore.kernel.org/linux-usb/> | JSONL |
| 196 | Engineering Q&A | SPI discussions | <https://lore.kernel.org/linux-spi/> | JSONL |
| 197 | Engineering Q&A | I2C discussions | <https://lore.kernel.org/linux-i2c/> | JSONL |
| 198 | Engineering Q&A | TI technical support | <https://e2e.ti.com/> | JSONL |
| 199 | Engineering Q&A | AMD FPGA discussions | <https://adaptivesupport.amd.com/> | JSONL |
| 200 | Engineering Q&A | ADI driver discussions | <https://ez.analog.com/> | JSONL |

## 14. Source provenance, versioning and licensing

| S.No | Knowledge type | Information to collect | Reference URL | Output format |
|---:|---|---|---|---|
| 201 | Provenance | Kernel releases | <https://www.kernel.org/> | JSON |
| 202 | Provenance | Release tags | <https://github.com/torvalds/linux/tags> | JSON |
| 203 | Provenance | Commit history | <https://github.com/torvalds/linux/commits/master/> | JSON |
| 204 | Provenance | Version-specific source | <https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/> | JSON |
| 205 | Provenance | Version-specific documentation | <https://docs.kernel.org/> | JSON |
| 206 | Provenance | Kernel licensing rules | <https://docs.kernel.org/process/license-rules.html> | JSON |
| 207 | Provenance | Kernel license files | <https://github.com/torvalds/linux/tree/master/LICENSES> | JSON |
| 208 | Provenance | SPDX identifiers | <https://spdx.org/licenses/> | JSON |
| 209 | Provenance | Creative Commons licenses | <https://creativecommons.org/share-your-work/cclicenses/> | JSON |
| 210 | Provenance | Repository metadata | <https://docs.github.com/en/rest> | JSON |
| 211 | Provenance | Git history extraction | <https://git-scm.com/docs/git-log> | JSONL |
| 212 | Provenance | Source line attribution | <https://git-scm.com/docs/git-blame> | JSON |
| 213 | Provenance | Code differences | <https://git-scm.com/docs/git-diff> | JSONL |
| 214 | Provenance | Robots exclusion protocol | <https://www.rfc-editor.org/rfc/rfc9309.html> | JSON |

## 15. Collection summary

| Category | Entries |
|---|---:|
| Conceptual knowledge and implementation logic | 10 |
| Source code and practical examples | 12 |
| Required headers, modules and libraries | 20 |
| API knowledge and function references | 12 |
| Execution flow and function relationships | 14 |
| Build and configuration knowledge | 14 |
| Testing and validation knowledge | 18 |
| Debugging knowledge, errors and solutions | 22 |
| Related and interconnected technical knowledge | 12 |
| Hardware knowledge and register specifications | 22 |
| Visual knowledge and architecture diagrams | 12 |
| Prerequisite engineering knowledge | 16 |
| Engineering questions and answers | 16 |
| Source provenance, versioning and licensing | 14 |
| **Total** | **214** |

## 16. Automated collection tools

| Knowledge category | Collector | Processor | Output |
|---|---|---|---|
| Conceptual knowledge | Crawl4AI | LLM + Pydantic | JSON |
| Source code | Git | Tree-sitter | C / H / JSON |
| Implementation logic | Crawl4AI | LLM | JSON |
| API knowledge | Git / Crawl4AI | Kernel-doc / Clang | JSON |
| Code explanation | Git | LLM + Clang | JSON |
| Dependencies | Git | Clang / Tree-sitter | JSON |
| Execution flow | Git | Doxygen / Ftrace / Clang | JSON / Mermaid |
| Build knowledge | Git | Makefile parser | Makefile / JSON |
| Testing knowledge | Git / Crawl4AI | Test parser + execution | JSON |
| Debugging knowledge | Git / API | PyDriller + LLM | JSONL |
| Related knowledge | Crawl4AI | Entity and relationship extraction | JSON |
| Hardware knowledge | HTTP downloader | Docling + Pydantic | JSON |
| Visual knowledge | Docling / HTML parser | Vision model + validation | PNG / JSON |
| Prerequisite knowledge | Crawl4AI | LLM classifier | JSON |
| Engineering Q&A | API / Git archives | Distilabel + expert review | JSONL |
| Source provenance | Git / HTTP | Metadata extractor | JSON |

## 17. Recommended storage structure

```text
Linux_Driver_Knowledge/
  01_Conceptual_Knowledge/
  02_Source_Code/
  03_Implementation_Logic/
  04_API_Knowledge/
  05_Code_Explanation/
  06_Dependencies/
  07_Execution_Flow/
  08_Build_Knowledge/
  09_Testing_Knowledge/
  10_Debugging_Knowledge/
  11_Related_Knowledge/
  12_Hardware_Knowledge/
  13_Visual_Knowledge/
  14_Prerequisite_Knowledge/
  15_Engineering_QA/
  16_Source_Provenance/
```

## Collection guidelines

- Download each unique authorized source once and extract all applicable knowledge categories.
- Preserve original files, URLs, section references, commit hashes, kernel versions and licenses.
- Check access permissions, terms and licensing before bulk collection or training.
- Validate forum answers, generated explanations, register maps and code before approving training records.
- Maintain relationships between concepts, APIs, source code, hardware and tests.
