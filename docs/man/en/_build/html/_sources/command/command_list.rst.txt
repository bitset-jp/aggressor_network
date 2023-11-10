.. _command_list:

Command List
================



The following commands are available on this device.
Commands can be entered from the "0: Main screen".

.. table:: general commands
   :widths: 10, 40, 10, 10

   =================  ==================================  ==================  =================
   command            description                          argument            target screen
   =================  ==================================  ==================  =================
   ``ifconfig``        Display network device settings     ---                  0
   ``clear``           Clear display                       ---                  0
   ``help``            Display help                        command              1
   ``stat``            Restart I/O Stat                    ---                  2
   ``iftop``           Display iftop                       ---                  3, 4
   ``tcpdump``         Display tcpdump                     ---                  3, 4
   ``height``          Set the number of display lines     number of  lines     3, 4
   =================  ==================================  ==================  =================

.. table:: filter commands
   :widths: 10, 60, 10

   ========================  ======================================================================================  ===========
   command                    description                                                                              argument
   ========================  ======================================================================================  ===========
   ``0`` / ``1`` / ``a``       Select target network  ``0``:eth0 / ``1``:eth1 / ``a``:all(eth0 & eth1)                ---
   ``edit``                    Display unapplied settings                                                             ---
   ``update``                  Apply filter settings                                                                  ---
   ``reset``                   Reset to initial state                                                                 ---
   ========================  ======================================================================================  ===========

.. table:: filter settings commands
   :widths: 10, 20, 40

   =================  ===============================  ========================================================
   command             description                       argument
   =================  ===============================  ========================================================
   ``delay``           delay packet transmission        delay time, {jitter time}, {occurrence rate(%)}
   ``loss``            loss                                        loss rate(%)
   ``duplicate``       duplicate                                   occurrence rate(%)
   ``corrupt``         corrupt                                     occurrence rate(%)
   ``reorder``         reorder                                     occurrence rate(%)
   ``rate``            rate                                        bandwidth(speed)
   =================  ===============================  ========================================================

.. table:: packet capture commands
   :widths: 15, 30, 30

   =================  ===================================  =========================
   command             description                          argument
   =================  ===================================  =========================
   ``ls``              display file list (USB memory)       ---
   ``cap start``       start packet capture                 rotate interval(sec)
   ``cap stop``        stop packet capture                  ---
   =================  ===================================  =========================

.. table:: system settings commands
   :widths: 15, 30, 30

   =================  ==========================  ==========================================
   command             description                 argument
   =================  ==========================  ==========================================
   ``rtc``             set system time             time setting(``YYYY-MM-DD hh:mm:ss``)
   ``keyboard``        change keyboard layout      layout (``us`` / ``jp`` / ``hhk``)
   =================  ==========================  ==========================================


.. note::

   From the next section, we will explain how to use each command.



.. raw:: latex

   \clearpage