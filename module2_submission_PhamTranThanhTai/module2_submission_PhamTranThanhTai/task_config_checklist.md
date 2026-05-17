# Task Config Checklist — HRC2026
Người thực hiện: Pham Tran Thanh Tai
Nguồn: Ubtech_sim/config/*.yaml + main.py

---

## Task 1 — Part Sorting
| Mục | Giá trị | Nguồn |
|-----|---------|-------|
| Config file | Ubtech_sim/config/Part_Sorting.yaml | find . -name "*.yaml" |
| task_number | 1 | Part_Sorting.yaml |
| Scene USD | assets/resources/Collected_Task4/SubUSDs/2_small_warehouse2.usd | yaml: scene_usd |
| Robot USD | assets/resources/Collected_s2_v1_ecbg/s2_v1.usd | yaml: robot.robot_usd |
| Robot root | /Root/Ref_Xform/Ref | main.py: RobotArticulation() |
| Robot position | [0.7, -0.2, 0.9] rotation [0,0,90] | yaml: robot position/rotation |
| URDF (IK) | assets/resources/s2.urdf | main.py: urdf_path |
| Table | assets/resources/Collected_table_v2/table_v2.usd pos [0.75,0.3,0.5] | yaml: table |
| Box | assets/resources/Box_blank/box_60_40_23_cut_0.usd pos [1.2,0.3,1.05] | yaml: box |
| Box locked | true | yaml: lock_boxes |
| Part A assets | Collected_Task1_PartA_ori_color, Collected_Task1_PartA_red | yaml: part_a_assets |
| Part B assets | Collected_Part_B_blue, Collected_Part_B_ori_color | yaml: part_b_assets |
| Num parts/class | 2 | yaml: num_parts |
| Scatter center | [0.75, 0.28, 1.04] size x±0.30 y±0.23 | yaml: scatter_area |
| TCP offset | [0.0, 0.0, 0.0] | yaml: grasp.tcp_offset |
| IK rot weight | 1.0 | yaml: ik_rot_weight |
| Settle time | 2.0s | yaml: settle_time |
| Timelimit | 100s | yaml: timelimit |
| Log output | poses.csv, camera_data.hdf5 | main.py: DataLogger |

---

## Task 2 — Conveyor Sorting
| Mục | Giá trị | Nguồn |
|-----|---------|-------|
| Config file | Ubtech_sim/config/Conveyor_Sorting.yaml | find |
| task_number | 2 | yaml |
| Scene USD | assets/resources/Collected_Task4/SubUSDs/2_small_warehouse2.usd | yaml |
| Robot position | [0.7, -0.35, 0.9] rotation [0,0,90] | yaml |
| Conveyor USD | assets/resources/Collected_ConveyorBelt_New/.../ConveyorBelt.usd | yaml |
| Conveyor position | [-0.134, 0.269, 0.0] | yaml |
| Num parts | 5, khoảng cách 0.4m | yaml |
| Part A USD | Collected_Part_B_ori_color/Part_B.usd | yaml |
| Part B USD | Collected_Task2_Part_A/Task2_Part_A.usd | yaml |
| Box 1 | pos [0.486, -0.062, 0.92] | yaml: box_position[0] |
| Box 2 | pos [0.886, -0.062, 0.92] | yaml: box_position[1] |
| Scatter center | [0.12, 0.269, 1.2] size x±0.06 y±0.04 | yaml |
| TCP offset | [0.0, 0.0, 0.0] | yaml |
| IK rot weight | 0.1 | yaml |
| Known issues | Conveyor speed không thấy trong yaml | — |

---

## Task 3 — Foam Inlaying
| Mục | Giá trị | Nguồn |
|-----|---------|-------|
| Config file | Ubtech_sim/config/Foam_Inlaying.yaml | find |
| task_number | 3 | yaml |
| Robot position | [0.75, -0.25, 0.9] rotation [0,0,90] | yaml |
| Foam USD | assets/resources/Collected_foam_collision/foam.usd | yaml: foam_usd |
| Foam position | [0.76, 0.3, 1.0] | yaml |
| Box 1 | pos [0.28, 0.3, 1.04] | yaml |
| Box 2 | pos [1.25, 0.3, 1.04] | yaml |
| Part A | Collected_28motor/28motor.usd | yaml |
| Part B | Collected_Part_B_blue/Part_B.usd | yaml |
| Num parts | 3 mỗi loại | yaml |
| Split in boxes | True | yaml: if_split_in_boxes |
| TCP offset | [0.0, 0.0, 0.22] | yaml |
| IK rot weight | 0.1 | yaml |

---

## Task 4 — Packing Box
| Mục | Giá trị | Nguồn |
|-----|---------|-------|
| Config file | Ubtech_sim/config/Packing_Box.yaml | find |
| task_number | 4 | yaml |
| Robot position | [0.847, -0.25, 0.9] rotation [0,0,90] | yaml |
| Table position | [0.846, 0.3, 0.5] | yaml |
| Box (carton) | assets/resources/Collected_foam/Box_with_foam.usd pos [0.855,0.3,1.13] | yaml |
| Foam | assets/resources/Collected_foam/foam.usd pos [0.856,0.185,1.040] scale [0.5,0.5,0.5] | yaml |
| TCP offset | [0.0, 0.0, 0.22] | yaml |
| Save poses CSV | False | yaml: save_poses_to_csv |
| Known issues | Lid ordering, dual-arm sequence chưa rõ | — |
