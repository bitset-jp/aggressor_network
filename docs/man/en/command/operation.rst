General Commands
=================

ifconfig: Display network settings
-------------------------------------------

Displays the settings of the selected network device (eth0, eth1).

.. table:: Devices displayed by ifconfig
   :widths: 10, 40

   ===========   ======================================
   Cursor        Display content
   ===========   ======================================
   ``0 >``        Display only eth0
   ``1 >``        Display only eth1
   ``a >``        Display both eth0 and eth1
   ===========   ======================================

Format::

   > ifconfig

Execution example:

   .. figure:: /_static/ss_ifconfig.png
      :width: 95%

      ifconfig example

clear: Clear the main screen
-------------------------------------------

Clears the main screen(0:main screen).

Format::

  > clear

help: Display help
-------------------------------------------

Displays the help screen on "1:help screen".

Format::

  > help {command_name}

Execution example:

   .. figure:: /_static/ss_1_help_rate.png
      :width: 95%

      help screen (help rate)

stat: Redisplay the traffic statistics screen
-----------------------------------------------

Redisplay the traffic statistics screen on "2:stat screen".

Format::

  > stat

.. note::

   If there was no active network device when booting, activating the network device will not display the traffic statistics screen.
   In that case, execute "stat" command.

.. raw:: latex

   \clearpage

iftop
----------------------------

Make "3:eth0 screen" and "4:eth1 screen" to display iftop.

Selected network device(s) will change to iftop mode.

Format::

  > iftop

.. figure:: /_static/ss_3-4_eth.png
   :width: 100%

   iftop

tcpdump
----------------------------

Make "3:eth0 screen" and "4:eth1 screen" to display tcpdump.

Selected network device(s) will change to tcpdump mode.

Format::

  > tcpdump

.. figure:: /_static/ss_3-4_eth_tcpdump.png
   :width: 100%

   tcpdump

.. raw:: latex
   
   \clearpage

height
----------------------------

Change the height of "3:eth0 screen" and "4:eth1 screen".

Format::

  > height {number_of_lines}

..

   .. table:: arguments of height command
      :widths: 20, 10, 60

      ===============   ========   =========
      Argument          Required   Value
      ===============   ========   =========
      number_of_lines   Yes        10 - 35
      ===============   ========   =========

Execution example:

  > height 20

.. raw:: latex

   \clearpage