System Configuration
====================

.. _rtc_command:

rtc: Set system time
--------------------

Set system time. The time is recorded in the RTC (real-time clock) which can keep counting the time even when the power is off.

Format::
   
   > rtc YYYY-MM-DD hh:mm:ss

Execution example::

   > rtc 2023-05-10 12:15:00

.. warning::
   
   To apply setting, the system needs restart after changing the time setting.


keyboard: Change keyboard layout
--------------------------------

Format::

   > keyboard {layout}

layout must be one of the following.


.. table:: layout list
   :widths: 10, 10, 40

   ==============   ========  =================================
   layout           language  keyboard type
   ==============   ========  =================================
   ``jp``           Japanese  PC-105
   ``us``           English   PC-105
   ``hhk``          English   PFU Happy Hacking keyboard
   ==============   ========  =================================


Execution example::

   > keyboard us

.. warning::

   To apply setting, the system needs restart after changing the keyboard layout.
