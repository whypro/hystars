===================
Arch Linux 配置备忘
===================

:date: 2015-04-11 19:20
:modified: 2015-04-12 22:25
:tags: Arch Linux

增加用户
========

.. code-block:: shell

    useradd whypro
    passwd whypro
    mkdir /home/whypro
    chown whypro:whypro /home/whypro

修改主机名
==========

.. code-block:: shell

    vi /etc/hostname

设置静态 IP 地址
================

本地化
======

本地化的程序与库若要本地化文本，都依赖 locales, 后者明确规定地域、货币、时区日期的格式、字符排列方式和其他本地化标准等等。在下面两个文件设置：``locale.gen`` 与 ``locale.conf``。

``/etc/locale.gen`` 是一个仅包含注释文档的文本文件。指定您需要的本地化类型，只需移除对应行前面的注释符号（#）即可，建议选择带 UTF-8 的项：

.. code-block:: shell

    # nano /etc/locale.gen
    en_US.UTF-8 UTF-8
    zh_CN.UTF-8 UTF-8
    zh_TW.UTF-8 UTF-8

接着执行 ``locale-gen`` 以生成 locale 信息：

.. code-block:: shell

    locale-gen

创建 ``locale.conf`` 并提交您的本地化选项：

.. code-block:: shell

    echo LANG=en_US.UTF-8 > /etc/locale.conf

将系统 locale 设置为 en_US.UTF-8，系统的 Log 就会用英文显示，这样更容易问题的判断和处理。


时区
====

可用的时区全集中在 ``/usr/share/zoneinfo/``\ *Zone*\ ``/``\ *SubZone* 目录里了，
所以要查看可用时区，直接浏览 ``/usr/share/zoneinfo`` 即可：

.. code-block:: shell

    ls /usr/share/zoneinfo/

同理，您也可以查看子目录下的可用时区：

.. code-block:: shell

    ls /usr/share/zoneinfo/Europe

将 ``/etc/localtime`` 软链接到 ``/usr/share/zoneinfo/``\ *Zone*\ ``/``\ *SubZone*，以上海为例：

.. code-block:: shell

    ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

注意: 如果提示 ``ln: failed to create symbolic link '/etc/localtime': File exists``，用 ``ls -l /etc/localtime`` 检查存在的文件并向 ``ln`` 添加 ``-f`` 选项来覆盖它。

设置登录后欢迎信息
==================

.. code-block:: shell

    vi /etc/motd
