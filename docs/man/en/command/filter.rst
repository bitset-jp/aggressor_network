.. _filter:

Setting Filter
=====================

Scope of filter application
---------------------------

The filter is applied to the output of the network device.

For example, if you set a delay option for only one device, the delay will occur only in one direction of the packet,
and no delay will occur in the opposite direction of the packet.

.. figure:: /_static/filter_delay_one.png
   :width: 90%

   Delay in one direction

So, if you want to delay in both directions, set the delay filter for both devices.

.. figure:: /_static/filter_delay_both.png
   :width: 90%

   Delay in both directions

.. raw:: latex

   \clearpage


Edit
---------------

Edit Command
------------------

The filter options are temporarily stored in the edit buffer and can be checked with the `edit` command.
The `update` command applies the filter settings in the edit buffer.
And it will be reset to the default with the `reset` command.

.. figure:: /_static/filter_command.png
   :width: 70%

   edit command



(1) edit
^^^^^^^^^^^^^^^^^^

Displays the contents of the edit buffer that is being edited which has not been applied to the filter yet.

.. figure:: /_static/edit.png
   :width: 95%

   edit command


.. raw:: latex

   \clearpage



(2) update
^^^^^^^^^^^^^^^^^^^^^^^^^

Applies the contents of the edit buffer to the filter.

.. figure:: /_static/update.png
   :width: 95%

   update command

In the example above, the bandwidth is set to 64Kpbs (= 512Kbit / second).


(3) reset
^^^^^^^^^^^^^^^^^^^^^^^^^^

Resets the applied and editing filter settings to the default.


.. figure:: /_static/reset.png
   :width: 95%

   reset command

.. raw:: latex

   \clearpage


Filter options
---------------------------

When you enter a filter option, it is temporarily stored in the edit buffer.
The `update` command applies the filter settings. (See previous section)


(1) delay
^^^^^^^^^^^^^^^^^^^

Sets the delay time of the packet.

Format::

  > delay delay_time   {jitter time}   {occurrence rate(%)}


..

   .. table:: delay option arguments
      :widths: 20, 10, 60

      =========================  =========  ==============================================
      argument                    optional    value
      =========================  =========  ==============================================
      delay_time                  required    unit: s:second / ms:millisecond / us:microsecond
      jitter time                 optional    unit: s:second / ms:millisecond / us:microsecond
      jitter occurrence rate      optional    unit: %
      =========================  =========  ==============================================


Execution example:

a. Generate a 100msec delay.

   .. code-block:: shell
      
      > delay 100ms

b. Generate a delay of 100msec ± 20msec.

   .. code-block:: shell

      > delay 100ms  20ms

c. Generate a delay of 100msec ± 20msec for 50% and a delay of 100msec for the rest.

   .. code-block:: shell

      > delay 100ms  20ms  50%

.. raw:: latex

   \clearpage

Caution::

  In the case of communication where packet round trip occurs like ping command, the total delay time will be different depending on the application range of the filter.

a. When delay is set in both directions

   .. code-block:: shell

      a > delay 100ms
   
   A round trip delay of 200ms will occur.

   .. figure:: /_static/filter_delay_both-2.png
      :width: 60%

      Both directions delay

   If you want to make it 100ms round trip, set the delay to 50ms on both sides.

b. When delay is set in one direction

   .. code-block:: shell

      1 > delay 100ms

   Only one direction will be delayed by 100ms.

   .. figure:: /_static/filter_delay_one-2.png
      :width: 60%

      Delay in one direction

.. raw:: latex

   \clearpage


When the communication volume is biased::

  When one side of the communication volume is large(for example, download from the server), be careful about the setting direction of the filter.

  .. figure:: /_static/filter_download.png
     :width: 100%

     Example of biased communication volume

.. raw:: latex

   \clearpage

(2) loss: Loss (packet loss)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generates packet loss at a specified rate.

Format::

  > loss  loss_rate(%)

..

   .. table:: loss option arguments
      :widths: 20, 10, 60

      =========================  =========  ==============================================
      argument                    optional    value
      =========================  =========  ==============================================
      loss_rate                   required    unit: %
      =========================  =========  ==============================================

Execution example:

a. 10% packet loss.

   .. code-block:: shell

      > loss 10%

.. note::

   Like delay, the filter is applied to the output of the network device.

.. raw:: latex

   \clearpage

(3) duplicate: Duplicate

Generates duplicate packets.

Format::

  > duplicate  occurrence rate(%)

..

   .. table:: duplicate option arguments
      :widths: 20, 10, 60

      =========================  =========  ==============================================
      argument                    optional    value
      =========================  =========  ==============================================
      occurrence rate             required    unit: %
      =========================  =========  ==============================================

Execution example:

a. 10% duplicate packets.

   .. code-block:: shell

      > duplicate 10%

.. note::

   Like delay, the filter is applied to the output of the network device.

.. raw:: latex

   \clearpage

(4) corrupt: Corrupt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Rewrites the packet data (inverts a random 1bit)

Format::

  > corrupt  occurrence rate(%)

..

   .. table:: corrupt option arguments
      :widths: 20, 10, 60

      =========================  =========  ==============================================
      argument                    optional    value
      =========================  =========  ==============================================
      occurrence rate             required    unit: %
      =========================  =========  ==============================================

Execution example:

a. 0.1% probability of rewriting a packet.

   .. code-block:: shell

      > corrupt 0.1%

.. note::

   1. Like delay, be careful about the application range of the filter.

   2. In the case of TCP/IP packets, the packet is discarded because the protocol stack detects the error with CRC check.
      If you disable the checksum in UDP packets, you need to detect the error at the upper layer.

.. raw:: latex

   \clearpage

(5) reorder: Reorder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changes the order of packet arrival.

Format::

  > reorder  occurrence rate(%)

..

   .. table:: reorder option arguments
      :widths: 20, 10, 60

      =========================  =========  ==============================================
      argument                    optional    value
      =========================  =========  ==============================================
      occurrence rate             required    unit: %
      =========================  =========  ==============================================

Execution example:

a. 10% probability of changing the order of packet arrival.

   .. code-block:: shell

      > reorder 10%

.. note::

   Like delay, the filter is applied to the output of the network device.

.. raw:: latex
   
   \clearpage

(6) rate: Bandwidth control

Format::

  > rate  bandwidth

..

   .. table:: rate option arguments
      :widths: 20, 10, 60

      =========================  =========  ==============================================
      argument                    optional    value
      =========================  =========  ==============================================
      bandwidth                   required    unit: bps:byte/second / bit:bit/second / K:Kbit / M:Mbit / G:Gbit
      =========================  =========  ==============================================

   .. table:: unit
      :widths: 10, 30

      ===========   ===========================
      notation        actual meaning
      ===========   ===========================
      bps            byte/second
      bit            bit/second
      unspecified    bit/second
      K / k          Killo (1,000)
      M / m          Mega (1,000,000)
      G / g          Giga (1,000,000,000)
      ===========   ===========================

   .. table:: setting
      :widths: 10, 30

      =============   =========================
      value example    actual meaning
      =============   =========================
      1000             1K bit/second
      1K               1K bit/second
      1Kbit            1K bit/second
      1Kbps            1K byte/second
      =============   =========================


Execution example:

   .. code-block:: shell

      > rate 64kbps

.. note::

   Like delay, the filter is applied to the output of the network device.

.. raw:: latex

   \clearpage