Abstract
========

This product is a network emulator that can intentionally generates various network failures, such as bandwidth control and packet filters (delay / loss / duplication / corruption / order change).
Packet capture results can be saved to a USB memory.

.. figure:: /_static/overview.png
   :width: 80%

   Usage image

.. raw:: latex

   \clearpage

Specification
--------------

.. table:: Network
   :widths: 10, 40

   ===============  ===================================
   Network          Wired
   Number of ports  2 ports (main, USB adapter)
   Maximum speed    1Gbps
   IP address       Not used
   ===============  ===================================

.. note::

   This product does not use IP addresses and transfers packets like a network HUB.

.. table:: Packet filter
   :widths: 10, 40

   =================  =============================================
   Delay              Specify the delay time. Jitter (fluctuation) can be specified
   Loss               Specify the occurrence rate
   Duplication        Specify the occurrence rate
   Corruption         Specify the occurrence rate
   Order change       Specify the occurrence rate
   Bandwidth control  Specify communication speed (bps - Gbps)
   =================  =============================================

.. table:: Packet capture
   :widths: 10, 40

   =========================  ===================================
   Data storage format        PCAP ... Displayable with Wireshark
   Data storage destination   USB memory
   USB memory                 FAT format
   =========================  ===================================

.. table:: Others
   :widths: 10, 40

   =========================  ==========================================
   Display                    HDMI monitor, resolution: Full HD
   Input device               USB keyboard (switchable between US / JP)
   Power                      USB Type-C 5V / 3A or more
   RTC                        Built-in (replaceable battery: CR1225)
   =========================  ==========================================

Included items
---------------

.. |main| image:: /_static/main.png
   :align: bottom

.. |eth| image:: /_static/ether-adapter.png
   :align: bottom

.. |hdmi| image:: /_static/hdmi-adapter.png
   :align: bottom

.. |power| image:: /_static/power.png
   :align: bottom

.. table:: Included items
   :widths: 20, 20, 20

   =======================================  ==============  ================================
   Item                                      Photo           Note
   =======================================  ==============  ================================
   1. Main device                           |main|          - Ethernet Gbit Ethernet x1
                                                            - USB3 x2
                                                            - USB2 x2
                                                            - microHDMI x2
                                                            - USB Type-C (power only) x1
                                                            - Built-in RTC

   2. USB network adapter                   |eth|           - USB3.0 Gbit Ethernt compatible
   3. microHDMI - HDMI conversion adapter   |hdmi|
   4. USB power supply                      |power|         - USB Type-C 5V / 3A or more
   =======================================  ==============  ================================

.. raw:: latex

   \clearpage

Port configuration
^^^^^^^^^^^^^^^^^^^^

(1) USB, Ethernet
`````````````````````

The blue USB port is USB3, and the black port is USB2.

.. figure:: /_static/side-usb.png
   :width: 45%

   Ethernt, USB2, USB3, Ethernet

.. table:: Ethernet port device name
   :widths: 20, 40

   =========================  ================================
   Port                        Ethernet device name
   =========================  ================================
   Ethernet port               eth0
   USB network adapter         eth1
   =========================  ================================

.. table:: USB port usage
   :widths: 20, 40

   =================  ===========================================
   Port               Usage
   =================  ===========================================
   USB3  (blue)       USB network adapter

                      USB memory
   USB2  (black)      Keyboard
   =================  ===========================================

(2) Power, HDMI
`````````````````````````````````````````

There are two microHDMI ports, but you can connect either one.

.. figure:: /_static/side-hdmi.png
   :width: 45%

   USB power supply, microHDMI

.. raw:: latex

   \clearpage

Items to be prepared separately
--------------------------------

The following items are not included in the product, so please prepare them yourself.

.. table:: Items to be prepared by the customer
   :widths: 50, 10, 60

   =====================  =========  ==================================================
   Item                   Quantity   Specification
   =====================  =========  ==================================================
   Keyboard                  1          USB, English or Japanese
   Display                   1          Resolution: Full HD, HDMI compatible
   Ethernet cable            2
   USB memory                1          USB3.0 compatible is desirable

                                        Only required when packet capture is performed
   =====================  =========  ==================================================

.. note::

   In addition to the above, you need a network device connected to both networks of this machine.
