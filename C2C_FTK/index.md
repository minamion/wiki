# C2C 电缆快速测试工具-C2C FTK(Cable Fast Test Toolkit)



欢迎使用TypeC线缆规格测试工具！这个工具可以帮助您快速测试TypeC线缆的规格和功能。通过将线缆两头连接到工具上，根据引脚对应的灯亮起情况，您可以轻松判断线缆支持的功能。本文档将帮助您了解如何正确使用工具，并提供了相关资源以供参考。
### 为什么设计这个工具？
TypeC线缆具有多种规格和功能，用户经常不清楚自己的线缆是否支持所需的功能。
传统的测试方法可能需要专业仪器或复杂的步骤，而我们的工具可以在短时间内提供明确的测试结果。

优势：

低成本：成本仅为8元，相对于专业测试设备来说，价格非常亲民。

简单易用：我简单直观，不需要特殊培训或技术知识。用户只需将线缆连接到工具上，观察灯的亮起情况即可。

高效快速：测试过程非常迅速，用户不需要等待或进行复杂的设置。结果几乎是即时的。

便携性：工具的小巧尺寸和钥匙扣设计使得用户可以随时随地进行测试，无需额外的设备或工具。


## 工具外观

![TypeC线缆规格测试工具外观](insert_image_url_here)

## 如何使用

1. 将要测试的TypeC线缆的两头连接到工具上。
2. 根据以下灯的亮起情况，参考快速检查表，判断线缆的功能。

## 快速检查表

以下是TypeC线缆规格的快速检查表，根据工具上的灯的亮起情况，您可以判断线缆支持的功能。

| 功能                      | 选项 A（引脚对应灯亮起）                            | 选项 B（引脚对应灯亮起）                            |
|---------------------------|-----------------------------------------------------|-----------------------------------------------------|
| USB Power Delivery        | VBUS | GND | CC1 | Shield                         | VBUS | GND | CC2 | Shield                         |
| USB 2.0/1.1              | VBUS | GND | D+  | D- | Shield                    | VBUS | GND | D+  | D- | Shield                    |
| USB 3.0/3.1/3.2/4         | VBUS | GND | TX1+ | RX1+ | TX1- | RX1- | Shield  | VBUS | GND | TX2+ | RX2+ | TX2- | RX2- | Shield  |
|                           | or    |     | TX2+ | RX2+ | TX2- | RX2- |     |                           |
| Debug Accessory Mode      | VBUS | GND | D+  | D- | CC1 | SBU1 | TX1+ | RX1+ | TX1- | RX1- | Shield  | VBUS | GND | D+  | D- | CC2 | SBU2 | TX2+ | RX2+ | TX2- | RX2- | Shield  |
| Alternate Mode            | VBUS | GND | TX1+ | RX1+ | TX1- | RX1- | Shield  | VBUS | GND | TX2+ | RX2+ | TX2- | RX2- | Shield  |
| Audio Adapter Accessory Mode | GND | CC1 | CC2 | SBU1 | SBU2 | D+  | D- | Shield  |

*请注意，VBUS（电源线）是可选的，用于同时为设备充电。

## 硬件开源内容

- [原理图下载链接](insert_schematic_link_here)
- [工程文件下载链接](insert_project_files_link_here)
