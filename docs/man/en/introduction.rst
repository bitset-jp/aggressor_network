Operation Description
=======================

Screen Configuration
---------------------

This is the execution screen of this device.

.. figure:: /_static/ss_overview.png
   :width: 95%

   Execution screen

The screen is divided into 5 screens, and each screen has the following functions.

.. table:: Screen configuration
   :widths: 20, 20, 70

   ===============  ======================  ===========================================================================
   Screen title     Name in this document    Function
   ===============  ======================  ===========================================================================
   0 main            0:Main screen           This is the command input screen.
   1 HELP            1:Help screen           Displays help.
   2 I/O Stat        2:Traffic screen        Displays the amount of communication every second.
   3 eth0            3:eth0 screen           Displays the communication status of eth0. (iftop / tcpdump switching)
   4 eth1            4:eth1 screen           Displays the communication status of eth1. (iftop / tcpdump switching)
   ===============  ======================  ===========================================================================

.. raw:: latex

   \clearpage


Main screen (0:main)
--------------------------

This is the screen for command operation.

.. figure:: /_static/ss_0_main.png
   :width: 90%

   Main screen

All key input is done on this screen, and the following can be done.

#. Select network device
#. Set filter options
#. Capture packets
#. Set system configuration
#. Display help

.. raw:: latex

   \clearpage


Display Filter Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Whenever you press ``ENTER`` or execute a command, the latest filter information is displayed.

.. figure:: /_static/prompt.png
   :width: 90%

   Filter information

* 1st line ( "[0] eth0:... ", "[1] eth1:... " )

  This is the filter setting. For details on filters, please refer to :ref:`filter`.

* 2nd-3rd line (blue text)

  Traffic statistics for each network device.

  .. table:: Display items
     :widths: 10, 40

     ===============    ==========================================
      Item                Meaning
     ===============    ==========================================
     Sent                Sent byte count, packet count
     dropped             Discarded
     overlimit           Number of times the queue became full
     requeues            Queuing for retransmission
     backlog             T.B.D
     ===============    ==========================================

.. raw:: latex

   \clearpage


Network device selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Indicates the selection status of the network device in the prompt.

.. table:: prompt
   :widths: 10, 40

   ============  ==================================
   Prompt        Selection status
   ============  ==================================
   ``0 >``       Select eth0
   ``1 >``       Select eth1
   ``a >``       Select both (eth0 & eth1)
   ============  ==================================

You can switch selection with the device selection command ( ``0`` / ``1`` / ``a`` ).

0: Select eth0::

   a > 0 [ENTER]
   0 >

1: Select eth1::

   0 > 1 [ENTER]
   1 >

a: Select both (eth0, eth1)::
   
   0 > a [ENTER]
   a >


.. raw:: latex

   \clearpage

Help screen (1:HELP)
------------------------------

Displays help for commands.

.. figure:: /_static/ss_1_help.png
   :scale: 35

   Help screen (command list)

Enter ``help command_name`` at "0:Main screen" to display the help for that command.

.. code:: text

   a > help rate

.. figure:: /_static/ss_1_help_rate.png
   :scale: 35

   Help screen (help rate)

.. note::
   
   For a list of available commands, see :ref:`command_list`.

.. raw:: latex

   \clearpage

Traffic screen (2:I/O Stat)
--------------------------------------

Update the transmission and reception amounts of each network device (eth0, eth1) every second.

.. figure:: /_static/ss_2_io_stat.png
   :width: 60%

   Traffic screen

Traffic information is displayed in the order of time, eth0 (received, sent) and eth1 (received, sent).
And, the color of the number changes depending on the amount of communication.

.. table:: Color of communication amount
   :widths: 10, 80

   ======   ==================
   Color    Unit
   ======   ==================
   Red      Byte
   Yellow   Kbyte
   Green    Mbyte
   ======   ==================

.. note::

   If the network device is not active (= not connected) at startup, the amount of communication will not be displayed even if you connect to the network after startup.
   In that case, execute the ``stat`` command on "0:Main screen".

.. raw:: latex

   \clearpage

Network device communication status screen(3:eth0) / (4:eth1)
--------------------------------------------------------------------

Displays the communication status of the network device (iftop or tcpdump).

* iftop
  
  Displays the bandwidth per TCP connection.

* tcpdump

  Displays the network packet.


Switch display contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From "0:Main screen", you can switch the display by entering the following command.

(1) iftop
```````````````````````

.. figure:: /_static/ss_3-4_eth.png
   :width: 100%

   iftop only

Procedure::

  0 > a        ... Select both devices
  a > iftop    ... Switch display

.. raw:: latex

   \clearpage

(2) tcpdump
```````````````````````

.. figure:: /_static/ss_3-4_eth_tcpdump.png
   :width: 100%

   tcpdump only

Procedure::

   0 > a          ... Select both devices
   a > tcpdump    ... Switch display

(3) Mixed
```````````````````````

You can also display different displays on the left (eth0) and right (eth1).

.. figure:: /_static/ss_3-4_eth_mix.png
   :width: 100%

   iftop(left:eth0), tcpdump(right:eth1)

Procedure::

   a > 0          ... Select eth0
   0 > iftop      ... Switch display of eth0
   0 > 1          ... Select eth1
   1 > tcpdump    ... Switch display of eth1




.. raw:: latex

   \clearpage


Adjust the display size
^^^^^^^^^^^^^^^^^^^^^^^^^^

From "0:Main screen", you can change the display size (number of lines) with the ``height`` command.

Procedure::

   0 > height 20     ... Specify in the range of 10-35
   
.. note::

   The screen 3 and 4 are changed simultaneously regardless of the device selection status.






