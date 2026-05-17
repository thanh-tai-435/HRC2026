# Scene Map — Task 1: Part Sorting
Người thực hiện: Pham Tran Thanh Tai
Nguồn: Ubtech_sim/config/Part_Sorting.yaml + Ubtech_sim/main.py

## Layout tổng quan
Robot Walker S2 đứng tại (0.7, -0.2, 0.9), xoay 90°, hướng về phía bàn.
Bàn làm việc phía trước robot. 4 workpieces (2 loại A + 2 loại B) scatter
ngẫu nhiên trên bàn. 1 box phân loại cố định tại (1.2, 0.3, 1.05).

## Prim Paths quan trọng

| STT | Tên | USD Source / Path | Vai trò |
|-----|-----|-------------------|---------|
| 1 | Scene | assets/resources/Collected_Task4/SubUSDs/2_small_warehouse2.usd | Scene chính |
| 2 | Robot USD | assets/resources/Collected_s2_v1_ecbg/s2_v1.usd | Walker S2 model |
| 3 | Robot root | /Root/Ref_Xform/Ref | Articulation root (main.py) |
| 4 | Robot URDF | assets/resources/s2.urdf | IK solver input |
| 5 | Table | assets/resources/Collected_table_v2/table_v2.usd | Bàn làm việc |
| 6 | Box | assets/resources/Box_blank/box_60_40_23_cut_0.usd | Hộp phân loại |
| 7 | Part A v1 | assets/resources/Collected_Task1_PartA_ori_color/Task1_PartA.usd | Workpiece A màu gốc |
| 8 | Part A v2 | assets/resources/Collected_Task1_PartA_red/Task1_PartA.usd | Workpiece A màu đỏ |
| 9 | Part B v1 | assets/resources/Collected_Part_B_blue/Part_B.usd | Workpiece B màu xanh |
| 10 | Part B v2 | assets/resources/Collected_Part_B_ori_color/Part_B.usd | Workpiece B màu gốc |

> ⚠️ Prim path /Root/Ref_Xform/Ref xác minh từ main.py dòng:
> robot = RobotArticulation(prim_path="/Root/Ref_Xform/Ref", name="walkerS2")
> Các path USD lấy từ Part_Sorting.yaml key: robot_usd, table_usd, box_usd, part_*_assets

## Vị trí các object (world coordinates)
| Object | Position | Ghi chú |
|--------|----------|---------|
| Robot | [0.7, -0.2, 0.9] | rotation [0,0,90] |
| Table | [0.75, 0.3, 0.5] | scale [1.99, 1.87, 1.11] |
| Box | [1.2, 0.3, 1.05] | lock_boxes=true, static |
| Scatter center | [0.75, 0.28, 1.04] | x±0.30m, y±0.23m |

## Physics
- Settle time: 2.0s sau khi spawn workpieces
- Box: lock_boxes=true → static collider
- Workpieces: rigid body, scatter ngẫu nhiên

## Camera
- 4 RGB cameras: head_left, head_right, wrist_left, wrist_right
- Prim path cụ thể: cần xác minh từ Isaac Sim Stage panel
