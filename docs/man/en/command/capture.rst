Packet Capture
============================

.. note::

   1. To use "Packet Capture", USB memory is required. (USB3.0 is recommended)
   2. Results are confirmed using Wireshark on PC.


Procedure for packet capture
-------------------------------

(1) Start
^^^^^^^^^^^^^
1. Insert USB memory into USB3.0 port.

   When USB memory is recognized, the message `insert USB memory` is displayed.

   .. figure:: /_static/ss_insert_usb.png
      :width: 90%

      USB memory insertion message

   .. note::

      Make sure that there is enough free space on the USB memory.



2. Enter the capture start command on the main screen.

   Format::

      > cap start  {rotate interval (seconds)}

   By default, the file is rotated every 3600 seconds (1 hour). If you want to change the interval, specify it with an argument.


   .. figure:: /_static/ss_cap_start.png
      :width: 40%

      Capture start

   In the above example, capture of both eth0 and eth1 is started.


(2) Stop
^^^^^^^^^^^^

1. Enter the capture stop command on the main screen.

   Format::

      > cap stop


2. Wait until the capture result file is saved.

   .. figure:: /_static/ss_cap_stop.png
      :width: 90%

      Capture stop

   After ``stopped``, if the file list in the USB memory is displayed, the processing is completed.



3. Remove the USB memory.

.. raw:: latex

   \clearpage

(3) Result confirmation
^^^^^^^^^^^^^^^^^^^^^^^^

Open and check the capture file (\*.gz) saved on the USB memory with Wireshark. (No need to unzip the gz file)

The files are saved with the following naming convention.

   .. code:: text

      eth{0|1}_{YYYY-MM-DD_hh-mm-ss}.pcap.gz


1. Open the file in the [File]-[Open] menu of Wireshark.

   .. figure:: /_static/ss_wireshark_open.png
      :width: 60%

      ファイルを開く=> Open file

2. Display capture data.

   .. figure:: /_static/ss_wireshark.png
      :width: 80%

      Display in Wireshark


.. raw:: latex

   \clearpage


ls: List files on USB memory
-----------------------------------------------


Format::

   > ls

 
Example:

   .. figure:: /_static/ls.png
      :width: 90%

      Example of ls command execution


``\*.pcap.gz`` is the result of packet capture.


cap start: Start packet capture
--------------------------------------


Format::

   > cap start  {ローテート間隔 (秒)}


..

   .. table:: cap start コマンドの引数
      :widths: 20, 10, 60


      =====================  ===========  ================================================
      Argument                 Required       value
      =====================  ===========  ================================================
      Rotate interval             x           unit:seconds, range:60 - 3600 (default 3600)
      =====================  ===========  ================================================



cap stop: Stop packet capture
-------------------------------


Format::

   > cap stop



After executing the command, the unsaved data is written to the USB memory, so please wait for a while.
If the file list on the USB memory is displayed, the processing is completed.


.. raw:: latex

   \clearpage
